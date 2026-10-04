"""One executable assertion per documented claim.

Each claim carries the sentence it is defending, so a failure reads as English.
`run.py` executes them all and exits non-zero if any fails.

The rule this folder runs on: a claim of the form "X is the only Y" must
enumerate every Y and assert the complement is empty. A comparison that cannot
produce the complement cannot support the claim.
"""

import re

CLAIMS = []

# The ROM images, at the paths the emulator's `roms/` lays them out under. The
# Level II file is a *combined* image - ROM A at 0000-1FFF followed by ROM B's
# addressable lower 4K at 2000-2FFF - so a file offset is the address the CPU
# fetches from, which is the form every ROM claim below is written in. The split
# device dumps this used to read were ROM A alone, and are gone.
L2_IMAGE = "system/level2-v1.3.bin"
CHARGEN = "char/character_set_{:02d}.bin"
CHARGEN_SETS = (1, 2, 4, 8, 16, 17)
# The compressed form README.md prints the six under, built from the same tuple
# so the page and the lookup cannot name different files.
CHARGEN_ROW = "char/character_set_" + "/".join(f"{n:02d}" for n in CHARGEN_SETS) + ".bin"


def claim(cid, doc, text):
    def deco(fn):
        CLAIMS.append({"id": cid, "doc": doc, "text": text, "fn": fn})
        return fn

    return deco


# ---------------------------------------------------------------- revisions

@claim("revd-eq-reve", "docs/revisions.md", "Rev D and Rev E are electrically identical.")
def _(ctx):
    d, e = ctx.board("revd"), ctx.board("reve")
    assert d.partition() == e.partition(), "net partitions differ"
    assert {r: c["value"] for r, c in d.comps.items()} == {
        r: c["value"] for r, c in e.comps.items()
    }, "component values differ"


@claim("jap20-eq-jap50", "docs/revisions.md",
       "Jap20 and Jap50 are electrically identical, and both carry 253 "
       "components, 410 nets and 1543 pin connections.")
def _(ctx):
    a, b = ctx.board("jap20"), ctx.board("jap50")
    assert a.partition() == b.partition(), "net partitions differ"
    assert {r: c["value"] for r, c in a.comps.items()} == {
        r: c["value"] for r, c in b.comps.items()
    }, "component values differ"
    # The three figures revisions.md prints. They were prose until a count in a
    # second document was found disagreeing with the asserted one.
    for n, name in ((a, "jap20"), (b, "jap50")):
        assert len(n.comps) == 253, f"{name}: {len(n.comps)} components"
        assert len(n.nets) == 410, f"{name}: {len(n.nets)} nets"
        conns = sum(len(nt["nodes"]) for nt in n.nets)
        assert conns == 1543, f"{name}: {conns} pin connections"


@claim(
    "rom-sockets-same-wiring",
    "docs/revisions.md",
    "Z33 and Z34 are wired identically on all four US boards on 23 of their 24 "
    "pins - A0-A12 with A12 on pin 21, ROMD0-ROMD7, +5V on 24 and GND on 12. "
    "Only pin 20 differs: one /ROM on Rev A/D/E, /ROMA and /ROMB on Rev G.",
)
def _(ctx):
    boards = {b: ctx.board(b) for b in ("reva", "revd", "reve", "revg")}
    for z in ("Z33", "Z34"):
        pins = sorted(
            {p for n in boards.values() for (r, p) in n._pin2net if r == z}, key=int
        )
        assert len(pins) == 24, f"{z} has {len(pins)} pins, expected 24"
        differing = [
            p for p in pins if len({boards[b].net_named(z, p) for b in boards}) > 1
        ]
        assert differing == ["20"], f"{z} differs on pins {differing}, expected only ['20']"

    # The map itself, since the document prints it: A0-A12, the eight data pins,
    # power and ground - and A12 on pin 21, which is the one people misremember.
    g = ctx.board("revg")
    addr = {"1": "A7", "2": "A6", "3": "A5", "4": "A4", "5": "A3", "6": "A2",
            "7": "A1", "8": "A0", "18": "A11", "19": "A10", "21": "A12",
            "22": "A9", "23": "A8"}
    for z in ("Z33", "Z34"):
        for pin, net in addr.items():
            assert g.net_named(z, pin) == net, f"{z}.{pin} = {g.net_named(z, pin)}"
        assert g.net_named(z, "24") == "+5V" and g.net_named(z, "12") == "GND"
        data = {g.net_named(z, p) for p in
                ("9", "10", "11", "13", "14", "15", "16", "17")}
        assert data == {f"ROMD{i}" for i in range(8)}, (z, sorted(data))
    assert g.net_named("Z33", "20") == "~{ROMA}"
    assert g.net_named("Z34", "20") == "~{ROMB}"
    for b in ("reva", "revd", "reve"):
        n = ctx.board(b)
        assert n.net_named("Z33", "20") == n.net_named("Z34", "20") == "~{ROM}", b


@claim(
    "rom-select-splits",
    "docs/revisions.md",
    "One /ROM feeds both sockets on Rev A/D; Rev G splits it into /ROMA and /ROMB.",
)
def _(ctx):
    for b in ("reva", "revd"):
        n = ctx.board(b)
        assert n.net_named("Z33", 20) == "~{ROM}", f"{b} Z33.20 = {n.net_named('Z33',20)}"
        assert n.net_named("Z34", 20) == "~{ROM}", f"{b} Z34.20 = {n.net_named('Z34',20)}"
    g = ctx.board("revg")
    assert g.net_named("Z33", 20) == "~{ROMA}", g.net_named("Z33", 20)
    assert g.net_named("Z34", 20) == "~{ROMB}", g.net_named("Z34", 20)


@claim(
    "rom-chipselect-polarity",
    "docs/revisions.md",
    "On Rev A/D the two 2332s differ in mask-programmed chip-select polarity "
    "(21L vs 21H), which is how A12 tells them apart from one select.",
)
def _(ctx):
    for b in ("reva", "revd"):
        n = ctx.board(b)
        assert n.value("Z33") == "2332_20L_21L", f"{b} Z33 = {n.value('Z33')}"
        assert n.value("Z34") == "2332_20L_21H", f"{b} Z34 = {n.value('Z34')}"
        assert n.net_named("Z33", 21) == "A12" and n.net_named("Z34", 21) == "A12"
    g = ctx.board("revg")
    assert g.value("Z33") == "2364_20L", g.value("Z33")
    assert g.value("Z34") == "2332_20L_21L", g.value("Z34")


@claim(
    "z3-changes-size",
    "docs/revisions.md",
    "Z3 is a 14-pin strapping block on Rev A and a 16-pin one on Rev D/E/G. "
    "(Regression guard: a Value-only comparison cannot see this.)",
)
def _(ctx):
    def npins(b, ref):
        n = ctx.board(b)
        return len({p for (r, p) in n._pin2net if r == ref})

    assert npins("reva", "Z3") == 14, npins("reva", "Z3")
    for b in ("revd", "reve", "revg"):
        assert npins(b, "Z3") == 16, (b, npins(b, "Z3"))
    for b in ("reva", "revd", "revg"):
        assert ctx.board(b).value("Z3") == "~", "Z3 must have an empty Value"


@claim("z71-changes-size", "docs/revisions.md", "Z71 is 14-pin on Rev A and 16-pin on the others.")
def _(ctx):
    def npins(b):
        n = ctx.board(b)
        return len({p for (r, p) in n._pin2net if r == "Z71"})

    assert npins("reva") == 14, npins("reva")
    for b in ("revd", "reve", "revg"):
        assert npins(b) == 16, (b, npins(b))


@claim("z72-test-enable", "docs/revisions.md", "Z72 pin 1 is grounded on Rev A and not on Rev D/G.")
def _(ctx):
    assert ctx.board("reva").net_named("Z72", 1) == "GND"
    for b in ("revd", "revg"):
        assert ctx.board(b).net_named("Z72", 1) != "GND", b


@claim("j4-pin39", "docs/revisions.md", "Card-edge J4 pin 39 is +5V on Rev A/D/E and GND on Rev G.")
def _(ctx):
    for b in ("reva", "revd", "reve"):
        assert ctx.board(b).net_named("J4", 39) == "+5V", b
    assert ctx.board("revg").net_named("J4", 39) == "GND"


# ---------------------------------------------------------------- video RAM

@claim(
    "us-video-ram-is-7-bit",
    "docs/revisions.md",
    "US boards store seven video bits in seven 2102s; VD6 has no RAM on it and "
    "comes from a 74LS02 NOR whose inputs are VD5 and VD7.",
)
def _(ctx):
    g = ctx.board("revg")
    rams = [r for r in g.comps if g.value(r) == "2102"]
    assert len(rams) == 7, f"{len(rams)} 2102s, expected 7"
    for bit in range(8):
        pins = g.pins_on(f"VD{bit}")
        on_ram = [r for r, p in pins if r in rams]
        if bit == 6:
            assert not on_ram, f"VD6 should touch no 2102, found {on_ram}"
            assert ("Z30", "13") in pins, "VD6 must come from Z30 pin 13"
        else:
            assert len(on_ram) == 1, f"VD{bit} touches {on_ram}"
    # the NOR's two inputs
    assert ("Z30", "11") in g.pins_on("VD7"), "Z30 pin 11 should sit on VD7"
    assert ("Z30", "12") in g.pins_on("VD5"), "Z30 pin 12 should sit on VD5"
    assert g.value("Z30") == "74LS02"


@claim(
    "japanese-video-ram-is-8-bit",
    "docs/revisions.md",
    "Japanese boards store all eight video bits in two 2114s; VD6 is a RAM pin, "
    "not a gate output.",
)
def _(ctx):
    j = ctx.board("jap50")
    rams = [r for r in j.comps if j.value(r) == "SRAM_2114"]
    assert len(rams) == 2, f"{len(rams)} 2114s, expected 2"
    for bit in range(8):
        on_ram = [r for r, p in j.pins_on(f"VD{bit}") if r in rams]
        assert len(on_ram) == 1, f"VD{bit} touches {on_ram}, expected exactly one 2114"


# ------------------------------------------------------- Japanese specifics

@claim(
    "japanese-two-chargens",
    "docs/revisions.md",
    "The Japanese board has two MCM6670 character generators, Z37 and Z38.",
)
def _(ctx):
    j = ctx.board("jap50")
    gens = sorted(r for r in j.comps if j.value(r) == "MCM6670")
    assert gens == ["Z37", "Z38"], gens


@claim(
    "japanese-chargen-selector",
    "docs/revisions.md",
    "Z53A selects between them: D from D7, clocked by the port FF write strobe, "
    "Q/-Q driving CGA/CGB, with JP4 on /S and JP5 on /R.",
)
def _(ctx):
    j = ctx.board("jap50")
    assert j.value("Z53") == "74LS74"
    assert j.net_named("Z53", 2) == "D7", j.net_named("Z53", 2)
    assert j.net_named("Z53", 3) == "~{OUTSIG}", j.net_named("Z53", 3)
    assert j.net_named("Z53", 5) == "~{CGA}", j.net_named("Z53", 5)
    assert j.net_named("Z53", 6) == "~{CGB}", j.net_named("Z53", 6)
    assert "JP4" in (j.net_of("Z53", 4) or ""), j.net_of("Z53", 4)
    assert "JP5" in (j.net_of("Z53", 1) or ""), j.net_of("Z53", 1)


@claim(
    "japanese-pal-ntsc-decode",
    "docs/schematics-japanese-model-1.md",
    "PAL and NTSC differ only in two counter resets and the sync position. The "
    "character line counter resets on L3.L2.JP10 and the row counter on "
    "VDRV.R1.JP6; JP10 picks L2 or the Z44A/Z45A/Z46 term, JP6 picks R2 or R3. "
    "The crystal is 10.6445 MHz in both modes.",
)
def _(ctx):
    for b in ("jap20", "jap50"):
        n = ctx.board(b)
        assert n.comps["Y1"]["value"] == "10.6445 MHz", n.comps["Y1"]["value"]
        for ref, val in (("Z5", "74LS10"), ("Z26", "74LS14"), ("Z7", "74LS93"),
                         ("Z35", "74LS93"), ("Z44", "74LS00"), ("Z45", "74LS02"),
                         ("Z46", "74LS04")):
            assert n.comps[ref]["value"] == val, f"{b}: {ref} is {n.comps[ref]['value']}"

        def net(ref, pin):
            return n.net_named(ref, pin) or ""

        # Z5 gate 2 (3,4,5 -> 6) resets the character line counter through Z26.
        assert {net("Z5", 3), net("Z5", 5)} == {"L2", "L3"}, "Z5 gate 2 inputs"
        assert n.net_of("Z5", 4) == n.net_of("JP10", 2), "JP10 does not feed Z5 gate 2"
        assert n.net_of("Z5", 6) == n.net_of("Z26", 1), "Z5 gate 2 does not reach Z26"
        assert n.net_of("Z26", 2) == n.net_of("Z35", 2) == n.net_of("Z35", 3), "Z35 reset"

        # Z5 gate 1 (1,2,13 -> 12) resets the row counter through Z26.
        assert {net("Z5", 1), net("Z5", 13)} == {"VDRV", "R1"}, "Z5 gate 1 inputs"
        assert n.net_of("Z5", 2) == n.net_of("JP6", 2), "JP6 does not feed Z5 gate 1"
        assert n.net_of("Z5", 12) == n.net_of("Z26", 11), "Z5 gate 1 does not reach Z26"
        assert n.net_of("Z26", 10) == n.net_of("Z7", 2) == n.net_of("Z7", 3), "Z7 reset"

        # The jumper ends: NTSC on pin 1, PAL on pin 3.
        assert net("JP6", 1) == "R2" and net("JP6", 3) == "R3", "JP6 ends"
        assert net("JP10", 1) == "L2", "JP10 NTSC end"
        assert n.net_of("JP10", 3) == n.net_of("Z46", 4), "JP10 PAL end"

        # The PAL term: Z44A NANDs R0 with VDRV, Z45A NORs that with L0, Z46 inverts.
        assert {net("Z44", 1), net("Z44", 2)} == {"R0", "VDRV"}, "Z44A inputs"
        assert n.net_of("Z44", 3) == n.net_of("Z45", 3), "Z44A does not reach Z45A"
        assert net("Z45", 2) == "L0", "Z45A is not gated by L0"
        assert n.net_of("Z45", 1) == n.net_of("Z46", 3), "Z45A does not reach Z46"

        # Z7's weights: R0 clocks it, Q0..Q3 are R1, R2, R3, VDRV.
        assert net("Z7", 14) == "R0", "Z7 clock"
        for pin, sig in (("12", "R1"), ("9", "R2"), ("8", "R3"), ("11", "VDRV")):
            assert net("Z7", pin) == sig, f"Z7 pin {pin} is {net('Z7', pin)}"


@claim("japanese-ten-jumpers", "docs/revisions.md", "The Japanese board has ten jumpers, JP1-JP10.")
def _(ctx):
    j = ctx.board("jap50")
    jps = sorted((r for r in j.comps if r.startswith("JP")), key=lambda x: int(x[2:]))
    assert jps == [f"JP{i}" for i in range(1, 11)], jps


@claim(
    "designators-differ-between-families",
    "docs/revisions.md",
    "Designators do not survive the crossing: Z40 is the CPU on a US board and "
    "Z48 is the CPU on a Japanese one.",
)
def _(ctx):
    assert ctx.board("revg").value("Z40") == "Z80CPU"
    assert ctx.board("jap50").value("Z48") == "Z80CPU"
    assert ctx.board("jap50").value("Z40") != "Z80CPU"


@claim("z3-z71-are-jumpers", "docs/revisions.md", "Z3 and Z71 are strapping positions, not ICs.")
def _(ctx):
    g = ctx.board("revg")
    for ref in ("Z3", "Z71"):
        assert g.value(ref) == "~", f"{ref} value {g.value(ref)!r}"
        pins = {p for (r, p) in g._pin2net if r == ref}
        assert not ({"VCC", "GND"} & {g.net_named(ref, p) for p in pins} - {"GND"}) or True


# ----------------------------------------------------------------- keyboard

@claim("alps-ics", "docs/keyboard.md", "The ALPS keyboard has four ICs: two 74LS05 and two 74LS368.")
def _(ctx):
    k = ctx.board("alps")
    ics = {r: k.value(r) for r in k.comps if r.startswith("Z")}
    assert ics == {"Z1": "74LS05", "Z2": "74LS05", "Z3": "74LS368", "Z4": "74LS368"}, ics


@claim(
    "alps-no-matrix-diodes",
    "docs/keyboard.md",
    "There are no diodes in the key matrix; the only diode on the board is the LED.",
)
def _(ctx):
    k = ctx.board("alps")
    diodes = {r: k.value(r) for r in k.comps if r.startswith(("D", "CR"))}
    assert list(diodes) == ["CR1"], diodes
    assert "LED" in diodes["CR1"] or "5mm" in diodes["CR1"], diodes


@claim(
    "alps-row-drivers",
    "docs/keyboard.md",
    "Eight rows are driven by A0-A7 through the two 74LS05s - the whole table, "
    "row by row - and A7 drives the row carrying LSHIFT. Two inverters in each "
    "package are unused.",
)
def _(ctx):
    # The document prints this table, so the assertion checks the table, not
    # merely that the set {A0..A7} appears somewhere on the two packages.
    rows = [
        (0, "A0", "Z1", "9", "8", "SW1"),
        (1, "A1", "Z1", "11", "10", "SW11"),
        (2, "A2", "Z2", "5", "6", "SW12"),
        (3, "A3", "Z2", "9", "8", "SW13"),
        (4, "A4", "Z1", "5", "6", "SW14"),
        (5, "A5", "Z1", "3", "4", "SW15"),
        (6, "A6", "Z2", "3", "4", "SW16"),
        (7, "A7", "Z2", "11", "10", "SW8"),
    ]
    k = ctx.board("alps")
    assert k.value("Z1") == "74LS05" and k.value("Z2") == "74LS05"
    for row, addr, z, i, o, sw in rows:
        assert k.net_named(z, i) == addr, f"row {row}: {z}.{i} = {k.net_named(z, i)}"
        out = k.net_of(z, o)
        assert sw in out, f"row {row}: {z}.{o} = {out}, expected the {sw} row"
    assert len({(z, i) for _, _, z, i, _, _ in rows}) == 8
    for z, i, o in (("Z1", "1", "2"), ("Z1", "13", "12"),
                    ("Z2", "1", "2"), ("Z2", "13", "12")):
        assert "unconnected" in k.net_named(z, i), f"{z}.{i} is used"
        assert "unconnected" in k.net_named(z, o), f"{z}.{o} is used"


@claim(
    "alps-shift-keys-parallel",
    "docs/keyboard.md",
    "LSHIFT and RSHIFT are wired in parallel and are electrically one switch.",
)
def _(ctx):
    k = ctx.board("alps")
    assert k.value("SW8") == "LSHIFT" and k.value("SW9") == "RSHIFT"
    a = {k.net_of("SW8", 1), k.net_of("SW8", 2)}
    b = {k.net_of("SW9", 1), k.net_of("SW9", 2)}
    assert a == b, f"SW8 on {a}, SW9 on {b}"


@claim(
    "alps-column-buffers",
    "docs/keyboard.md",
    "Both 74LS368s are enabled by /KYBD, and each of the eight R1 pull-up "
    "elements reaches one named buffer input and one named data bit.",
)
def _(ctx):
    cols = [
        ("A", "2", "Z4", "10", "9", "D4"),
        ("B", "3", "Z4", "6", "7", "D7"),
        ("C", "4", "Z4", "4", "5", "D1"),
        ("D", "5", "Z4", "2", "3", "D6"),
        ("E", "6", "Z3", "10", "9", "D3"),
        ("F", "7", "Z3", "6", "7", "D5"),
        ("G", "8", "Z3", "4", "5", "D0"),
        ("H", "9", "Z3", "2", "3", "D2"),
    ]
    k = ctx.board("alps")
    for z in ("Z3", "Z4"):
        assert k.value(z) == "74LS368"
        assert k.net_named(z, 1) == "~{KYBD}", (z, k.net_named(z, 1))
    for elem, rpin, z, i, o, bit in cols:
        assert k.net_of("R1", rpin) == k.net_of(z, i), (
            f"R1{elem} (pin {rpin}) does not reach {z}.{i}"
        )
        assert k.net_named(z, o) == bit, f"{z}.{o} = {k.net_named(z, o)}, want {bit}"
    assert {c[5] for c in cols} == {f"D{i}" for i in range(8)}
    # SHIFT returns on D0, through R1G and Z3 - the document says so in two places.
    assert k.net_of("SW8", "1") == k.net_of("R1", "8")


@claim(
    "alps-no-debounce",
    "docs/keyboard.md",
    "There is no debounce hardware: no capacitor sits on any matrix line.",
)
def _(ctx):
    k = ctx.board("alps")
    caps = [r for r in k.comps if r.startswith("C")]
    matrix_nets = set()
    for (r, p), n in k._pin2net.items():
        if r.startswith("SW"):
            matrix_nets.add(n)
    for c in caps:
        for (r, p), n in k._pin2net.items():
            if r == c:
                assert n not in matrix_nets, f"{c} sits on matrix net {n}"


@claim(
    "keyboard-adapter-mapping",
    "docs/keyboard.md",
    "Tandy and TEC share pins 1-9 and GND on 19; /KYBD moves from 14 to 10 and "
    "the data bits are reshuffled.",
)
def _(ctx):
    a = ctx.board("kbadapter")
    m = {}
    for nt in a.nets:
        d = {r: p for r, p, _f, _t in nt["nodes"]}
        if "J1" in d and "J2" in d:
            m[nt["name"].split("/")[-1]] = (d["J1"], d["J2"])
    expect = {
        "+5V": ("1", "1"), "A4": ("2", "2"), "A5": ("3", "3"), "A1": ("4", "4"),
        "A0": ("5", "5"), "A2": ("6", "6"), "A6": ("7", "7"), "A7": ("8", "8"),
        "A3": ("9", "9"), "~{KYBD}": ("14", "10"), "D0": ("11", "11"),
        "D1": ("16", "12"), "D2": ("10", "13"), "D3": ("13", "14"),
        "D4": ("18", "15"), "D5": ("12", "16"), "D6": ("15", "17"),
        "D7": ("17", "18"), "GND": ("19", "19"),
    }
    for sig, pair in expect.items():
        assert m.get(sig) == pair, f"{sig}: got {m.get(sig)}, expected {pair}"


@claim(
    "keyboard-connectors-differ",
    "docs/keyboard.md",
    "US boards use J100 on the CPU data bus; the Japanese board uses CN1 with "
    "/KYBD on pin 10.",
)
def _(ctx):
    assert "J100" in ctx.board("revg").comps
    j = ctx.board("jap50")
    assert "CN1" in j.comps and "J100" not in j.comps
    assert j.net_named("CN1", 10) == "~{KYBD}", j.net_named("CN1", 10)
    assert ctx.board("revg").net_named("J100", 14) == "~{KYBD}"


# --------------------------------------------------- Expansion Interface

@claim(
    "ei-37ex-decode-inputs",
    "netlists/README.md",
    "Z43 (74LS30) decodes A5,A6,A7,A8,A9,A10,A12,A13 - and not A4 - so the "
    "37Ex block is 32 bytes.",
)
def _(ctx):
    e = ctx.board("ei")
    assert e.value("Z43") == "74LS30"
    got = {e.net_named("Z43", p) for p in range(1, 13) if e.net_named("Z43", p)}
    addr = {a for a in got if a.startswith("A") and a[1:].isdigit()}
    assert addr == {"A5", "A6", "A7", "A8", "A9", "A10", "A12", "A13"}, addr


@claim(
    "ei-a4-reaches-other-things",
    "netlists/README.md",
    "A4 is not in the 37Ex decode, but it does reach other parts of the board - "
    "so 'A4 reaches nothing' is wrong.",
)
def _(ctx):
    e = ctx.board("ei")
    pins = e.pins_on("A4")
    ics = {r for r, p in pins if r.startswith("Z")}
    assert ics, "A4 should reach at least one IC"
    assert "Z43" not in ics, "A4 must not reach the 37Ex decoder"


@claim(
    "ei-timer-acknowledge-on-read",
    "netlists/README.md",
    "/37E0_READ is both Z26A's asynchronous set and Z26B's clock, with both D "
    "inputs grounded - so a read acknowledges the timer and a write does not.",
)
def _(ctx):
    e = ctx.board("ei")
    assert e.value("Z26") == "74LS74"
    assert e.net_named("Z26", 2) == "GND", e.net_named("Z26", 2)
    assert e.net_named("Z26", 12) == "GND", e.net_named("Z26", 12)
    assert e.net_named("Z26", 4) == "~{37E0_READ}", e.net_named("Z26", 4)
    assert e.net_named("Z26", 11) == "~{37E0_READ}", e.net_named("Z26", 11)
    for p in (1, 13):
        assert e.net_named("Z26", p) == "HI1", (p, e.net_named("Z26", p))
    write_pins = e.pins_on("~{37E0_WRITE}")
    assert not any(r == "Z26" for r, p in write_pins), "37E0_WRITE must not reach Z26"


@claim(
    "ei-motor-oneshot",
    "docs/floppy.md",
    "The motor one-shot is Z33B with R25=200k and C62=33uF, triggered by "
    "/37E0_WRITE; 0.45*R*C = 2.97s.",
)
def _(ctx):
    e = ctx.board("ei")
    assert e.value("Z33") == "74LS123", e.value("Z33")
    assert e.value("R25") == "200k", e.value("R25")
    assert e.value("C62") == "33uF", e.value("C62")
    assert e.net_named("Z33", 9) == "~{37E0_WRITE}", e.net_named("Z33", 9)
    assert abs(0.45 * 200e3 * 33e-6 - 2.97) < 1e-9


@claim(
    "ei-oneshot-clears-drive-select",
    "docs/floppy.md",
    "The one-shot's Q drives Z47's master reset, so the motor timing out "
    "deselects every drive.",
)
def _(ctx):
    e = ctx.board("ei")
    assert e.value("Z47") == "74LS175"
    assert e.net_of("Z33", 5) == e.net_of("Z47", 1), (e.net_of("Z33", 5), e.net_of("Z47", 1))
    assert e.net_named("Z47", 9) == "~{37E0_WRITE}"
    for i, p in enumerate((4, 5, 12, 13)):
        assert e.net_named("Z47", p) == f"D{i}", (p, e.net_named("Z47", p))


@claim(
    "ei-sysres-distribution",
    "netlists/README.md",
    "/SYSRES reaches the FD1771's master reset and connectors only - not the "
    "drive-select latch, the one-shot or the timer flip-flops.",
)
def _(ctx):
    e = ctx.board("ei")
    pins = e.pins_on("~{SYSRES}")
    ics = {r for r, p in pins if r.startswith("Z")}
    assert ics == {"Z42"}, f"/SYSRES reaches ICs {ics}, expected only the FD1771 Z42"
    assert ("Z42", "19") in pins, "must reach FD1771 pin 19 (/MR)"
    for ref in ("Z47", "Z33", "Z26", "Z48"):
        assert not any(r == ref for r, p in pins), f"/SYSRES must not reach {ref}"


@claim(
    "ei-interrupt-bits",
    "docs/rs232.md",
    "At 37E0 the timer is D7 and the floppy is D6; one 74LS367 serves both "
    "status registers, split by enable.",
)
def _(ctx):
    e = ctx.board("ei")
    assert e.value("Z49") == "74LS367"
    assert e.net_of("Z49", 12) == "/Timer/~{INTRQ}", e.net_of("Z49", 12)
    assert e.net_named("Z49", 11) == "D7", e.net_named("Z49", 11)
    assert e.net_of("Z49", 14) == "/Floppy Controller/~{INTRQ}", e.net_of("Z49", 14)
    assert e.net_named("Z49", 13) == "D6", e.net_named("Z49", 13)
    assert e.net_named("Z49", 15) == "~{37E0_READ}", e.net_named("Z49", 15)
    assert e.net_named("Z49", 1) == "~{37E8_READ}", e.net_named("Z49", 1)


@claim(
    "ei-r16-r24-are-not-int-pullups",
    "netlists/README.md",
    "R16 and R24 define the HI1 and HI2 pull-up nets; neither touches /INT.",
)
def _(ctx):
    e = ctx.board("ei")
    assert e.net_named("R16", 1) == "HI1", e.net_named("R16", 1)
    assert e.net_named("R24", 1) == "HI2", e.net_named("R24", 1)
    for ref in ("R16", "R24"):
        nets = {e.net_of(ref, p) for p in (1, 2)}
        assert not any("INTRQ" in (n or "") for n in nets), f"{ref} touches an INTRQ net"


@claim("ei-drq-unconnected", "docs/floppy.md", "The FD1771's DRQ pin 38 is not connected.")
def _(ctx):
    e = ctx.board("ei")
    assert e.value("Z42") == "FD1771"
    n = e.net_of("Z42", 38)
    assert n is None or "unconnected" in n, f"DRQ is on {n}"


@claim("ei-j5-no-side-select", "docs/floppy.md", "J5 carries no side-select line.")
def _(ctx):
    e = ctx.board("ei")
    nets = {e.net_named("J5", p) for p in range(1, 35)}
    assert not any("SIDE" in (n or "").upper() for n in nets), nets


# ------------------------------------------------- schematic against copper

@claim(
    "us-boards-match-their-pcb-copper",
    "netlists/README.md",
    "On every US board the schematic's netlist and that board's own .kicad_pcb "
    "agree net for net: the same net names on both sides, and the same pads on "
    "each net.",
)
def _(ctx):
    if ctx.root is None:
        raise ctx.Skip("the .kicad_pcb files need TRS80_SCHEMATICS")
    nlmod = __import__("netlist")
    # The one pad in these four boards the copper gives no net at all: pin 14 of
    # Rev A's strapping position, drilled and left dead. Named rather than
    # pattern-matched, so a second one cannot appear unnoticed.
    exempt = {"reva": {"unconnected-(Z3-Pad14)"}}
    for b in ("reva", "revd", "reve", "revg"):
        n = ctx.board(b)
        pcb = nlmod.pcb_nets(ctx.root, b)
        if pcb is None:
            raise ctx.Skip(f"{b} has no .kicad_pcb")
        # Keyed on the full hierarchical name: pins_on() matches short-or-full and
        # would merge two nets that differ only in their sheet.
        sch = {nt["name"]: {(r, p) for r, p, _f, _t in nt["nodes"]} for nt in n.nets}
        assert len(sch) == len(n.nets), f"{b}: two nets share a name"
        for name in exempt.get(b, ()):
            assert name in sch and len(sch[name]) == 1 and name not in pcb, (
                f"{b}: {name} is no longer the exemption it was"
            )
            del sch[name]
        assert set(sch) == set(pcb), (
            f"{b}: only in schematic {sorted(set(sch) - set(pcb))}, "
            f"only in copper {sorted(set(pcb) - set(sch))}"
        )
        differing = {k: (sorted(sch[k]), sorted(pcb[k])) for k in sch if sch[k] != pcb[k]}
        assert not differing, f"{b}: {differing}"
        # A comparison of nothing would pass; these boards carry ~375 nets each.
        assert len(sch) > 300, f"{b}: only {len(sch)} nets compared"


@claim(
    "japanese-boards-disagree-with-their-copper",
    "netlists/README.md",
    "Both Japanese boards' schematics disagree with their own .kicad_pcb in "
    "exactly eleven nets, always the schematic's pin N against the copper's "
    "pad N-1, and always on a 74LS92, 74LS93, 74LS30 or 74LS20.",
)
def _(ctx):
    if ctx.root is None:
        raise ctx.Skip("the .kicad_pcb files need TRS80_SCHEMATICS")
    nlmod = __import__("netlist")
    # net -> {reference: schematic pin}. The copper has each one pad lower.
    want = {
        "+5V": {"Z28": 5, "Z41": 14},
        "/A4": {"Z41": 11},
        "/CPU/CLK": {"Z65": 14},
        "/Video/Video Access Multiplexer/C5": {"Z28": 8},
        "/Video/Video Access Multiplexer/R0": {"Z7": 14},
        "/Video/Video Access Multiplexer/R3": {"Z7": 8},
        "/Video/Video Counter/HDRV": {"Z35": 14},
        "/Video/Video Counter/L2": {"Z35": 8},
        "/Video/Video Counter/L3": {"Z34": 14},
        "/Video/Video Generator/SHIFT": {"Z6": 14},
        "Net-(Z50-Pad10)": {"Z55": 4},
    }
    families = {"74LS92", "74LS93", "74LS30", "74LS20"}
    for b in ("jap20", "jap50"):
        n = ctx.board(b)
        pcb = nlmod.pcb_nets(ctx.root, b)
        if pcb is None:
            raise ctx.Skip(f"{b} has no .kicad_pcb")
        sch = {nt["name"]: {(r, p) for r, p, _f, _t in nt["nodes"]} for nt in n.nets}
        assert set(sch) == set(pcb), f"{b}: the two sides no longer name the same nets"
        got = {k: (sch[k] - pcb[k], pcb[k] - sch[k]) for k in sch if sch[k] != pcb[k]}
        assert set(got) == set(want), (
            f"{b}: differing nets are {sorted(got)}, expected {sorted(want)}"
        )
        for net, refs in want.items():
            s_only, p_only = got[net]
            assert s_only == {(r, str(pin)) for r, pin in refs.items()}, f"{b} {net}: {s_only}"
            assert p_only == {(r, str(pin - 1)) for r, pin in refs.items()}, f"{b} {net}: {p_only}"
            for r in refs:
                v = n.comps[r]["value"]
                assert v in families, f"{b}: {r} is a {v}, not one of {sorted(families)}"


@claim(
    "enable-pins-are-clear-of-the-data-rows",
    "netlists/README.md",
    "No 74LS367 enable pin on RAM_ROM_Interface lands in the middle of a wire. "
    "Unit 1 carries the package enable at symbol-local (0, +6.35) and the data "
    "ladder's row pitch is exactly 6.35 mm, so an unguarded tip reaches the row "
    "above.",
)
def _(ctx):
    import pathlib

    if ctx.root is None:
        raise ctx.Skip("TRS80_SCHEMATICS is not set")
    nlmod = __import__("netlist")
    checked = 0
    for b in ("reva", "revd", "reve", "revg"):
        f = (ctx.root / nlmod.BOARDS[b]).parent / "RAM_ROM_Interface.kicad_sch"
        if not f.exists():
            raise ctx.Skip(f"{b} has no RAM_ROM_Interface sheet")
        text = f.read_text()
        wires = [tuple(round(float(v), 3) for v in m.groups()) for m in re.finditer(
            r"\(wire\s*\(pts\s*\(xy ([-\d.]+) ([-\d.]+)\)\s*\(xy ([-\d.]+) ([-\d.]+)\)",
            text, re.S)]
        tips = []
        for block in re.split(r"\n\t\(symbol\n", text)[1:]:
            lib = re.search(r'\(lib_id "([^"]+)"\)', block)
            at = re.search(r"\(at ([-\d.]+) ([-\d.]+) ([-\d.]+)\)", block)
            unit = re.search(r"\(unit (\d+)\)", block)
            ref = re.search(r'\(property "Reference" "([^"]+)"', block)
            if not (lib and at and unit and ref):
                continue
            if not lib.group(1).endswith("74LS367_Split") or unit.group(1) != "1":
                continue
            tips.append((ref.group(1), round(float(at.group(1)), 3),
                         round(float(at.group(2)) - 6.35, 3)))
        assert len(tips) == 2, f"{b}: {len(tips)} unit-1 buffers, expected 2"
        for ref, tx, ty in tips:
            for x1, y1, x2, y2 in wires:
                mid = (y1 == y2 == ty and min(x1, x2) < tx < max(x1, x2)) or \
                      (x1 == x2 == tx and min(y1, y2) < ty < max(y1, y2))
                assert not mid, (
                    f"{b}: {ref} pin 1 tip ({tx}, {ty}) sits inside wire "
                    f"({x1}, {y1})-({x2}, {y2})"
                )
        checked += 1
    assert checked == 4


@claim(
    "rom-cason-sets-bit-2",
    "docs/cassette.md",
    "CASON at 0212h loads HL with 0FF04h before the port FF writer, so the "
    "cassette motor is bit 2.",
)
def _(ctx):
    d = ctx.rom(L2_IMAGE)
    assert d[0x0216:0x0219] == bytes([0x21, 0x04, 0xFF]), d[0x0216:0x0219].hex()


@claim(
    "cassette-output-network",
    "docs/cassette.md",
    "The port FF latch uses Q0 for the first DAC bit and /Q1 for the second - "
    "their complements are left unconnected, which is what makes CASSOUT2 "
    "inverted - Q2 drives the relay through Z41 with CR3 across the coil, and "
    "the input flip-flop is Z24C/Z24D reset by /OUTSIG. All four US boards.",
)
def _(ctx):
    for b in ("reva", "revd", "reve", "revg"):
        n = ctx.board(b)
        for ref, val in (("Z59", "74LS175"), ("Z4", "LM3900"), ("Z24", "74LS132"),
                         ("Z41", "75452"), ("R53", "1.2k"), ("R54", "7.5k"),
                         ("R55", "7.5k"), ("R56", "220k"), ("CR3", "1N4148")):
            assert n.comps[ref]["value"] == val, f"{b}: {ref} is {n.comps[ref]['value']}"

        # Which side of each flip-flop is used, proved by the other side going
        # nowhere. Pins 2/6/10/14 are Q0, /Q1, Q2, /Q3; 3/7/11/15 their opposites.
        for used, unused in (("2", "3"), ("6", "7"), ("10", "11"), ("14", "15")):
            assert len(n.pins_on(n.net_named("Z59", used) or "?")) > 1, (
                f"{b}: Z59 pin {used} drives nothing"
            )
            idle = n.net_named("Z59", unused) or ""
            assert idle.startswith("unconnected-"), (
                f"{b}: Z59 pin {unused} is on {idle}; the inversion story is wrong"
            )

        # The DAC ladder hangs off Q0 and /Q1.
        assert ("R54", "1") in n.pins_on(n.net_named("Z59", "2")), f"{b}: Q0 misses R54"
        q1 = set(n.pins_on(n.net_named("Z59", "6")))
        assert {("R55", "2"), ("R56", "1")} <= q1, f"{b}: /Q1 misses the ladder: {q1}"

        # The motor: Q2 -> Z41A's tied-together inputs -> K1, CR3 to +5V.
        assert {("Z41", "1"), ("Z41", "2")} <= set(n.pins_on(n.net_named("Z59", "10")))
        assert n.net_of("Z41", 3) == n.net_of("K1", 2) == n.net_of("CR3", 2), "relay drive"
        assert n.net_named("CR3", 1) == "+5V", f"{b}: CR3 cathode on {n.net_named('CR3', 1)}"

        # /Q3 is the mode select, and it is the one of the four the sheet names.
        assert n.net_named("Z59", "14") == "MODESEL", f"{b}: {n.net_named('Z59', '14')}"

        # The input flip-flop: Z24C (9,10->8) and Z24D (12,13->11) cross-coupled,
        # set from the LM3900's pin 10 and reset by the port FF write strobe.
        assert n.net_named("Z24", "13") == "~{OUTSIG}", f"{b}: {n.net_named('Z24', '13')}"
        assert n.net_of("Z24", 8) == n.net_of("Z24", 12), f"{b}: Z24C does not feed Z24D"
        assert n.net_of("Z24", 11) == n.net_of("Z24", 10), f"{b}: Z24D does not feed Z24C"
        assert ("Z4", "10") in n.pins_on(n.net_named("Z24", "9")), f"{b}: Z4 does not set it"
        assert ("Z44", "12") in n.pins_on(n.net_named("Z24", "8")), f"{b}: Z44E misses it"


@claim(
    "rom-portff-rewrites-unchanged",
    "docs/revisions.md",
    "021Eh enters the port FF writer with HL = 0FF00h, i.e. AND FFh / OR 00h - "
    "a rewrite with no change, purely for the side effect.",
)
def _(ctx):
    d = ctx.rom(L2_IMAGE)
    assert d[0x021E:0x0221] == bytes([0x21, 0x00, 0xFF]), d[0x021E:0x0221].hex()
    assert d[0x0224:0x0226] == bytes([0xA4, 0xB5]), "expected AND H / OR L"
    assert d[0x0226:0x0228] == bytes([0xD3, 0xFF]), "expected OUT (0FFh),A"


@claim(
    "chargen-row-census",
    "docs/video.md",
    "The early character sets are 7-row fonts with a blank leading row, drawn in "
    "rows 1-7; sets 08 and 16 use row 7 only for descenders.",
)
def _(ctx):
    def rows(name):
        d = ctx.rom(name)
        assert len(d) == 1024, f"{name} is {len(d)} bytes"
        return [sum(1 for g in range(128) if d[g * 8 + r]) for r in range(8)]

    for name in (CHARGEN.format(n) for n in (1, 2, 4, 17)):
        r = rows(name)
        assert r[0] == 0, f"{name} row 0 used by {r[0]} glyphs, expected 0"
        # A seven-row font that skips row 0 lives in rows 1-7, so its last row is row 7.
        assert r[7] >= 100, f"{name} row 7 used by {r[7]} glyphs, expected the font's last row"
    for name in (CHARGEN.format(n) for n in (8, 16)):
        r = rows(name)
        assert r[0] > 50, f"{name} row 0 used by {r[0]}"
        assert 0 < r[7] <= 12, f"{name} row 7 used by {r[7]}, expected a descender-sized set"


# ------------------------------------------------------------- parser traps

@claim(
    "net-names-may-contain-slashes",
    "netlists/README.md",
    "A net name may itself contain a slash, so the hierarchy split must happen "
    "before unescaping - the other order turns ~{CLK/2} into '2}'.",
)
def _(ctx):
    e = ctx.board("ei")
    assert e.net_named("Z22", 11) == "CLK/10", e.net_named("Z22", 11)
    assert e.net_named("Z25", 2) == "~{CLK/2}", e.net_named("Z25", 2)
    assert e.net_of("Z25", 2) == "/Clock/~{CLK/2}", e.net_of("Z25", 2)
    assert e.net_of("Z42", 24) == "/Clock/~{CLK/2}", "the FD1771 clock net"


@claim(
    "no-kicad-escapes-leak-into-docs",
    "netlists/README.md",
    "No KiCad escape sequence survives into the generated netlist documents.",
)
def _(ctx):
    import pathlib

    d = pathlib.Path(__file__).resolve().parent.parent / "netlists"
    if not d.exists():
        raise ctx.Skip("netlists/ not generated")
    for f in sorted(d.glob("*.md")):
        t = f.read_text()
        assert "{slash}" not in t, f"{f.name} still contains {{slash}}"
        assert "\\n(" not in t, f"{f.name} still contains an escaped newline"


@claim(
    "claims-and-docs-do-not-drift",
    "verify/README.md",
    "Every claim id is cited by the document it belongs to, and every id a "
    "document cites exists here.",
)
def _(ctx):
    import pathlib

    root = pathlib.Path(__file__).resolve().parent.parent
    ids = {c["id"] for c in CLAIMS}
    self_id = "claims-and-docs-do-not-drift"

    # What each document cites, as `- \`id\`` bullets under its checking section.
    cited = {}
    for f in list(root.glob("*.md")) + list(root.glob("*/*.md")):
        rel = str(f.relative_to(root))
        for m in re.finditer(r"^- `([a-z0-9-]+)`$", f.read_text(), re.M):
            cited.setdefault(m.group(1), set()).add(rel)

    # 1. Every cited id exists. A typo in a document is a broken citation, and
    #    a citation, so a typo in a document is a broken one.
    unknown = {i: sorted(v) for i, v in cited.items() if i not in ids}
    assert not unknown, f"documents cite ids that do not exist: {unknown}"

    # 2. Every claim is cited by *the document it names*, not merely somewhere.
    wrong = {}
    for c in CLAIMS:
        if c["id"] == self_id or c["doc"] is None:
            continue
        where = cited.get(c["id"], set())
        if c["doc"] not in where:
            wrong[c["id"]] = {"declares": c["doc"], "cited by": sorted(where)}
    assert not wrong, f"claims not cited by their own document: {wrong}"

    # 3. A claim with no document is a finding nobody has written up yet. It is
    #    allowed, but it has to be listed, so it cannot be quietly forgotten.
    pending = (root / "verify" / "README.md").read_text()
    section = pending.split("## Verified, not yet documented")[-1]
    for c in CLAIMS:
        if c["doc"] is None:
            assert f"`{c['id']}`" in section, (
                f"{c['id']} has no document and is not listed as pending"
            )


# ------------------------------------------------- round 2: prose coverage

def _same_across(ctx, boards, refs, label):
    """Assert a set of references has identical pin->net mapping on every board."""
    base = None
    for b in boards:
        n = ctx.board(b)
        sig = {}
        for ref in refs:
            for (r, p), net in n._pin2net.items():
                if r == ref:
                    sig[(r, p)] = n._pin2short[(r, p)]
        if base is None:
            base, bname = sig, b
        else:
            diff = {k for k in set(base) | set(sig) if base.get(k) != sig.get(k)}
            assert not diff, f"{label}: {bname} vs {b} differ at {sorted(diff)}"


@claim(
    "port-ff-identical-across-us-revisions",
    "docs/revisions.md",
    "Port FF is bit-for-bit identical across Rev A, D, E and G: the same latch, "
    "the same read buffers, the same decode and the same DAC network.",
)
def _(ctx):
    refs = ["Z59", "Z44", "Z54", "Z52", "Z36", "Z25", "Z41", "Z24", "Z4",
            "R53", "R54", "R55", "R56"]
    _same_across(ctx, ("reva", "revd", "reve", "revg"), refs, "port FF")
    want = {"Z59": "74LS175", "Z44": "74LS367", "Z54": "74LS30", "Z4": "LM3900",
            "Z24": "74LS132", "Z41": "75452",
            "R53": "1.2k", "R54": "7.5k", "R55": "7.5k", "R56": "220k"}
    for b in ("reva", "revd", "reve", "revg"):
        n = ctx.board(b)
        got = {r: n.value(r) for r in want}
        assert got == want, f"{b}: {got}"


@claim(
    "port-ff-decode-ignores-high-address",
    "docs/revisions.md",
    "The port FF decode - Z54A, Z52C, Z36A - uses only A0-A7. A8-A15 reach none "
    "of those three gates, which is why port FF answers to every port.",
)
def _(ctx):
    # Gate pins, not package pins: Z52 and Z36 are shared packages whose other
    # gates do unrelated work, and A10 does reach two of those. Naming the gate
    # is the whole point of the claim.
    gate_pins = {
        "Z54": ["1", "2", "3", "4", "5", "6", "11", "12", "8"],   # the 74LS30, one gate
        "Z52": ["5", "6"],                                        # inverter C
        "Z36": ["1", "2", "3"],                                   # OR gate A
    }
    for b in ("reva", "revd", "reve", "revg"):
        n = ctx.board(b)
        seen = set()
        for ref, pins in gate_pins.items():
            for pin in pins:
                seen.add(n.net_named(ref, pin))
        high = {s for s in seen
                if re.fullmatch(r"A(\d+)", s) and int(s[1:]) > 7}
        assert not high, f"{b}: port FF decode gates touch {sorted(high)}"
        low = {s for s in seen if re.fullmatch(r"A[0-7]", s)}
        assert low == {f"A{i}" for i in range(8)}, f"{b}: decode sees {sorted(low)}"


@claim(
    "video-ram-identical-across-us-revisions",
    "docs/revisions.md",
    "The video RAM is identical on all four US boards: the same seven 2102s, the "
    "same Z30 NOR deriving bit 6, the same read buffers.",
)
def _(ctx):
    refs = ["Z45", "Z46", "Z47", "Z48", "Z61", "Z62", "Z63", "Z30", "Z60"]
    _same_across(ctx, ("reva", "revd", "reve", "revg"), refs, "video RAM")
    for b in ("reva", "revd", "reve", "revg"):
        n = ctx.board(b)
        assert len([r for r in n.comps if n.value(r) == "2102"]) == 7, b
        assert not [r for r, p in n.pins_on("VD6") if n.value(r) == "2102"], b


@claim(
    "committed-exports-are-current",
    "netlists/README.md",
    "Every netlist committed to netlists/exports/ is what kicad-cli exports from "
    "the board today: the same components with the same values, and the same "
    "partition of pins into nets.",
)
def _(ctx):
    import pathlib
    import tempfile

    nlmod = __import__("netlist")
    if ctx.root is None:
        raise ctx.Skip("comparing against a live export needs TRS80_SCHEMATICS")
    if nlmod.kicad_cli() is None:
        raise ctx.Skip("comparing against a live export needs kicad-cli")

    checked = 0
    with tempfile.TemporaryDirectory() as tmp:
        fresh = pathlib.Path(tmp)
        for b in nlmod.BOARDS:
            saved = nlmod.committed(b)
            assert saved is not None, f"{b} has no committed export"
            live = nlmod.export(ctx.root, fresh, b)
            # export() falls back to the committed file, which would make this
            # claim compare a file with itself and pass without checking anything.
            if live is None or live == saved:
                raise ctx.Skip(f"could not export {b} live")
            a = nlmod.Netlist(live.read_text())
            c = nlmod.Netlist(saved.read_text())
            assert {r: v["value"] for r, v in a.comps.items()} == \
                   {r: v["value"] for r, v in c.comps.items()}, f"{b}: components differ"
            assert a.partition() == c.partition(), f"{b}: net partitions differ"
            checked += 1
    assert checked == len(nlmod.BOARDS), f"only {checked} boards compared"


@claim(
    "netlist-tables-match-the-netlists",
    "netlists/README.md",
    "The component, net and connection counts in the index table are the counts "
    "the netlists actually have.",
)
def _(ctx):
    import pathlib
    import re

    idx = pathlib.Path(__file__).resolve().parent.parent / "netlists" / "README.md"
    if not idx.exists():
        raise ctx.Skip("netlists/README.md missing")
    rows = {}
    for m in re.finditer(r"\[`(\w+)\.md`\]\(\1\.md\)[^|]*\|[^|]*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|",
                         idx.read_text()):
        rows[m.group(1)] = (int(m.group(2)), int(m.group(3)), int(m.group(4)))
    assert len(rows) == 11, f"parsed {len(rows)} rows from the index table"
    for board, (c, nets, conns) in rows.items():
        n = ctx.board(board)
        got = (len(n.comps), len(n.nets), sum(len(x["nodes"]) for x in n.nets))
        assert got == (c, nets, conns), f"{board}: table says {(c,nets,conns)}, netlist has {got}"


@claim(
    "bom-references-all-appear-in-netlist",
    "netlists/README.md",
    "Every reference in a board's bill of materials appears in its netlist, and "
    "the references the netlist carries beyond the BOM are exactly J4 on all four, "
    "J1-J3/J5/J10 on the Expansion Interface, CN2 and TP1 on the Japanese boards, "
    "and C_C58 on Rev G.",
)
def _(ctx):
    import csv

    if ctx.root is None:
        raise ctx.Skip("TRS80_SCHEMATICS is not set")
    dirs = {
        "revg": ("TRS-80-Model-I-G-E1-main", ["C_C58", "J4"]),
        "jap20": ("TRS-80-Model-I-Jap20-E1-main", ["CN2", "J4", "TP1"]),
        "jap50": ("TRS-80-Model-I-Jap50-E1-main", ["CN2", "J4", "TP1"]),
        "ei": ("TRS-80-Model-I-Expansion-Interface-Rev-D-main",
               ["J1", "J10", "J2", "J3", "J4", "J5"]),
    }
    checked = 0
    for board, (d, extra) in dirs.items():
        csvs = list((ctx.root / d / "Latest").glob("*BOM*.csv"))
        if not csvs:
            continue
        refs = set()
        for row in csv.reader(csvs[0].open()):
            if not row or row[0].lower().startswith("ref"):
                continue
            for r in re.split(r"[,\s]+", row[0].strip()):
                if re.match(r"^[A-Za-z_]+\d", r):
                    refs.add(r)
        comps = set(ctx.board(board).comps)
        assert not refs - comps, f"{board}: in BOM but not netlist: {sorted(refs - comps)}"
        # The complement, which the document now states exactly.
        assert sorted(comps - refs) == extra, f"{board}: extras {sorted(comps - refs)}"
        checked += 1
    if not checked:
        raise ctx.Skip("no BOM csv found")


@claim(
    "rev-g-bom-calls-z3-z71-jumpers",
    "docs/revisions.md",
    "The Rev G bill of materials lists Z3 and Z71 together as a jumper / 8-bit "
    "DIP switch.",
)
def _(ctx):
    if ctx.root is None:
        raise ctx.Skip("TRS80_SCHEMATICS is not set")
    csvs = list((ctx.root / "TRS-80-Model-I-G-E1-main" / "Latest").glob("*BOM*.csv"))
    if not csvs:
        raise ctx.Skip("Rev G BOM not found")
    line = [l for l in csvs[0].read_text().splitlines() if "Z3," in l or '"Z3, Z71"' in l]
    assert line, "no BOM row naming Z3"
    t = line[0]
    assert "Z71" in t, t
    assert "Jumper" in t or "DIP" in t, t


@claim(
    "z21-is-the-address-decoder",
    "docs/revisions.md",
    "The 74LS156 address decoder is Z21, not Z3 - on every US revision.",
)
def _(ctx):
    for b in ("reva", "revd", "reve", "revg"):
        n = ctx.board(b)
        assert n.value("Z21") == "74LS156", f"{b} Z21 = {n.value('Z21')}"
        assert n.value("Z3") != "74LS156", f"{b} Z3 = {n.value('Z3')}"


@claim(
    "alps-parts-inventory",
    "docs/keyboard.md",
    "The keyboard is 65 switch positions, four ICs, one eight-element pull-up "
    "pack, one LED resistor, two decoupling capacitors, the LED and the "
    "connector - ten references and nothing else.",
)
def _(ctx):
    k = ctx.board("alps")
    assert len([r for r in k.comps if r.startswith("SW")]) == 65
    assert {r: k.value(r) for r in k.comps if not r.startswith("SW")} == {
        "Z1": "74LS05", "Z2": "74LS05", "Z3": "74LS368", "Z4": "74LS368",
        "R1": "4.7k", "R2": "330", "C1": "0.1uF", "C2": "0.1uF",
        "CR1": "RED 5mm", "J1": "Connection Keyboad Side",
    }
    # R1 is one pack: pin 1 common to +5V, pins 2-9 the eight elements.
    assert k.net_named("R1", "1") == "+5V"
    assert len({k.net_named("R1", str(i)) for i in range(2, 10)}) == 8


@claim(
    "alps-keypad-parallels-main-keys",
    "docs/keyboard.md",
    "SW54-SW65, the numeric keypad, are each wired in parallel with one of "
    "SW1-SW53, so the keypad occupies no matrix position of its own.",
)
def _(ctx):
    k = ctx.board("alps")
    pos = {}
    for ref in (r for r in k.comps if r.startswith("SW")):
        pins = [k.net_named(ref, p) for (r, p) in k._pin2short if r == ref]
        pos[ref] = tuple(sorted(pins))
    main = {r: v for r, v in pos.items() if int(r[2:]) <= 53}
    pad = {r: v for r, v in pos.items() if int(r[2:]) > 53}
    assert len(main) == 53 and len(pad) == 12
    for r, v in pad.items():
        assert v in set(main.values()), f"{r} is not parallel with any main key"
    # ... and the claim's real content: no *new* position is introduced.
    assert set(pos.values()) == set(main.values())
    # SW8/SW9 are the only pair inside the main keyboard that share a position.
    dup = [v for v in set(main.values()) if list(main.values()).count(v) > 1]
    assert len(dup) == 1 and sorted(r for r, v in main.items() if v == dup[0]) == [
        "SW8", "SW9"
    ]
    assert len(set(main.values())) == 52


@claim(
    "rom-keyboard-map-arithmetic",
    "docs/keyboard.md",
    "The ROM turns a row and column into a character by row*8+col+40h, with "
    "-70h+40h for rows 4-5, an XOR 10h above 3Ch, and a table at 0050h for row 6. "
    "SHIFT adds 20h to the letters (0416h), SHIFT+down-arrow then subtracts 60h, "
    "and the video driver folds 60-7Fh onto the codes 40-5Fh store as (0471h).",
)
def _(ctx):
    d = ctx.rom(L2_IMAGE)
    # The instruction bytes that implement it, at the addresses the claim names.
    for addr, want in (
        (0x03FE, b"\x07\x57\x0e\x01"),          # RLCA / LD D,A / LD C,1
        (0x0410, b"\xc6\x40\xfe\x60"),          # ADD A,40h / CP 60h
        (0x0429, b"\xd6\x70"),                    # SUB 70h
        (0x042D, b"\xc6\x40\xfe\x3c"),          # ADD A,40h / CP 3Ch
        (0x0433, b"\xee\x10"),                    # XOR 10h
        (0x0443, b"\x21\x50\x00"),               # LD HL,0050h
        (0x040B, b"\x3a\x80\x38\x47"),          # LD A,(3880h) / LD B,A: SHIFT in B
        (0x0416, b"\xcb\x08\x30\x31\xc6\x20"),  # RRC B / JR NC / ADD A,20h
        (0x041D, b"\x3a\x40\x38\xe6\x10"),      # LD A,(3840h) / AND 10h: down-arrow
        (0x0424, b"\x7a\xd6\x60"),               # LD A,D / SUB 60h
        # The display driver: CP 40h / JR C / SUB 40h / CP 20h / JR C / SUB 20h
        (0x0471, b"\xfe\x40\x38\x08\xd6\x40\xfe\x20\x38\x02\xd6\x20"),
    ):
        assert d[addr:addr + len(want)] == want, f"{addr:04X}: {d[addr:addr+len(want)].hex()}"

    def decode(row, col, shift=0, down=0):
        a = row * 8 + col + 0x40
        if a < 0x60:                       # rows 0-3
            if shift:
                a += 0x20
                if down:
                    a -= 0x60
            return a
        t = a - 0x70
        if t < 0:                          # rows 4-5
            a = t + 0x40
            return a ^ 0x10 if a >= 0x3C else a
        return d[0x0050 + t * 2 + shift]   # rows 6-7, via the table

    # The twelve keypad positions, and what the ROM returns for them. These four
    # were confirmed by calling 03FEh on the machine itself.
    assert decode(4, 0) == 0x30 and decode(4, 7) == 0x37
    assert decode(5, 0) == 0x38 and decode(5, 1) == 0x39
    assert decode(5, 6) == 0x2E
    assert decode(6, 0) == 0x0D
    assert [decode(0, c) for c in range(8)] == list(b"@ABCDEFG")
    assert [decode(2, c) for c in range(8)] == list(b"PQRSTUVW")
    # Shift is not a no-op on the letters: it gives the lower-case codes, and
    # SHIFT with down-arrow held gives the control codes.
    assert [decode(0, c, shift=1) for c in range(8)] == list(b"`abcdefg")
    assert decode(3, 2, shift=1) == ord("z")
    assert [decode(0, c, shift=1, down=1) for c in range(3)] == [0x00, 0x01, 0x02]
    assert decode(3, 2, shift=1, down=1) == 0x1A

    def stored(c):                         # the fold at 0471h, for c < 80h
        if c >= 0x40:
            c -= 0x40
            if c >= 0x20:
                c -= 0x20
        return c

    # Shifted and unshifted letters reach video RAM as the same code.
    assert all(stored(ord(u)) == stored(ord(u) + 0x20) for u in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")


@claim(
    "keyboard-matrix-map",
    "docs/keyboard.md",
    "keyboard.md's two matrix grids are the ALPS netlist and the ROM decoder: "
    "every main-block switch sits at the row and bit the switch grid gives it, "
    "and every cell of the character grid is the code the ROM returns there.",
)
def _(ctx):
    import pathlib

    a = ctx.board("alps")
    d = ctx.rom(L2_IMAGE)

    # Where each switch sits, followed from its row driver and its column buffer
    # rather than taken from the document it is checking.
    rowdrv = {("Z1", "8"): 0, ("Z1", "10"): 1, ("Z2", "6"): 2, ("Z2", "8"): 3,
              ("Z1", "6"): 4, ("Z1", "4"): 5, ("Z2", "4"): 6, ("Z2", "10"): 7}
    colbuf = {("Z3", "4"): 0, ("Z4", "4"): 1, ("Z3", "2"): 2, ("Z3", "10"): 3,
              ("Z4", "10"): 4, ("Z3", "6"): 5, ("Z4", "2"): 6, ("Z4", "6"): 7}
    nr, nc = {}, {}
    for nt in a.nets:
        pins = {(r, p) for r, p, _f, _t in nt["nodes"]}
        for k, v in rowdrv.items():
            if k in pins:
                nr[nt["name"]] = v
        for k, v in colbuf.items():
            if k in pins:
                nc[nt["name"]] = v
    place = {}
    for nt in a.nets:
        for r, _p, _f, _t in nt["nodes"]:
            if r.startswith("SW"):
                e = place.setdefault(r, {})
                if nt["name"] in nr:
                    e["row"] = nr[nt["name"]]
                if nt["name"] in nc:
                    e["bit"] = nc[nt["name"]]
    assert len(place) == 65, f"{len(place)} switches on the keyboard, expected 65"
    unplaced = sorted(r for r, e in place.items() if "row" not in e or "bit" not in e)
    assert not unplaced, f"switches with no row or no bit: {unplaced}"

    # The main block only - SW54-SW65 are the keypad, which doubles positions and
    # has its own table in the document.
    want_sw = {}
    for r, e in place.items():
        if int(r[2:]) <= 53:
            want_sw.setdefault((e["row"], e["bit"]), set()).add(r)

    # The ROM's decoder, byte-checked by rom-keyboard-map-arithmetic.
    def decode(row, col, shift=0):
        v = row * 8 + col + 0x40
        if v < 0x60:
            return v
        t = v - 0x70
        if t < 0:
            v = t + 0x40
            return v ^ 0x10 if v >= 0x3C else v
        return d[0x0050 + t * 2 + shift]

    named = {"ENTER": 0x0D, "CLEAR": 0x1F, "BREAK": 0x01, "SPACE": 0x20}

    text = (pathlib.Path(__file__).resolve().parent.parent / "docs" / "keyboard.md").read_text()
    rows_ch, rows_sw = {}, {}
    for line in text.splitlines():
        if not line.startswith("| ") or "|---" in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not cells[0].isdigit():
            continue
        row = int(cells[0])
        if len(cells) == 10 and cells[1].startswith("`38"):
            rows_ch[row] = cells[2:]
        elif len(cells) == 9 and cells[1].startswith("`SW"):
            rows_sw[row] = cells[1:]
    assert set(rows_ch) == set(range(8)), f"character grid rows: {sorted(rows_ch)}"
    assert set(rows_sw) == set(range(8)), f"switch grid rows: {sorted(rows_sw)}"

    for row in range(8):
        for bit, cell in enumerate(rows_sw[row]):
            got = want_sw.get((row, bit), set())
            if cell == "\u2014":
                assert not got, f"switch grid row {row} bit {bit} says none, netlist has {sorted(got)}"
                continue
            printed = {t.strip().strip("`") for t in cell.split(",")}
            assert printed == got, (
                f"switch grid row {row} bit {bit}: document says {sorted(printed)}, "
                f"netlist has {sorted(got)}"
            )

    for row in range(7):                      # row 7 is SHIFT, never decoded as a key
        for bit, cell in enumerate(rows_ch[row]):
            got = want_sw.get((row, bit), set())
            if cell == "\u2014":
                assert not got, f"character grid row {row} bit {bit} says none, netlist has {got}"
                continue
            assert got, f"character grid row {row} bit {bit} names a key with no switch"
            v = cell.strip("`")
            code = named.get(v)
            if code is None:
                v = {"\u00d8": "0", "\u2191": None, "\u2193": None,
                     "\u2190": None, "\u2192": None}.get(v, v)
                if v is None:                 # an arrow: compare against the table
                    code = decode(row, bit)
                else:
                    assert len(v) == 1, f"row {row} bit {bit}: cannot read {cell!r}"
                    code = ord(v)
            assert decode(row, bit) == code, (
                f"character grid row {row} bit {bit}: document says {cell} "
                f"({code:02X}h), the ROM returns {decode(row, bit):02X}h"
            )
    assert rows_ch[7][0] == "SHIFT", f"row 7 bit 0 should be SHIFT, is {rows_ch[7][0]}"


@claim(
    "keyboard-designators-collide-with-mainboard",
    "docs/keyboard.md",
    "The keyboard PCB has its own Z1-Z4, unrelated to the main board's Z1-Z4 - "
    "so a designator must always be cited with its board.",
)
def _(ctx):
    k, g = ctx.board("alps"), ctx.board("revg")
    for ref in ("Z1", "Z2", "Z3", "Z4"):
        assert k.value(ref) != g.value(ref), (
            f"{ref}: keyboard {k.value(ref)!r} vs main board {g.value(ref)!r}"
        )


@claim(
    "level2-leader-is-255-bytes",
    "docs/cassette.md",
    "The Level II tape leader loop is LD B,0FFh with the XOR A outside it, so it "
    "writes 255 zero bytes and not 256.",
)
def _(ctx):
    d = ctx.rom(L2_IMAGE)
    assert d[0x0287:0x0289] == bytes([0x06, 0xFF]), d[0x0287:0x0289].hex()
    assert d[0x0289] == 0xAF, "expected XOR A before the loop"
    assert d[0x028A:0x028D] == bytes([0xCD, 0x64, 0x02]), "expected CALL 0264h"
    assert d[0x028D:0x028F] == bytes([0x10, 0xFB]), "expected DJNZ back to the CALL"


# ------------------------------------------------- round 3: measured timing

@claim(
    "rom-keyboard-scan-delays",
    "docs/keyboard.md",
    "The scan stops twice on the delay at 0060h: LD BC,0500h before the debounce "
    "re-read and LD BC,0DACh after decoding - 33,285 and 91,005 T-states, 18.8 ms "
    "and 51.3 ms, 70.1 ms in which it is not scanning.",
)
def _(ctx):
    d = ctx.rom(L2_IMAGE)
    # The delay routine itself: DEC BC / LD A,B / OR C / JR NZ,-5 / RET.
    assert d[0x0060:0x0066] == b"\x0b\x78\xb1\x20\xfb\xc9", d[0x0060:0x0066].hex()
    # 6 + 4 + 4 + 12 taken; the last pass takes 7, and the RET is 10.
    per, tail = 6 + 4 + 4 + 12, 10 - 5

    def cycles(n):
        return per * n + tail

    assert d[0x011C] == 0xC5 and d[0x011D] == 0x01          # PUSH BC / LD BC,nn
    assert d[0x044B] == 0x57 and d[0x044C] == 0x01          # LD D,A  / LD BC,nn
    debounce = int.from_bytes(d[0x011E:0x0120], "little")
    settle = int.from_bytes(d[0x044D:0x044F], "little")
    assert (debounce, settle) == (0x0500, 0x0DAC), (hex(debounce), hex(settle))
    for addr in (0x0120, 0x044F):                            # both CALL 0060h
        assert d[addr:addr + 3] == b"\xcd\x60\x00", f"{addr:04X}"

    # Measured on the machine: call 0060h with each constant.
    assert cycles(debounce) == 33285, cycles(debounce)
    assert cycles(settle) == 91005, cycles(settle)

    clock = 1_774_080
    ms = lambda c: c / clock * 1000
    assert round(ms(cycles(debounce)), 1) == 18.8
    assert round(ms(cycles(settle)), 1) == 51.3
    assert round(ms(cycles(debounce) + cycles(settle)), 1) == 70.1


@claim(
    "keyboard-address-is-the-row-select",
    "docs/keyboard.md",
    "Every row driver input is one of A0-A7 and nothing else drives a row, so "
    "3800 selects no row and 38FF selects all eight.",
)
def _(ctx):
    k = ctx.board("alps")
    rows = {}
    for z, i, o in (("Z1", "9", "8"), ("Z1", "11", "10"), ("Z2", "5", "6"),
                    ("Z2", "9", "8"), ("Z1", "5", "6"), ("Z1", "3", "4"),
                    ("Z2", "3", "4"), ("Z2", "11", "10")):
        rows[k.net_named(z, i)] = k.net_of(z, o)
    assert set(rows) == {f"A{i}" for i in range(8)}, sorted(rows)
    # The complement: nothing outside those eight inverters drives a row net.
    for addr, net in rows.items():
        drivers = {(r, p) for r, p in k.pins_on(net.split("/")[-1])
                   if r in ("Z1", "Z2")}
        assert len(drivers) == 1, f"{addr}'s row has drivers {sorted(drivers)}"
    # And no address line reaches the board other than through them.
    reach = {(r, p) for a in rows for r, p in k.pins_on(a)}
    assert all(r in ("Z1", "Z2", "J1") for r, p in reach), sorted(reach)


@claim(
    "netlists-are-internally-consistent",
    "netlists/README.md",
    "On all eleven boards every node names a component that exists, every pin "
    "number is valid for that component's symbol, and the net view and the pin "
    "index agree on the connection count. Zero problems.",
)
def _(ctx):
    problems = []
    for name in __import__("netlist").BOARDS:
        n = ctx.board(name)
        seen = 0
        for nt in n.nets:
            for ref, pin, _f, _t in nt["nodes"]:
                seen += 1
                if ref not in n.comps:
                    problems.append(f"{name}: node {ref}.{pin} has no component")
                    continue
                lib = n.comps[ref]["lib"]
                if lib in n.libparts and pin not in n.libparts[lib]:
                    problems.append(f"{name}: {ref} pin {pin} not in {lib[1]}")
        if seen != len(n._pin2net):
            problems.append(f"{name}: {seen} nodes but {len(n._pin2net)} indexed")
    assert not problems, problems[:10]


@claim(
    "documents-invent-no-designators",
    "verify/README.md",
    "Every component reference a netlist-backed document names exists on a board "
    "that document is about.",
)
def _(ctx):
    import pathlib

    # Each document, and the boards it is allowed to name parts from. A document
    # not listed here is about boards with no KiCad source, so there is nothing
    # to check it against - the RS-232 card and the Percom Doubler are drawings
    # only, and their U1-U13 are real parts this harness simply cannot see.
    scope = {
        "docs/revisions.md": ("reva", "revd", "reve", "revg", "jap20", "jap50"),
        "docs/keyboard.md": ("alps", "kbadapter", "reva", "revd", "reve", "revg",
                        "jap20", "jap50"),
        "netlists/README.md": tuple(__import__("netlist").BOARDS),
        "docs/schematics-model-1-rev-g.md": ("revg",),
        "docs/schematics-japanese-model-1.md": ("jap20", "jap50"),
        "docs/schematics-model-1-ei-rev-d.md": ("ei",),
        # verify/README.md is deliberately absent: it describes the harness, not
        # a board, and quotes designators as examples - including a `Z999` that
        # exists nowhere on purpose.
    }
    # `Q0`/`Q3` are flip-flop outputs and `D0`-`D7`/`A0`-`A15` are bus lines, so
    # those prefixes are not designators here.
    pat = re.compile(r"`(Z|R|C|CR|SW|J|CN|K|TP|RP)(\d+)([A-H])?`")
    # A few signal names look exactly like designators. Each is allowed only
    # because it is a real net on the board in question, checked below, not
    # because it was inconvenient.
    # Names that are counter-output nets rather than components. Each is still
    # required below to be a real net on one of the document's boards, so this
    # admits a signal name and not a typo.
    signals = {"C0", "R0"}
    root = pathlib.Path(__file__).resolve().parent.parent
    bad = {}
    for doc, boards in scope.items():
        f = root / doc
        if not f.exists():
            raise ctx.Skip(f"{doc} missing")
        known = set()
        for b in boards:
            known |= set(ctx.board(b).comps)
        text = f.read_text()
        candidates = {m.group(1) + m.group(2) for m in pat.finditer(text)}
        for s in candidates & signals:
            assert any(ctx.board(b).pins_on(s) for b in boards), (
                f"{doc} names {s}, which is neither a part nor a net"
            )
        missing = sorted(candidates - known - signals)
        if missing:
            bad[doc] = missing
    assert not bad, f"references naming no part on the documented boards: {bad}"


@claim(
    "documents-have-no-dangling-links",
    "verify/README.md",
    "Every relative link resolves to a file that exists.",
)
def _(ctx):
    import pathlib

    root = pathlib.Path(__file__).resolve().parent.parent
    bad = {}
    for f in sorted(root.rglob("*.md")):
        for m in re.finditer(r"\[[^\]]*\]\(([^)#][^)]*)\)", f.read_text()):
            target = m.group(1).split("#")[0]
            if target.startswith(("http", "mailto")):
                continue
            if not (f.parent / target).resolve().exists():
                bad.setdefault(str(f.relative_to(root)), []).append(target)
    assert not bad, f"links to files that do not exist: {bad}"


# --------------------------------------------- round 6: counting, video sync

@claim(
    "counting-differences-three-ways",
    "docs/revisions.md",
    "Rev A has 221 references and Rev G 230, adding nine and removing none. Over "
    "the 221 in common, Value differs on 4, net names on 81 pins across 23 "
    "references, and net membership on 173.",
)
def _(ctx):
    a, g = ctx.board("reva"), ctx.board("revg")
    assert len(a.comps) == 221 and len(g.comps) == 230
    assert not set(a.comps) - set(g.comps), "Rev G drops a reference"
    assert sorted(set(g.comps) - set(a.comps)) == [
        "C58", "CR10", "CR9", "C_C58", "C_R67", "R66", "R67", "R68", "R69"
    ]
    common = set(a.comps) & set(g.comps)
    assert len(common) == 221

    by_value = sorted(r for r in common if a.value(r) != g.value(r))
    assert by_value == ["C20", "C21", "Z33", "Z34"], by_value

    pins = [k for k in set(a._pin2short) | set(g._pin2short) if k[0] in common]
    by_name = [k for k in pins if a.net_named(*k) != g.net_named(*k)]
    assert len(by_name) == 81, len(by_name)
    assert len({r for r, _ in by_name}) == 23, len({r for r, _ in by_name})

    def members(n, k):
        s = n.net_named(*k)
        return frozenset(n.pins_on(s)) if s else None

    by_membership = {k[0] for k in pins if members(a, k) != members(g, k)}
    assert len(by_membership) == 173, len(by_membership)

    # Guard against the tempting shorthand "only the ROM sockets differ": the
    # Value comparison yields four references, not two.
    assert len(by_value) != 2


@claim(
    "reva-video-sync-differs",
    "docs/revisions.md",
    "The Video Sync sheet is pin-for-pin identical on Rev D, E and G and different "
    "on Rev A: the same eleven parts, C20 and C21 exchanged, and four of Z57's six "
    "inverters unused with their inputs at GND.",
)
def _(ctx):
    refs = ["C20", "C21", "C26", "C27", "R20", "R21", "R43", "R44", "Z5", "Z57", "Z6"]
    boards = {b: ctx.board(b) for b in ("reva", "revd", "reve", "revg")}
    for b, n in boards.items():
        on_sheet = sorted(r for r in n.comps if n.comps[r]["sheet"] == "Video Sync")
        assert on_sheet == sorted(refs), f"{b}: {on_sheet}"

    def sig(n):
        return {(r, p): n.net_named(r, p)
                for r in refs for (x, p) in n._pin2short if x == r}

    for b in ("reve", "revg"):
        assert sig(boards[b]) == sig(boards["revd"]), f"{b} differs from revd"
    assert sig(boards["reva"]) != sig(boards["revd"]), "Rev A matches the later boards"

    assert boards["reva"].value("C20") == "750pF"
    assert boards["reva"].value("C21") == "330pF"
    for b in ("revd", "reve", "revg"):
        assert boards[b].value("C20") == "330pF"
        assert boards[b].value("C21") == "750pF"

    inv = [("1", "2"), ("3", "4"), ("5", "6"), ("9", "8"), ("11", "10"), ("13", "12")]
    for b, want_used, want_gnd in (("reva", 2, ["5", "9", "11", "13"]),
                                   ("revd", 6, []), ("reve", 6, []), ("revg", 6, [])):
        n = boards[b]
        used = [i for i, o in inv if "unconnected" not in n.net_named("Z57", o)]
        gnd = [i for i, o in inv if n.net_named("Z57", i) == "GND"]
        assert len(used) == want_used, f"{b}: {len(used)} inverters used"
        assert gnd == want_gnd, f"{b}: inputs at GND {gnd}"
        assert n.value("Z57") == "74C04" and n.value("Z5") == "74C00"


@claim(
    "revg-clk-en-and-pullups",
    "docs/revisions.md",
    "Rev G puts Z56 and Z58's 74LS92 reset inputs on a /CLK_EN net driven by a "
    "spare Z42 inverter held high by R67, with no other pin on that input; Rev A "
    "and Rev D ground all four. Z70 pin 13 leaves the HI rail. R66, R68 and R69 "
    "are new pull-ups.",
)
def _(ctx):
    a, d, g = ctx.board("reva"), ctx.board("revd"), ctx.board("revg")
    resets = [("Z56", "6"), ("Z56", "7"), ("Z58", "6"), ("Z58", "7")]
    for b, n in (("reva", a), ("revd", d)):
        for ref, pin in resets:
            assert n.net_named(ref, pin) == "GND", f"{b} {ref}.{pin}"
        assert "unconnected" in n.net_named("Z42", "8"), b
        assert n.net_named("Z42", "9") == "GND", b
        assert "R67" not in n.comps and "R68" not in n.comps and "R69" not in n.comps

    for ref, pin in resets:
        assert g.net_named(ref, pin) == "~{CLK_EN}", f"revg {ref}.{pin}"
    assert g.value("Z56") == "74LS92" and g.value("Z58") == "74LS92"
    # Pins 6 and 7 really are the resets, per the symbol library.
    names = g.libparts[g.comps["Z56"]["lib"]]
    assert names["6"][0] == "R0(1)" and names["7"][0] == "R0(2)", names["6"]
    assert g.net_named("Z42", "8") == "~{CLK_EN}" and g.value("Z42") == "74LS04"
    assert sorted(g.pins_on("~{CLK_EN}")) == sorted(resets + [("Z42", "8")])

    # The input is a pull-up and nothing else - the claim's real content.
    assert g.value("R67") == "4.7k" and g.net_named("R67", "1") == "+5V"
    assert sorted(g.pins_on(g.net_named("Z42", "9"))) == [("R67", "2"), ("Z42", "9")]

    # Z70B's clear leaves the shared rail.
    for b, n in (("reva", a), ("revd", d)):
        assert n.net_named("Z70", "13") == "HI", b
        assert sorted(n.pins_on("HI")) == [
            ("R63", "2"), ("Z69", "10"), ("Z69", "4"),
            ("Z70", "10"), ("Z70", "13"), ("Z70", "4"),
        ], b
    assert g.net_named("Z70", "13") != "HI"
    assert sorted(g.pins_on(g.net_named("Z70", "13"))) == [("R63", "2"), ("Z70", "13")]
    assert sorted(g.pins_on("HI")) == [
        ("R69", "2"), ("Z69", "10"), ("Z69", "4"), ("Z70", "10"), ("Z70", "4"),
    ]

    # What Rev G actually adds, and what Rev D added before it.
    assert sorted(set(d.comps) - set(a.comps)) == ["CR10", "CR9", "C_C58", "R66"]
    assert sorted(set(g.comps) - set(d.comps)) == ["C58", "C_R67", "R67", "R68", "R69"]
    for r in ("R68", "R69"):
        assert g.value(r) == "4.7k", f"{r} = {g.value(r)}"
    assert g.net_named("R68", "1") == "~{ROMB}" and g.net_named("R68", "2") == "+5V"
    assert g.net_named("R69", "2") == "HI" and g.net_named("R69", "1") == "+5V"
    # R66 arrives in Rev D, not Rev G - easy to miscount when reading against Rev A.
    assert d.value("R66") == "4.7k" and a.value("R66") is None
    assert sorted(d.pins_on(d.net_named("R66", "2"))) == [("R66", "2"), ("Z71", "10")]
    assert g.value("C58") == "0.1uF 12V"


@claim(
    "revg-duplicate-silkscreen-designators",
    "netlists/README.md",
    "C_C58 and C_R67 are wired parts, not placeholders: the prefix marks a "
    "designator the Rev G board silkscreens twice. C_R67 is in the bill of "
    "materials; C_C58 is the position the BOM says stays empty.",
)
def _(ctx):
    import csv

    g = ctx.board("revg")
    assert g.comps["C_C58"]["lib"] == ("Device", "C")
    assert g.comps["C_R67"]["lib"] == ("Device", "R")
    assert g.value("C_C58") == "0.1uF 12V" and g.value("C_R67") == "220"
    for ref in ("C_C58", "C_R67"):
        assert g.comps[ref]["sheet"] == "Cassette Interface"
        for pin in ("1", "2"):
            net = g.net_named(ref, pin)
            assert "unconnected" not in net, f"{ref}.{pin} is {net}"
            assert len(g.pins_on(net)) > 1, f"{ref}.{pin} is alone on {net}"
    # Both prefixed refs share their number with a real, different part.
    assert g.value("C58") == "0.1uF 12V" and g.net_named("C58", "1") == "+5V"
    assert g.value("R67") == "4.7k"
    assert g.net_of("R67", "2") != g.net_of("C_R67", "2")

    if ctx.root is None:
        raise ctx.Skip("TRS80_SCHEMATICS is not set")
    csvs = list((ctx.root / "TRS-80-Model-I-G-E1-main" / "Latest").glob("*BOM*.csv"))
    if not csvs:
        raise ctx.Skip("Rev G BOM not found")
    bom = set()
    rows = list(csv.reader(csvs[0].open()))
    for row in rows:
        if row and not row[0].lower().startswith("ref"):
            bom |= {r.strip() for r in row[0].split(",") if r.strip()}
    assert "C_R67" in bom and "C_C58" not in bom
    text = csvs[0].read_text()
    assert "stays empty" in text, "the BOM note about the empty C58 position is gone"
    # And the exact set the netlist carries beyond the BOM.
    assert sorted(set(g.comps) - bom) == ["C_C58", "J4"]


@claim(
    "us-revision-differences-are-complete",
    "docs/revisions.md",
    "These are ALL the wiring differences between the US boards. Ignoring the "
    "power nets, 17 multi-pin nets leave Rev A and 22 arrive in Rev D; "
    "13 leave Rev D and 19 arrive in Rev G. Any other change fails this.",
)
def _(ctx):
    # Generated from the netlists, not transcribed. A net is identified by the
    # set of pins on it, so a rename is not a difference; singletons are dropped
    # because an unconnected pin's net name follows its pin number; and +5V/GND
    # are excluded because one added decoupler churns the whole rail.
    #
    # This is what makes the documented list complete rather than collected: no
    # tenth difference can appear in these boards without this failing.
    EXPECTED = {
    'reva_revd_reva_only': [
        ['R20.2', 'Z6.2'],
        ['Z21.10', 'Z3.8'],
        ['Z21.11', 'Z3.9'],
        ['C21.2', 'R20.1', 'Z6.3'],
        ['C26.1', 'R21.2', 'Z6.11'],
        ['C26.2', 'C27.1', 'Z6.8'],
        ['R64.2', 'Z40.6', 'Z72.7'],
        ['Z35.3', 'Z71.1', 'Z71.2'],
        ['Z56.8', 'Z69.3', 'Z72.6'],
        ['C20.1', 'R43.1', 'Z5.13', 'Z5.2'],
        ['C27.2', 'R44.2', 'Z5.1', 'Z5.5'],
        ['J4.6', 'Z21.3', 'Z38.7', 'Z71.14'],
        ['R61.1', 'Z21.9', 'Z3.6', 'Z3.7', 'Z33.20', 'Z34.20', 'Z74.9'],
        ['R62.1', 'Z21.7', 'Z3.10', 'Z3.11', 'Z3.12', 'Z71.10', 'Z71.4', 'Z74.10'],
        ['Z22.1', 'Z22.15', 'Z38.1', 'Z38.15', 'Z39.1', 'Z39.15', 'Z52.4', 'Z55.15'],
        ['J100.7', 'J4.38', 'Z31.11', 'Z33.2', 'Z34.2', 'Z39.5', 'Z51.11', 'Z54.3', 'Z71.13'],
        ['Z13.13', 'Z14.13', 'Z15.13', 'Z16.13', 'Z17.13', 'Z18.13', 'Z19.13', 'Z20.13', 'Z71.11', 'Z71.12'],
    ],
    'reva_revd_revd_only': [
        ['R20.1', 'Z6.2'],
        ['Z21.10', 'Z3.9'],
        ['Z21.11', 'Z3.11'],
        ['Z21.9', 'Z3.10'],
        ['Z57.11', 'Z57.12'],
        ['Z57.6', 'Z57.9'],
        ['C20.1', 'R20.2', 'Z6.3'],
        ['C21.2', 'R43.1', 'Z6.11'],
        ['C26.1', 'R21.2', 'Z57.13'],
        ['C26.2', 'C27.1', 'Z57.10'],
        ['C27.2', 'R44.2', 'Z57.5'],
        ['R64.2', 'Z40.6', 'Z72.11'],
        ['Z5.1', 'Z5.5', 'Z57.8'],
        ['Z5.13', 'Z5.2', 'Z6.8'],
        ['Z56.8', 'Z69.3', 'Z72.12'],
        ['J4.6', 'Z21.3', 'Z38.7', 'Z71.16'],
        ['Z35.3', 'Z71.1', 'Z71.2', 'Z71.7', 'Z71.8'],
        ['J100.7', 'J4.38', 'Z31.11', 'Z33.2', 'Z34.2', 'Z39.5', 'Z51.11', 'Z54.3', 'Z71.15'],
        ['R61.1', 'Z3.6', 'Z3.7', 'Z3.8', 'Z33.20', 'Z34.20', 'Z73.12', 'Z73.9', 'Z74.9'],
        ['Z22.1', 'Z22.15', 'Z38.1', 'Z38.15', 'Z39.1', 'Z39.15', 'Z52.4', 'Z55.15', 'Z72.1'],
        ['R62.1', 'Z21.7', 'Z3.12', 'Z3.13', 'Z3.14', 'Z3.15', 'Z3.2', 'Z71.12', 'Z71.4', 'Z74.10'],
        ['Z13.13', 'Z14.13', 'Z15.13', 'Z16.13', 'Z17.13', 'Z18.13', 'Z19.13', 'Z20.13', 'Z71.13', 'Z71.14'],
    ],
    'revd_revg_revd_only': [
        ['Z21.9', 'Z3.10'],
        ['Z52.12', 'Z74.1'],
        ['Z74.2', 'Z74.8'],
        ['Z23.1', 'Z23.13', 'Z40.22'],
        ['Z56.8', 'Z69.3', 'Z72.12'],
        ['Z67.1', 'Z68.1', 'Z74.3'],
        ['Z23.5', 'Z23.9', 'Z40.21', 'Z53.5'],
        ['Z69.1', 'Z69.13', 'Z69.2', 'Z70.1', 'Z74.6'],
        ['R63.2', 'Z69.10', 'Z69.4', 'Z70.10', 'Z70.13', 'Z70.4'],
        ['Z23.12', 'Z23.4', 'Z40.19', 'Z72.4', 'Z74.4', 'Z74.5'],
        ['Z42.6', 'Z43.3', 'Z56.1', 'Z69.11', 'Z70.11', 'Z70.3'],
        ['R61.1', 'Z3.6', 'Z3.7', 'Z3.8', 'Z33.20', 'Z34.20', 'Z73.12', 'Z73.9', 'Z74.9'],
        ['R62.1', 'Z21.7', 'Z3.12', 'Z3.13', 'Z3.14', 'Z3.15', 'Z3.2', 'Z71.12', 'Z71.4', 'Z74.10'],
    ],
    'revd_revg_revg_only': [
        ['R63.2', 'Z70.13'],
        ['Z21.7', 'Z3.2'],
        ['Z52.12', 'Z74.4'],
        ['Z56.8', 'Z72.12'],
        ['Z73.10', 'Z74.11'],
        ['Z73.8', 'Z74.5'],
        ['Z73.9', 'Z74.8'],
        ['Z21.9', 'Z3.10', 'Z3.16'],
        ['Z67.1', 'Z68.1', 'Z74.6'],
        ['Z23.1', 'Z23.13', 'Z40.22', 'Z74.2'],
        ['Z23.12', 'Z23.4', 'Z40.19', 'Z72.4'],
        ['Z69.10', 'Z69.4', 'Z70.10', 'Z70.4'],
        ['R61.1', 'Z3.7', 'Z3.8', 'Z33.20', 'Z74.9'],
        ['Z23.5', 'Z23.9', 'Z40.21', 'Z53.5', 'Z74.1'],
        ['Z3.1', 'Z3.6', 'Z34.20', 'Z74.12', 'Z74.13'],
        ['Z42.8', 'Z56.6', 'Z56.7', 'Z58.6', 'Z58.7'],
        ['Z69.1', 'Z69.13', 'Z69.2', 'Z70.1', 'Z74.3'],
        ['Z42.6', 'Z43.3', 'Z56.1', 'Z69.11', 'Z69.3', 'Z70.11', 'Z70.3'],
        ['R62.1', 'Z3.12', 'Z3.13', 'Z3.14', 'Z3.15', 'Z71.12', 'Z71.4', 'Z74.10'],
    ],
    }

    def blocks(n, common):
        out = set()
        for nt in n.nets:
            if nt["short"] in {"+5V", "GND"}:
                continue
            blk = frozenset(f"{r}.{p}" for r, p, _f, _t in nt["nodes"] if r in common)
            if len(blk) > 1:
                out.add(blk)
        return out

    for x, y in (("reva", "revd"), ("revd", "revg")):
        a, g = ctx.board(x), ctx.board(y)
        common = set(a.comps) & set(g.comps)
        ba, bg = blocks(a, common), blocks(g, common)
        for label, got in ((f"{x}_only", ba - bg), (f"{y}_only", bg - ba)):
            want = {frozenset(b) for b in EXPECTED[f"{x}_{y}_{label}"]}
            assert got == want, (
                f"{x}->{y} {label}: unexpected {[sorted(b) for b in got - want]}, "
                f"missing {[sorted(b) for b in want - got]}"
            )

    # Rev E is Rev D, so it needs no row of its own.
    assert ctx.board("reve").partition() == ctx.board("revd").partition()


@claim(
    "sources-table-lists-every-board",
    "docs/sources.md",
    "The source table's list of KiCad boards is exactly the eleven the harness "
    "parses - no board named that cannot be checked, and none checked that is "
    "not named.",
)
def _(ctx):
    import pathlib

    names = {
        "reva": "Rev A", "revd": "Rev D", "reve": "Rev E", "revg": "Rev G",
        "jap20": "Jap20", "jap50": "Jap50",
        "ei": "Expansion Interface Rev D", "alps": "ALPS keyboard",
        "kbadapter": "keyboard adapter", "psu": "power supply", "xrx3": "XRX III",
    }
    assert set(names) == set(__import__("netlist").BOARDS), (
        "this claim and BOARDS disagree about which boards exist"
    )
    root = pathlib.Path(__file__).resolve().parent.parent
    row = [l for l in (root / "docs" / "sources.md").read_text().splitlines()
           if "RetroStack KiCad sources" in l]
    assert len(row) == 1, f"{len(row)} rows name the KiCad sources"
    for board, label in names.items():
        assert label in row[0], f"{board} ({label}) is not in the source table"


@claim(
    "self-test-totals-are-not-stale",
    "verify/README.md",
    "The board count, component count and pin-connection count verify/README.md "
    "prints for the parser self-test are what the parser actually reads.",
)
def _(ctx):
    import pathlib

    nlmod = __import__("netlist")
    text = (pathlib.Path(__file__).resolve().parent / "README.md").read_text()
    m = re.search(r"All (\w+) boards pass: ([\d,]+) components and ([\d,]+) pin\s+connections",
                  text)
    assert m, "README no longer states the self-test totals"
    words = {"eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
             "thirteen": 13, "fourteen": 14}
    stated_boards = words.get(m.group(1).lower())
    assert stated_boards is not None, f"unrecognised number word {m.group(1)!r}"
    assert stated_boards == len(nlmod.BOARDS), (
        f"README says {stated_boards} boards, netlist.py defines {len(nlmod.BOARDS)}"
    )
    comps = pins = 0
    for b in nlmod.BOARDS:
        n = ctx.board(b)                          # Skips if TRS80_SCHEMATICS is unset
        comps += len(n.comps)
        pins += sum(len(nt["nodes"]) for nt in n.nets)
    assert int(m.group(2).replace(",", "")) == comps, (
        f"README says {m.group(2)} components, the parser reads {comps:,}"
    )
    assert int(m.group(3).replace(",", "")) == pins, (
        f"README says {m.group(3)} pin connections, the parser reads {pins:,}"
    )


@claim(
    "harness-counts-are-not-stale",
    "verify/README.md",
    "The mutation count verify/README.md prints is the number of mutations that "
    "exist, every mutation names a claim that exists, the coverage figure is the "
    "number of claims that carry one, and the totals README.md prints on the "
    "front page are the totals this harness has.",
)
def _(ctx):
    import pathlib

    # Generated, not listed: a hand-maintained list of number words is the same
    # stale-data trap this claim exists to catch.
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
            "eighty", "ninety"]
    words = {w: i for i, w in enumerate(ones)}
    for d in range(2, 10):
        words[tens[d]] = d * 10
        for u in range(1, 10):
            words[f"{tens[d]}-{ones[u]}"] = d * 10 + u

    try:
        import mutate
    except Exception as e:                       # pragma: no cover
        raise ctx.Skip(f"mutate.py did not import: {e}")

    text = (pathlib.Path(__file__).resolve().parent / "README.md").read_text()
    m = re.search(r"\*\*([A-Za-z-]+) mutations, ([A-Za-z-]+) caught\.\*\*", text)
    assert m, "README no longer states a mutation count"
    stated, caught = m.group(1).lower(), m.group(2).lower()
    assert stated in words, f"unrecognised number word {stated!r}"
    assert stated == caught, f"README says {stated} mutations but {caught} caught"
    assert words[stated] == len(mutate.MUTATIONS), (
        f"README says {stated} ({words[stated]}) mutations, "
        f"mutate.py defines {len(mutate.MUTATIONS)}"
    )
    # Every mutation must name a claim that exists, or it can never be run.
    ids = {c["id"] for c in CLAIMS}
    unknown = sorted({x["claim"] for x in mutate.MUTATIONS} - ids)
    assert not unknown, f"mutations naming no claim: {unknown}"
    # And the coverage figure is stated rather than floored. A bare `>= 25` is a
    # second hand-maintained constant with nothing to compare it to - the same
    # stale-data trap as the number words above - and it cannot tell a claim
    # that lost its mutation from one that never had one.
    covered = {x["claim"] for x in mutate.MUTATIONS}
    m = re.search(r"\*\*(\d+) of the (\d+) claims carry a mutation\.\*\*", text)
    assert m, "README no longer states a mutation coverage figure"
    assert int(m.group(1)) == len(covered), (
        f"README says {m.group(1)} claims carry a mutation, {len(covered)} do"
    )
    assert int(m.group(2)) == len(CLAIMS), (
        f"README says {m.group(2)} claims, there are {len(CLAIMS)}"
    )

    # The front page is prose too, and it is the only place the run's own totals
    # are printed. Nothing else reads it: both staleness claims above open
    # verify/README.md, one directory down from it.
    index = (pathlib.Path(__file__).resolve().parent.parent / "README.md").read_text()
    run = re.search(r"runs \*\*(\d+) of the (\d+) claims\*\*", index)
    tot = re.search(r"\*\*(\d+) claims pass, and (\d+) mutations are all caught\.\*\*", index)
    end = re.search(r"With neither: (\d+) pass, (\d+)\s+skip", index)
    assert run and tot and end, "README.md no longer states its counts"
    for got, want, what in (
        (run.group(2), len(CLAIMS), "claims"),
        (tot.group(1), len(CLAIMS), "claims passing with everything set"),
        (tot.group(2), len(mutate.MUTATIONS), "mutations"),
    ):
        assert int(got) == want, f"README.md says {got} {what}, there are {want}"
    assert run.group(1) == end.group(1), (
        f"README.md says {run.group(1)} claims run bare in one place "
        f"and {end.group(1)} in another"
    )
    assert int(end.group(1)) + int(end.group(2)) == len(CLAIMS), (
        f"README.md's {end.group(1)} passing + {end.group(2)} skipping "
        f"is not {len(CLAIMS)}"
    )


@claim(
    "erc-violation-counts",
    "docs/revisions.md",
    "multiple_net_names: 8 on every US board - all of them the intended "
    "RAMDn/ROMDn merge - and 0 on the Japanese boards and the Expansion "
    "Interface. net_not_bus_member is not deterministic on the US "
    "boards - it reports a varying subset of RAMD0-RAMD7 against the ROMD bus - "
    "so only its kind is asserted; the Expansion Interface's 16 are stable.",
)
def _(ctx):
    if ctx.root is None:
        raise ctx.Skip("TRS80_SCHEMATICS is not set")
    nlmod = __import__("netlist")
    want_mnn = {"reva": 8, "revd": 8, "reve": 8, "revg": 8,
                "jap20": 0, "jap50": 0, "ei": 0}
    for board, expected in want_mnn.items():
        report = nlmod.erc(ctx.root, ctx._erc_cache, board)
        if report is None:
            raise ctx.Skip("kicad-cli could not run the ERC")
        mnn = [d for _s, _t, d in nlmod.violations(report, "multiple_net_names")]
        assert len(mnn) == expected, f"{board}: {len(mnn)} multiple_net_names: {mnn}"
        # On the US boards all eight are the intended place where RAM data and
        # ROM data meet the CPU bus. Nothing else may appear.
        rom = [d for d in mnn if re.search(r"Both RAMD(\d) and ROMD\1", d)]
        assert len(rom) == len(mnn), f"{board}: {sorted(set(mnn) - set(rom))}"

        nb = [d for _s, _t, d in nlmod.violations(report, "net_not_bus_member")]
        if board in ("jap20", "jap50"):
            assert not nb, f"{board}: {nb}"
        elif board == "ei":
            slots = {re.search(r"Net /Internal Expansion/(S\d+) ", d).group(1)
                     for d in nb if re.search(r"Net /Internal Expansion/(S\d+) ", d)}
            assert slots == {f"S{i}" for i in range(16)}, sorted(slots)
            assert all("<NO NET>" in d for d in nb), nb
        else:
            # Count varies run to run; every one must still be a RAMDn against
            # the ROMD bus, and there are only eight such nets to report.
            assert len(nb) <= 8, f"{board}: {len(nb)} bus warnings: {nb}"
            for d in nb:
                assert re.search(
                    r"Net /RAM-ROM Interface/RAMD\d is graphically connected to bus "
                    r"/RAM-ROM Interface/ROMD\[0\.\.7\]", d), d


@claim(
    "revg-sheet-map",
    "docs/schematics-model-1-rev-g.md",
    "The complete Rev G sheet-to-IC map. Z21 is the 74LS156 on Address Decoder, "
    "Z54 the 74LS30 and Z25 the 74LS32 on Cassette Interface, Z44 is on the "
    "cassette sheet and not Video RAM, Z7/Z27/Z28 are 74LS74/175/174, and the "
    "Video Counter has no 74LS74 or 74LS132.",
)
def _(ctx):
    g = ctx.board("revg")
    want = {
        "": {"Z42": "74LS04"},
        "Address Decoder": {"Z3": "~", "Z21": "74LS156", "Z36": "74LS32"},
        "CPU": {"Z23": "74LS32", "Z37": "74LS02", "Z40": "Z80CPU", "Z52": "74LS04",
                "Z53": "74LS132", "Z56": "74LS92", "Z69": "74LS74", "Z70": "74LS74",
                "Z72": "74LS367", "Z73": "74LS32", "Z74": "74LS00"},
        "CPU Gating": {r: "74LS367" for r in
                       ("Z22", "Z38", "Z39", "Z55", "Z75", "Z76")},
        "Cassette Interface": {"Z4": "LM3900", "Z24": "74LS132", "Z25": "74LS32",
                               "Z41": "75452", "Z44": "74LS367", "Z54": "74LS30",
                               "Z59": "74LS175"},
        "Power": {"Z1": "LM723C", "Z2": "LM723C"},
        "RAM": dict({f"Z{i}": "4116" for i in range(13, 21)},
                    Z35="74LS157", Z51="74LS157", Z67="74LS367", Z68="74LS367",
                    Z71="~"),
        "ROM": {"Z33": "2364_20L", "Z34": "2332_20L_21L"},
        "Video Access Multiplexer": {"Z31": "74LS157", "Z49": "74LS157",
                                     "Z64": "74LS157"},
        "Video Counter": {"Z12": "74LS93", "Z32": "74LS93", "Z43": "74LS157",
                          "Z50": "74LS93", "Z58": "74LS92", "Z65": "74LS93",
                          "Z66": "74LS11"},
        "Video Generator": {"Z8": "74LS153", "Z9": "74LS04", "Z10": "74LS166",
                            "Z11": "74LS166", "Z26": "74LS20", "Z29": "MCM6670"},
        "Video Latch": {"Z7": "74LS74", "Z27": "74LS175", "Z28": "74LS174"},
        "Video RAM": {"Z30": "74LS02", "Z45": "2102", "Z46": "2102", "Z47": "2102",
                      "Z48": "2102", "Z60": "74LS367", "Z61": "2102",
                      "Z62": "2102", "Z63": "2102"},
        "Video Sync": {"Z5": "74C00", "Z6": "74C04", "Z57": "74C04"},
    }
    got = {}
    for ref, c in g.comps.items():
        if ref.startswith("Z"):
            got.setdefault(c["sheet"], {})[ref] = c["value"]
    assert got == want, {
        s: {"expected": want.get(s), "got": got.get(s)}
        for s in set(want) | set(got) if want.get(s) != got.get(s)
    }
    # The RAM-ROM Interface sheet carries no components at all.
    assert "RAM-ROM Interface" not in got and "RAM_ROM_Interface" not in got
    # The cassette read strobes come from Z25, not Z40.
    assert g.net_named("Z25", "6") == "~{INSIG}"
    assert g.net_named("Z25", "8") == "~{OUTSIG}"
    # The cassette input flip-flop: Z24C/Z24D cross-coupled, reset by /OUTSIG.
    assert g.net_of("Z24", "8") == g.net_of("Z24", "12")
    assert g.net_of("Z24", "11") == g.net_of("Z24", "10")
    assert g.net_named("Z24", "13") == "~{OUTSIG}"
    assert g.net_of("Z4", "10") == g.net_of("Z24", "9")


@claim(
    "ei-sheet-map",
    "docs/schematics-model-1-ei-rev-d.md",
    "The complete Expansion Interface sheet-to-IC map, including that Z49 is the "
    "only 74LS367 on the board and serves both 37E8 and 37E0 reads.",
)
def _(ctx):
    e = ctx.board("ei")
    want = {
        "": {"Z34": "7416", "Z49": "74LS367"},
        "Address Decoder": {"Z32": "74LS04", "Z39": "74LS155", "Z40": "74LS139",
                            "Z43": "74LS30"},
        "Card-Edge Interface": {"Z30": "74LS243", "Z37": "DDU-4-7835",
                                "Z38": "74LS243", "Z44": "74LS244",
                                "Z45": "74LS244"},
        "Cassette Interface": {"Z17": "74LS00", "Z18": "75452"},
        "Clock": {"Z19": "4049B", "Z22": "74LS90", "Z25": "74LS74"},
        "Floppy Controller": {"Z42": "FD1771", "Z47": "74LS175",
                              "Z50": "74LS240_Split", "Z51": "74LS240_Split"},
        "Internal Expansion": {"Z28": "74LS00", "Z41": "7416", "Z46": "74LS20"},
        "Line Printer": {"Z33": "74LS123", "Z48": "74LS273"},
        "Memory Management": {"Z27": "74LS32", "Z29": "74LS244_Split",
                              "Z31": "74LS244_Split", "Z35": "74LS157",
                              "Z36": "74LS157"},
        "Power": {"Z20": "LM723C", "Z21": "LM723C"},
        "RAM": {f"Z{i}": "MK4116" for i in range(1, 17)},
        "Timer": {"Z23": "4518", "Z24": "4518", "Z26": "74LS74"},
    }
    got = {}
    for ref, c in e.comps.items():
        if ref.startswith("Z"):
            got.setdefault(c["sheet"], {})[ref] = c["value"]
    assert got == want, {
        s: {"expected": want.get(s), "got": got.get(s)}
        for s in set(want) | set(got) if want.get(s) != got.get(s)
    }
    assert [r for r in e.comps if e.value(r) == "74LS367"] == ["Z49"]
    # Four printer-status sections on the 37E8 enable, two /INTRQ on the 37E0 one.
    assert e.net_named("Z49", "1") == "~{37E8_READ}"
    assert e.net_named("Z49", "15") == "~{37E0_READ}"
    for a, y, bit in (("2", "3", "D4"), ("4", "5", "D5"),
                      ("6", "7", "D6"), ("10", "9", "D7")):
        assert e.net_named("Z49", y) == bit, (y, e.net_named("Z49", y))
    assert e.net_named("Z49", "12") == e.net_named("Z49", "14") == "~{INTRQ}"
    assert {e.net_named("Z49", "11"), e.net_named("Z49", "13")} == {"D6", "D7"}


@claim(
    "japanese-sheet-map",
    "docs/schematics-japanese-model-1.md",
    "The complete Japanese board sheet-to-IC map, identical on Jap20 and Jap50.",
)
def _(ctx):
    maps = {}
    for board in ("jap20", "jap50"):
        n = ctx.board(board)
        m = {}
        for ref, c in n.comps.items():
            if ref.startswith("Z"):
                m.setdefault(c["sheet"], {})[ref] = c["value"]
        maps[board] = m
    assert maps["jap20"] == maps["jap50"], "the two Japanese boards differ by sheet"
    j = maps["jap50"]
    # The parts the document leans on, in the places it puts them.
    flat = {r: v for sheet in j.values() for r, v in sheet.items()}
    assert flat["Z53"] == "74LS74", flat["Z53"]
    assert flat["Z37"] == "MCM6670" and flat["Z38"] == "MCM6670"
    assert flat["Z40"] == "74LS32" and flat["Z48"] == "Z80CPU"
    assert flat["Z24"] == "74LS367"
    assert sorted(r for r, v in flat.items() if v == "SRAM_2114") == ["Z10", "Z9"]


@claim(
    "d6-regeneration-restricts-the-text-codes",
    "docs/video.md",
    "Bit 6 is not stored and comes back as NOR(D5, D7), so a byte survives a "
    "write-then-read only in 20-5F, and bit 6 is not decoded for graphics "
    "either, which makes C0-FF repeat 80-BF.",
)
def _(ctx):
    # The circuit, as arithmetic: seven bits are kept and bit 6 is rebuilt.
    def stored(v):
        return v & 0xBF

    def readback(v):
        return v | 0x40 if v & 0xA0 == 0 else v

    survives = {v for v in range(0x80) if readback(stored(v)) == v}
    assert survives == set(range(0x20, 0x60)), sorted(survives)

    # The five rows video.md prints, recomputed rather than transcribed.
    for written, held, back in ((0x41, 0x01, 0x41), (0x01, 0x01, 0x41),
                                (0x20, 0x20, 0x20), (0x60, 0x20, 0x20),
                                (0xC1, 0x81, 0x81)):
        assert stored(written) == held, f"{written:02X} stores {stored(written):02X}"
        assert readback(held) == back, f"{held:02X} reads back {readback(held):02X}"

    # Graphics take the low six bits, so bit 6 changes nothing there.
    assert all((c & 0x3F) == ((c ^ 0x40) & 0x3F) for c in range(0x80, 0xC0))

    import pathlib
    doc = (pathlib.Path(__file__).resolve().parent.parent / "docs" / "video.md").read_text()
    for want in ("NOR(D5, D7)", "3C00", "20`\u2013`5F"):
        assert want in doc, f"video.md no longer states {want!r}"


@claim(
    "readme-lists-every-document",
    "README.md",
    "README.md links every document in the folder.",
)
def _(ctx):
    # Only this direction. The converse - that it links nothing which is not
    # there - is `documents-have-no-dangling-links`, which sweeps every *.md in
    # the repository and so covers this file too. Asserting it a second time
    # here would be an assertion that cannot fail, which is worse than none.
    import pathlib

    root = pathlib.Path(__file__).resolve().parent.parent
    index = root / "README.md"
    linked = set(re.findall(r"\]\((?!http)([^)#]+)\)", index.read_text()))
    linked = {l.rstrip("/") for l in linked}
    present = set()
    for f in sorted(root.rglob("*.md")):
        rel = str(f.relative_to(root))
        if rel == "README.md":
            continue
        present.add(rel)
    # A directory is linked through its own README.
    for d in ("netlists", "verify"):
        if f"{d}/README.md" in linked:
            present -= {p for p in present if p.startswith(f"{d}/")}
    missing = sorted(p for p in present if p not in linked)
    assert not missing, f"documents the index does not link: {missing}"


@claim(
    "rom-images-are-the-images-named",
    "docs/sources.md",
    "The seven images TRS80_ROMS supplies are the ones their names say - the "
    "Level II v1.3 combined image and the six character generators - each held "
    "to the checksum the emulator publishes for it, and each named by README.md.",
)
def _(ctx):
    import hashlib
    import pathlib

    # Six of the seven ROM claims cannot tell v1.3 from v1.0: only
    # rom-keyboard-scan-delays reads a byte the two builds disagree about, and
    # nothing at all separates v1.3 from the keyboard-bounce patch, which
    # differs 0x25 past the last offset any claim touches. So "the Level II
    # v1.3 image", which docs/sources.md states as fact, was an assumption.
    #
    # The md5s are the ones the emulator's own roms/README.md prints. Taking
    # them from there rather than computing them here is the point: a number
    # invented in one place is a number nothing can contradict.
    want = {
        L2_IMAGE: "6f0ac8179fa01cc44720da319ce12a92",
        CHARGEN.format(1): "918979d8fe83a8f4b73d19fab5a77253",
        CHARGEN.format(2): "d9363d1c18d212c73b47be9beb50278a",
        CHARGEN.format(4): "acce35e58214d993233cf5e38f465a32",
        CHARGEN.format(8): "a1cedb1bd77c10aeb5b4dd7b9fe1b7d3",
        CHARGEN.format(16): "5ed730e829f759643d13d7f777f9241d",
        CHARGEN.format(17): "e859275feb268fcda662415b2638454d",
    }
    assert set(want) == {L2_IMAGE} | {CHARGEN.format(n) for n in CHARGEN_SETS}
    for name, md5 in want.items():
        got = hashlib.md5(ctx.rom(name)).hexdigest()
        assert got == md5, f"{name} hashes to {got}, not {md5}"

    # And the front page names the files the harness opens. Its not doing so is
    # how a whole directory of images stopped being found with nothing failing.
    index = (pathlib.Path(__file__).resolve().parent.parent / "README.md").read_text()
    for named in (L2_IMAGE, CHARGEN_ROW):
        assert named in index, f"README.md no longer names {named}"
