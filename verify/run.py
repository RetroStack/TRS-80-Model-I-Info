#!/usr/bin/env python3
"""Run every claim in claims.py and report.

    python3 verify/run.py                 # run the claims
    python3 verify/run.py --self-test     # validate the parser first
    python3 verify/run.py --list          # list claim ids

Two environment variables point at third-party material this repository does not
ship, and every claim needing one skips cleanly when it is unset:

    TRS80_SCHEMATICS   RetroStack's KiCad board repositories
    TRS80_ROMS         a directory of Model I ROM images

With neither set the run still passes; it just checks less, and says so.
"""

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import claims as claims_mod  # noqa: E402
import netlist as nl  # noqa: E402

REPO = HERE.parent
CACHE = Path(os.environ.get("TMPDIR", "/tmp")) / "trs80-verify-cache"

# ROM images are third-party firmware and are not in this repository. TRS80_ROMS
# names a directory laid out the way the emulator's `roms/` is - `system/` for
# the combined system images, `char/` for the character generators - and a
# `roms/` inside this repository or beside it is used if one happens to be
# there, which is what lets this run unchanged inside a tree that already has
# the images.
ROM_DIRS = [Path(d) for d in (os.environ.get("TRS80_ROMS"),) if d]
ROM_DIRS += [REPO / "roms", REPO.parent / "roms"]


class Skip(Exception):
    pass


class Ctx:
    Skip = Skip

    _erc_cache = CACHE

    def __init__(self, root):
        self.root = root
        self._boards = {}

    def board(self, name):
        if name not in self._boards:
            n = nl.load(self.root, CACHE, name)
            if n is None:
                raise Skip(f"could not export {name}")
            self._boards[name] = n
        return self._boards[name]

    def rom(self, name):
        """Read a ROM image by its path under a ROM directory.

        `name` carries the subdirectory - `system/…` or `char/…` - because that
        is how the images are laid out where they come from, and because a
        directory that holds the right bytes under the wrong names is a
        misconfiguration the message below has to be able to describe.
        """
        for d in ROM_DIRS:
            p = d / name
            if p.exists():
                return p.read_bytes()
        raise Skip(f"{name} not found; point TRS80_ROMS at a directory laid out "
                   f"like the emulator's roms/ (system/ and char/)")


def self_test(ctx):
    """Validate the parser against KiCad's own XML export - a different format
    down a different code path. This is what makes the rest trustworthy."""
    print("Parser self-test (s-expression vs KiCad XML)")
    bad = checked = 0
    for name in nl.BOARDS:
        try:
            mine = ctx.board(name)
        except Skip as e:
            print(f"  {name:10} SKIP  {e}")
            continue
        xp = nl.export(ctx.root, CACHE, name, "kicadxml")
        if xp is None:
            print(f"  {name:10} SKIP  no XML export")
            continue
        root = ET.parse(xp).getroot()
        xc = {c.get("ref"): nl.unescape(c.findtext("value") or "")
              for c in root.find("components")}
        xn = {}
        for n in root.find("nets"):
            for nd in n.findall("node"):
                xn[(nd.get("ref"), nd.get("pin"))] = nl.unescape(n.get("name"))
        mc = {r: c["value"] for r, c in mine.comps.items()}
        mn = dict(mine._pin2net)

        def part(m):
            g = {}
            for k, v in m.items():
                g.setdefault(v, set()).add(k)
            return {frozenset(v) for v in g.values()}

        ok = mc == xc and set(mn) == set(xn) and part(mn) == part(xn)
        bad += 0 if ok else 1
        checked += 1
        print(f"  {name:10} {'OK' if ok else 'MISMATCH':9} "
              f"{len(mc):4} comps  {len(mn):5} pins")

    # A skip is not a pass. Counting only mismatches let this print "parser
    # validated" on a tree where every board skipped and nothing was compared
    # at all - the one failure mode a self-test must not have, since the rest
    # of the harness rests on this having happened.
    total = len(nl.BOARDS)
    if checked == 0:
        print(f"  => validated nothing: all {total} boards skipped. The XML "
              f"cross-check needs kicad-cli and TRS80_SCHEMATICS.\n")
        return False
    if bad:
        print(f"  => {bad} board(s) mismatched\n")
        return False
    print(f"  => parser validated on {checked} of {total} boards\n")
    return True


def main():
    args = sys.argv[1:]
    if "--list" in args:
        for c in claims_mod.CLAIMS:
            print(f"{c['id']:34} {c['doc']}")
        return 0

    root = os.environ.get("TRS80_SCHEMATICS")
    root = Path(root).expanduser() if root else None
    if root and not root.exists():
        print(f"TRS80_SCHEMATICS={root} does not exist")
        return 2
    ctx = Ctx(root)
    claims_mod.__dict__["Skip"] = Skip

    if "--self-test" in args:
        if not self_test(ctx):
            return 1

    npass = nfail = nskip = 0
    failures = []
    for c in claims_mod.CLAIMS:
        try:
            c["fn"](ctx)
            npass += 1
            status = "PASS"
        except Skip as e:
            nskip += 1
            status = f"SKIP ({e})"
        except AssertionError as e:
            nfail += 1
            status = "FAIL"
            failures.append((c, str(e)))
        except Exception as e:  # a broken assertion is a failure too
            nfail += 1
            status = "ERROR"
            failures.append((c, f"{type(e).__name__}: {e}"))
        print(f"  {status:34} {c['id']}")

    print(f"\n{npass} passed, {nfail} failed, {nskip} skipped")
    if failures:
        print("\nFailures:")
        for c, msg in failures:
            print(f"\n  {c['id']}  [{c['doc']}]")
            print(f"    claim: {c['text']}")
            print(f"    why:   {msg}")
    if nskip and not root:
        print("\n(Set TRS80_SCHEMATICS to the directory holding RetroStack's KiCad "
              "repositories to run the netlist-backed claims.)")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
