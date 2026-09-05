# Which machine are we talking about?

There is no single "TRS-80 Model I". There are four US main-board revisions, at least two
Japanese boards, an Expansion Interface, two doubler boards, a serial card and a keyboard
that is its own PCB — and a claim that is true of one is not automatically true of another.

This document is the scope every other document in this folder attaches its claims to. The
useful news, established below, is that **almost nothing software can see changed across the
US revisions.** The differences are real but they are few, and they are listed here so that
the rest of the folder can stop hedging.

## The US main boards: A, D, E, G

`[sheet]` throughout, from RetroStack's KiCad reconstructions of all four boards, compared
page by page.

### Rev D and Rev E are the same board

All 21 drawing pages are identical in wires *and* text; the only differences are the revision
letter and the date. Confirmed independently from the netlists: exporting both and comparing
component for component, net for net and pin for pin gives **no differences at all**.

**Any statement about Rev D holds for Rev E verbatim**, and this folder treats them as one
board.

### A note on counting differences

"How many parts differ" has no single answer, and the trap is waiting for anyone comparing these
boards.

Rev A has 221 references and Rev G has 230, and nothing is ever removed. Four of the nine arrive
in Rev D (`CR9`, `CR10`, `C_C58`, `R66`) and five in Rev G (`C58`, `R67`, `R68`, `R69`,
`C_R67`); `C_C58` and `C_R67` are wired parts whose prefix marks a duplicate silkscreen
designator, not placeholders. Over the 221 references Rev A and Rev G share, three comparisons
give three different answers:

| method | says | why it is not the answer |
|---|---|---|
| compare each part's `Value` | **4** differ — `C20`, `C21`, `Z33`, `Z34` | blind to a part with no value: `Z3` is a **14-pin** block on Rev A and a **16-pin** block on the others, and its `Value` is `~` on both |
| compare each pin's net **name** | **81 pins on 23 references** | counts a rename as a change; `/ROM` becoming `/ROMA` is one signal split in two, not 24 pins moving |
| compare net **membership**, names ignored | **173 references touched** | one extra pin on `+5V` makes the whole power net differ, dragging in everything connected to it |

The first row is the one to watch. Comparing `Value` fields is the obvious method and the most
misleading: it is blind to `Z3` and `Z71`, which have no value at all, and it counts `C20` and
`C21` — whose values are merely exchanged between two positions in the same video-sync chain —
alongside the ROM sockets, which is a genuine difference.

So this document does not give a count. **"How many parts differ" is not a well-posed question**
until you say what counts as a difference, and every answer above is defensible under some
definition and misleading under the others. What follows describes what changed instead.

### What is identical across A, D, E and G

This is the important half, because it is what lets the rest of the documentation speak about
"the Model I" without qualification:

- **Port `FF`, bit for bit.** The same `Z59` 74LS175 with the same choice of true and inverted
  outputs, the same `Z44E`→`D7` and `Z44F`→`D6` read buffers, the same `Z54A`+`Z52C`+`Z36A`
  address decode with `A8`–`A15` unused, the same `R53`/`R54`/`R55`/`R56` DAC network, the same
  printed voltage table, and the same "Any write to port … will reset flip-flop" annotation.
- **The seven-bit video RAM.** The video RAM page is byte-identical in all four: seven 2102
  static RAMs and `Z30D` deriving bit 6. **No US revision has an eight-bit video RAM.**
- The video generator, counter, latch, sync and mixer.
- The keyboard connector, the CPU clock, reset, `/INT`, NMI and `/WAIT`.
- The address map.

### What differs, in order of how visible it is to software

| # | Difference | A | D / E | G | evidence |
|---|---|---|---|---|---|
| 1 | The ROM select | one `/ROM` net | one `/ROM` net | **`/ROMA` + `/ROMB`** | netlist |
| 2 | `Z3` strapping block | **14-pin** | 16-pin | 16-pin, all used | netlist |
| 3 | `Z71` strapping block | **14-pin** | 16-pin | 16-pin | netlist |
| 4 | `MUX` buffer tri-states on `/TEST` | **no** | yes | yes | `Z72` pin 1 |
| 5 | Card-edge `J4` pin 39 | `+5V` | `+5V` | **`GND`** | netlist |
| 6 | Cassette clamp `CR9`/`CR10` | absent | present | present | sheet 10 |
| 7 | Video sync generator | **its own wiring** | common | common | netlist |
| 8 | Counter reset `/CLK_EN` | tied to `GND` | tied to `GND` | **a real net** | netlist |
| 9 | `Z70B`'s clear | on the `HI` rail | on the `HI` rail | **its own net** | netlist |

### The ROM sockets themselves do not change

This is worth stating plainly because it is easy to get wrong. `Z33` and `Z34` are 24-pin
sockets wired **identically on all four US boards on 23 of their 24 pins** — same `A0`–`A11` on
the same pins, same `ROMD0`–`ROMD7`, same `A12` on pin 21, same power and ground.

Only **pin 20** differs, and only in which net reaches it:

| | Rev A / D / E | Rev G |
|---|---|---|
| `Z33` pin 20 | `/ROM` | `/ROMA` |
| `Z34` pin 20 | `/ROM` | `/ROMB` |

On Rev A and D **one select feeds both sockets**, and the two devices are told apart by
`A12` on pin 21 — because the two 2332s are mask-programmed with *opposite chip-select
polarity*. The part names record it: `2332_20L_21L` in `Z33`, `2332_20L_21`**`H`** in `Z34`.
Pin 20 active low on both, pin 21 active low on one and active high on the other. So `A12`
low selects the lower ROM and `A12` high selects the upper, from a single wire.

On Rev G that trick is not available, because `Z33` becomes a **2364** — an 8K device for
which `A12` is a real address input rather than a chip select. The decode therefore has to
supply two separate selects, and `/ROM` splits into `/ROMA` and `/ROMB`.

Software cannot tell the difference: `0000`–`2FFF` is 12K of ROM either way. And note that the
change lives in the **decode**, not in the sockets — which is why `Z3`, `Z21`, `Z73` and `Z74`
are the references that actually move.

**(4)** `Z72` pin 1 — the output enable of the `ZMUX`→`MUX` buffer — is hard-wired to `GND` on
Rev A, so that buffer keeps driving during `/TEST`; from Rev D onward it joins the common
enable spine. Visible only to a device taking over the bus, never to Z80 code.

**(5)** is a real electrical difference at the Expansion Interface connector.

### Rev G adds a way to stop both counters, and four pull-ups

Rev G adds five references to Rev D's board — `C58`, `R67`, `R68`, `R69` and `C_R67` — and two
of them add capability the earlier boards do not have.

**`/CLK_EN` — a reset line on both 74LS92 counters.** `Z56` (the CPU sheet's divider) and `Z58`
(the video counter) are both 74LS92s, whose pins 6 and 7 are `R0(1)` and `R0(2)`: hold both high
and the counter is held at zero.

| | Rev A and Rev D | Rev G |
|---|---|---|
| `Z56` pins 6, 7 | `GND` | `~{CLK_EN}` |
| `Z58` pins 6, 7 | `GND` | `~{CLK_EN}` |
| `Z42` pin 8 (74LS04 output) | unconnected | `~{CLK_EN}` |
| `Z42` pin 9 (its input) | `GND` | `R67` (4.7 kΩ) to `+5V` |

On Rev A and Rev D those four reset inputs are grounded, so **neither counter can ever be
reset**. On Rev G they are one net, driven by a spare inverter in `Z42` whose input is held high
by `R67`, so the output is low and the counters run exactly as before.

**Nothing on the board drives that input.** `R67` pin 2 and `Z42` pin 9 are the *only* two pins
on the net. Pull it low from outside and both the CPU clock divider and the video counter are
held in reset together — which is what you would do to stop the machine cleanly, or to bring the
two into a known phase. It is a provision, wired and unused.

**`Z70B`'s clear comes off the shared rail.** On Rev A and Rev D, `Z70` pin 13 sits on `HI`
alongside `Z69` pins 4 and 10 and `Z70` pins 4 and 10 — one pull-up serving every preset and
clear on the two 74LS74s. On Rev G it has its own net with `R63`, and the rail keeps `R69`. That
makes it individually drivable, for the same reason.

**And two plain pull-ups.** `R68` on `~{ROMB}` — the second ROM select, which did not exist
before — and `R69` on what is left of `HI`. Plus `C58`, a 0.1 µF decoupler, and `C_R67`, a
220 Ω resistor from `CASSIN` to `GND` on the cassette input.

`R66`, the pull-up on `Z71` pin 10, is easy to miscount as a Rev G addition and is not: it
arrives in **Rev D**, along with `CR9`, `CR10` and `C_C58`. And neither `C_C58` nor `C_R67` is a
placeholder — the prefix marks a duplicate silkscreen designator, which
[`netlists/README.md`](../netlists/README.md) explains.

None of this is visible to software on a working machine: the defaults reproduce the earlier
behaviour exactly. It matters for anyone driving the board, and it is why Rev G is the revision
to reverse-engineer from.

### The list above is complete, and that is asserted

Differences 1–9 were not found by reading the drawings. Two of them — the video sync generator
and `/CLK_EN` — were missed by exactly that method, and turned up only when every net on every
board was compared mechanically.

So the completeness is now the claim, not the reading. Identify a net by the *set of pins on it*
(a rename is then not a difference), drop single-pin nets (an unconnected pin's name follows its
pin number), and set aside `+5V` and `GND` (one added decoupler churns the whole rail). What is
left:

| | nets that leave | nets that arrive |
|---|---|---|
| Rev A → Rev D | 17 | 22 |
| Rev D → Rev G | 13 | 19 |
| Rev D → Rev E | 0 | 0 |

`us-revision-differences-are-complete` holds every one of those 71 nets and requires the set to
match exactly. **A tenth difference cannot appear in these boards without the harness failing.**

The counts are larger than the nine differences because one change moves several nets: splitting
`/ROM` into `/ROMA` and `/ROMB` re-hangs four gates in `Z74` and brings three of `Z73`'s into
use, and growing `Z3` and `Z71` from 14 pins to 16 renumbers every net that touches them. Nine
differences, seventy-one nets, and none of the seventy-one unaccounted for.

### Rev A's video sync generator is not the later one

`C20` and `C21` are the only two capacitors on the board whose values differ across the US
revisions, and chasing that turned up a difference the rest of this document had missed.

The `Video Sync` sheet carries the same eleven references on every board — `C20`, `C21`, `C26`,
`C27`, `R20`, `R21`, `R43`, `R44`, `Z5` (74C00), `Z6` and `Z57` (both 74C04) — with the same
values apart from the two capacitors. **Rev D, Rev E and Rev G are pin-for-pin identical here.
Rev A is not.**

| | Rev A | Rev D onward |
|---|---|---|
| `C20` / `C21` | 750 pF / 330 pF | **330 pF / 750 pF** |
| `Z57` inverters in circuit | **two** of six | **all six** |
| `Z57` unused inputs | pins 5, 9, 11, 13 tied to `GND` | none |
| `Z5` pins 1, 2, 5, 13 | in the timing chain | on their own nets |
| `Z6` pins 2, 3, 8, 11 | one arrangement | another |

So it is not a component substitution. Four inverters that Rev A grounds and leaves unused are
brought into service from Rev D, and the two timing networks are re-hung around them; the
capacitor values follow the rearrangement rather than causing it.

**What this changes about the picture on screen is not established here.** The connectivity
difference is certain — it is in the netlists, and the assertion below re-derives it — but the
sync timing that results has not been measured on either board, and no source in this folder
discusses it. It is recorded as an open difference, not as a known one.

### Two things that are not jumpers

`Z3` (address decoder) and `Z71` (RAM configuration) look like ICs and are not. Both carry an
empty `Value` field in the schematic source, have no power pins, and appear in the bill of
materials as a single line: **`Z3, Z71 │ 2 │ Jumper │ 8-Bit DIP Switch │ Replacement`**.

They are configuration strapping positions. `Z3` hard-wires the 74LS156's open-collector
outputs into `/ROMA`, `/ROMB` and `/RAM`; `Z71`'s pin pairs are annotated with the memory size
each selects (`16k`, `4k`, `8/16k`, `8k`). "Replacement" records that the reconstruction fits a
DIP switch where the original board had a soldered shunt in a 16-pin socket — the 1978 parts
list calls that position `X3` and lists no IC in it.

**So the board does have jumpers, and the drawings give them away nowhere.** There are no `JPn`
designators anywhere on any revision and the word "jumper" never appears, so the only way to
find these two is the bill of materials or the symbol's empty `Value`.

## The Japanese boards

Two reconstructions exist, **Jap20** and **Jap50**, and they are **electrically identical** —
253 components, 410 nets, 1543 connections, no differences at all. Whatever separates them is
mechanical. The trailing digits are a revision counter, not a frame rate; both carry the full
PAL/NTSC jumper set.

### The designators are a different scheme entirely

This is the trap that matters most when reading across the families. Japanese designators are
**not** the US ones renumbered slightly — they are unrelated:

| designator | US boards | Japanese boards |
|---|---|---|
| `Z4` | LM3900 (cassette amplifier) | 74LS175 |
| `Z25` | 74LS32 | LM3900 |
| `Z29` | MCM6670 character generator | 74LS157 |
| `Z40` | **the Z80 CPU** | 74LS32 |
| `Z48` | 2102 video RAM | **the Z80 CPU** |

A claim of the form "`Z59` is the port `FF` latch" is meaningless without naming the board.

### It has a genuine eight-bit video RAM

**This is the largest difference between the families, and it is invisible on a parts list
unless you count.**

| | US boards | Japanese boards |
|---|---|---|
| video RAM | **seven** 2102 (1K×1) | **two** 2114 (1K×4) |
| stored bits | 7 | **8** |
| `VD6` comes from | `Z30` pin 13 — **a 74LS02 NOR output** | `Z9` pin 12 — **a RAM data pin** |

On a US board bit 6 is not stored anywhere; the video board regenerates it as `NOR(D5, D7)`.
On a Japanese board it is simply held in RAM like every other bit, and the video RAM sheet's
subtitle drops the US board's *"& bit-6 recovery"* wording accordingly.

So the most famous quirk of Model I video — that `POKE 15360,193` reads back as 129, that
lowercase needs a modification, that the reachable text codes are only `20`–`5F` — **does not
apply to the Japanese machine at all.** See [`video.md`](video.md).

### Otherwise it is a Model I

Two further differences software can see: it has **two character generators** with a
CPU-selectable switch, and it can be built for PAL.

### Two character generators, and the flip-flop that picks one

`[sheet]` Both are **MCM6670** — `Z37` and `Z38`. The selector is **`Z53A`, a 74LS74**, and its
wiring is exactly what an emulator needs to model:

| `Z53A` pin | net |
|---|---|
| 2 (`D`) | `D7` — data bit 7 of the CPU bus |
| 3 (`C`) | `~{OUTSIG}` — **the port `FF` write strobe** |
| 5 (`Q`) | `~{CGA}` — select generator A |
| 6 (`~{Q}`) | `~{CGB}` — select generator B |
| 4 (`~{S}`) | `JP4` |
| 1 (`~{R}`) | `JP5` |

So **every `OUT` to port `FF` clocks bit 7 into this flip-flop**, whatever else the write was
for. Grounding `/S` through `JP4` forces `Q` high, `/CGA` inactive and `/CGB` active —
generator B, permanently. Grounding `/R` through `JP5` forces generator A, which is also what a
single-generator machine looks like. With both jumpers idle the bit is live.

There are **ten jumper positions**, `JP1`–`JP10`.

### The trap

The flip-flop has no reset line that any reset reaches, so nothing but another `OUT` can move
it. And the ROM rewrites port `FF` from its own shadow at `403Dh`, so a bare `OUT 255,128` is
undone the moment the ROM next sets the display width. Software that wants the second generator
has to `POKE 16445,128` first. This is ROM behaviour rather than a board quirk, and it is the
first thing anyone driving this machine trips over — see [`video.md`](video.md).

## The Expansion Interface

One reconstruction is available, **Rev D**. A Radio Shack service manual exists for a board it
calls the **"Redesigned PCB"**, and whether that is the same board is not yet established; until
it is, claims are attributed to whichever source carried them.

What KiCad's electrical rule check says about each, counting only the two classes that bear on
connectivity — `multiple_net_names` and `net_not_bus_member`:

| board | net-naming | bus-membership | what they are |
|---|---|---|---|
| Rev A / D / E / G | 8 | 3–5, varying | all eight net-naming ones are the intended RAM/ROM data merge |
| Jap20 / Jap50 | **0** | **0** | clean |
| Expansion Interface | **0** | **16** | `S0`–`S15` on the `Internal Expansion` sheet, drawn onto an unnamed bus |

All eight net-naming violations on a US board are the intended place where RAM data and ROM data
meet the CPU bus, on one sheet.

**The bus-membership count is not stable.** Six consecutive runs of the same rule check on the
same Rev G file returned 4, 5, 4, 4, 5 and 3 warnings, naming a different subset of
`RAMD0`–`RAMD7` each time. They all say the same thing — a `RAMDn` net drawn onto the
`ROMD[0..7]` bus without being a member of it — and KiCad appears to report a sample rather than
the set. So this folder asserts what those warnings *are*, never how many. The net-naming count
is stable and is asserted exactly.

The Expansion Interface has no net-*naming* problem at all, which is what matters for reading
signals off it. Its sixteen bus-membership warnings are stable, because `S0`–`S15` is the
complete set: the slot lines are graphically connected to a bus carrying no net name, so KiCad
cannot confirm they belong to it. A drafting style issue rather than a short — the nets come out
correctly named and separate.

## Everything else

| Thing | Status here |
|---|---|
| Percom Doubler | two hand-drawn boards, 1982 and 1986 — see [`floppy.md`](floppy.md) |
| Radio Shack doubler (26-1143) | **no drawing available**; behaviour established from software |
| RS-232-C card | a modern rebuild of the 26-1145 — see [`rs232.md`](rs232.md) |
| ALPS keyboard | its own PCB, its own `Z1`–`Z4` — see [`keyboard.md`](keyboard.md) |
| The lowercase modification | a wire and an eighth RAM — see [`video.md`](video.md) |

### The keyboard interface is incompatible

The Tandy and TEC keyboards use the same 20-pin connector with the same pinout for power,
address and `D0`. `/KYBD` moves from **pin 14** to **pin 10**, and the other seven data bits
are reshuffled. A keyboard from one machine will not work on the other —
RetroStack's keyboard adapter exists precisely to bridge them. The full mapping is in
[`keyboard.md`](keyboard.md).

The US connector is `J100` and hangs directly on the CPU data bus. The Japanese one is `CN1`
and joins the ROM/RAM data bus instead, reaching the CPU through a 74LS367.

## What this settles

1. **Rev D and Rev E need one description, not two**, and neither do Jap20 and Jap50 — both
   pairs are electrically identical.
2. **The ROM sockets are wired identically on every US board** except for pin 20's select. What
   changes between revisions is the address decode — `Z3`, `Z21`, `Z73`, `Z74` — and it changes
   at both steps, A→D and D→G.
3. **Port `FF` is revision-invariant** across A, D, E and G, so the most consequential
   software-visible fact about the machine can be stated without qualification.
4. **The seven-bit video RAM is a US-only feature.** The Japanese boards store eight bits.
   Every statement about `D6` regeneration has to be scoped to the US family.
5. **Designators do not survive the crossing between families.** `Z40` is the CPU on a US
   board and a 74LS32 on a Japanese one.
6. **`Z3` and `Z71` are strapping positions**, so the board does have configuration jumpers.
7. **The two keyboards are not interchangeable.**

## How the claims here are checked

Every factual claim in this document has an executable assertion in [`verify/claims.py`](../verify/claims.py). They are run by:

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

which also validates the netlist parser against KiCad's own XML export before testing anything. The assertions covering this document:

- `revd-eq-reve`
- `jap20-eq-jap50`
- `rom-sockets-same-wiring`
- `rom-select-splits`
- `rom-chipselect-polarity`
- `z3-changes-size`
- `z71-changes-size`
- `z72-test-enable`
- `j4-pin39`
- `us-video-ram-is-7-bit`
- `japanese-video-ram-is-8-bit`
- `japanese-two-chargens`
- `japanese-chargen-selector`
- `japanese-ten-jumpers`
- `designators-differ-between-families`
- `z3-z71-are-jumpers`
- `rom-cason-sets-bit-2`
- `rom-portff-rewrites-unchanged`

- `port-ff-identical-across-us-revisions`
- `port-ff-decode-ignores-high-address`
- `video-ram-identical-across-us-revisions`
- `rev-g-bom-calls-z3-z71-jumpers`
- `z21-is-the-address-decoder`

- `counting-differences-three-ways`
- `reva-video-sync-differs`

- `revg-clk-en-and-pullups`

- `us-revision-differences-are-complete`

- `erc-violation-counts`

If a claim below and its assertion disagree, one of them is wrong and the run says so. See [`verify/README.md`](../verify/README.md) for why this exists.
