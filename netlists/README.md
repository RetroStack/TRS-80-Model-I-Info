# The schematics as text

Eleven boards, every component, every pin, every connection — in a form you can `grep`.

A schematic is a picture, and a picture cannot answer "what else is on this net?" without a
person tracing wires. These files can. They are generated from the KiCad sources with
`kicad-cli sch export netlist`, so they are not a reading of a drawing — they are the
drawing's own connectivity, mechanically extracted.

## The boards

| file | board | components | nets | connections |
|---|---|---|---|---|
| [`reva.md`](reva.md) | Model I main board, **Rev A** | 221 | 377 | 1540 |
| [`revd.md`](revd.md) | Model I main board, **Rev D** | 225 | 377 | 1552 |
| [`reve.md`](reve.md) | Model I main board, **Rev E** | 225 | 377 | 1552 |
| [`revg.md`](revg.md) | Model I main board, **Rev G** | 230 | 375 | 1562 |
| [`jap20.md`](jap20.md) | Japanese main board, **Jap20** | 253 | 410 | 1543 |
| [`jap50.md`](jap50.md) | Japanese main board, **Jap50** | 253 | 410 | 1543 |
| [`ei.md`](ei.md) | **Expansion Interface** Rev D | 185 | 337 | 1346 |
| [`alps.md`](alps.md) | **ALPS keyboard** | 75 | 55 | 227 |
| [`kbadapter.md`](kbadapter.md) | Keyboard adapter, Tandy ↔ TEC | 2 | 20 | 39 |
| [`psu.md`](psu.md) | Power supply | 10 | 11 | 32 |
| [`xrx3.md`](xrx3.md) | XRX III | 11 | 22 | 42 |

## How to read one

Each file has three views of the same information, which is what makes it checkable against
itself:

- **Components** — reference, value, and the sheet it lives on.
- **Connections** — for each pin: its name, its net, and *what else is on that net*. This is
  the view that answers "what is `Z59` pin 12 wired to?". Nets with more than twelve pins
  (power, ground, the data bus) are named rather than expanded, because listing every pin of
  `+5V` under every pin of `+5V` helps nobody.
- **Nets** — every net, with every pin on it. This is the view that answers "what is on
  `/37E0_READ`?".

Pin names come from the netlist where it carries them, and from the symbol library where it
does not — KiCad omits the name on multi-unit symbols, which is most of the 74-series parts.

## Two things these files are not

**They are not the boards.** They are RetroStack's reconstructions of the boards, and a
reconstruction can contain a drafting error that the physical board does not. That is why every
US board's netlist is checked against that board's own copper, below.

**They are not a substitute for the drawings.** A netlist has no geometry, so it cannot tell
you that two gates sit side by side, or that a note in the corner says
"Any write to port … will reset flip-flop". Read them alongside the schematics, not instead
of them.

## Verified three ways

Every file was checked before it was written, and every check passed:

1. **Internally.** Every node names a component that exists; every pin number is valid for
   that component's symbol; and the net view and the pin index agree on the total connection
   count. **Zero problems on all eleven boards.**
2. **Against the bills of materials**, which are a separate artefact from the schematic. For
   the four boards that ship a BOM — Rev G, Jap20, Jap50 and the Expansion Interface —
   **every BOM reference appears in the netlist**, with no exceptions. The netlist carries a
   few extra references the BOMs omit, and the complete list is short: `J4` on all four boards,
   `J1`–`J3`, `J5` and `J10` on the Expansion Interface, `CN2` and `TP1` on the Japanese boards,
   and `C_C58` on Rev G. All but the last are connectors and a test point, which a BOM would not
   list because they are not parts you buy. `C_C58` is a fitted-position that is meant to stay
   empty, and the Rev G BOM says so in its own note — see below.
3. **Against independent sources**, for the claims that matter. The Expansion Interface's
   `Z43` decode inputs, its timer flip-flops, its motor one-shot values and its `/SYSRES`
   distribution all match the Radio Shack service manual — the floppy half of that is in
   [`../floppy.md`](../docs/floppy.md). The Rev G part-to-designator map
   matches the 1978 Radio Shack parts list on every IC. The keyboard adapter's pin map is
   confirmed by two boards it was derived from and by the ROM.

## Two positions on Rev G carry a designator that is already used

Rev G's netlist has `C_C58` and `C_R67`, which look like placeholders and are not. Both are
real, wired parts on the `Cassette Interface` sheet:

| ref | symbol | value | where |
|---|---|---|---|
| `C_C58` | `Device:C` | 0.1 µF | across the relay contacts, with `CR9`/`CR10`, `J3` and `K1` |
| `C_R67` | `Device:R` | 220 Ω | `CASSIN` to `GND`, with `C24` and `J3` pin 4 |

The prefix marks a **duplicate silkscreen designator**. The board has two positions labelled
`C58` and two labelled `R67`, so KiCad cannot use the printed name twice, and the Rev G bill of
materials disambiguates them by location in its own notes:

- `C58` — *"C58 is located to the right of ROM B; C58 next to the relay stays empty (!!!)"*
- `R67` — *"R67 is located to the left of Z42"*, against *"C_R67 is located to the left of K1"*

So `C_R67` (220 Ω) **is** in the bill of materials, in the row it shares with `R19`. `C_C58` is
not, and the note explains why: that position is drawn but deliberately left unfitted. Neither
is a placeholder and neither is unconnected.

## Two boards that turn out to be one

Comparing the generated files directly, with only the revision name normalised:

- **Rev D and Rev E are electrically identical** — same components, same nets, same
  connections, no differences at all.
- **Jap20 and Jap50 are electrically identical** — likewise.

Whatever separates those pairs is mechanical, or a revision digit, and not something software
or a circuit reader will ever see. Two documents can describe four boards.

## The data bus and the buffer enables

`RAM_ROM_Interface` is where ROM data and RAM data meet the CPU bus, through `Z67` and `Z68` —
two 74LS367s — and it carries a geometric hazard worth knowing about before editing it.

**`74LS367_Split` unit 1 puts the package's `/1G` output-enable on pin 1 at symbol-local
`(0, +6.35)`, pointing up, and the data ladder's row pitch is exactly 6.35 mm.** So an enable
pin's tip reaches precisely the data row above the one its symbol sits on. The drawing gives
nothing away, because a tip landing dead on a wire reads as a deliberate T-junction.

The data wires are therefore broken around both tips, and the left stub carries its own label —
that stub holds the buffer output, `Z67.5` / `Z68.5`, and without the label the bit would never
reach the bus. The geometry is re-checked on every run, so dragging one of those wires across an
enable pin fails the harness.

## The schematic agrees with the copper

A `.kicad_pcb` is a second, independent artefact: it was routed from the schematic and then
carries its own copper. So each of the four US main boards is compared against its own board
file **net for net** — the same net names on both sides, and the same pads on each net. There
are no exceptions on Rev D, Rev E or Rev G.

Rev A has exactly one, and the assertion names it rather than matching a pattern: `Z3` pin 14 is
a drilled pad on a strapping position that the copper gives no net at all, so the schematic's
`unconnected-(Z3-Pad14)` has nothing to match. Every other unconnected pin does appear in the
copper under the same name, so the exemption is one pad and not a class, and a second one cannot
appear unnoticed.

The assertion reads the `.kicad_pcb` itself rather than any table here, so the drawing and the
board cannot drift apart unnoticed.

### The Japanese boards do not agree, and that is why they are out of scope

Running the same comparison on `jap20` and `jap50` fails, identically on both: **eleven nets
where the schematic and the copper put a pin in different places.** They are not excluded from
the assertion above because they are awkward — they are excluded because they genuinely differ,
and the difference is held by its own assertion so that it cannot grow or shift unnoticed.

Every one has the same shape — the schematic's pin `N` against the copper's pad `N-1` — and all
eight references involved are 74LS92, 74LS93, 74LS30 or 74LS20:

| net | part | schematic pin → copper pad |
|---|---|---|
| `+5V` | `Z28` 74LS93, `Z41` 74LS30 | 5 → 4, 14 → 13 |
| `/A4` | `Z41` 74LS30 | 11 → 10 |
| `/CPU/CLK` | `Z65` 74LS92 | 14 → 13 |
| `/Video/Video Access Multiplexer/C5` | `Z28` 74LS93 | 8 → 7 |
| `/Video/Video Access Multiplexer/R0` | `Z7` 74LS93 | 14 → 13 |
| `/Video/Video Access Multiplexer/R3` | `Z7` 74LS93 | 8 → 7 |
| `/Video/Video Counter/HDRV` | `Z35` 74LS93 | 14 → 13 |
| `/Video/Video Counter/L2` | `Z35` 74LS93 | 8 → 7 |
| `/Video/Video Counter/L3` | `Z34` 74LS93 | 14 → 13 |
| `/Video/Video Generator/SHIFT` | `Z6` 74LS92 | 14 → 13 |
| `Net-(Z50-Pad10)` | `Z55` 74LS20 | 4 → 3 |

**The schematics are right and the board files are wrong.** Two of the eleven settle it against
the datasheets rather than against a preference: a 74LS93 takes `VCC` on pin 5, which is where
the schematic puts `Z28`, while the copper puts it on pin 4, which is a no-connect; and a 74LS30
takes `VCC` on pin 14, where the schematic puts `Z41`, while the copper puts it on pin 13, which
is an input. A board built to the copper would have two dead packages, so the copper cannot be
what the physical board carries.

Nothing downstream depends on it: every claim in this folder reads the schematic netlist, and
the emulator was never derived from these `.kicad_pcb` files.

## One caution about the rule check

Where several labels sit on one net, KiCad's `multiple_net_names` reports a *pair* of them, and
which pair comes back varies between runs. **A single ERC run tells you a pair, not the set.**
Read the netlist if you need to know everything on a net.

## Reproducing them

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/emit.py
```

That exports each board with `kicad-cli` and regenerates these files. It uses the same parser
as the assertions in [`../verify/claims.py`](../verify/claims.py), so the tables here and the
claims that cite them cannot disagree about what the netlist says.

The parser is itself checked — `run.py --self-test` re-exports every board as KiCad XML, a
different format down a different code path, and requires the component set, the node set and
the partition of pins into nets to agree. Two subtleties in the parser are covered by regression
claims, both to do with KiCad escaping `/` inside a net name.

## `exports/`, and why they are committed

[`exports/`](exports/) holds `kicad-cli`'s own s-expression netlist for each of the eleven
boards, checked in. They are **derived data, not RetroStack's sources**: the same bytes the tool
produces, kept so that the connectivity claims can run with neither KiCad installed nor the
eleven board repositories cloned. With nothing set at all the run goes from 7 claims to 63.

Two header fields are normalised on the way in, and a re-export has to be normalised the same
way: `kicad-cli` writes the absolute path it was handed into `(source …)` and `(uri …)`, which
would publish whatever directory the exporting machine happened to use, and it stamps a
wall-clock `(date …)` that makes every regeneration a diff. The paths are cut back to the board
repository's own name and the timestamp to its day. Nothing reads either field — the parser
takes components and nets — so this changes no claim.

**A live export always wins.** When `TRS80_SCHEMATICS` and `kicad-cli` are both available the
harness exports afresh and ignores what is here; the committed files are reached only when it
cannot. That order matters, because a snapshot is a thing that rots.

So `committed-exports-are-current` holds them to the source: whenever a live export *is*
possible it re-exports all eleven into a temporary directory and requires the committed copy to
agree, component for component and net for net. It compares the parsed content rather than the
bytes, so a KiCad version that reformats its output is not a failure, and it refuses to run at
all if it finds itself comparing a file with itself.

Seven claims still need more than a netlist and skip without `TRS80_SCHEMATICS`: the two that
read `.kicad_pcb` copper, the one that reads wire geometry out of a `.kicad_sch`, the three that
read bills of materials, and the one that runs the rule check.

## How the claims here are checked

Every factual claim in this document has an executable assertion in [`../verify/claims.py`](../verify/claims.py). They are run by:

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

which also validates the netlist parser against KiCad's own XML export before testing anything. The assertions covering this document:

- `ei-37ex-decode-inputs`
- `ei-a4-reaches-other-things`
- `ei-timer-acknowledge-on-read`
- `ei-sysres-distribution`
- `ei-r16-r24-are-not-int-pullups`
- `us-boards-match-their-pcb-copper`
- `committed-exports-are-current`
- `japanese-boards-disagree-with-their-copper`
- `enable-pins-are-clear-of-the-data-rows`
- `net-names-may-contain-slashes`
- `no-kicad-escapes-leak-into-docs`

- `netlist-tables-match-the-netlists`
- `bom-references-all-appear-in-netlist`

- `netlists-are-internally-consistent`

- `revg-duplicate-silkscreen-designators`


If a claim below and its assertion disagree, one of them is wrong and the run says so. See [`../verify/README.md`](../verify/README.md) for why this exists.
