# The Japanese Model I — how it differs from Rev G

Source: `TRS80_Model_I_Jap50_E1_Schematics.pdf`, RetroStack's reconstruction of the
Japanese board marked **Rev HE11E011550** (drawing rev E1A, 23 sheets, KiCad 9.0.2), with
`TRS80_Model_I_Jap50_E1_BOM.csv` for the part list. Read
`schematics-model-1-rev-g.md` first; this document only covers what changed.

The machine is a Model I in every way software can see except two: it has **two
character generators** with a CPU-selectable switch, and it can be built for **PAL**.
Everything else is repackaging.

## Sheets with no Rev G equivalent

| # | Sheet | Why it exists |
|---|---|---|
| 10 | `KeyboardROMSelector` | Connector `CN2` (9 pins) carrying `A8`–`A11`, `/CS1`–`/CS4` and `/SYSRES` off-board to a ROM-select daughter board. Logic, not just wiring, moved off the main board. |
| 14 | `VideoMode` | Selects the dot rate between two clocks. Rev G does the equivalent inside `VideoCounter`. |

Rev G's `VideoCounter` and `VideoSync` are still present (sheets 15 and 20) but rebuilt
around the PAL/NTSC option.

## Part substitutions

| Function | Rev G | Japanese |
|---|---|---|
| CPU bus buffering (sheet 4) | 74LS367 x several | **74LS244 / 74LS245** |
| Address decode (sheet 5) | 74LS156 dual 2-to-4 | **74LS139** plus 74LS11, and it also emits `/CS1`–`/CS4` |
| Video RAM (sheet 17) | 1Kx1 statics + 74LS367 | **2114 SRAM** + 74LS245 |
| Clock (sheet 2) | one divider | 74LS92 giving **`CLK_DIV2`** and **`CLK_DIV6`** |
| Character generator (sheet 19) | one MCM6670 | **two**, `Z37` and `Z38` |

Designators are **not** comparable between the boards. The port-FF latch is `Z59` on
Rev G and `Z4` here; the port-FF read buffer is `Z44` on Rev G and `Z59` here.

## The two character generators

### The chips (sheet 19, `VideoGen`)

| Ref | Part | Contents | Chip select |
|---|---|---|---|
| `Z37` | MCM6670 | **Kana** | `/CS` <- `/CGA` |
| `Z38` | MCM6670 | **ASCII** | `/CS` <- `/CGB` |

The sheet notes the part as "Motorola MCM6670 (fixed floating 'a')". The BOM marks one
of the two sockets optional — a board can be built with either alone.

Both chips see the same display code and row count; only the chip select differs, so
exactly one drives the dot outputs at a time.

### The switch (sheet 12, `Cassette`)

`Z53A`, a **74LS74** D flip-flop, sitting in the cassette circuit beside the port-FF
latch:

| Pin | Signal |
|---|---|
| 2 (`D`) | bus **`D7`**, net `CHARGEN_SEL` |
| 3 (`C`) | **`/OUTSIG`** — the same write strobe that clocks the 74LS175 |
| 4 (`/S`) | **JP4** |
| 1 (`/R`) | **JP5** |
| 5 (`Q`) | `/CGA` — enables the Kana generator, active low |
| 6 (`/Q`) | `/CGB` — enables the ASCII generator, active low |

Because the clock is `/OUTSIG`, **every `OUT (0FFh)` latches bit 7**, whatever else the
write was for. There is no separate port.

```
D7 = 0  ->  Q = 0  ->  /CGA low  ->  Z37, Kana
D7 = 1  ->  Q = 1  ->  /CGB low  ->  Z38, ASCII
```

### JP4 and JP5

Both are 3-pin headers with the centre pin on the flip-flop input, one end pulled to
+5 V through 4.7k (`R65`, `R67`) and the other to ground. Note the pin numbering runs
the opposite way on the two headers: JP4 pin 1 is the +5 V end, JP5 pin 2 is.

The table printed on the sheet:

| Setting | JP4 (`/S`) | JP5 (`/R`) | Result |
|---|---|---|---|
| **ASCII** | 2 = GND | 2 = +5 V | held **set**, `Q` = 1, `Z38` (ASCII) always |
| **Kana** | 1 = +5 V | 1 = GND | held **reset**, `Q` = 0, `Z37` (Kana) always |
| **Switchable** | 1 = +5 V | 2 = +5 V | both idle — **`D7` decides** |

In the switchable position the flip-flop has **no asynchronous input connected to
anything**. Nothing on the board can put it back: not power-on, not `/SYSRES`, and not
the front-panel RESET button (which is wired to the Z80's NMI in any case). Real
hardware powers up in whichever state it lands in and settles on the first
`OUT (0FFh)` — which the ROM issues early during cassette initialisation, so in practice
it settles on whatever bit 7 the ROM's shadow byte happens to hold, which is 0.

The emulator models this as: power-on selects generator A, and a reset deliberately leaves
the bit alone — a deterministic stand-in for hardware that comes up wherever it lands.

### Driving it from software — the trap

The obvious `OUT 255,128` **does not hold**, and this catches everyone.

The ROM never reads port `FF` back, so it maintains a shadow byte at `403Dh` and always
rewrites the *whole* latch from it. Three routines do this:

| Address | Code | Purpose |
|---|---|---|
| `021Eh` | `LD HL,0FF00h` / `LD A,(403Dh)` / `AND H` / `OR L` / `OUT (0FFh),A` / `LD (403Dh),A` | the general masked writer the cassette code uses |
| `04C3h` | `LD A,(403Dh)` / `AND 0F7h` / `LD (403Dh),A` / `OUT (0FFh),A` | 64 characters per line |
| `04F6h` | `LD A,(403Dh)` / `OR 08h` / `LD (403Dh),A` / `OUT (0FFh),A` | 32 characters per line |

All three preserve bit 7 **of the shadow**, not of the hardware. So a BASIC `OUT 255,128`
sets the flip-flop, and the next thing the ROM does that touches the width clears it
again — which, at the BASIC prompt, is immediate.

The fix is to set the shadow as well:

```basic
POKE 16445,128 : OUT 255,128    ' generator B (ASCII), and it stays
POKE 16445,0   : OUT 255,0      ' back to generator A (Kana)
```

`16445` is `403Dh`. From assembly, write `403Dh` and then `OUT (0FFh),A` — or just call
`021Eh` with `HL` set appropriately.

The emulator's test suite asserts this end to end, by booting the real ROM and watching a
bare `OUT 255,128` be undone.

## Port FF otherwise

Functionally identical to Rev G, but the 74LS175 (`Z4`) has its **D inputs wired to a
rotated set of bus bits**, with the outputs rotated to match, presumably for layout:

| Bus bit | Latch input | Output used | Net |
|---|---|---|---|
| `D2` | `D0` | `Q0` | `CASSREMOTE` |
| `D3` | `D1` | `/Q1` | `MODESEL` |
| `D1` | `D2` | `/Q2` | `CASSOUT2` |
| `D0` | `D3` | `Q3` | `CASSOUT1` |

Same pattern as Rev G — motor and `CASSOUT1` non-inverted, `MODESEL` and `CASSOUT2`
inverted — so software sees no difference. This sheet labels the bus bit feeding the
mode select `/MODESEL`, which is the more accurate name: the bus bit is the complement
of the `MODESEL` net.

The read buffers are `Z59A` (`MODESEL` -> `D6`) and `Z59B` (`CASSIN` -> `D7`), both
74LS367, same as Rev G's `Z44F`.

## What 32-column mode physically does (sheet 14, `VideoMode`)

`MODESEL` is the select input of `Z27`, a **74LS157** quad 2-to-1 multiplexer labelled
"Mode Selector", choosing between two clock rates for `SHIFT`, `C0`, `DOT_CLK` and
`HCLK`:

- `CLK` — 10.6445 MHz, 64 columns
- `CLK_DIV2` — 5.32225 MHz, 32 columns

So 32-column mode halves the **shift rate**: each character occupies twice the horizontal
time and the same 5-dot glyph is stretched, which is why the odd cells vanish rather than
being blanked. The emulator reproduces the visible result in `render_ram`; this is the
mechanism behind it.

**`DOT_CLK` does not halve with it.** `Z27`'s `Zc` output switches from `Z6`'s Q3 (÷12) to its
Q2 (÷6) in the same move, so `DOT_CLK` stays at 887.042 kHz in both modes — which is why the
line rate, and everything derived from it, is independent of the column width. `Z27`'s `Zb`
output ties `C0` to ground in 32-column mode, which is what drops the odd cells.

## PAL

Not relevant to the emulator — it models NTSC timing — but it is the other reason this
board exists, and the mechanism is worth stating because it is not what the frequencies
first suggest.

**Nothing above the character-row rate changes.** Same crystal — `Y1` is 10.6445 MHz here and
on all four US boards — same 887.042 kHz character clock, same **15.84 kHz line rate**, and the
same **192 active scan lines**. Sheet 15 prints PAL values in parentheses, and the first
annotation that carries one is the character-row rate: everything above it is unparenthesised
because it is identical in both modes.

PAL buys its 50 Hz entirely out of **blanking**.

### The two counters that change

Both resets are built the same way: a 3-input NAND in `Z5` (74LS10) inverted by `Z26`
(74LS14), so the counter clears when all three terms are high. The jumper picks one term.

**Character line counter `Z35`** — reset `= L3 · L2 · JP10`:

| | JP10 common | resets at |
|---|---|---|
| NTSC | `L2` | **12** scan lines per character row |
| PAL | `Z46` pin 4 | **12**, or **13** while `R0 · VDRV` is high |

`Z46` pin 4 is `L0 + ¬(R0 · VDRV)`, assembled by `Z44A` (74LS00, `R0` and `VDRV`), `Z45A`
(74LS02, that against `L0`) and `Z46`'s second inverter. So in PAL the counter needs `L0` as
well, one count later, but only inside the window `Z44A` opens once per frame.

**Row counter `Z7`** — clocked by `R0`, its outputs weighted `R1` = 1, `R2` = 2, `R3` = 4 and
`VDRV` = 8; reset `= VDRV · R1 · JP6`:

| | JP6 common | resets at | rows per frame |
|---|---|---|---|
| NTSC | `R2` | 8 + 2 + 1 = **11** | 22 |
| PAL | `R3` | 8 + 4 + 1 = **13** | 26 |

`R0` is a ÷2 prescaler ahead of `Z7` (`Z34`'s Q0), so each count spans two character rows —
which is why 11 counts are 22 rows. The sheet prints exactly this as `CP0/11 (CP0/13)`.

*`R0`–`R3`, `L0`–`L3` and `C0`–`C5` are counter-output nets. `R1`, `R2`, `R3` and `C1`–`C5`
are also real component designators on this board; the nets are what is meant here.*

### What that adds up to

`VDRV` is `Z7`'s Q3, so it is low for counts 0–7 — **16 character rows, the visible picture, in
both modes**. The difference is what follows:

| | blanking | lines per frame | frame rate |
|---|---|---|---|
| NTSC | counts 8–10 = 6 rows × 12 | 192 + 72 = **264** | 15840 / 264 = **60.000 Hz** |
| PAL | counts 8–12 = 10 rows, five of 12 and five of 13 | 192 + 125 = **317** | 15840 / 317 = **49.969 Hz** |

So PAL costs four extra character rows and five extra scan lines, all of them blank, at the
bottom of the frame. The sheet's PAL column — 1.30 kHz, 650, 325, 162.5, 81.25, 50 Hz — is
**rounded**; the exact values are 1299.2, 649.6, 324.8, 162.4, 81.2 and 49.969. That rounding
is the only reason 15840 / 50 = 316.8 looks like it fails to divide.

### V-sync has to move too, and that is the other pair of jumpers

A frame four rows longer needs its vertical sync pulse in a different place, so sheet 20
carries its own identical `PAL C→2 / NTSC C→1` table for **JP7 and JP8**. Through `Z52`
(74LS08) the pulse is `VDRV · L3 · ¬R0 ·` `R1` in NTSC and `VDRV · L3 · ¬R0 ·` `¬R1 · R2` in
PAL — `Z7` count 9 against count 10, one count into the blanking window either way. `JP7`
selects `R1` or its inverse from `Z33`; `JP8` selects a hard high through `R64` or `R2`.

**So the mode is four jumpers, not two:** `JP6` and `JP10` set the frame rate, `JP7` and `JP8`
follow it with the sync pulse. Sheet 15 carries the note "See Video Sync for more jumpers".

## The full jumper map

| Jumper | Sheet | Function |
|---|---|---|
| JP1, JP2, JP3 | 5 `AddressDecoder` | ROM select: which of `1000–1FFF`, `2000–2FFF`, `3000–33FF`/`3000–3FFF` the ROM sockets answer |
| **JP4, JP5** | 12 `Cassette` | **Character generator: ASCII / Kana / Switchable** |
| JP6, JP10 | 15 `VideoCounter` | **PAL / NTSC** — the two counter resets that set the frame rate |
| JP7, JP8 | 20 `VideoSync` | **PAL / NTSC** — the matching vertical sync position |
| JP9 | 21 `VideoMixer` | `+5V` to pin 1 of the monitor socket |

Per the BOM, JP1–JP3 and JP9 are single jumpers; JP4–JP8 and JP10 are 3-pin ("double")
headers.

`JP9` is not a video-mode option despite sitting on the mixer sheet: its two pins are `+5V` and
pin 1 of `J2`, the 5-pin DIN the monitor plugs into, whose video is on pin 4 and ground on pin
5. It offers the monitor power, nothing more.

## Emulator support

`--charset-b <FILE>` fits the second generator; `--chargen a|b|switchable` sets the
JP4/JP5 position, defaulting to `switchable` when a second image is given. The switch itself is
port `FF` bit 7, edge-detected against the flip-flop's own state.

Not modelled: PAL timing, the ROM-select jumpers, and the off-board keyboard ROM
selector. None of them change what a program observes on a machine running the stock
Level II ROM at 60 Hz.

## How the claims here are checked

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

- `japanese-sheet-map`
- `japanese-pal-ntsc-decode`

If a claim above and its assertion disagree, one of them is wrong and the run says so.
