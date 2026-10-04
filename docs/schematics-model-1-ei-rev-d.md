# Model I Expansion Interface Rev D — a sheet-by-sheet reading

Source: `TRS80_Model_I_EI_D_Schematics.pdf`, RetroStack's reconstruction of the Expansion
Interface (drawing `1700077 D E1`, rev E1A, 14 sheets, KiCad 9.0.7). Sheet numbers below are
PDF pages, and each is named by its `.kicad_sch` file so a claim can be traced back.

The top sheet describes the board as *"System with interrupt request generator & buffered
data-read"*, which is the whole design in five words: two interrupt sources OR'd onto one
open-collector line, and a pair of bus buffers that report which of them is asking.

Four things the emulator does that the period documentation gets wrong were settled by these
sheets; they are listed at the end.

## Sheet inventory

| # | Sheet | What is on it |
|---|---|---|
| 1 | `TRS80_Model_I_EI_RevD` | Top level. The interrupt generator and the D7/D6 buffers. |
| 2 | `CardEdgeInterface` | `J2` to the keyboard unit, address/data buffering, and the RAS/CAS/MUX generator. |
| 3 | `CardEdgeInterfaceExtension` | `J3`, the pass-through for chaining another device. |
| 4 | `InternalExpansion` | `J10`/`J1`, the internal connector the RS-232 card plugs into. |
| 5 | `Clock` | 4 MHz crystal, a 74LS90 ÷10 and a 74LS74 ÷2. |
| 6 | `AddressDecoder` | The whole `37Ex` decode: 74LS30, two 74LS139s and a 74LS155. |
| 7 | `Timer` | The 40 Hz chain and the two flip-flops that make it an interrupt. |
| 8 | `LinePrinter` | 74LS273 data latch, 74LS123 strobe, four 74LS367 status buffers. |
| 9 | `FloppyController` | The FD1771, its drive-select latch, the motor one-shot and `J5`. |
| 10 | `Cassette` | A relay that routes the keyboard unit's cassette port to one of two sockets. |
| 11 | `Memory_Management` | Bank selects, the address multiplexer and the data-bus gating. |
| 12 | `RAM` | Sixteen MK4116 DRAMs — 32K in two banks. |
| 13 | `Power` | Two LM723C regulators for +5V and +12V, and a −5V divider. |
| 14 | `Capacitors` | Decoupling, and the unused gates. |

## The address decode (sheet 6)

Three chips, and between them they explain every aliasing quirk the emulator models.

**`Z43A` (74LS30, 8-input NAND)** takes `A5`, `A6`, `A7`, `A8`, `A9`, `A10`, `A12`, `A13`.
For `37E0` those are all high, so its output goes low. **`A4` is not one of its inputs, and
no `37Ex` decode looks at it** — though it is not unused: it reaches `Z28D` (the `E8`–`EF` port
decode, via `Z28C` to `/E8`), `Z36` and `Z45`.

**`Z40A` (74LS139, half 1)**, enabled by `/RAS`, decodes `A15`/`A14`:

| output | range | net |
|---|---|---|
| `O0` | `0000–3FFF` | enables `Z40B` |
| `O1` | `4000–7FFF` | not connected — that RAM is in the keyboard unit |
| `O2` | `8000–BFFF` | `/32K` |
| `O3` | `C000–FFFF` | `/48K` |

So the `37Ex` block is gated by `A15 = A14 = 0`; it does **not** alias into `7FEx`, `BFEx`
or `FFEx`.

**`Z40B` (74LS139, half 2)** takes `A1 ← A11` and `A0 ← Z43A`, enabled by `Z40A.O0`. Its
`O0` is labelled on the drawing as **`37E0..37FF`** — a 32-byte block, because `A4` is a
don't-care. `O2` (`3FE0..3FFF`) is left unconnected.

**`Z39` (74LS155, dual 2-to-4 decoder)** takes `A0 ← A2` and `A1 ← A3` and produces eight
strobes, the a-side gated by `/RD` and the b-side by `/WR`:

| | read | write |
|---|---|---|
| `37E0–37E3` | `/37E0_READ` | `/37E0_WRITE` |
| `37E4–37E7` | **not connected** | `/CSW` |
| `37E8–37EB` | `/37E8_READ` | `/37E8_WRITE` |
| `37EC–37EF` | `/37EC_READ` | `/37EC_WRITE` |

Two consequences the emulator depends on:

1. **Each group is a four-byte alias.** `A1` and `A0` are decoded nowhere except inside the
   FD1771, which is why the ROM's boot loader can write drive select to `37E1` (`069F`) and
   the emulator can answer at `37E0`.
2. **`37E4` is write-only.** `Z39` pin 6 goes nowhere, so a read of the cassette-select
   group leaves the bus undriven and returns `FF`.

## The clock (sheet 5)

`Y1` is **4 MHz**, buffered through two 4049B inverters into `Z22` (74LS90) wired as a ÷10:
`CP0` takes the 4 MHz, `Q0` (2 MHz) feeds back into `CP1`, and `Q3` is **400 kHz**, the net
named `CLK/10`. `Z25A` (74LS74) then divides `Q0` by two with its `/Q` fed back to `D`,
giving **1 MHz** on `/CLK/2` — the FD1771's clock, which is the rate a 1771 wants for 5¼-inch
drives.

## The timer, and how it is acknowledged (sheet 7)

400 kHz enters a chain of four **4518** BCD counters — `Z23A`, `Z23B`, `Z24A`, `Z24B` — each
dividing by ten, so the drawing carries the frequency at every stage: 400 kHz, 40 kHz, 4 kHz,
400 Hz, **40 Hz**.

Then two 74LS74s, and this is the part worth reading carefully.

```
Z26A:  C  <- 40 Hz        D <- GND    /S <- /37E0_READ   /R <- HI    Q -> "20 Hz"
Z26B:  C  <- /37E0_READ   D <- GND    /S <- Z26A.Q       /R <- HI    Q -> TIMER_INTRQ
```

Both have `D` tied to ground and both are asynchronously **set** — not reset — by activity on
`37E0`. Reading the pair together:

- `Z26A.Q` sits at 0. A read of `37E0` sets it; the next 40 Hz edge clocks it back to 0.
  It is `Z26B`'s `/S`, so while it is 0 `Z26B` is held set.
- `Z26B.Q` is therefore forced to 1 at each 40 Hz tick and cleared by the rising edge at the
  **end** of a read of `37E0`.

`Z26B.Q` drives `Z34F` (7416, open-collector inverter) which pulls the shared `/INT` low, so
`Q = 1` means an interrupt is pending.

**The acknowledge is a read of `37E0`, not a write.** Nothing on this sheet is connected to
`/37E0_WRITE`. The "20 Hz" annotation on the intermediate net is descriptive rather than
structural: if the CPU services every interrupt, `Z26A.Q` toggles once per 40 Hz tick and the
node carries a 20 Hz square wave.

## The interrupt generator and the data-read buffers (sheet 1)

```
TIMER_INTRQ  -> Z34F (7416, o.c.) -\
                                    >- /INT  (no pull-up on this board)
FLOPPY_INTRQ -> Z34E (7416, o.c.) -/

TIMER_INTRQ  -> Z49E (74LS367 pin 12 -> 11) -> D7
FLOPPY_INTRQ -> Z49F (74LS367 pin 14 -> 13) -> D6
                both enabled by pin 15 (/2G) <- /37E0_READ
```

Nothing on the Expansion Interface pulls `/INT` up. The net is `Z34.10`, `Z34.12`, `J2.21`,
`J3.21` and `J10.15` — two open-collector outputs and three connectors, no resistor. The pull-up
is on the main board, at the end of the line that also reaches the Z80's own `/INT` pin. `R16`
and `R24` define the `HI1` and `HI2` rails and touch neither `/INT` nor either `INTRQ`, which
`ei-r16-r24-are-not-int-pullups` asserts.

So a read of `37E0` puts **the timer on D7 and the floppy on D6**, and nothing drives
`D5`–`D0`, which float high. An idle read is `3F`; a pending timer interrupt reads `BF`.

The floppy half is a **buffer, not a latch**: it reports the FD1771's `INTRQ` pin as it stands
at that instant. The chip's own rules clear it — reading the status register, or writing a new
command — and `/37E0_READ` has no effect on it whatsoever.

## The floppy controller (sheet 9)

**`Z42`, an FD1771.** `/RE ← /37EC_READ`, `/WE ← /37EC_WRITE`, `A0 ← A0`, `A1 ← A1`, so the
four registers land at `37EC` command/status, `37ED` track, `37EE` sector, `37EF` data.
`/CS` is tied to ground — the read and write strobes do the selecting. `CLK` is the 1 MHz from
sheet 5, `/MR` comes from `/SYSRES`, and `INTRQ` (pin 39) is pulled up by `R30` (10k).

Three pins are worth calling out:

- **`DRQ` (pin 38) is not connected.** There is no DMA and no data-request interrupt; software
  polls status bit 1, which is exactly what the ROM's boot loader does at `06C0`.
- **`/XTDS` (pin 25) is tied high** through `R29`, selecting the chip's internal data
  separator. This is the pin a doubler takes over.
- `TG43` and `PH3` are unconnected; `3PM` is tied high, selecting step/direction rather than
  three-phase stepper drive.

**`Z47` (74LS175) is the drive-select latch.** `D0`–`D3` take data bits 0–3, `Cp ← /37E0_WRITE`,
and `/Mr` comes from the one-shot below. `Q0`–`Q3` drive `DS0`–`DS3` on `J5` through 7416s.

**`Z33B` (74LS123) is the motor one-shot.** `R25` = **200k**, `C62` = **33 µF**, and the
74LS123's `0.45·R·C` puts the pulse at **2.97 seconds**. It is triggered on the falling edge of
`/37E0_WRITE`, so every write to the drive-select group retriggers it. Its `Q` goes two places:

- `Z41B` (7416) → **`MOTOR_ON`** on `J5`;
- **`Z47`'s `/Mr`** — so when the one-shot expires it *clears the drive-select latch*.

**`Z46A` (74LS20)** NANDs the four `/Q` outputs of `Z47`, giving "any drive is selected", and
that drives the FD1771's **`HLT` and `READY`** together. The 34-pin Shugart bus has no READY
line, so the board synthesises one from the latch: with no drive selected the controller
reports NOT READY, and a command issued more than ~3 s after the last `37E0` write finds the
latch already cleared.

**`J5`** carries `INDEX_PULSE`, `DS0`–`DS3`, `MOTOR_ON`, `DIR_SEL`, `STEP`, `WRITE_DATA`,
`WRITE_GATE`, `TRACK_ZERO`, `WRITE_PROTECT` and `READ_DATA`. **There is no side-select line
and no ready line** — single sided, single density, as shipped.

## The line printer (sheet 8)

`Z48` (74LS273) latches the data byte on `/37E8_WRITE` and drives `DATA1`–`DATA8` on `J4`.
`Z33A` (74LS123, 20k × 200 pF ≈ 1.8 µs) turns the same strobe into `DATA_STROBE`.

Reads go through four sections of a **single** 74LS367 — `Z49`, the only one on the board —
enabled by `/37E8_READ` on pin 1:

| buffer | signal | bit |
|---|---|---|
| `Z49D` | `/BUSY` | D7 |
| `Z49C` | `/OUT_OF_PAPER` | D6 |
| `Z49B` | `/UNIT_SELECT` | D5 |
| `Z49A` | `/FAULT` | D4 |

`D3`–`D0` have no buffer and float high.

`Z49`'s remaining two sections are on the *other* enable, pin 15 (`/37E0_READ`), and put the two
interrupt sources onto `D7` and `D6`. Both of their nets are short-named `~{INTRQ}` because each
is the `INTRQ` output of its own sheet — they are `/Timer/~{INTRQ}` and
`/Floppy Controller/~{INTRQ}` in full, and the drawing labels them `TIMER_INTRQ` and
`FLOPPY_INTRQ` where they meet the buffers. One hex buffer therefore serves both the printer
status port and the disk interrupt status port. The ROM's printer routine at `05D1` is
`LD A,(37E8) / AND F0 / CP 30`, so a ready printer must present `0011` in the top nibble — and
the emulator's `3F` is that pattern plus the four floating bits. With nothing plugged in every
input floats high and the port reads `FF`, so `LPRINT` hangs, which is what a real machine
does.

## The cassette (sheet 10)

There is **no cassette circuitry on this board**. `/CSW` — a write to `37E4`–`37E7` — clocks a
cross-coupled 74LS00 R-S latch (`Z17B`/`Z17C`) from `D0`. That drives a 75452 (`Z18A`) and a
physical relay, **`K1`**, which switches the keyboard unit's own cassette port (`J8`, marked
"Cassette M1") between `J6` (Cassette 1) and `J7` (Cassette 2).

The motor relay, the DAC and the input comparator all stay in the keyboard unit; the
Expansion Interface only decides which socket they are wired to. That is exactly the model the emulator implements: two decks, one shared motor, routed by a
one-bit unit select. See [`cassette.md`](cassette.md).

## Memory (sheets 11 and 12)

`Z27D` ORs `/48K` with `/CAS` to make `UPPER CAS`, and `Z27A` ORs `/32K` with `/CAS` to make
`LOWER CAS`. Sixteen **MK4116** 16K×1 DRAMs in two banks of eight give **32K**: `8000–BFFF`
lower, `C000–FFFF` upper. With the keyboard unit's 16K that is the 48K maximum.

`Z35`/`Z36` (74LS157) multiplex `A0`–`A6` against `A7`–`A13` for the DRAMs, and `Z29`/`Z31`
(74LS244) gate the data bus with 33 Ω series resistors on the address lines.

## The internal expansion connector (sheet 4)

This is where the RS-232 card plugs in, and it decodes more ports than the card uses.

```
Z46B (74LS20):  A7 . A6 . A5 . A3          -> inverted by Z41A (7416)
Z28D (74LS00):  /A4
Z28C (74LS00):  NAND of those two          -> /E8
```

So `/E8` asserts for `A7 A6 A5 = 111`, `A4 = 0`, `A3 = 1` — **ports `E8`–`EF`**, eight of them,
with `A2`, `A1` and `A0` passed through to the card on `J10` to decode as it likes. `J10` also
carries `D0`–`D7`, `/SYSRES`, `/IN`, `/OUT` and **`/INT`**, so a card here can pull the
interrupt line — though nothing reports it in the `37E0` buffers, which is why Model I serial
software polls.

`J1` carries sixteen spare signals `S0`–`S15` straight through to a second connector.

## Power (sheet 13)

Two LM723C regulators with MJE2955 pass transistors produce +5V and +12V from a 19.8V DC
supply; −5V comes from a 220 Ω divider and a 1N5231 zener. The DRAMs need all three, which is
the origin of the Expansion Interface's reputation for marginal power.

## What this sheet set settles

Four things the emulator implements trace to these sheets rather than to the ROM or to period
documentation:

1. **The timer interrupt is acknowledged by *reading* `37E0`.** `Z26A` and `Z26B` are both
   clocked or set from `/37E0_READ`, and nothing on sheet 7 touches `/37E0_WRITE`. A write
   does not acknowledge it.
2. **The timer is on D7 and the floppy on D6**, from `Z49E` and `Z49F` on sheet 1, and
   confirmed independently by xtrs (`M1_TIMER_BIT 0x80`, `M1_DISK_BIT 0x40`). The order is
   easy to assume backwards.
3. **`A4` is not in the `37Ex` decode**, so the latch block is `37E0–37FF` and `37F0–37FF`
   mirrors it. (It does reach the port decode, `Z36` and `Z45`.)
4. **The drive-motor one-shot is 2.97 s, not 3.00**, and it does not merely time the motor —
   it clears the drive-select latch, which drops `READY` through `Z46A`.

## Terminology note

RetroStack numbers parts `Zn` following the original Radio Shack drawings, and as on the main
board the numbering is **not stable between boards**. `Z34` here is a 7416 hex inverter; on
the Rev G main board `Z34` is a mask ROM. Always name the part and the sheet, not just the
designator.

## How the claims here are checked

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

- `ei-sheet-map`

If a claim above and its assertion disagree, one of them is wrong and the run says so.
