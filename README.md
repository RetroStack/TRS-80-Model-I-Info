# The TRS-80 Model I, as established

What is actually true about the TRS-80 Model I — the machine, across every revision of it. Not a
tutorial and not a restoration guide: a reference whose every testable sentence has an executable
assertion behind it, so that a claim here is either checkable or marked as one that is not.

The evidence is RetroStack's KiCad reconstructions of eleven boards, the period Radio Shack
manuals, the ROM images, and a working emulator used as an instrument — a circuit claim with a
software-visible consequence can be run rather than argued about.

## Running the checks

```sh
TRS80_SCHEMATICS=~/schematics TRS80_ROMS=~/roms python3 verify/run.py --self-test
TRS80_SCHEMATICS=~/schematics TRS80_ROMS=~/roms python3 verify/mutate.py
```

**Nothing has to be installed to get most of the way.** `python3 verify/run.py` on a fresh clone
runs **63 of the 79 claims** and passes, because `kicad-cli`'s netlist export for all eleven
boards is committed in [`netlists/exports/`](netlists/exports) — derived data, not RetroStack's
sources. A live export always takes precedence over it, and `committed-exports-are-current`
requires the two to agree whenever both are possible.

Two directories of third-party material are not shipped here. Point the variables at them for the
rest, and every claim needing one **skips cleanly** when it is absent — the run still passes, it
just checks less and says so:

| variable | what it points at | where to get it |
|---|---|---|
| `TRS80_SCHEMATICS` | a directory holding RetroStack's KiCad board repositories, one folder per board | github.com/RetroStack |
| `TRS80_ROMS` | a directory laid out like the emulator's `roms/`: `system/level2-v1.3.bin` and `char/character_set_01/02/04/08/16/17.bin` | the emulator repository below, or your own dumps |

With both set, and `kicad-cli` on the path for the two claims that re-export and rule-check:
**79 claims pass, and 69 mutations are all caught.** With neither: 63 pass, 16
skip, nothing fails.

## Where this came from

This folder was written alongside an emulator, which is where several of its facts were first
measured and where the behavioural claims are exercised end to end. Nothing here depends on it:
the assertions read schematics, ROM images and the documents themselves.

> **TRS-80 Model I emulator** — a Rust emulator an LLM can drive over MCP.
> `github.com/RetroStack/TRS80_M1_Emulator`

## The documents

| file | what it is |
|---|---|
| [`revisions.md`](docs/revisions.md) | **Which machine are we talking about.** The four US main boards, the two Japanese ones, and every wiring difference between them — a list that is asserted to be complete. |
| [`keyboard.md`](docs/keyboard.md) | The matrix, the wire-OR that makes a read the sum of the selected rows, the numeric keypad the machine cannot see, and the ROM scan timings that make emulated typing drop characters. |
| [`video.md`](docs/video.md) | **The screen.** A kilobyte at `3C00`, seven bits stored and the eighth rebuilt by a NOR gate, block graphics, the character generators, and what 32-column mode really does. |
| [`floppy.md`](docs/floppy.md) | **Disk.** The FD1771 and its four registers, the motor one-shot that clears drive select, a `READY` line the board invents, and the two incompatible ways to add double density. |
| [`cassette.md`](docs/cassette.md) | **Tape.** A two-bit DAC whose rest state is not zero, an input flip-flop that any port `FF` write clears, the motor relay, and the 255-byte leader. |
| [`rs232.md`](docs/rs232.md) | **Serial.** Four ports on `E8`–`EB`, two baud rates at once, a reset that does not clear the control latch, and why no Model I serial driver uses interrupts. |
| [`sources.md`](docs/sources.md) | Every source, what kind of thing it is, how much it can carry, and where each has been caught being wrong. |
| [`netlists/`](netlists/README.md) | All eleven boards as text: every component, every pin, every connection, `grep`-able. Generated, not transcribed. |
| [`verify/`](verify/README.md) | The harness. One assertion per documented claim, a parser validated against a second format, and mutation tests proving the assertions can fail. |

### Board-by-board readings

| file | what it is |
|---|---|
| [`schematics-model-1-rev-g.md`](docs/schematics-model-1-rev-g.md) | The Rev G main board, sheet by sheet. |
| [`schematics-japanese-model-1.md`](docs/schematics-japanese-model-1.md) | The Japanese board: two character generators and a flip-flop selecting between them from port `FF` bit 7, and how it differs from Rev G. |
| [`schematics-model-1-ei-rev-d.md`](docs/schematics-model-1-ei-rev-d.md) | The Expansion Interface Rev D: the `37Ex` decode, the 40 Hz timer and how it is acknowledged, the interrupt buffers, the FD1771 and its drive-select latch, the printer, the cassette relay and the RAM banks. |
| [`schematics-percom-doubler.md`](docs/schematics-percom-doubler.md) | The Percom Doubler: two controllers on one board and the `37EC` write that chooses between them. |
| [`schematics-model-1-rs232.md`](docs/schematics-model-1-rs232.md) | The RS-232-C card: an HD6402 and a COM8116 on ports `E8`–`EB`, and why a status register that reads zero deadlocks a driver. |

Four things here contradict the period documentation and are right anyway — the port-`FF` width
readback, the mode-select inversion, the cassette DAC's rest voltage and the two Japanese
character generators. Each is traced to the sheet that settles it.

Every document that exists is listed above, and every one is linked. A document still to be
written is named in prose and marked `*(planned)*` rather than linked, so this folder has no
dead link at any commit — there are none outstanding at present.

## Licence and sources

The documents and the harness are MIT, in [`LICENSE`](LICENSE). Everything they describe belongs
to someone else: no schematic, ROM image or manual page is redistributed here, and the one thing
derived from someone else's work that is — `kicad-cli`'s netlists, generated from RetroStack's
boards — is called out as such. [`NOTICE.md`](NOTICE.md) covers all of it.

---

Checked by `readme-lists-every-document`:

- `readme-lists-every-document`
