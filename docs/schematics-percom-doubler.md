# The Percom Doubler — a reading of the hand-drawn schematics

Sources: `PercomDoubler.pdf`, five pages of hand-drawn schematics collected from two
machines — pages 2 and 3 are the "Doubler V.D. Pijl voor TRS80 M1" (drawn 1986 by
F. J. Kraan), pages 4 and 5 the "Percom Doubler Model 1 / TRS-80" (February 1982,
A. Colson). They are different boards solving the same problem the same way, which is what
makes them worth reading together.

A doubler replaces the FD1771 in the Expansion Interface's socket. The board plugs into that
socket and the 1771 plugs into the board, so everything on
[`schematics-model-1-ei-rev-d.md`](schematics-model-1-ei-rev-d.md) sheet 9 stays true —
the drive-select latch, the motor one-shot, `READY` from `Z46A`, `J5` — and only the
controller changes.

## Two chips, not one chip with a flag

The board-layout drawing on page 3 lists the parts:

| | |
|---|---|
| `U13` | **FDC 1771** |
| `U12` | **FDC 1791-01** or **MB8876** |
| `U11` | 74LS157 |
| `U10` | 74LS02 |
| `U9` | 74LS05 |
| `U8` | 74S04 |
| `U7` | 74LS153 |
| `U6`, `U5` | 74LS161 |
| `U4` | 74LS27 |
| `U3`, `U2` | 74LS74 |
| `U1` | 74LS20 |
| `Y` | 16 MHz crystal |

Both controllers are present and powered. The 1771 does single density (FM), the 1791 does
double (MFM) and can also do FM. The `74LS157` multiplexes `STEP`, `DIRC`, `WG`, `WD` and the
read clock between the two, so exactly one of them is driving `J5` at any moment.

**Each chip keeps its own track, sector and data registers.** That is not an implementation
choice, it is two physical chips; a DOS that switches density mid-operation has to re-seek,
because the head position lives in the drive, not in either chip.

## How the density is selected

Page 4's pin table shows the socket signals passing straight through, with one addition: a
`/DOUBLE` net that reaches the 1791's `/DDEN` (pin 37) and the `74LS157`'s select line.

`/DOUBLE` is the `Q` of a `74LS74` flip-flop, its `D` input is **`DAL0`** — data bus bit 0 —
and it is clocked by a gate cluster fed from the `37EC` write strobe. So the shape is settled:
**a write to `37EC` carrying the right pattern in its upper bits latches bit 0 as the density.**

**`[unresolved]` Which gate does the decoding, and how many bits it looks at.** The two halves
of this reading come from two different boards and they do not agree:

| | says | source |
|---|---|---|
| the decode drawing | a `74LS02`/**`74LS30`** cluster taking `DAL7`, `DAL6`, `DAL5`, `DAL4`, `DAL3`, `A1`, `A0` and the write strobe — eight inputs, which is what a 74LS30 has, and which leaves `DAL2` and `DAL1` undecoded | page 4, the February 1982 Colson board |
| the parts list | `U1` is a **74LS20** and `U10` a 74LS02; there is no 74LS30 on the board at all | page 3, the 1986 Kraan board |

Neither settles the other, because the parts list is not a list of the parts on the board the
decode was read from. The bit range follows the gate: eight inputs means bits 7 through 3 are
tested and the two below are ignored, a 4-input gate means something narrower.

**What would settle it:** re-reading pages 3 and 4 against each other to establish whether the
two boards share this decode at all, and if they do, counting the inputs on the gate in the
drawing. Both pages are hand-drawn scans with no text layer, so this is eye work, not a query.

The Colson drawing states the result outright, handwritten beside the FD1771:

```
Op 37EC:
  /FF  in double density
  /FE  in single density
```

So `OUT`-ing `FF` to `37EC` selects the 1791 and MFM; `FE` selects the 1771 and FM. `FE` and
`FF` are undefined FD1771 opcodes, which is precisely why the board can steal them — but they
sit inside the Write Track opcode space (`F0`–`FF`), so an emulator must test the intercept
**before** dispatching a command, and must still let a real `FORMAT` reach Write Track.

Nothing an emulator does depends on the unresolved decode above: `FE` and `FF` both carry every
upper bit set, so they select correctly under either reading. What is undecided is only whether
values like `F8` would have worked too.

The flip-flop's `/MR` comes from `/SYSRES`, so a reset returns the board to single density and
the 1771.

## The data separator

The rest of both boards is the part an emulator does not need. A 16 MHz crystal drives a
`74LS74` divider chain to 8 MHz; on the Percom a bipolar PROM (`A1`) plus a `74LS161` counter
(`B1`) form a state machine that recovers the clock from the raw read data, replacing the
1771's internal separator. The `/XTDS` pin the Expansion Interface ties high on sheet 9 is
what the doubler takes over.

`EARLY` and `LATE` on the 1791 (pins 17 and 18) drive write precompensation through a
`74LS153`. Precompensation shifts write pulses a few hundred nanoseconds to counter bit
crowding on inner tracks; on an emulator that stores bytes rather than flux it has no
observable effect, and the only reason to model the control bit at all is that software sets
it.

## The Radio Shack doubler, for contrast

Tandy's own kit — catalogue **26-1143**, the *Double-Density Adapter Kit* — solves the same
problem with a different control channel: writes to the **sector register at `37EE`** with the
top three bits set carry the command, rather than writes to `37EC`.

| bits 7:5 | value | meaning |
|---|---|---|
| `100` | `0x80` | select the 1791, double density |
| `101` | `0xA0` | select the 1771, single density |
| `010` / `011` | `0x40` / `0x60` | side 0 / side 1 |
| `110` / `111` | `0xC0` / `0xE0` | precompensation off / on |
| `000` / `001` | `0x00`–`0x3F` | not a command: an ordinary sector number |

**Only the top three bits are decoded.** Bits 4 through 0 reach nothing, which the
documented values hide because they are all written as though the low bits mattered. They
do not, and the difference is observable: TRSDOS 2.7 on a Radio Shack doubler selects the
FD1791 by writing **`0x81`**, not `0x80`. A decoder that insists on the documented byte
leaves it reading double-density tracks with a single-density controller, and the disk
reports `DISK ERROR` before the banner. This was found by booting the real disk.

Real sector numbers on a Model I disk never exceed `0x12`, so the channel does not collide
with ordinary use, and only one function can be set per write. This is also the **only** way
to reach side 1: `J5` on the Expansion Interface carries no side-select line, so a
double-sided drive is unreachable without a Tandy-style doubler.

No drawing of the Tandy board was available; this section is from its service manual and from
xtrs's `TRSDISK_R1791`/`TRSDISK_R1771` constants, and is marked as such in the code. The
three-bit decode is not from either — xtrs matches the six values exactly — but from what
the real disk does.

## What these drawings settle

1. **The Percom control port is `37EC`, the command register, and the values are `FE` and
   `FF`** — stated in the author's own handwriting, and matching xtrs's `TRSDISK_P1771 = 0xfe`
   and `TRSDISK_P1791 = 0xff`.
2. **A doubler is two controllers, not one with a mode bit.** Register state does not carry
   across a density switch.
3. **`/SYSRES` returns the board to the 1771 and single density.**
4. Everything on the Expansion Interface's floppy sheet is unaffected: the doubler sits in the
   1771's socket and inherits the drive-select latch, the one-shot and `READY`.

## How the claims here are checked

This board has no KiCad source and no machine-readable drawing, so nothing in this document can
be re-derived by the harness. Every statement here is a reading of a hand-drawn or rasterised
scan — a single, unverifiable source, as [`sources.md`](sources.md) ranks it — and the
`[unresolved]` note above marks where that reading does not settle the question.

The values were cross-checked against a working emulator during development; that check lives in
the emulator's own test suite rather than here, because it tests the emulator and not the board.
