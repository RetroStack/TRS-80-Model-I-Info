"""Parse a KiCad s-expression netlist.

This is the single parsing path used by every claim in `claims.py`. It is itself
verified: `run.py --self-test` re-exports each board as KiCad XML — a different
format down a different code path in `kicad-cli` — and asserts that the component
set, the node set and the partition of pins into nets all agree. `unescape` exists
because KiCad escapes `/` as `{slash}` inside a net name, `/` being the hierarchy
separator.
"""

import re
import subprocess
from pathlib import Path


def unescape(s: str) -> str:
    """KiCad escapes inside s-expression strings that the XML export does not use."""
    return s.replace("{slash}", "/").replace("\\n", "\n")


def split_net(raw: str):
    """Split a raw (still-escaped) net name into (full, short).

    The escaping matters here and getting it wrong is a real trap. A hierarchical
    net is `/Sheet/Sheet/NAME`, so the short name is the part after the last `/`.
    But a net name may itself contain a slash - the Expansion Interface has
    `~{CLK/2}` and `CLK/10` - and KiCad escapes those as `{slash}` precisely so
    the two cannot be confused. So the split must happen *before* unescaping.
    Unescaping first turns `~{CLK{slash}2}` into `~{CLK/2}` and then splitting
    yields `2}`.
    """
    short = raw.split("/")[-1]
    return unescape(raw), unescape(short)


class Netlist:
    def __init__(self, text: str):
        self.libparts = {}
        for m in re.finditer(
            r'\(libpart \(lib "([^"]*)"\) \(part "([^"]*)"\)(.*?)'
            r"(?=\n    \(libpart |\n  \)\n  \(libraries)",
            text,
            re.S,
        ):
            pins = {}
            for p in re.finditer(
                r'\(pin \(num "([^"]+)"\) \(name "([^"]*)"\) \(type "([^"]*)"\)\)', m.group(3)
            ):
                pins[p.group(1)] = (unescape(p.group(2)), p.group(3))
            self.libparts[(m.group(1), m.group(2))] = pins

        self.comps = {}
        for m in re.finditer(
            r'\(comp \(ref "([^"]+)"\)\s*\(value "([^"]*)"\)(.*?)\(tstamps "[^"]*"\)\)',
            text,
            re.S,
        ):
            ref, val, body = m.group(1), m.group(2), m.group(3)
            ls = re.search(r'\(libsource \(lib "([^"]*)"\) \(part "([^"]*)"\)', body)
            sh = re.search(r'\(property \(name "Sheetname"\) \(value "([^"]*)"\)', body)
            self.comps[ref] = {
                "value": unescape(val),
                "lib": (ls.group(1), ls.group(2)) if ls else None,
                "sheet": unescape(sh.group(1)) if sh else "",
            }

        self.nets = []
        for m in re.finditer(
            r'\(net \(code "(\d+)"\) \(name "([^"]*)"\)[^\n]*\n((?:\s*\(node[^\n]*\n?)*)', text
        ):
            nodes = []
            for n in re.finditer(
                r'\(node \(ref "([^"]+)"\) \(pin "([^"]+)"\)'
                r'(?:\s*\(pinfunction "([^"]*)"\))?(?:\s*\(pintype "([^"]*)"\))?',
                m.group(3),
            ):
                nodes.append([n.group(1), n.group(2), unescape(n.group(3) or ""), n.group(4) or ""])
            full, short = split_net(m.group(2))
            self.nets.append({"name": full, "short": short, "nodes": nodes})

        # Fill pin names the netlist omits (multi-unit symbols) from the library.
        for nt in self.nets:
            for nd in nt["nodes"]:
                if not nd[2]:
                    c = self.comps.get(nd[0])
                    if c and c["lib"] in self.libparts:
                        pn = self.libparts[c["lib"]].get(nd[1])
                        if pn:
                            nd[2] = pn[0]

        self._pin2net = {}
        self._pin2short = {}
        for nt in self.nets:
            for r, p, _f, _t in nt["nodes"]:
                self._pin2net[(r, p)] = nt["name"]
                self._pin2short[(r, p)] = nt["short"]

    # -- queries -----------------------------------------------------------

    def value(self, ref):
        return self.comps.get(ref, {}).get("value")

    def net_of(self, ref, pin):
        """The net a pin sits on, or None. Pin may be int or str."""
        return self._pin2net.get((ref, str(pin)))

    def pins_on(self, name):
        """Every (ref, pin) on the net whose short name matches exactly."""
        out = set()
        for nt in self.nets:
            if nt["short"] == name or nt["name"] == name:
                out |= {(r, p) for r, p, _f, _t in nt["nodes"]}
        return out

    def net_named(self, ref, pin):
        """Short net name (last path component) for a pin."""
        return self._pin2short.get((ref, str(pin)))

    def refs(self, pattern):
        return sorted(r for r in self.comps if re.fullmatch(pattern, r))

    def partition(self):
        """Pins grouped into nets, net names discarded. The comparison that
        answers 'are these two boards wired the same' without being fooled by
        a rename."""
        return {frozenset((r, p) for r, p, _f, _t in nt["nodes"]) for nt in self.nets}

    def unconnected(self, ref):
        return {p for (r, p), n in self._pin2net.items() if r == ref and "unconnected" in n}


# -- loading ---------------------------------------------------------------

BOARDS = {
    "reva": "TRS-80-Model-I-A-E1-main/KiCAD/TRS80_Model_I_A_E1.kicad_sch",
    "revd": "TRS-80-Model-I-D-E1-main/KiCAD/TRS80_Model_I_D_E1.kicad_sch",
    "reve": "TRS-80-Model-I-E-E1-main/KiCAD/TRS80_Model_I_E_E1.kicad_sch",
    "revg": "TRS-80-Model-I-G-E1-main/KiCAD/TRS80_Model_I_G_E1.kicad_sch",
    "jap20": "TRS-80-Model-I-Jap20-E1-main/KiCAD/TRS80_Model_I_Jap20_E1.kicad_sch",
    "jap50": "TRS-80-Model-I-Jap50-E1-main/KiCAD/TRS80_Model_I_Jap50_E1.kicad_sch",
    "ei": "TRS-80-Model-I-Expansion-Interface-Rev-D-main/KiCAD/TRS80_Model_I_EI_RevD.kicad_sch",
    "alps": "TRS-80-Model-I-Keyboard-ALPS-main/KiCAD/TRS80_Model_I_Keyboard_ALPS_E1.kicad_sch",
    "kbadapter": "TRS-80-Model-I-Keyboard-Adapter-main/KiCAD/TRS80_Model_I_Keyboard_Adpter.kicad_sch",
    "psu": "TRS-80-Model-I-Power-Supply-main/KiCAD/TRS80_Model_I_Power_Supply.kicad_sch",
    "xrx3": "TRS-80-Model-I-XRX-III-main/KiCAD/XRX_Mod.kicad_sch",
}

KICAD_CLI_CANDIDATES = [
    "kicad-cli",
    "/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli",
]


def kicad_cli():
    import shutil

    for c in KICAD_CLI_CANDIDATES:
        if shutil.which(c) or Path(c).exists():
            return c
    return None


COMMITTED = Path(__file__).resolve().parent.parent / "netlists" / "exports"


def committed(board: str, fmt="kicadsexpr"):
    """The netlist export committed to this repository, if there is one.

    These are derived data, not RetroStack's sources: `kicad-cli`'s own output,
    checked in so that the connectivity claims can run without KiCad and without
    the eleven board repositories. A live export always wins over one of these,
    and `committed-exports-are-current` requires the two to agree whenever both
    are available - a snapshot nothing re-derives is the trap this folder exists
    to avoid.
    """
    if fmt != "kicadsexpr":
        return None                      # only the s-expression form is committed
    p = COMMITTED / f"{board}.net"
    return p if p.exists() else None


def newest_sheet(root: Path, board: str):
    """When a board's project was last edited, or None if it is not here.

    Every board is a hierarchy, so the root sheet named in `BOARDS` is not
    enough to date it by: an edit to a sub-sheet leaves the root untouched.
    """
    if root is None:
        return None
    d = (root / BOARDS[board]).parent
    return max((p.stat().st_mtime for p in d.glob("*.kicad_sch")), default=None)


def usable_cache(out: Path, root: Path, board: str, fmt: str):
    """A cache entry, if it can still be trusted. Two ways it cannot.

    The sources may have moved on since it was written, in which case an export
    that nothing re-derives is exactly the snapshot this folder exists to avoid.
    Or there may be no sources at all - and then what this repository ships is
    the answer, not a file some other run happened to leave in the temporary
    directory. The exception is a format that is not committed: the XML used by
    the parser self-test has no shipped copy, so a cached one is all there is.
    """
    if not out.exists():
        return None
    if root is None:
        return None if committed(board, fmt) else out
    newest = newest_sheet(root, board)
    if newest is not None and newest > out.stat().st_mtime:
        return None
    return out


def export(root: Path, cache: Path, board: str, fmt="kicadsexpr"):
    """Export one board's netlist, caching the result.

    Falls back to the committed export when the KiCad sources or `kicad-cli` are
    not available.
    """
    ext = {"kicadsexpr": "net", "kicadxml": "xml"}[fmt]
    out = cache / f"{board}.{ext}"
    cached = usable_cache(out, root, board, fmt)
    if cached is not None:
        return cached
    cli = kicad_cli()
    if cli is None:
        return committed(board, fmt)
    src = (root / BOARDS[board]) if root is not None else None
    if src is None or not src.exists():
        return committed(board, fmt)
    cache.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        [cli, "sch", "export", "netlist", "--format", fmt, "-o", str(out), str(src)],
        capture_output=True,
        timeout=300,
    )
    if out.exists() and r.returncode == 0:
        return out
    return committed(board, fmt)


def load(root: Path, cache: Path, board: str):
    p = export(root, cache, board)
    return None if p is None else Netlist(p.read_text())


def erc(root: Path, cache: Path, board: str):
    """Run KiCad's electrical rule check and return the parsed JSON report.

    Quoting a rule-check violation is quoting a tool's output, and a quote is only
    worth anything if the tool actually said it. So the ERC is run rather than
    remembered.
    """
    import json

    src = root / BOARDS[board]
    if not src.exists():
        return None
    cache.mkdir(parents=True, exist_ok=True)
    out = cache / f"{board}.erc.json"
    # Remembering a report is the thing the docstring above says this does not
    # do, so a report older than the sheets it describes is thrown away.
    newest = newest_sheet(root, board)
    if out.exists() and newest is not None and newest > out.stat().st_mtime:
        out.unlink()
    if not out.exists():
        cli = kicad_cli()
        if cli is None:
            return None
        subprocess.run(
            [cli, "sch", "erc", "--severity-all", "--format", "json",
             "-o", str(out), str(src)],
            capture_output=True, text=True,
        )
        if not out.exists():
            return None
    return json.loads(out.read_text())


def violations(report, kind=None):
    """Flatten an ERC report to (sheet, type, description) triples."""
    out = []
    for sheet in report.get("sheets", []):
        for v in sheet.get("violations", []):
            if kind is None or v.get("type") == kind:
                out.append((sheet.get("path"), v.get("type"), v.get("description")))
    return out


def pcb_nets(root: Path, board: str):
    """`{net name: {(ref, pad), ...}}` from a board's .kicad_pcb.

    The PCB is a second, independent artefact: it was routed from a netlist and
    carries its own copper. Comparing the schematic's netlist against it catches
    a schematic that has drifted from the board it was routed into.
    """
    d = (root / BOARDS[board]).parent
    pcbs = sorted(d.glob("*.kicad_pcb"))
    if not pcbs:
        return None
    text = pcbs[0].read_text()
    out = {}
    for block in re.split(r"\n\t\(footprint ", text)[1:]:
        ref = re.search(r'\(property "Reference" "([^"]+)"', block)
        if not ref:
            continue
        for m in re.finditer(
            r'\(pad "([^"]+)"[^\n]*\n(?:[^\n]*\n){0,14}?\s*\(net \d+ "([^"]+)"\)', block
        ):
            out.setdefault(m.group(2), set()).add((ref.group(1), m.group(1)))
    return out
