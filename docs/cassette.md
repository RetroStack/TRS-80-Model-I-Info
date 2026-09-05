# The cassette interface

Two bits out through a resistor ladder, one bit back through an op-amp and a flip-flop, and a
relay for the motor. There is no UART, no baud-rate generator and no framing: the ROM shapes
every pulse itself and reads the tape back by timing.

`[sheet]` from the Rev G reconstruction, sheet 10, which is titled **"Cassette Interface with
Video Mode Select"** — the display width lives on this sheet because it shares the port `FF`
latch. Port `FF` as a whole is described in [`revisions.md`](revisions.md); this document is
about the tape half of it.

## The output: a two-bit DAC

`Z59`, a 74LS175, latches four bits on the port `FF` write strobe. Two of them drive the tape:

| bus bit | output used | the sheet calls it |
|---|---|---|
| `D0` | `Q0` (pin 2) | `CASSOUT1` |
| `D1` | **`/Q1`** (pin 6) | `CASSOUT2` |

Those two names are printed on the drawing; they are not net labels, so they do not appear in
[`netlists/revg.md`](../netlists/revg.md) — the nets there are auto-named after the pins. What is
in the netlist, and is the proof, is that **`/Q0` on pin 3 and `Q1` on pin 7 go nowhere at
all.** Each bit uses exactly one side of its flip-flop, and for `D1` that side is the inverted
one.

**`CASSOUT2` comes off the inverted side of the flip-flop**, and that one fact explains the
whole shape of the output. The two signals drive a resistor network — `R54` and `R55` at 7.5 kΩ,
`R56` at 220 kΩ and `R53` at 1.2 kΩ — and because one is inverted the four bit patterns do not
produce four evenly spaced voltages:

| `D1:D0` | volts |
|---|---|
| `00` | **0.46** |
| `01` | 0.85 |
| `10` | 0 |
| `11` | 0 |

The rest state is `00`, which is **not** zero volts: an idle tape output sits at 0.46 V. Writing
a pulse means stepping to `01` and back, and both `1x` patterns collapse to the same 0 V because
the inverted bit dominates the ladder. The emulator's `LEVEL_MV = [460, 850, 0, 0]` was measured
from ROM behaviour before anyone read the circuit; this is the circuit that produces it.

## The input: an op-amp and a flip-flop the CPU cannot clear directly

The return path is **`Z4`**, an LM3900 quad Norton amplifier. Its four sections are clamped
between stages by `CR4`, `CR5` and `CR6`, with the reference divider built from `R33`–`R38`,
`R41`, `R42` and `R45`. Pin 10 is the output.

That output sets an **R-S flip-flop made from two cross-coupled 74LS132 gates, `Z24C` and
`Z24D`**. The sheet annotates its reset in as many words:

> Any write to port … will reset flip-flop

`/OUTSIG` arrives on pin 13. So **any** `OUT` to port `FF` clears the tape-input flip-flop,
whatever the write was actually for — setting the display width clears it, and so does starting
the motor. That is not a side effect the ROM tolerates, it is the mechanism it uses: the read-bit
routine at `0241h` writes port `FF` to arm the flip-flop, waits, then reads bit 7 back to see
whether a pulse arrived in the window.

Bit 7 of `IN (0FFh)` is that flip-flop, buffered onto the bus by `Z44E`.

## The motor

`CASSREMOTE` is `Q2` of the same latch, non-inverted, from bus bit `D2`. It drives `Z41A`, a
75452 dual peripheral driver, which pulls relay **`K1`**; `CR3` is the flyback diode across the
coil, cathode to `+5V`. The relay contacts are the `REM` pins of the 5-pin DIN socket `J3`.

The ROM's `CASON` routine at `0212h` loads `HL` with `0FF04h` before calling the port `FF`
writer, so the motor is bit 2 — `04h` is the OR mask.

## Why a bare `OUT` to port FF is never quite bare

The ROM never reads port `FF` back. It keeps a shadow byte at `403Dh` and rewrites the whole
latch from it, so every cassette operation also rewrites the display width, and every width
change also rewrites the cassette bits. The entry at `021Eh` is the general masked writer:

```
021E   LD HL,0FF00h     ; AND FFh / OR 00h - a rewrite with no change
       LD A,(403Dh)
       AND H
       OR L
       OUT (0FFh),A
       LD (403Dh),A
```

Called with `HL = 0FF00h` it changes nothing at all, which is the point: the write itself is the
side effect, because it resets the input flip-flop.

## The tape format is entirely software

Nothing on the board knows what a bit is. The ROM writes a **255-byte leader of zeros** followed
by a sync byte, then one pulse pair per bit. The leader loop is `LD B,0FFh` with the `XOR A`
outside it, so it is 255 bytes and not 256 — a detail worth stating because the obvious reading
of `LD B,0` would give 256.

## Two decks, on the Expansion Interface

The keyboard unit has one cassette port. The Expansion Interface adds a second by **routing**,
not by duplicating anything: `/CSW`, a write to `37E4`–`37E7`, clocks a cross-coupled 74LS00 R-S
latch (`Z17B`/`Z17C`) from `D0`, which drives a 75452 (`Z18A`) and a physical relay, `K1`, that
switches the keyboard unit's own cassette port (`J8`, marked "Cassette M1") between `J6`
(Cassette 1) and `J7` (Cassette 2).

**There is no cassette circuitry on the Expansion Interface at all.** The DAC, the input
comparator and the motor relay all stay in the keyboard unit; the Expansion Interface only
decides which socket they are wired to. See
[`schematics-model-1-ei-rev-d.md`](schematics-model-1-ei-rev-d.md).

## What this settles

1. **The output is a two-bit DAC whose rest state is 0.46 V**, not zero, because `CASSOUT2` is
   taken from `/Q1`.
2. **Both `1x` patterns give 0 V**, so the DAC has three levels and not four.
3. **Any write to port `FF` clears the input flip-flop**, and the ROM depends on it.
4. **The motor is bit 2**, driven through a 75452 and a relay with `CR3` across the coil.
5. **The leader is 255 bytes**, not 256.
6. **A second deck is a routing relay**, not a second interface.

## How the claims here are checked

Every factual claim in this document has an executable assertion in [`verify/claims.py`](../verify/claims.py). They are run by:

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

which also validates the netlist parser against KiCad's own XML export before testing anything. The assertions covering this document:

- `level2-leader-is-255-bytes`
- `rom-cason-sets-bit-2`
- `cassette-output-network`

If a claim above and its assertion disagree, one of them is wrong and the run says so. See [`verify/README.md`](../verify/README.md) for why this exists.
