# The floppy disk system

One FD1771 in the Expansion Interface, four drive selects, a motor that switches itself off
after three seconds, and a `READY` line the board invents because the drive bus has none. Every
disk operating system for the Model I is written against exactly this, and against the two ways
of bolting double density on top of it.

`[sheet]` from RetroStack's Expansion Interface Rev D reconstruction, sheet 9, unless a section
says otherwise. The board reading is
[`schematics-model-1-ei-rev-d.md`](schematics-model-1-ei-rev-d.md); this document is the
subsystem across all of it.

## The controller and its four registers

**`Z42` is an FD1771.** `/RE` comes from `/37EC_READ`, `/WE` from `/37EC_WRITE`, and `A0`/`A1`
pass straight through, so the chip's four registers land at:

| address | register |
|---|---|
| `37EC` | command on write, status on read |
| `37ED` | track |
| `37EE` | sector |
| `37EF` | data |

`/CS` is tied to ground — the read and write strobes do all the selecting. `CLK` is 1 MHz,
divided down from the Expansion Interface's own 4 MHz crystal, which is the rate a 1771 wants
for 5¼-inch drives. `/MR` comes from `/SYSRES`.

**Each group of four addresses is an alias.** `A1` and `A0` are decoded nowhere except inside
the FD1771 itself, which is why the boot loader can write drive select to `37E1` and a
correctly-modelled machine answers at `37E0`.

Three pins decide how much of the chip is in play:

- **`DRQ` (pin 38) is not connected.** There is no DMA and no data-request interrupt. Software
  polls status bit 1, which is exactly what the ROM's boot loader does at `06C0`.
- **`/XTDS` (pin 25) is tied high** through `R29`, selecting the chip's internal data separator.
  This is the pin a doubler takes over.
- **`3PM` is tied high**, selecting step/direction drive rather than a three-phase stepper.
  `TG43` and `PH3` are unconnected.

## Drive select, and the motor that clears it

**`Z47`, a 74LS175, is the drive-select latch.** It takes data bits 0–3 clocked by
`/37E0_WRITE`, and `Q0`–`Q3` drive `DS0`–`DS3` on `J5` through 7416 open-collector inverters. So
a write to the `37E0` group selects drives; there is no way to read back which is selected.

**`Z33B`, a 74LS123, is the motor one-shot.** `R25` is 200 kΩ and `C62` is 33 µF, and the
74LS123's `0.45·R·C` puts the pulse at **2.97 seconds** — not the round 3 that documentation
tends to quote. It is triggered on the *falling* edge of `/37E0_WRITE`, so every write to the
drive-select group retriggers it. Its `Q` goes two places:

- to `Z41B`, a 7416, and out to `J5` as **`MOTOR_ON`**;
- to **`Z47`'s `/Mr`** — so when the one-shot expires it *clears the drive-select latch*.

That second path is the one that surprises people. The motor timing out does not merely stop the
spindle; it deselects every drive.

## READY is synthesised, not read

The 34-pin Shugart bus that `J5` carries **has no READY line**. `Z46A`, a 74LS20, NANDs the four
`/Q` outputs of the drive-select latch to give "any drive is selected", and that single signal
drives the FD1771's **`HLT` and `READY` together**.

Two consequences follow directly, and both are visible to software:

1. **With no drive selected the controller reports NOT READY.** A command issued without a
   preceding drive select fails immediately.
2. **A command issued more than about three seconds after the last `37E0` write also fails**,
   because the one-shot has expired, the latch is clear, and `READY` has gone with it. A DOS
   that seeks, thinks, and then reads has to re-select first.

## What `J5` does not carry

`J5` carries `INDEX_PULSE`, `DS0`–`DS3`, `MOTOR_ON`, `DIR_SEL`, `STEP`, `WRITE_DATA`,
`WRITE_GATE`, `TRACK_ZERO`, `WRITE_PROTECT` and `READ_DATA`.

**There is no side-select line.** A double-sided drive cannot be reached through a stock
Expansion Interface at all — the second side is unaddressable, not merely unsupported. Only a
Tandy-style doubler, which adds its own side select, makes it reachable.

## The interrupt is a buffer, not a latch

A read of `37E0` puts the FD1771's `INTRQ` on **`D6`** and the 40 Hz timer on `D7`, through two
sections of `Z49`. The floppy half **reports the pin as it stands at that instant**: the chip's
own rules clear it — reading the status register, or writing a new command — and the `37E0` read
has no effect on it whatsoever. This is the opposite of the timer half on `D7`, which the same
read does acknowledge.

`INTRQ` (pin 39) is pulled up by `R30`, 10 kΩ.

## Double density, two incompatible ways

The FD1771 does single density only. Both add-ons work by putting a second controller — an
FD1791 or an MB8876, which do MFM — beside it and multiplexing the drive lines, so **a doubler is
two chips and not one chip with a mode bit**. Each keeps its own track, sector and data
registers, which is why a DOS that switches density mid-operation has to re-seek: the head
position lives in the drive, not in either controller.

They differ entirely in how the density is chosen:

| | Percom | Radio Shack 26-1143 |
|---|---|---|
| control port | `37EC`, the command register | `37EE`, the sector register |
| single density | write `FE` | write `A0` |
| double density | write `FF` | write `80` |
| side select | none | `40` / `60` |
| precompensation | none | `C0` / `E0` |
| decoded bits | the upper bits, exactly which is `[unresolved]` | **the top three only** |

The Percom values sit inside the FD1771's Write Track opcode space (`F0`–`FF`) and are undefined
opcodes there, which is precisely why the board can steal them — but it means an emulator has to
test for the intercept **before** dispatching a command, and must still let a real `FORMAT`
reach Write Track.

The Radio Shack channel has a trap of its own: **only the top three bits are decoded**, and the
documented values are written as though the low bits mattered. TRSDOS 2.7 selects the FD1791 by
writing `0x81`, not `0x80`. A decoder that insists on the documented byte leaves the disk reading
double-density tracks with a single-density controller, and it reports `DISK ERROR` before the
banner. Real sector numbers on a Model I disk never exceed `0x12`, so the command values cannot
collide with an ordinary sector write.

`/SYSRES` returns a Percom board to the 1771 and single density — the behaviour the board's
author and xtrs agree on; the drawing's flip-flop polarity is unresolved (see the Percom
reading).

The full reading of the Percom drawings, including what is not settled about them, is
[`schematics-percom-doubler.md`](schematics-percom-doubler.md).

## What this settles

1. **Four registers at `37EC`–`37EF`**, each aliased across four addresses because `A0` and `A1`
   are decoded only inside the chip.
2. **`DRQ` is unconnected**, so all data transfer is polled.
3. **The motor one-shot is 2.97 s**, and expiring it clears the drive-select latch.
4. **`READY` is synthesised from "any drive selected"**, so it drops when the latch clears.
5. **There is no side-select line on `J5`.**
6. **The floppy interrupt bit is a live buffer**, cleared by the chip's rules and not by reading
   `37E0`.
7. **A doubler is two controllers**, and the two families choose density through different
   ports with different rules.

## How the claims here are checked

Every factual claim in this document that can be tested has an executable assertion in [`verify/claims.py`](../verify/claims.py). They are run by:

```sh
TRS80_SCHEMATICS=~/schematics python3 verify/run.py --self-test
```

- `ei-motor-oneshot`
- `ei-oneshot-clears-drive-select`
- `ei-drq-unconnected`
- `ei-j5-no-side-select`

The doubler half rests on hand-drawn scans with no extractable text and is marked as such in
[`schematics-percom-doubler.md`](schematics-percom-doubler.md); the `0x81` finding came from
booting a real TRSDOS 2.7 disk rather than from any drawing.
