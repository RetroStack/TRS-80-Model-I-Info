# Sources, and how much each one can carry

Every claim in this folder is only as good as what established it. This document names each
source, says what kind of thing it is, and — the part that matters — says where it has already
been caught being wrong.

No source here is treated as infallible. Radio Shack's own manuals contain errors, and so do
modern reconstructions. What this folder does about that is state the corrected value, in place,
with an assertion behind it wherever one can be written.

What makes a claim trustworthy is not its pedigree but the number of independent things that
agree with it, and whether anything re-derives it on demand.

## How claims are ranked

1. **Measured.** The machine's own behaviour, or a byte read out of a ROM image. This outranks
   every document, because it is the thing the documents are describing. Marked `[measured]`.
2. **Two independent sources agreeing.** The 1978 Radio Shack parts list and RetroStack's Rev G
   bill of materials are independent of each other — one is period, one is a fresh reading of a
   physical board — so where they agree, the answer is settled.
3. **One primary source.** A period Radio Shack manual, or a schematic drawing. Marked
   `[manual p.N]` or `[sheet]`.
4. **One secondary or unverifiable source.** A modern reconstruction on its own, or a scan that
   cannot be machine-read.

Where sources conflict and nothing settles it, the claim is marked `[unresolved]` and carries a
table of who says what, plus the experiment that would settle it. That marker is a feature. A
document that hides its uncertainty is not more correct, only more confident.

## The sources

| Source | Kind | Machine-readable | Weight |
|---|---|---|---|
| **RetroStack KiCad sources** — eleven boards: main board Rev A, Rev D, Rev E, Rev G; Jap20 and Jap50; Expansion Interface Rev D; ALPS keyboard; keyboard adapter; power supply; XRX III | modern reconstruction, **schematic source** | **yes — exact netlists** | **highest for connectivity** |
| Bills of materials for those boards | modern reconstruction | yes | high, and independent of the schematic |
| TRS-80 Technical Manual (1978) | period primary — theory of operation and parts list | yes, OCR | high |
| Expansion Interface Service Manual | period primary | yes, OCR | high |
| Model I RS-232 (Murley / BYTESHiFT) | modern **rebuild**, not the original card | yes | good, with a caveat |
| Percom Doubler drawings | hand-drawn scans of **two different boards** | **no — zero extractable text** | weakest |
| The ROM and character images in `roms/` | primary artefact | yes | measurable directly |
| This emulator and its test suite | instrument | n/a | measures behaviour, not circuits |

**None of these files is in this repository.** The schematics, the manuals and the ROM images
are all third-party material. `TRS80_SCHEMATICS` points the harness at the KiCad repositories
and `TRS80_ROMS` at a directory of ROM images; without them the claims that need them skip and
the run still passes. See [`README.md`](../README.md) for where each comes from.

### Why the KiCad sources outrank the PDFs

The published PDFs are pictures. Two of them — the Expansion Interface and the Percom drawings
— carry **no extractable text at all**, so a claim from either was a human reading a rendered
image, with no way to check it mechanically.

The KiCad sources are the connectivity itself. `kicad-cli sch export netlist` produces the
exact net list the board was manufactured from, and `kicad-cli sch erc` reports the design's own
rule violations. That moves the Expansion Interface from the weakest evidence class to the
strongest, and it is what made it possible to state, rather than infer, that `/37E0_READ` is
both `Z26A`'s set and `Z26B`'s clock.

Every board's full connectivity is transcribed in [`netlists/`](../netlists/), with the
verification that was done on it.

A caution that came out of doing this: **a machine-readable source is not an infallible one; it
is one whose errors can be found.** A reconstruction is a redrawing, and a redrawing can differ
from the board it was taken from. So every US main board's netlist is checked against that
board's own `.kicad_pcb` copper — not a second opinion about the drawing but the artefact the
drawing was routed into — net for net, names and pads alike.

### Comparing two boards is harder than it looks

A netlist makes "what is this pin connected to" exact. It does **not** make "what is different
between these two boards" exact. Three methods, three answers, all defensible and all
misleading:

- **Compare each part's `Value`.** Blind to any part with no value. `Z3` is a 14-pin strapping
  block on Rev A and a 16-pin one on Rev D/E/G, and its `Value` is `~` on both — so this method
  reports them identical.
- **Compare each pin's net *name*.** Counts a rename as a change. When one `/ROM` select becomes
  `/ROMA` and `/ROMB`, this reports both ROM sockets as changed, when in fact 23 of their 24
  pins are wired identically and the change is in the decode that feeds them.
- **Compare net *membership*, ignoring names.** One extra pin on `+5V` makes the entire power
  net differ, which drags in every component connected to it — most of the board. The three
  counts, and what each is blind to, are in
  [`revisions.md`](revisions.md#a-note-on-counting-differences), where
  `counting-differences-three-ways` asserts them; they are not restated here, because a number
  kept in two places is a number that will disagree with itself.

The rule this leaves: **never claim "X is the only difference" from a comparison that could not
have found the others**, and prefer describing what changed to counting it. A count needs a
definition of "different" stated alongside it, and usually the definition is the interesting
part.

### TRS-80 Technical Manual (1978, Radio Shack)

*"For Radio Shack Service Centers"*, 42 pages: an introduction, a memory map, a full theory of
operation, a parts list and fold-out schematics. It is the single most useful document about the
machine, because it explains *why* the circuit is shaped the way it is rather than only what is
connected to what.

It describes a **Level I** machine — the memory map is captioned "Level I Memory Map" and the
parts list is headed "Level I Logic Board Parts List". Level II is a two-page appendix describing
a piggyback ROM board. Claims taken from it are scoped accordingly.

**Where it is wrong.** Four errors are known, and they are worth stating because they show the
failure mode:

- Its memory map figure gives the keyboard as `3800–380F` and calls `3810–3BFF` "Not used". Its
  own address-decoder chapter proves otherwise: `A0`–`A9` are undecoded, so the keyboard occupies
  the whole of `3800–3BFF`. The figure is a map of what Level I BASIC *uses*, not of what the
  hardware *decodes*.
- It places a latch input on "pin 18 of `Z59`". A 74LS175 has sixteen pins.
- Its parts list describes `Z54` as a "Triple 3-Input NOR Gate". A 74LS30 is an eight-input NAND,
  and the manual's own body text uses it correctly as one.
- Its parts list describes the 74LS92 and 74LS93 counters with trailing text copied from the
  74LS157 rows above them.

The OCR adds its own damage — `A1 through A7` reads as "Z1 through Z7", `Z60` as "Z6~". Where
that happens it is resolved against a schematic and said so in place. The manual's fold-out
schematic pages are scanned artwork with no usable text layer, so **the manual cannot settle a
pin-level question on its own.**

### Expansion Interface Service Manual (Radio Shack)

44 pages. Titled *"Redesigned PCB"*, which is **not necessarily the Rev D board** the
reconstruction draws; establishing which revision it documents is an open item, and until it is
settled, claims are attributed to "the service manual" rather than to a revision.

This document carries unusual weight for one reason: the reconstruction of the Expansion
Interface cannot be machine-read (below), so for that board the manual is the only source a
claim can be checked against by anything other than a human eye.

### RetroStack board reconstructions

Redrawn in KiCad from physical boards. Sheet numbers cited in this folder are **PDF page order**,
and each sheet is named by its `.kicad_sch` file so a claim can be traced.

**Rev G main board** — 21 sheets, drawing rev E1C, KiCad 8.0.3. The default machine.

| # | Sheet | # | Sheet | # | Sheet |
|---|---|---|---|---|---|
| 1 | `TRS80_Model_I_G_E1` | 8 | `ROM` | 15 | `Video Latch` |
| 2 | `Clock` | 9 | `Keyboard` | 16 | `VideoGen` |
| 3 | `CPU` | 10 | `Cassette` | 17 | `VideoSync` |
| 4 | `CPUGating` | 11 | `Video` | 18 | `VideoMixer` |
| 5 | `AddressDecoder` | 12 | `VideoCounter` | 19 | `CardEdgeInterface` |
| 6 | `RAM` | 13 | `VideoAccessMultiplexer` | 20 | `Power` |
| 7 | `RAM_ROM_Interface` | 14 | `VideoRAM` | 21 | `Capacitors` |

**Rev A, Rev D, Rev E** — earlier main boards, and a Rev G bill of materials that lists every
designator against its part.

**Japanese Jap50 and Jap20** — 23 sheets each, with a bill of materials.

**Expansion Interface Rev D** — 14 sheets. **This PDF yields zero extractable text.** Its
creator field says KiCad, but the text is outlined or rasterised, so nothing in it can be
verified by extraction. Every claim sourced from it is a *visual* reading with no machine-checkable
trace, and is weighted accordingly.

**ALPS keyboard** — one sheet, and the only drawing of the key matrix, which lives on its own PCB.
The main board's `Keyboard` sheet is just the connector.

**XRX III** — one sheet.

### Designators are not stable across boards

RetroStack numbers parts `Zn` following the original Radio Shack drawings, and the numbering is
faithful: the 1978 parts list and the Rev G bill of materials agree on **every IC designator
except `Z33` and `Z34`**, and that difference is a real revision change rather than an error —
Level II moved from a piggyback board into the two main-board sockets, so the same positions hold
2K devices in 1978 and an 8K plus a 4K device on Rev G.

Two traps remain:

- **The numbering is not stable between revisions.** A designator must always be cited with its
  board and sheet, never on its own.
- **The keyboard PCB has its own `Z1`–`Z4`**, unrelated to the main board's `Z1`/`Z2` (voltage
  regulators), `Z3` (a DIP-shunt position, not an IC) and `Z4` (the LM3900). Any index keyed on
  designator alone will merge them.

### Model I RS-232 (Roger Murley / BYTESHiFT, Rev 2.1)

One sheet, KiCad 9.0.0. A **modern rebuild rather than a reconstruction** of the original
26-1145 card: the 1488/1489 line drivers are replaced by a single SP3243 and the TR1602 by its
pin-compatible HD6402. It is programmed identically, which is what makes it usable — but it is
evidence about the *programming model*, not about what was inside a 1979 card.

What it confirms directly: `U3` a 74LS155 making four read and four write strobes; `U7` a 74LS367
driving exactly `D7`, `D6`, `D5`, `D4` and `D0`, so `D3`–`D1` are undriven; `U8` a 74LS174 whose
`/Mr` is tied high through `R1` (4.7 kΩ); the HD6402; the COM8116; and `Y1` at 5.0688 MHz.

### The Percom Doubler drawings

Five pages of **hand-drawn** schematics from **two different boards** — one dated 1986, one
February 1982 — solving the same problem the same way. They yield **zero extractable text**.

This is the weakest source in the set, and it is load-bearing: it is the only authority for the
two undefined FD1771 opcodes a Percom board uses to select density. Every claim drawn from it is
marked as visually read and single-source, and its one corroboration is behavioural — TRSDOS 2.7
boots against a doubler modelled this way.

### The ROM and character images

Eight system ROMs and six character generators — the Level I and Level II builds, and the
generator images numbered by the option-select value of RetroStack's replacement device. These
are primary artefacts: a question about what a ROM contains is answered by reading it, and that
answer outranks any document. The harness reads them from `TRS80_ROMS`.

### This emulator, as an instrument

The emulator does not establish what is connected to what. What it does is let a circuit claim
with a software-visible consequence be *tested*: if bit 6 of port `FF` really is a readback of the
display width, then `INP(255)` returns one value in 64-column mode and another in 32, and that is
a thing which can be run rather than argued about.

Its test suite is the durable form of this. A claim pinned by a named test is one that cannot
quietly rot, which is why `[measured]` citations name the test rather than describing the result.

## How the claims here are checked

Every factual claim in this document has an executable assertion in [`verify/claims.py`](../verify/claims.py). They are run by:

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

which also validates the netlist parser against KiCad's own XML export before testing anything. The assertions covering this document:

- `sources-table-lists-every-board`

If a claim below and its assertion disagree, one of them is wrong and the run says so. See [`verify/README.md`](../verify/README.md) for why this exists.
