# The video system

A kilobyte of RAM, one character generator, and no frame buffer in the modern sense. The screen
is 64 by 16 characters, each of them a byte, and the machine's most famous quirk is that seven
of those eight bits are stored and the eighth is rebuilt by a NOR gate every time the byte is
read back.

`[sheet]` throughout, from the Rev G reconstruction unless a section says otherwise.
[`revisions.md`](revisions.md) establishes that the video RAM and port `FF` are identical on all
four US boards, so "the Model I" is safe here except where the Japanese board is named.

## The screen

**1024 bytes at `3C00`–`3FFF`**, one per character cell, 64 columns by 16 rows, laid out left to
right and top to bottom. There is no separate attribute memory, no scroll register and no
palette. Writing a byte changes a cell; the video hardware reads the same RAM on its own
schedule through the access multiplexer (`Z31`, `Z49`, `Z64`, all 74LS157) and the CPU is not
locked out while it does.

Each cell is drawn as **6 dots wide by 12 scan lines**, so the active picture is 384 by 192
dots. The character generator supplies only **5 dots by 8 rows**, top-aligned: the sixth column
and the bottom four lines are inter-character gap, which is what gives the display its open
look. Pixels are not square — the raster is roughly 2:1 — so anything rendering this needs an
aspect correction rather than square dots.

## Seven bits stored, one rebuilt

**The video RAM is seven bits wide.** `Z45`–`Z48` and `Z61`–`Z63` are seven 2102 static RAMs,
one per stored bit, and there is no eighth. Bit 6 is not stored anywhere. It is regenerated on
the way out by `Z30`, a 74LS02, whose gate D takes `VD5` and `VD7` on pins 11 and 12 and puts
the result on pin 13:

```
D6 = NOR(D5, D7)
```

So what the display shows, and what a `PEEK` reads back, is not always what was written:

| written | stored (bits 5,7 kept, 6 dropped) | read back | why |
|---|---|---|---|
| `41` `A` | `01` | `41` | `D5`=0 `D7`=0 → `D6`=1 |
| `01` | `01` | `41` | indistinguishable from the above |
| `20` space | `20` | `20` | `D5`=1 → `D6`=0 |
| `60` | `20` | `20` | bit 6 was never kept |
| `C1` | `81` | `81` | `D7`=1 → `D6`=0 |

**The reachable non-graphic display codes are therefore exactly `20`–`5F`.** A byte survives the
round trip only when its bit 6 already equals `NOR(D5, D7)`, which is true for `20`–`3F` (bit 5
set, bit 6 clear) and for `40`–`5F` (bit 5 clear, bit 6 set) and false everywhere else. This is
why the machine has no lower case: `61`–`7A` cannot be stored.

`POKE 15360,193` reading back as 129 is this and nothing else — `193` is `C1`, the stored value
is `81`, and `81` is 129.

## Block graphics

Codes with bit 7 set **bypass the character generator entirely**. `Z8`, a 74LS153, builds the
pattern straight from the stored bits, selected by the `GRAPHICS` line the latch sheet derives
from `D7`. The cell splits into **2 across by 3 down**, each sub-block 3 dots wide by 4 lines
tall, and bits 0 to 5 fill them in reading order:

```
 bit 0 | bit 1
 bit 2 | bit 3
 bit 4 | bit 5
```

**Bit 6 is not decoded here either**, so `C0`–`FF` draw the same 64 patterns as `80`–`BF`. On a
stock machine the point is moot — bit 6 is not stored, so `C0`–`FF` can never be read back — but
a lowercase-modified machine stores all eight bits and the duplication becomes visible.

The ROM's `SET`, `RESET` and `POINT` address a 128 by 48 grid, and the arithmetic is worth
stating because it is the same in both directions:

```
address = 3C00h + (y / 3) * 64 + (x / 2)
bit     = 1 << ((y mod 3) * 2 + (x mod 2))
```

## The character generator

One **MCM6670** (`Z29`), sitting outside the CPU's address space with its chip select tied
active. It takes the latched display code and a 3-bit row count and returns five dots, which
`Z10` and `Z11` (74LS166) shift out serially as `PIXEL`. The device holds **128 glyphs of 8 rows,
5 dots wide** — 1024 bytes — and the code reaching it is masked to seven bits, so `00`–`1F` draw
the same glyphs as `40`–`5F`.

Six generator images are known, numbered by the option-select value of the replacement device.
They are not interchangeable, and the differences are visible in the row census:

| set | what it is | row 0 | row 7 |
|---|---|---|---|
| `01` | the earliest, with the notorious floating `a` | blank | the font's last row |
| `02` | the floating `a` corrected | blank | the font's last row |
| `04` | adds the arrows and `£` | blank | the font's last row |
| `08` | adds true descenders | used | descenders only |
| `16` | the common late set | used | descenders only |
| `17` | Japanese Kana | blank | the font's last row |

**Four of the six are seven-row fonts with a blank leading row**, drawn in rows 1–7. Only `08`
and `16` use all eight, and they use row 7 for descenders alone — a handful of glyphs, not the
whole set. Which
of a cell's twelve scan lines the eight glyph rows land on is a separate question from what the
ROM holds, and a font with a blank leading row will sit one line lower than one without.

The display codes are not ASCII above `5A`. `5B`–`5E` are the four arrows rather than
`[ \ ] ^`, `5F` is underscore, `60` is `£` and `7E` is `¥`.

## Thirty-two column mode

Port `FF` bit 3 drives `MODESEL`, and the video counter halves the shift rate when it is
asserted. **Only the even cells are shown**, each stretched to double width; the odd cells keep
whatever they held and reappear the moment the mode is switched back. Nothing is blanked and
nothing is moved — the hardware simply clocks the shift register half as often, so a 64-byte row
of RAM produces 32 visible characters.

Two consequences that catch people:

- The bit is **inverted** on its way out of the latch. `Z59`'s `/Q3` is `MODESEL`, so writing a
  1 selects 32 columns while the board-level signal goes low. See [`revisions.md`](revisions.md).
- **Bit 6 of `IN (0FFh)` reads `MODESEL` back** through `Z44F`, which makes it the one
  write-only latch bit the machine returns. It reports the width, inverted relative to the bit
  that was written.

## The lowercase modification

The missing eighth RAM bit, added back. The modification fits an eighth memory device, wires it
to `D6`, and cuts the `Z30` NOR out of the read path so the stored bit reaches the bus
unaltered. A character generator with lower-case glyphs is fitted at the same time, because the
codes `61`–`7A` are useless without one.

After it every byte written reads back unchanged, `60`–`7F` become reachable, and `C0`–`FF`
become storable — which is when the block-graphics duplication above stops being theoretical.

## The Japanese board is different in three ways

Established in [`schematics-japanese-model-1.md`](schematics-japanese-model-1.md); collected
here because every one of them is a video fact.

**The video RAM is genuinely eight bits.** Two 2114 (1K by 4) devices instead of seven 2102s,
and `VD6` is a RAM data pin rather than a gate output. Everything in "Seven bits stored, one
rebuilt" above is a US-family fact and **none of it applies** — no regeneration, no `20`–`5F`
restriction, no lowercase modification needed.

**There are two character generators**, `Z37` (Kana) and `Z38` (ASCII), selected by `Z53A`, a
74LS74 clocked by the port `FF` write strobe with `D7` on its `D` input. `Q` is `/CGA`, so
**`D7` = 0 selects `Z37`, the Kana generator** — worth stating plainly, because a machine
configured this way comes up on Kana rather than on ASCII.

**The ROM undoes a bare `OUT`.** It never reads port `FF` back, keeping a shadow byte at `403Dh`
and rewriting the whole latch from it whenever it sets the display width. So `OUT 255,128` is
reverted at the next width change, which at the BASIC prompt is immediate; the shadow has to be
set too:

```basic
POKE 16445,128 : OUT 255,128    ' generator B, and it stays
```

PAL is the fourth difference and is not a video-*memory* difference at all — same 15.84 kHz line
rate, same 192 active lines, four extra rows of blanking. The mechanism is in
[`schematics-japanese-model-1.md`](schematics-japanese-model-1.md).

## What this settles

1. **The screen is 1 K at `3C00`, 64 by 16**, one byte per cell, no attributes.
2. **Seven bits are stored and bit 6 is `NOR(D5, D7)`**, which is the whole of the `20`–`5F`
   restriction and the reason there is no lower case.
3. **Bit 6 is not decoded for graphics either**, so `C0`–`FF` repeat `80`–`BF`.
4. **A cell is 6 by 12 and a glyph is 5 by 8**, top-aligned, and four of the six generator
   images leave their first row blank.
5. **32-column mode halves the shift rate**; the odd cells are retained, not cleared.
6. **None of the seven-bit story is true of the Japanese board.**

## How the claims here are checked

Every factual claim in this document has an executable assertion in [`verify/claims.py`](../verify/claims.py). They are run by:

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

which also validates the netlist parser against KiCad's own XML export before testing anything. The assertions covering this document:

- `chargen-row-census`
- `d6-regeneration-restricts-the-text-codes`

If a claim above and its assertion disagree, one of them is wrong and the run says so. See [`verify/README.md`](../verify/README.md) for why this exists.
