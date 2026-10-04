#!/usr/bin/env python3
"""Prove the assertions are not vacuous.

An assertion that cannot fail is worse than none: it looks like verification and
provides none. So each mutation below corrupts the primary data in exactly the
way one claim denies, and the claim is required to fail. A mutation that the
claim survives is reported as SURVIVED, and that is a bug in the claim.

    python3 verify/mutate.py

Most mutations touch only the in-memory parse. Six write into the repository -
into a committed netlist export, into three documents, and two probe files that
exist only for as long as the claim reading them runs - and one edits a KiCad
source sheet under TRS80_SCHEMATICS, the only way to prove that claim watches
the drawing rather than a copy of it. `restore()` puts every one of them back
from the original bytes, and the run ends by re-reading them to check that it
did.
"""

import copy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import claims as claims_mod  # noqa: E402
import run as runner  # noqa: E402

MUTATIONS = []


def mutation(claim_id, what):
    def deco(fn):
        MUTATIONS.append({"claim": claim_id, "what": what, "fn": fn})
        return fn

    return deco


def _rebuild(board):
    board._pin2net = {}
    board._pin2short = {}
    for nt in board.nets:
        for r, p, _f, _t in nt["nodes"]:
            board._pin2net[(r, p)] = nt["name"]
            board._pin2short[(r, p)] = nt["short"]


def _set(board, ref, pin, net):
    """Move a pin onto another net.

    `nets` is the authoritative structure and `_pin2net`/`_pin2short` are derived
    from it, so a mutation that writes only the derived maps is not a mutation at
    all: every claim using `pins_on` or `partition` reads straight past it. The
    first version of this file did exactly that, and ten mutations "survived"
    claims that were in fact perfectly sound.
    """
    pin = str(pin)
    node = None
    for nt in board.nets:
        for nd in list(nt["nodes"]):
            if nd[0] == ref and nd[1] == pin:
                node = nd
                nt["nodes"].remove(nd)
    if node is None:
        node = [ref, pin, "", ""]
    for nt in board.nets:
        if nt["short"] == net or nt["name"] == net:
            nt["nodes"].append(node)
            break
    else:
        board.nets.append({"name": net, "short": net.split("/")[-1], "nodes": [node]})
    _rebuild(board)


def _swap(board, a, b):
    """Exchange the nets of two pins."""
    na, nb = board.net_of(*a), board.net_of(*b)
    _set(board, a[0], str(a[1]), nb)
    _set(board, b[0], str(b[1]), na)


# ------------------------------------------------------------------ netlist

@mutation("revd-eq-reve", "move one Rev E pin to another net")
def _(ctx):
    _set(ctx.board("reve"), "Z59", "12", "D5")


@mutation("rom-sockets-same-wiring", "rewire a ROM socket pin")
def _(ctx):
    _set(ctx.board("revg"), "Z33", "18", "GND")


@mutation("z3-changes-size", "give Rev A's Z3 a sixteenth pin")
def _(ctx):
    _set(ctx.board("reva"), "Z3", "16", "+5V")


@mutation("ei-timer-acknowledge-on-read", "lift the timer flip-flop's D off ground")
def _(ctx):
    _set(ctx.board("ei"), "Z26", "2", "+5V")


@mutation("ei-timer-acknowledge-on-read", "clock the timer from the write strobe")
def _(ctx):
    _set(ctx.board("ei"), "Z26", "11", "~{37E0_WRITE}")


@mutation("ei-motor-oneshot", "change R25 to 220k")
def _(ctx):
    ctx.board("ei").comps["R25"]["value"] = "220k"


@mutation("ei-oneshot-clears-drive-select", "repoint the drive-select latch's reset")
def _(ctx):
    _set(ctx.board("ei"), "Z47", "1", "+5V")


@mutation("ei-sysres-distribution", "extend /SYSRES to the drive-select latch")
def _(ctx):
    _set(ctx.board("ei"), "Z28", "1", "~{SYSRES}")


@mutation("alps-no-matrix-diodes", "add a diode to the key matrix")
def _(ctx):
    k = ctx.board("alps")
    k.comps["D99"] = {"value": "1N4148", "sheet": "", "lib": ("Device", "D")}


@mutation("alps-shift-keys-parallel", "separate the two shift keys")
def _(ctx):
    _set(ctx.board("alps"), "SW9", "2", "Net-(R1E-R5.2)")


@mutation("alps-parts-inventory", "add a sixty-sixth switch")
def _(ctx):
    ctx.board("alps").comps["SW66"] = {"value": "SW_Push", "sheet": "",
                                       "lib": ("Switch", "SW_Push")}


@mutation("alps-keypad-parallels-main-keys", "give a keypad key its own matrix position")
def _(ctx):
    _set(ctx.board("alps"), "SW60", "1", "Net-(SW99-Pad1)")


@mutation("port-ff-identical-across-us-revisions", "change Rev A's DAC network")
def _(ctx):
    ctx.board("reva").comps["R55"]["value"] = "10k"


@mutation("port-ff-decode-ignores-high-address", "feed A12 into the port FF decode")
def _(ctx):
    _set(ctx.board("revg"), "Z54", "3", "A12")


@mutation("video-ram-identical-across-us-revisions", "give Rev D an eighth video RAM")
def _(ctx):
    d = ctx.board("revd")
    d.comps["Z64"] = {"value": "2102", "sheet": "", "lib": ("Memory", "2102")}
    _set(d, "Z64", "11", "VD6")


@mutation("z21-is-the-address-decoder", "move the 74LS156 to Z3")
def _(ctx):
    ctx.board("revg").comps["Z21"]["value"] = "74LS138"


@mutation("us-boards-match-their-pcb-copper", "move a pin onto another net")
def _(ctx):
    _set(ctx.board("revg"), "Z35", "1", "GND")


@mutation("us-boards-match-their-pcb-copper", "rename a net the copper knows by another name")
def _(ctx):
    # The other half of the comparison: membership is untouched, only the name
    # moves, so this fails only if net names are checked as well as pin sets.
    a = ctx.board("reva")
    for nt in a.nets:
        if nt["name"] == "/Address Decoder/~{RAS}":
            nt["name"], nt["short"] = "/Address Decoder/~{ROWSEL}", "~{ROWSEL}"
    _rebuild(a)


@mutation("japanese-boards-disagree-with-their-copper", "heal one of the eleven")
def _(ctx):
    # Move the schematic pin onto the pad the copper uses: that net then agrees,
    # and the set of eleven is no longer eleven.
    _set(ctx.board("jap50"), "Z6", "14", "GND")


@mutation("enable-pins-are-clear-of-the-data-rows", "drag a data wire over an enable pin")
def _(ctx):
    ctx.patch_sheet(
        "revg", "RAM_ROM_Interface.kicad_sch",
        "(xy 140.335 74.93) (xy 262.255 74.93)",
        "(xy 123.825 74.93) (xy 262.255 74.93)",
    )


@mutation("cassette-output-network", "take the second DAC bit off the true output")
def _(ctx):
    # Connect Q1, the side the board leaves idle. If both sides of the flip-flop
    # are used the inversion the document rests on is not there.
    _set(ctx.board("revg"), "Z59", "7", "MODESEL")


@mutation("keyboard-matrix-map", "move one key to another column")
def _(ctx):
    # SW10 is row 0 bit 1, the `A` key; R1C's net is bit 1's column.
    _set(ctx.board("alps"), "SW10", "2", "Net-(R1H-R8.2)")


@mutation("keyboard-matrix-map", "unplug a key from its row")
def _(ctx):
    _set(ctx.board("alps"), "SW17", "2", "GND")


@mutation("keyboard-adapter-mapping", "empty the adapter's pin map")
def _(ctx):
    a = ctx.board("kbadapter")
    for key in list(a._pin2net):
        _set(a, key[0], key[1], "GND")


@mutation("keyboard-connectors-differ", "move /KYBD off the TEC connector's pin 10")
def _(ctx):
    _set(ctx.board("jap50"), "CN1", "10", "KBD0")


@mutation("net-names-may-contain-slashes", "drop the slash-bearing net")
def _(ctx):
    e = ctx.board("ei")
    for (ref, pin), net in list(e._pin2short.items()):
        if "/" in net:
            _set(e, ref, pin, "PLAIN")


@mutation("alps-column-buffers", "swap two column buffer pull-ups")
def _(ctx):
    _swap(ctx.board("alps"), ("R1", "8"), ("R1", "9"))


@mutation("alps-row-drivers", "swap rows 0 and 1")
def _(ctx):
    _swap(ctx.board("alps"), ("Z1", "9"), ("Z1", "11"))


@mutation("alps-row-drivers", "use a fifth inverter in Z1")
def _(ctx):
    _set(ctx.board("alps"), "Z1", "1", "A0")


@mutation("committed-exports-are-current", "let a committed export go stale")
def _(ctx):
    import pathlib as _pl
    f = _pl.Path(__file__).resolve().parent.parent / "netlists" / "exports" / "psu.net"
    ctx.remember(f)
    text = f.read_text()
    old = '(value "1N4001")'
    assert old in text, "psu.net no longer names the rectifier"
    f.write_text(text.replace(old, '(value "1N4002")', 1))


@mutation("netlist-tables-match-the-netlists", "delete a component")
def _(ctx):
    ctx.board("revg").comps.pop("Z59")


# ---------------------------------------------------------------------- ROM

@mutation("level2-leader-is-255-bytes", "make the leader loop LD B,0")
def _(ctx):
    ctx.patch_rom(claims_mod.L2_IMAGE, 0x0288, b"\x00")


@mutation("rom-keyboard-map-arithmetic", "change the row 4-5 bias")
def _(ctx):
    ctx.patch_rom(claims_mod.L2_IMAGE, 0x042A, b"\x60")


@mutation("rom-keyboard-map-arithmetic", "move the control-key table")
def _(ctx):
    ctx.patch_rom(claims_mod.L2_IMAGE, 0x0444, b"\x70")


@mutation("rom-keyboard-map-arithmetic", "take the shift term off the letters")
def _(ctx):
    ctx.patch_rom(claims_mod.L2_IMAGE, 0x041B, b"\x00")   # ADD A,20h -> ADD A,00h


@mutation("chargen-row-census", "blank row 7 of the earliest character set")
def _(ctx):
    for g in range(128):
        ctx.patch_rom(claims_mod.CHARGEN.format(1), g * 8 + 7, b"\x00")


@mutation("rom-keyboard-scan-delays", "halve the debounce constant")
def _(ctx):
    ctx.patch_rom(claims_mod.L2_IMAGE, 0x011E, b"\x80\x02")


@mutation("rom-keyboard-scan-delays", "make the delay loop one instruction shorter")
def _(ctx):
    ctx.patch_rom(claims_mod.L2_IMAGE, 0x0061, b"\x00")


@mutation("rom-images-are-the-images-named", "hand it the keyboard-bounce patch instead")
def _(ctx):
    # The three bytes that build differs by. They sat past the last offset any
    # other claim read until rom-keyboard-map-arithmetic began asserting the
    # display driver's fold at 0471h-047Ch, which now covers 0476h as well; this
    # claim stays the one that names the whole image.
    ctx.patch_rom(claims_mod.L2_IMAGE, 0x0476, b"\x00")


@mutation("keyboard-address-is-the-row-select", "drive a row from something else")
def _(ctx):
    _set(ctx.board("alps"), "Z2", "12", ctx.board("alps").net_of("Z1", "8"))


@mutation("keyboard-address-is-the-row-select", "take a row off its address line")
def _(ctx):
    _set(ctx.board("alps"), "Z1", "9", "A9")


@mutation("netlists-are-internally-consistent", "invent a node with no component")
def _(ctx):
    ctx.board("revg").nets[0]["nodes"].append(["Z999", "1", "", ""])
    _rebuild(ctx.board("revg"))


@mutation("netlists-are-internally-consistent", "give a component an impossible pin")
def _(ctx):
    _set(ctx.board("revg"), "Z59", "99", "GND")


@mutation("documents-invent-no-designators", "delete a part only one in-scope board has")
def _(ctx):
    # Has to be unique to a single board. Deleting `R2` from the keyboard does
    # not fail the claim, because the main boards have an `R2` too and the claim
    # checks the union of the boards a document is about. That is what the claim
    # says, and it is weaker than it first reads.
    ctx.board("alps").comps.pop("SW65")


@mutation("rom-sockets-same-wiring", "make a second socket pin differ")
def _(ctx):
    _set(ctx.board("reva"), "Z33", "18", "GND")


@mutation("documents-have-no-dangling-links", "add a document with a link to nothing")
def _(ctx):
    ctx.tempfile("mutation-probe.md", "See [nothing](no-such-file.md).\n")


@mutation("documents-invent-no-designators", "add a document naming a part that does not exist")
def _(ctx):
    # The claim only reads the documents it scopes, so the probe has to be one of
    # them. revisions.md is restored from its original bytes afterwards.
    ctx.append_doc("docs/revisions.md", "\nA stray reference to `Z999`.\n")


@mutation("counting-differences-three-ways", "make Rev A's C20 match Rev G's")
def _(ctx):
    ctx.board("reva").comps["C20"]["value"] = "330pF"


@mutation("counting-differences-three-ways", "add a reference to Rev A")
def _(ctx):
    ctx.board("reva").comps["Z998"] = {"value": "74LS00", "sheet": "", "lib": None}


@mutation("reva-video-sync-differs", "give Rev A all six Z57 inverters")
def _(ctx):
    for i, o in (("5", "6"), ("9", "8"), ("11", "10"), ("13", "12")):
        _set(ctx.board("reva"), "Z57", i, f"Net-(Z57-Pad{i})")
        _set(ctx.board("reva"), "Z57", o, f"Net-(Z57-Pad{o})")


@mutation("reva-video-sync-differs", "make Rev G's video sync differ from Rev D's")
def _(ctx):
    _set(ctx.board("revg"), "R21", "1", "GND")


@mutation("revg-clk-en-and-pullups", "ground the Z42 inverter input again")
def _(ctx):
    _set(ctx.board("revg"), "Z42", "9", "GND")


@mutation("revg-clk-en-and-pullups", "put a second driver on the CLK_EN input")
def _(ctx):
    _set(ctx.board("revg"), "Z55", "3", ctx.board("revg").net_of("Z42", "9"))


@mutation("revg-clk-en-and-pullups", "leave Z70 pin 13 on the HI rail")
def _(ctx):
    _set(ctx.board("revg"), "Z70", "13", "HI")


@mutation("revg-duplicate-silkscreen-designators", "disconnect C_R67")
def _(ctx):
    _set(ctx.board("revg"), "C_R67", "2", "unconnected-(C_R67-Pad2)")


@mutation("bom-references-all-appear-in-netlist", "add a part no BOM lists")
def _(ctx):
    ctx.board("ei").comps["Z997"] = {"value": "74LS00", "sheet": "", "lib": None}


@mutation("us-revision-differences-are-complete", "introduce a twelfth difference")
def _(ctx):
    _set(ctx.board("revg"), "Z55", "3", "CLK")


@mutation("us-revision-differences-are-complete", "undo one of the eleven")
def _(ctx):
    for ref, pin in (("Z56", "6"), ("Z56", "7"), ("Z58", "6"), ("Z58", "7")):
        _set(ctx.board("revg"), ref, pin, "GND")


@mutation("rom-sockets-same-wiring", "move A12 off pin 21")
def _(ctx):
    _set(ctx.board("revg"), "Z33", "21", "A13")


@mutation("sources-table-lists-every-board", "drop a board from the source table")
def _(ctx):
    p = ctx.RESEARCH / "docs" / "sources.md"
    ctx.remember(p)
    p.write_text(p.read_text().replace("Rev E, ", ""))


@mutation("self-test-totals-are-not-stale", "let the README's component total go stale")
def _(ctx):
    p = ctx.HERE_README
    ctx.remember(p)
    text = p.read_text()
    assert "1,690 components" in text, "README no longer states the component total"
    p.write_text(text.replace("1,690 components", "1,691 components", 1))


@mutation("harness-counts-are-not-stale", "let the README's mutation count go stale")
def _(ctx):
    p = ctx.HERE_README
    ctx.remember(p)
    import re

    p.write_text(re.sub(r"\*\*[A-Za-z-]+ mutations, [A-Za-z-]+ caught\.\*\*",
                        "**Twelve mutations, twelve caught.**", p.read_text()))


@mutation("revg-sheet-map", "move a part to another sheet")
def _(ctx):
    ctx.board("revg").comps["Z44"]["sheet"] = "Video RAM"


@mutation("revg-sheet-map", "make Z3 the 74LS156 again")
def _(ctx):
    g = ctx.board("revg")
    g.comps["Z3"]["value"] = "74LS156"


@mutation("ei-sheet-map", "add a second 74LS367 to the Expansion Interface")
def _(ctx):
    ctx.board("ei").comps["Z52"] = {"value": "74LS367", "sheet": "Line Printer",
                                    "lib": None}


@mutation("japanese-pal-ntsc-decode", "swap the two jumper ends on JP6")
def _(ctx):
    j = ctx.board("jap50")
    _set(j, "JP6", "1", "R3")
    _set(j, "JP6", "3", "R2")


@mutation("japanese-pal-ntsc-decode", "take L0 out of the PAL gating term")
def _(ctx):
    _set(ctx.board("jap20"), "Z45", "2", "GND")


@mutation("japanese-sheet-map", "make the two Japanese boards differ by sheet")
def _(ctx):
    ctx.board("jap20").comps["Z53"]["sheet"] = "Elsewhere"


@mutation("readme-lists-every-document", "add a document the index does not list")
def _(ctx):
    ctx.tempfile("unlisted.md", "# Not in the index\n")


class MutCtx(runner.Ctx):
    """A Ctx whose data can be corrupted, and restored between mutations."""

    RESEARCH = HERE.parent
    HERE_README = HERE / "README.md"

    def __init__(self, root):
        super().__init__(root)
        self._roms = {}
        self._pristine = {}
        self._temp = []
        self._docs = {}
        # restore() clears the two above after every mutation, so by the end of
        # a run there is nothing left to check against. This ledger is never
        # cleared: it is what `verify_restored()` compares the tree to.
        self._ledger = {}
        self._touched = set()

    def remember(self, p):
        """Record a file's original bytes before a mutation writes to it.

        Every write into the repository or into TRS80_SCHEMATICS goes through
        here, so `verify_restored()` has something to compare against.
        """
        original = p.read_bytes()
        self._ledger.setdefault(p, original)
        self._docs.setdefault(p, original)

    def verify_restored(self):
        """What the run has been claiming all along: nothing left behind.

        restore() puts each file back from its original bytes, but a claim that
        it worked is worth no more than any other unchecked claim - and this one
        is about the repository the reader is standing in.
        """
        wrong = [str(p) for p, original in self._ledger.items()
                 if not p.exists() or p.read_bytes() != original]
        wrong += [f"{p} still exists" for p in self._touched if p.exists()]
        return sorted(wrong)

    def tempfile(self, name, text):
        """Create a file in the repository that restore() removes."""
        p = self.RESEARCH / name
        assert not p.exists(), f"{name} already exists; refusing to overwrite"
        p.write_text(text)
        self._temp.append(p)
        self._touched.add(p)

    def patch_sheet(self, board, sheet, old, new):
        """Edit a KiCad source sheet, remembering its original bytes.

        The only mutation that touches TRS80_SCHEMATICS. restore() puts it back
        from the original bytes, and `verify_restored()` re-reads it at the end
        of the run to check that it did.
        """
        import netlist as _nl

        if self.root is None:
            raise runner.Skip("TRS80_SCHEMATICS is not set")
        p = (self.root / _nl.BOARDS[board]).parent / sheet
        self.remember(p)
        text = p.read_text()
        assert old in text, f"{sheet}: nothing to patch"
        p.write_text(text.replace(old, new, 1))
        self._boards.pop(board, None)
        self._pristine.pop(board, None)

    def append_doc(self, name, text):
        """Append to a real document, remembering its original bytes."""
        p = self.RESEARCH / name
        self.remember(p)
        p.write_text(p.read_text() + text)

    def board(self, name):
        if name not in self._boards:
            b = super().board(name)
            self._pristine[name] = copy.deepcopy(b)
        return self._boards[name]

    def rom(self, name):
        if name not in self._roms:
            self._roms[name] = bytearray(super().rom(name))
            self._pristine["rom:" + name] = bytes(self._roms[name])
        return bytes(self._roms[name])

    def patch_rom(self, name, addr, data):
        self.rom(name)
        self._roms[name][addr:addr + len(data)] = data

    def restore(self):
        for p in self._temp:
            p.unlink(missing_ok=True)
        self._temp.clear()
        for p, original in self._docs.items():
            p.write_bytes(original)
        self._docs.clear()
        for k, v in self._pristine.items():
            if k.startswith("rom:"):
                self._roms[k[4:]] = bytearray(v)
            else:
                self._boards[k] = copy.deepcopy(v)


def main():
    root = runner.os.environ.get("TRS80_SCHEMATICS")
    root = Path(root).expanduser() if root else None
    ctx = MutCtx(root)
    claims_mod.__dict__["Skip"] = runner.Skip
    by_id = {c["id"]: c for c in claims_mod.CLAIMS}

    caught = survived = skipped = 0
    bad = []
    for m in MUTATIONS:
        c = by_id.get(m["claim"])
        if c is None:
            bad.append((m, "no such claim"))
            survived += 1
            continue
        # Applying the mutation is kept out of the try below on purpose. If a
        # mutation's own setup raised, the AssertionError handler would count it
        # as a catch and report success for a mutation that changed nothing.
        try:
            m["fn"](ctx)          # corrupt
        except runner.Skip as e:
            ctx.restore()
            skipped += 1
            print(f"  SKIP      {m['claim']}: {m['what']} ({e})")
            continue
        except Exception as e:
            ctx.restore()
            survived += 1
            bad.append((m, f"the mutation did not apply: {type(e).__name__}: {e}"))
            print(f"  BROKEN    {m['claim']}: {m['what']} ({type(e).__name__}: {e})")
            continue

        try:
            c["fn"](ctx)          # the claim must now fail
        except runner.Skip as e:
            ctx.restore()
            skipped += 1
            print(f"  SKIP      {m['claim']}: {m['what']} ({e})")
            continue
        except AssertionError:
            caught += 1
            print(f"  caught    {m['claim']}: {m['what']}")
            ctx.restore()
            continue
        except Exception as e:
            caught += 1
            print(f"  caught    {m['claim']}: {m['what']} ({type(e).__name__})")
            ctx.restore()
            continue
        ctx.restore()
        survived += 1
        bad.append((m, "the claim still passed"))
        print(f"  SURVIVED  {m['claim']}: {m['what']}")

    ctx.restore()
    print(f"\n{caught} caught, {survived} survived, {skipped} skipped")
    for m, why in bad:
        print(f"  ! {m['claim']}: {m['what']} — {why}")

    left = ctx.verify_restored()
    n = len(ctx._ledger) + len(ctx._touched)
    if left:
        print(f"\nrestore left {len(left)} of {n} file(s) changed:")
        for f in left:
            print(f"  ! {f}")
        return 1
    print(f"{n} file(s) written and restored, byte for byte")
    return 1 if survived else 0


if __name__ == "__main__":
    sys.exit(main())
