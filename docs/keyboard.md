# The keyboard

There is no keyboard controller. There is no encoder, no debounce circuit, no diode matrix
and no interrupt. There are 65 switch positions, four ICs and two resistor references, and
everything else is done by the ROM.

That is not a simplification for an emulator's benefit — it is what the schematic shows, and
it is why keyboard handling is the part of Model I emulation that most often goes subtly
wrong.

## The matrix

`[sheet]` The key matrix lives on its own PCB. The main board's `Keyboard` sheet is a
connector and nothing else.

Eight address lines drive eight rows; eight column lines return to eight data bits.

**Row drivers — `Z1` and `Z2`, both 74LS05 hex inverters with open-collector outputs.** Four
of the six inverters in each are used; the other two in each package are unconnected.

| row | address line | inverter | first key on the row |
|---|---|---|---|
| 0 | `A0` | `Z1` pin 9 → 8 | `SW1` |
| 1 | `A1` | `Z1` pin 11 → 10 | `SW2` |
| 2 | `A2` | `Z2` pin 5 → 6 | `SW3` |
| 3 | `A3` | `Z2` pin 9 → 8 | `SW4` |
| 4 | `A4` | `Z1` pin 5 → 6 | `SW5` |
| 5 | `A5` | `Z1` pin 3 → 4 | `SW6` |
| 6 | `A6` | `Z2` pin 3 → 4 | `SW7` |
| 7 | `A7` | `Z2` pin 11 → 10 | `SW8` — **LSHIFT** |

`SW1`–`SW8` are one per row, in order, which is the tidiest thing about the numbering: the
eighth of them is LSHIFT, and that is the whole of row 7 apart from `SW9` beside it.

Row 7 carrying SHIFT is what makes `3880` the shift row, and it is the reason the ROM can
sample SHIFT separately from the key that was pressed.

**Column buffers — `Z3` and `Z4`, both 74LS368 inverting tri-state buffers**, each enabled by
`/KYBD` on pin 1. Their inputs are held up by an eight-element resistor pack `R1A`–`R1H`
(4.7 kΩ):

| pull-up | buffer | data bit | | pull-up | buffer | data bit |
|---|---|---|---|---|---|---|
| `R1G` | `Z3` 4→5 | **`D0`** | | `R1C` | `Z4` 4→5 | `D1` |
| `R1H` | `Z3` 2→3 | `D2` | | `R1E` | `Z3` 10→9 | `D3` |
| `R1A` | `Z4` 10→9 | `D4` | | `R1F` | `Z3` 6→7 | `D5` |
| `R1D` | `Z4` 2→3 | `D6` | | `R1B` | `Z4` 6→7 | `D7` |

## Why a read is the OR of the selected rows

This falls out of the open-collector row drivers, and the 1978 Radio Shack manual flags it as
the one thing worth knowing about the keyboard `[manual p.25]`:

> The inverters on the address lines are open collector types. You may not be able to see the
> address signal on `Z1` or `Z2`'s output unless one of the keys associated with that output
> is pressed. **With no key pressed, there is no voltage applied to the KR (Keyboard Row)
> lines. When a key is pressed, the associated pull-up resistor supplies voltage.**

A selected row is pulled low by its 74LS05. An unselected row is open-collector-off — high
impedance, contributing nothing. A closed key ties its row to its column, dragging that column
low against the pull-up, and the inverting 74LS368 turns that into a `1` on the data bus.

Two inversions cancel, and the wired-AND on the column line *is* a logical OR across every
selected row. So:

- **`3800` always reads zero.** No address bit high, so no row is pulled low, so nothing shorts.
- **`38FF` is "is any key down?"** — all eight rows selected at once.
- **A multi-row address genuinely aliases.** `3803` returns row 0 OR row 1. There is nothing to
  prevent it, because there are no diodes.

Measured, rather than argued. `A` is row 0 bit 1; `H` is row 1 bit 0:

| key held | `3800` | `3801` | `3802` | `3803` | `38FF` |
|---|---|---|---|---|---|
| none | 0 | 0 | 0 | 0 | 0 |
| `A` | 0 | **2** | 0 | **2** | **2** |
| `H` | 0 | 0 | **1** | **1** | **1** |

`3803` follows whichever of the two rows has the key, which is what an OR does and what a
per-row decode could not. Reproduce it with:

```basic
10 IF PEEK(14591)=0 THEN 10
20 A=PEEK(14336):B=PEEK(14337):C=PEEK(14338):D=PEEK(14339):E=PEEK(14591)
30 PRINT"3800=";A;"3801=";B;"3802=";C;"3803=";D;"38FF=";E
40 END
```

then `RUN` and hold a key.

`A8` and `A9` are not decoded, so the 256-byte window repeats four times across
`3800`–`3BFF` `[manual p.10]`: *"instead of using two hex digits, which is eight binary lines,
we can ignore two bits and use only six binary lines."*

## No diodes, and no debounce

**The only diode on the keyboard is `CR1`, a red 5 mm LED.** There is nothing in the matrix to
block a sneak path, so ghosting is real hardware behaviour rather than something an emulator
must suppress.

There is no debounce hardware either — no capacitors on any matrix line, no monostable, no
Schmitt trigger. The complete parts list is ten references and nothing else:

| ref | value | what |
|---|---|---|
| `Z1`, `Z2` | 74LS05 | row drivers, open collector |
| `Z3`, `Z4` | 74LS368 | column buffers, inverting tri-state |
| `R1` | 4.7 k | one eight-element pull-up pack, common pin 1 to `+5V` |
| `R2` | 330 | the LED's series resistor |
| `C1`, `C2` | 0.1 uF | decoupling |
| `CR1` | RED 5mm | the power LED |
| `J1` | - | the connector to the main board |

Debouncing is the ROM's job, and how it does it is the reason emulated typing drops
characters.

## The keys as they sit on the machine

`[measured]` Read off a Model I with the 16K Level II badge, and reconciled against the netlist
below. Shifted legends are printed above the unshifted ones on the key cap; here they follow it.

```
    1!  2"  3#  4$  5%  6&  7'  8(  9)  Ø   :*  -=  BREAK

    ↑   Q   W   E   R   T   Y   U   I   O   P   @   ←   →           7   8   9

    ↓   A   S   D   F   G   H   J   K   L   ;+  ENTER   CLEAR       4   5   6

    SHIFT   Z   X   C   V   B   N   M   ,<  .>  /?    SHIFT         1   2   3

                    [_________ SPACE _________]                     Ø   .   ENTER
```

**53 keys on the main block and 12 on the keypad**, which is exactly `SW1`–`SW53` and
`SW54`–`SW65`. Counting the picture is an independent check on the netlist, and it agrees.

### Two characters on one key

Sixteen keys carry a second legend. Every one of them is on row 4 or row 5, and the pairing is
the same arithmetic in each case: **shift toggles bit 4 of the code**.

| key | shifted | | key | shifted | | key | shifted |
|---|---|---|---|---|---|---|---|
| `1` | `!` | | `7` | `'` | | `:` | `*` |
| `2` | `"` | | `8` | `(` | | `;` | `+` |
| `3` | `#` | | `9` | `)` | | `,` | `<` |
| `4` | `$` | | `Ø` | **space** | | `-` | `=` |
| `5` | `%` | | | | | `.` | `>` |
| `6` | `&` | | | | | `/` | `?` |

**The zero key is the one with no shifted legend printed on it, and it is not inert.** `0` is
`30h`, so shifted it is `20h` — a space. `[measured]` at the `READY` prompt: `SHIFT`+`Ø` advances
the cursor by one, `SHIFT`+`1` prints `!`.

The letters carry no second legend because shift does nothing to them: the ROM's row 0–3
arithmetic has no shift term at all, which is the whole reason a stock Model I is upper-case
only.

The four arrows do have shifted codes, from the table at `0050h` rather than from arithmetic:
`SHIFT`+`↑` gives `1Bh` (escape), `SHIFT`+`←` gives `18h`, `SHIFT`+`→` gives `19h`, and
`SHIFT`+`↓` gives `00h`. `ENTER`, `CLEAR`, `BREAK` and `SPACE` return the same code either way.

### Where each key sits in the matrix

Read at `3800 + 2^row`. Every cell was derived from the ALPS netlist by following each switch to
its row driver and its column buffer, not read off a key-cap drawing:

| row | address | `D0` | `D1` | `D2` | `D3` | `D4` | `D5` | `D6` | `D7` |
|---|---|---|---|---|---|---|---|---|---|
| 0 | `3801` | `@` | `A` | `B` | `C` | `D` | `E` | `F` | `G` |
| 1 | `3802` | `H` | `I` | `J` | `K` | `L` | `M` | `N` | `O` |
| 2 | `3804` | `P` | `Q` | `R` | `S` | `T` | `U` | `V` | `W` |
| 3 | `3808` | `X` | `Y` | `Z` | — | — | — | — | — |
| 4 | `3810` | `Ø` | `1` | `2` | `3` | `4` | `5` | `6` | `7` |
| 5 | `3820` | `8` | `9` | `:` | `;` | `,` | `-` | `.` | `/` |
| 6 | `3840` | ENTER | CLEAR | BREAK | `↑` | `↓` | `←` | `→` | SPACE |
| 7 | `3880` | SHIFT | — | — | — | — | — | — | — |

**Row 3 stops after three keys.** The arithmetic would put `[`, `\`, `]`, `^` and `_` on bits
3–7, and the keyboard simply has no switches there — which is why row 3's net carries three
switches when rows 0, 1 and 2 carry eight. It is also why `3808` can only ever return `1`, `2`
or `4`.

The same grid by switch number, which is how the netlist names them:

| row | `D0` | `D1` | `D2` | `D3` | `D4` | `D5` | `D6` | `D7` |
|---|---|---|---|---|---|---|---|---|
| 0 | `SW1` | `SW10` | `SW17` | `SW24` | `SW30` | `SW36` | `SW42` | `SW48` |
| 1 | `SW2` | `SW11` | `SW18` | `SW25` | `SW31` | `SW37` | `SW43` | `SW49` |
| 2 | `SW3` | `SW12` | `SW19` | `SW26` | `SW32` | `SW38` | `SW44` | `SW50` |
| 3 | `SW4` | `SW13` | `SW20` | — | — | — | — | — |
| 4 | `SW5` | `SW14` | `SW21` | `SW27` | `SW33` | `SW39` | `SW45` | `SW51` |
| 5 | `SW6` | `SW15` | `SW22` | `SW28` | `SW34` | `SW40` | `SW46` | `SW52` |
| 6 | `SW7` | `SW16` | `SW23` | `SW29` | `SW35` | `SW41` | `SW47` | `SW53` |
| 7 | `SW8`, `SW9` | — | — | — | — | — | — | — |

**The numbering runs down the columns, not along the rows.** `SW1`–`SW8` are bit 0 of rows 0 to
7, `SW9` is the second SHIFT beside `SW8`, then `SW10`–`SW16` are bit 1 of rows 0 to 6, and so on
to `SW48`–`SW53` for bit 7. Bit 0's column is nine long because both SHIFT keys are on it; bits
1 and 2 are seven, since row 7 holds nothing else; and bits 3 to 7 are six, because row 3 stops
at `Z`. So the numbering follows the matrix and ignores the case entirely: `SW29`, `SW35`, `SW41`
and `SW47` are the four arrows, which sit in three different places on the machine.

## Both shift keys are one switch

`SW8` (LSHIFT) and `SW9` (RSHIFT) are wired **in parallel** — both span the same two nets. They
are electrically indistinguishable, which is why the matrix has one SHIFT bit and not two.

SHIFT returns on **`D0`** through `R1G` and `Z3`.

## The numeric keypad is twelve keys the machine cannot see

`SW1`–`SW53` are the main keyboard. `SW54`–`SW65` are a numeric keypad — and **every one of
the twelve is wired in parallel with a main key.** There is no thirteenth row, no spare column
and no extra data bit: the keypad occupies matrix positions the main keyboard already uses.

| keypad | parallel with | row | bit | character |
|---|---|---|---|---|
| `SW54` | `SW5` | 4 | `D0` | `0` |
| `SW57` | `SW14` | 4 | `D1` | `1` |
| `SW59` | `SW21` | 4 | `D2` | `2` |
| `SW60` | `SW27` | 4 | `D3` | `3` |
| `SW61` | `SW33` | 4 | `D4` | `4` |
| `SW62` | `SW39` | 4 | `D5` | `5` |
| `SW63` | `SW45` | 4 | `D6` | `6` |
| `SW65` | `SW51` | 4 | `D7` | `7` |
| `SW55` | `SW6` | 5 | `D0` | `8` |
| `SW58` | `SW15` | 5 | `D1` | `9` |
| `SW64` | `SW46` | 5 | `D6` | `.` |
| `SW56` | `SW7` | 6 | `D0` | ENTER |

The set is its own confirmation. Nothing about the netlist knows what a keypad is — the twelve
duplicated positions were found by comparing switch net-pairs — and they come out as exactly
`0`–`9`, `.` and ENTER, which is precisely the twelve keys a numeric keypad has and no others.
A random dozen duplicates would not do that.

**So the keypad is invisible to software.** Keypad `7` and main-row `7` are the same bit of the
same row; no program can distinguish them, and no emulator needs a separate keypad matrix. It
also means the keypad inherits the main keyboard's ghosting rather than being isolated from it.

The characters in that table are not read off a key-cap drawing. They are what the ROM's own
decoder returns for those coordinates: calling `03FE` with `A` = row x 4 and `E` = the column
mask gives `30h` for row 4 bit 0, `37h` for row 4 bit 7, `2Eh` for row 5 bit 6, and `0Dh` for
row 6 bit 0 — the last arriving via the control-key table at `0050h`, with `HL` left pointing
at it.

## The map the ROM computes

Worth stating once, because every keyboard claim above resolves to it. After the scan the ROM
holds a row index and a column mask, converts the mask to a column index, and computes:

| rows | arithmetic | result |
|---|---|---|
| 0-3 | `row*8 + col + 40h` | `@`, `A`-`G`, `H`-`O`, `P`-`W`, `X`-`Z` |
| 4-5 | `row*8 + col + 40h - 70h + 40h` | `0`-`9`, then `:;,-./` after an `XOR 10h` for codes `3Ch` and up |
| 6 | index `col*2 + shift` into the table at `0050h` | ENTER, CLEAR, BREAK, the four arrows, space |
| 7 | not decoded as a key | SHIFT, sampled separately |

Row 7 is never reached by that arithmetic because the scan loop stops before it; SHIFT is read
directly from `3880h` after a key has been found, which is why SHIFT has to be down *first*.

## The ROM's scan, and why typing needs timing

The driver at `03E3` is **edge-triggered**. It XORs each row against a saved copy at
`4036`–`403C` and ANDs with the current reading, so it reports only *newly* pressed keys. Having
accepted one it stops scanning twice, and both waits are the same delay routine at `0060h`:

```
0060  DEC BC / LD A,B / OR C / JR NZ,0060 / RET      26 T-states per iteration
```

| where | constant | iterations | T-states | at 1.77408 MHz |
|---|---|---|---|---|
| `011Dh`, before re-reading the row to debounce | `LD BC,0500h` | 1280 | 33,285 | **18.8 ms** |
| `044Ch`, after the character is decoded | `LD BC,0DACh` | 3500 | 91,005 | **51.3 ms** |
| | | | 124,290 | **70.1 ms not scanning** |

Those cycle counts are measured, not estimated: calling `0060h` on the machine with `BC` set to
each constant returns after exactly 33,285 and 91,005 T-states. The loop is `26n + 5` — twenty-six
per iteration, less five for the untaken jump, plus ten for the `RET`.

Two consequences, and both bite:

- A key must stay down long enough to survive the debounce re-read.
- It must stay *up* long enough for a scan to observe the release, or the saved state never
  clears and the next press of the same key is silently swallowed.

Getting the second one wrong is the classic way an emulator drops the second `P` of `PRINT`.

SHIFT is on its own row and the driver samples it only *after* it has found the pressed key, so
pressing both on the same scan is a race; SHIFT has to lead.

## Two incompatible keyboard interfaces

The Tandy and TEC (Japanese) machines use the same 20-pin connector and **the same pinout for
power, address and `D0`**. `/KYBD` moves from pin 14 to pin 10 and the other seven data bits
are reshuffled, so a keyboard from one will not work on the other.

| signal | Tandy | TEC | | signal | Tandy | TEC |
|---|---|---|---|---|---|---|
| `+5V` | 1 | 1 | | `D0` | 11 | 11 |
| `A4` | 2 | 2 | | `D1` | **16** | **12** |
| `A5` | 3 | 3 | | `D2` | **10** | **13** |
| `A1` | 4 | 4 | | `D3` | **13** | **14** |
| `A0` | 5 | 5 | | `D4` | **18** | **15** |
| `A2` | 6 | 6 | | `D5` | **12** | **16** |
| `A6` | 7 | 7 | | `D6` | **15** | **17** |
| `A7` | 8 | 8 | | `D7` | **17** | **18** |
| `A3` | 9 | 9 | | `GND` | 19 | 19 |
| **`/KYBD`** | **14** | **10** | | *(n/c)* | 20 | — |

The TEC layout is the tidier one: `D0`–`D7` in order on pins 11–18, with `/KYBD` on 10. Tandy
scatters the data bits and puts `/KYBD` on 14 — so plugging a Tandy keyboard into a TEC machine
drives `/KYBD` onto a data line.

This table is not inferred from the two main boards. It is read directly from RetroStack's
**keyboard adapter**, a board built for exactly this purpose, whose two connectors are labelled
`Tandy Model 1` and `TEC (Japanese) Model 1`. It agrees with both main boards' connectors.

### The Japanese side is buffered differently

On a US board the keyboard connector hangs **directly on the CPU data bus** — `J100`'s data
pins are the `D0`–`D7` nets themselves.

On a Japanese board `CN1`'s data pins are a separate `KBD0`–`KBD7` bus, which is the machine's
ROM/RAM data bus: it also carries the outputs of `Z42` (2364 ROM), `Z43` (2332 ROM) and the
4116 DRAMs, is held up by the `RP2` 4.7 kΩ pack, and reaches the CPU bus through `Z24`, a
74LS367. The keyboard joins that bus rather than the CPU's.

## What this settles

1. **No diodes, no debounce, no controller** — confirmed at the parts level, not inferred.
2. **A read really is the wire-OR of the selected rows**, and the mechanism is the
   open-collector 74LS05 row drivers, not a convention.
3. **`3800` reads zero and `38FF` reads everything**, as a consequence of the above.
4. **The two shift keys are one switch**, on `D0`.
5. **Tandy and TEC keyboards are not interchangeable**, and the difference is `/KYBD` moving
   from pin 14 to pin 10 plus a reshuffle of every data bit except `D0`.

Full connectivity: [`netlists/alps.md`](../netlists/alps.md) and
[`netlists/kbadapter.md`](../netlists/kbadapter.md).

## How the claims here are checked

Every factual claim in this document has an executable assertion in [`verify/claims.py`](../verify/claims.py). They are run by:

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

which also validates the netlist parser against KiCad's own XML export before testing anything. The assertions covering this document:

- `alps-ics`
- `alps-no-matrix-diodes`
- `alps-row-drivers`
- `alps-shift-keys-parallel`
- `alps-column-buffers`
- `alps-no-debounce`
- `keyboard-adapter-mapping`
- `keyboard-connectors-differ`

- `alps-parts-inventory`
- `keyboard-matrix-map`
- `alps-keypad-parallels-main-keys`
- `rom-keyboard-map-arithmetic`
- `keyboard-designators-collide-with-mainboard`

- `rom-keyboard-scan-delays`
- `keyboard-address-is-the-row-select`

If a claim below and its assertion disagree, one of them is wrong and the run says so. See [`verify/README.md`](../verify/README.md) for why this exists.
