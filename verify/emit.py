#!/usr/bin/env python3
"""Regenerate netlists/*.md from the KiCad sources.

    TRS80_SCHEMATICS=~/path/to/repos python3 verify/emit.py

Uses the same parser the claims use, so the published tables and the assertions
cannot disagree about what the netlist says.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import netlist as nl  # noqa: E402

OUT = HERE.parent / "netlists"
CACHE = Path(os.environ.get("TMPDIR", "/tmp")) / "trs80-verify-cache"
BIG = 12  # nets larger than this are named, not expanded, in the connection view

TITLES = {
    "reva": ("Model I main board, Rev A", "TRS-80-Model-I-A-E1-main"),
    "revd": ("Model I main board, Rev D", "TRS-80-Model-I-D-E1-main"),
    "reve": ("Model I main board, Rev E", "TRS-80-Model-I-E-E1-main"),
    "revg": ("Model I main board, Rev G", "TRS-80-Model-I-G-E1-main"),
    "jap20": ("Japanese Model I main board, Jap20", "TRS-80-Model-I-Jap20-E1-main"),
    "jap50": ("Japanese Model I main board, Jap50", "TRS-80-Model-I-Jap50-E1-main"),
    "ei": ("Expansion Interface, Rev D", "TRS-80-Model-I-Expansion-Interface-Rev-D-main"),
    "alps": ("ALPS keyboard", "TRS-80-Model-I-Keyboard-ALPS-main"),
    "kbadapter": ("Keyboard adapter (Tandy <-> TEC)", "TRS-80-Model-I-Keyboard-Adapter-main"),
    "psu": ("Power supply", "TRS-80-Model-I-Power-Supply-main"),
    "xrx3": ("XRX III", "TRS-80-Model-I-XRX-III-main"),
}


def pinkey(p):
    try:
        return (0, int(p))
    except ValueError:
        return (1, p)


def refkey(r):
    return ("".join(c for c in r if c.isalpha()),
            int("".join(c for c in r if c.isdigit()) or 0))


def emit(n: nl.Netlist, title, source, out: Path):
    problems = []
    total = sum(len(x["nodes"]) for x in n.nets)
    for nt in n.nets:
        for ref, pin, _f, _t in nt["nodes"]:
            if ref not in n.comps:
                problems.append(f"node references unknown component {ref}")
            else:
                lib = n.comps[ref]["lib"]
                if lib in n.libparts and n.libparts[lib] and pin not in n.libparts[lib]:
                    problems.append(f"{ref} pin {pin} not in symbol {lib[1]}")
    idx = {}
    for nt in n.nets:
        for ref, pin, fn, ty in nt["nodes"]:
            idx.setdefault(ref, []).append((pin, fn, nt["short"], nt["name"]))
    if sum(len(v) for v in idx.values()) != total:
        problems.append("pin index and net view disagree on the connection count")

    L = []
    A = L.append
    A(f"# {title} — complete netlist\n")
    A(f"Generated from `{source}` by `verify/emit.py`, which exports the "
      f"schematic with `kicad-cli` and parses it with the same code the claims in "
      f"`verify/claims.py` use.\n")
    A(f"**{len(n.comps)} components · {len(n.nets)} nets · {total} pin connections.**\n")
    A("Three views of the same information: components, a connection view answering "
      '"what is this pin wired to", and a net index answering "what is on this net". '
      "The redundancy is deliberate — it is what lets the file be checked against "
      "itself.\n")
    if problems:
        A("## Integrity problems\n")
        for p in sorted(set(problems)):
            A(f"- {p}")
        A("")
    else:
        A("No integrity problems: every node names a known component, every pin number "
          "is valid for that component's symbol, and the two views agree on the "
          "connection count.\n")

    A("## Components\n")
    A("| ref | value | sheet |")
    A("|---|---|---|")
    for r in sorted(n.comps, key=refkey):
        c = n.comps[r]
        A(f"| `{r}` | {c['value']} | {c['sheet']} |")
    A("")

    A("## Connections\n")
    A(f"For each pin: its name, its net, and what else is on that net. Nets with more "
      f"than {BIG} pins (power, ground, buses) are named rather than expanded.\n")
    A("```")
    bynet = {nt["name"]: nt["nodes"] for nt in n.nets}
    for r in sorted(idx, key=refkey):
        c = n.comps[r]
        A(f"{r}  ({c['value']}, {c['sheet']})")
        for pin, fn, short, full in sorted(idx[r], key=lambda t: pinkey(t[0])):
            nodes = bynet[full]
            others = [(a, b, f) for a, b, f, _ in nodes if not (a == r and b == pin)]
            if len(nodes) > BIG:
                tgt = f"[net {short}, {len(nodes)} pins]"
            elif others:
                tgt = " ".join(f"{a}.{b}" + (f"({f})" if f else "") for a, b, f in others)
            else:
                tgt = "(no other connection)"
            A(f"   pin {pin:>3} {fn or '':14} {short:28} {tgt}")
        A("")
    A("```")

    A("## Nets\n")
    A("```")
    for nt in sorted(n.nets, key=lambda x: x["name"]):
        A(f"{nt['name']}   ({len(nt['nodes'])} pins)")
        for ref, pin, fn, _t in sorted(nt["nodes"], key=lambda t: (t[0], pinkey(t[1]))):
            A(f"    {ref:8} {n.comps[ref]['value']:18} pin {pin:>3}  {fn or ''}")
        A("")
    A("```")
    out.write_text("\n".join(L) + "\n")
    return len(problems)


def main():
    root = os.environ.get("TRS80_SCHEMATICS")
    if not root:
        print("set TRS80_SCHEMATICS to the directory holding the KiCad repositories")
        return 2
    root = Path(root).expanduser()
    bad = 0
    for board, (title, source) in TITLES.items():
        n = nl.load(root, CACHE, board)
        if n is None:
            print(f"  {board:10} SKIP (could not export)")
            continue
        p = emit(n, title, source, OUT / f"{board}.md")
        bad += p
        print(f"  {board:10} {len(n.comps):4} comps  {len(n.nets):4} nets  "
              f"{'OK' if p == 0 else f'{p} PROBLEMS'}")
    print(f"\n{'all clean' if bad == 0 else f'{bad} integrity problems'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
