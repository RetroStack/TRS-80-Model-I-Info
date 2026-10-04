# Model I Rev G schematics — a sheet-by-sheet reading

Source: `TRS80_Model_I_G_E1_Schematics.pdf`, RetroStack's reconstruction of the Rev G
main board (drawing rev E1C, 21 sheets, KiCad 8.0.3). Sheet numbers below are PDF pages,
and each is named by its `.kicad_sch` file so a claim can be traced back.

This is the **standard** board — the one the emulator models by default. Everything the
Japanese machine does differently is in `schematics-japanese-model-1.md`.

Three things the emulator does that the period documentation gets wrong were settled by
these sheets rather than by the ROM; they are listed at the end.

## Sheet inventory

| # | Sheet | What is on it |
|---|---|---|
| 1 | `TRS80_Model_I_G_E1` | Top level. The global net names every other sheet uses. |
| 2 | `Clock` | The master oscillator, buffered through `Z42` (74LS04). |
| 3 | `CPU` | The Z80 (`Z40`), its reset and wait logic. `Z23`, `Z37`, `Z52`, `Z53`, `Z56`, `Z69`, `Z70`, `Z72`–`Z74`. |
| 4 | `CPUGating` | Address and data buffering onto the internal buses — **six** 74LS367 hex three-state buffers (`Z22`, `Z38`, `Z39`, `Z55`, `Z75`, `Z76`). |
| 5 | `AddressDecoder` | A **74LS156** dual 2-to-4 decoder — **`Z21`**, not `Z3` — plus `Z36` (74LS32), producing `/ROMA`, `/ROMB`, `/RAM`, `/KYBD`, `/VID`. `Z3` is the strapping block that wires the decoder's open-collector outputs to those names. |
| 6 | `RAM` | Eight 4116 16Kx1 DRAMs (`Z13`–`Z20`), address multiplexers `Z35`/`Z51` (74LS157), the `Z71` strapping block, and `Z67`/`Z68` (74LS367). `/RAS` and `/CAS`. |
| 7 | `RAM_ROM_Interface` | Where `RAMD0-7` and `ROMD0-7` meet the CPU data bus. **No components sit on this sheet** — the buffers `Z67`/`Z68` are drawn on `RAM`. |
| 8 | `ROM` | `Z33` and `Z34`, selected by `/ROMA` and `/ROMB`. The symbols are `2364_20L` and `2332_20L_21L` — an 8K and a 4K mask ROM, differing in chip-select polarity. |
| 9 | `Keyboard` | Connector `J100` and `/KYBD`. The matrix itself is off-board. |
| 10 | `Cassette` | **"Cassette Interface with Video Mode Select"** — the whole of port `FF`. See below. |
| 11 | `Video` | Container sheet; the global video nets. |
| 12 | `VideoCounter` | The dot/character/line counter chain: `Z58` (74LS92), `Z12`/`Z32`/`Z50`/`Z65` (74LS93), `Z43` (74LS157), `Z66` (74LS11). Produces `SHIFT`, `/LATCH`, `HDRV`, `VDRV`. |
| 13 | `VideoAccessMultiplexer` | 74LS157s (`Z31`, `Z49`, `Z64`) arbitrating CPU vs. display access to video RAM. |
| 14 | `VideoRAM` | The 1K screen: **seven** 2102s — `Z45`–`Z48` and `Z61`–`Z63` — with `Z30` (74LS02) deriving bit 6 and `Z60` (74LS367) buffering. `Z44` is drawn on the cassette sheet, but its first section buffers video RAM bits 0–3 onto `D0`–`D3` under `/VRD`. |
| 15 | `Video Latch` | `Z7` (74LS74), `Z27` (74LS175) and `Z28` (74LS174) latching the fetched byte; `CHARGAP`, `GRAPHICS`, `/BLANK`, `/VCLR`. |
| 16 | `VideoGen` | The **MCM6670** character generator (`Z29`), `Z10`/`Z11` (74LS166) shift registers, `Z8` (74LS153) block-graphics synthesiser, `Z9` (74LS04) and `Z26` (74LS20). |
| 17 | `VideoSync` | Composite sync from `HDRV`/`VDRV`. |
| 18 | `VideoMixer` | `Z41` (75452) combining `PIXEL` and `SYNC` onto the video output. |
| 19 | `CardEdgeInterface` | The 40-pin Expansion Interface bus. |
| 20 | `Power` | LM723C regulator, MJE34/TIP29A pass transistors, MDA202 bridge. |
| 21 | `Capacitors` | Decoupling only. |

**This board has two strapping positions.** `Z3` and `Z71` carry no value in the schematic and
appear in the bill of materials as *"Z3, Z71 │ 2 │ Jumper │ 8-Bit DIP Switch │ Replacement"*.
They are easy to miss: there are no `JPn` designators anywhere and the drawings never use the
word "jumper", so the only way to find them is the bill of materials or the empty `Value`. See
[`revisions.md`](revisions.md).

## Port FF, in full (sheet 10)

Everything the CPU can do with `IN`/`OUT` on a base Model I is on this one sheet, and it
is titled "Cassette Interface with Video Mode Select" because the mode select genuinely
lives in the cassette circuit.

### Address decode

`Z54` (74LS30, 8-input NAND) tests `A1`–`A7` all high — `A7` twice, to fill its eight inputs —
and `A0` arrives inverted through `Z52C`, the pair combining in `Z36A` (74LS32). That result is
combined with `/IN` and `/OUT` in **`Z25`** (74LS32) to give **`/INSIG`** on pin 6 and
**`/OUTSIG`** on pin 8, the read and write strobes. Note that `Z40` is the Z80 itself and `Z36`
is a 74LS32; the 8-input NAND is `Z54`. `A8`–`A15` are not decoded at all, which is why
`IN A,(0FFh)` works no matter what `A` holds — the Z80 puts `A` on the high address byte
and nothing here looks at it.

### The output latch: a 74LS175, and two of its four bits are inverted

`Z59` is a 74LS175 quad D flip-flop clocked by `/OUTSIG`. Only four bits of the byte are
latched; bits 4–7 go nowhere. **Two of the four outputs are taken from the inverted
side of the flip-flop**, which is easy to miss and explains two long-standing puzzles:

| Bus bit | Latch input | Output used | Net | Function |
|---|---|---|---|---|
| `D0` | `D0` (pin 4) | **`Q0`** (pin 2) | `CASSOUT1` | DAC bit, non-inverted |
| `D1` | `D1` (pin 5) | **`/Q1`** (pin 6) | `CASSOUT2` | DAC bit, **inverted** |
| `D2` | `D2` (pin 12) | **`Q2`** (pin 10) | `CASSREMOTE` | motor relay, non-inverted |
| `D3` | `D3` (pin 13) | **`/Q3`** (pin 14) | `MODESEL` | mode select, **inverted** |

`Q1`, `/Q0`, `/Q2` and `Q3` are all marked no-connect on the sheet.

The `/Q1` inversion is why the cassette DAC's voltage table looks arbitrary. `CASSOUT1`
(from `Q0`) and `CASSOUT2` (from `/Q1`) drive a resistor network — `R54` 7.5k, `R55`
7.5k, `R56` 220k and `R53` 1.2k — so the rest state `D1:D0 = 00` already sits at
0.46 V, `01` gives 0.85 V, and both `10` and `11` give 0 V. The emulator's level table
`[460, 850, 0, 0]` was measured from ROM behaviour long before anyone read the circuit;
this is the circuit that produces it, and [`cassette.md`](cassette.md) works it through.

### MODESEL, and bit 6 of the read

`MODESEL` is the net that leaves `/Q3`, so:

```
CPU writes D3 = 1  ->  Q3 = 1  ->  /Q3 = 0  ->  MODESEL low   ->  32 characters/line
CPU writes D3 = 0  ->  Q3 = 0  ->  /Q3 = 1  ->  MODESEL high  ->  64 characters/line
```

The sheet annotates the net in as many words: **`0 = 32 characters/line`,
`1 = 64 characters/line`**.

`MODESEL` then goes two places. It leaves for the video sheets (sheet 12) to halve the
dot rate, and it comes straight back onto the data bus through **`Z44F`, a 74LS367**:
pin 14 (`6A`, input) from `MODESEL`, pin 13 (`6Y`, output) to **`D6`**, enabled only
while the port `FF` read strobe is asserted.

So **bit 6 of `IN (0FFh)` is a genuine readback of the display width**, on stock
hardware, on every Model I. It is the one write-only-latch bit the machine hands back.
It is inverted relative to the bit that was written:

| | 64 columns | 32 columns |
|---|---|---|
| bare machine, no tape signal | `7Fh` (127) | `3Fh` (63) |
| with an Expansion Interface | `5Fh` (95) | `1Fh` (31) |

The familiar "`INP(255)` returns 127" is only the 64-column half of that.

### The rest of the read

The same 74LS367 (`Z44`, its second section, enabled by `/INSIG`) supplies `D7` from the
cassette input flip-flop alongside `D6`. Nothing on the main board drives `D5` on a port `FF`
read, nor bits 0–4: they float high.

The cassette input path is **`Z4`** (LM3900 quad Norton amplifier), whose four sections are
clamped between stages by `CR4`, `CR5` and `CR6`, with the reference divider built from
`R33`–`R38`, `R41`, `R42` and `R45`. Its pin 10 output feeds an **RS flip-flop made from two
74LS132 gates** — **`Z24C`/`Z24D`**, cross-coupled, with `/OUTSIG` on pin 13 as the reset. The sheet's own annotation next to the
write strobe reads *"Any write to port ... will reset flip-flop"*. That is the behaviour
the emulator's cassette input models — derivable from the ROM's `0241h` read-bit routine,
and stated here directly in the circuit.

### The motor

`CASSREMOTE` drives `Z41A` (75452 dual peripheral driver) which pulls relay `K1`, with
`CR3` as the flyback diode. The relay contacts are the `REM` pins of the 5-pin DIN
socket `J3`.

## The character generator (sheet 16)

One **MCM6670** (`Z29`), outside the CPU's address space, with `/CS` tied active. It
takes the latched display code and a 3-bit row count and returns five dots, which
`Z10`/`Z11` (74LS166) shift out serially as `PIXEL`. Block graphics never reach it: the
74LS153 — **`Z8`** alone — synthesises those from the stored bits directly, selected by the
`GRAPHICS` line the latch sheet derives from `D7`. `Z9` is a 74LS04 and is not the multiplexer.

This is the circuit-level statement of what [`video.md`](video.md) describes: 1024 bytes,
128 glyphs of 8 rows, 5 dots wide, and codes with bit 7 set bypassing the chip entirely.

## What this sheet set settles

Three things the emulator implements trace to these sheets rather than to the ROM:

1. **`IN (0FFh)` bit 6 is not undriven.** Notes written before these sheets were read said
   it "floats high"; `Z44F` says otherwise.
2. **Port `FF` bit 3 is inverted on the way out of the latch.** The software-visible
   behaviour (write 1 for 32 columns) is unchanged, but the board-level signal is
   `MODESEL` active high for 64 columns, which is what the readback reports.
3. **The cassette DAC's rest voltage is a consequence of `/Q1`,** not a quirk.

## Terminology note

RetroStack numbers parts `Zn` following the original Radio Shack drawings, but the
numbering is **not stable between board revisions**. On this board `Z59` is the port-FF
latch and `Z44` the read buffer; on the Japanese board those roles fall to `Z4` and
`Z59`. Always name the part and the sheet, not just the designator.

## How the claims here are checked

The sheet inventory and the designators above are asserted in
[`verify/claims.py`](../verify/claims.py), run by:

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

- `revg-sheet-map`
- `z21-is-the-address-decoder`
- `z3-z71-are-jumpers`
- `us-video-ram-is-7-bit`
- `port-ff-decode-ignores-high-address`

`revg-sheet-map` asserts the sheet inventory in full — every sheet, every IC, every value — so
the table above cannot drift from the schematic.

A few designators on this board are easy to transpose and worth checking twice: the 74LS156 is
`Z21` and not `Z3`; `Z40` is the Z80 itself, not a gate; the LM3900 is `Z4`, not `Z25`; the
cassette flip-flop is `Z24C`/`Z24D`, not `Z31`; and `Z44` is drawn on the cassette sheet, not
the video RAM one, though half of it buffers video RAM reads.
