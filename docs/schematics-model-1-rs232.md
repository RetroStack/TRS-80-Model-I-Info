# The Model I RS-232-C card — a sheet-by-sheet reading

Source: `Model I RS232.pdf`, *TRS-80 Model I RS-232 Interface*, Rev 2.1, Roger Murley /
BYTESHIFT, KiCad 9.0.0, one sheet. This is a modern rebuild rather than a reconstruction of
the original 26-1145 card: the 1488/1489 line drivers are replaced by a single SP3243 and the
TR1602 by its pin-compatible HD6402. It is programmed identically, which is what makes it
usable as the reference.

The card plugs into the Expansion Interface's internal expansion connector, so
[`schematics-model-1-ei-rev-d.md`](schematics-model-1-ei-rev-d.md) sheet 4 is the other half
of the story: the Expansion Interface decodes `/E8` for **eight** ports, `E8`–`EF`, and passes
`A2`, `A1`, `A0`, the data bus, `/IN`, `/OUT`, `/SYSRES` and `/INT` through on `J10`.

## The decode

`U4B` inverts `/E8` and `U4C` inverts `A2`; `U5A` (74LS00) NANDs the two, so the card
qualifies the Expansion Interface's eight-port window down to `A2 = 0` — **`E8`–`EB`**.

`U3` (74LS155) then decodes `A1`/`A0` into four read strobes and four write strobes, the
a-side enabled by `/IN` and the b-side by `/OUT`:

| port | read strobe | write strobe |
|---|---|---|
| `E8` | `Q0a` | `Q0b` |
| `E9` | **`Q1a` — not connected** | `Q1b` |
| `EA` | `Q2a` | `Q2b` |
| `EB` | `Q3a` | `Q3b` |

**`E9` has no read strobe.** Period documentation describes a "sense switches" read at `E9`;
this board has no such thing, and a read there leaves the bus undriven.

Whether `EC`–`EF` mirror `E8`–`EB` depends on what the *card* does with `A2`, and `U5A` says
it simply refuses to answer when `A2` is high. So the Expansion Interface decodes eight ports
and the card claims the lower four; the upper four are undriven.

## The chips

| | |
|---|---|
| `U1` | **HD6402** UART — the TR1602 / AY-3-1015's pin-compatible successor |
| `U2` | **COM8116** baud rate generator, on a **5.0688 MHz** crystal (`Y1`) |
| `U3` | 74LS155 address decoder |
| `U6A`, `U6B` | 74LS244 data bus buffers — see the `[unresolved]` note below |
| `U7` | 74LS367 modem-status buffer |
| `U8` | 74LS174 modem-control latch |
| `U9` | **SP3243** RS-232 line driver, five receivers and three transmitters |

## Port `E8` — modem status in, modem control out

**Read.** `U7` (74LS367), enabled by the `E8` read strobe, buffers five signals onto the bus:
its outputs land on **`D7`, `D6`, `D5`, `D4` and `D0`**, and its sixth channel is unused.
`D3`, `D2` and `D1` have no buffer and float high. The five inputs come from the SP3243's
receivers — `CTS`, `DSR`, `CD`, `RI` and the received-data line.

**Write.** `U8` (74LS174 hex D flip-flop) latches **`D0`, `D1` and `D2`** on the `E8` write
strobe. `Q0`, `Q1` and `Q2` drive the SP3243's three transmitter inputs — `DTR`, `RTS` and the
transmit gate, the last AND-ed with the UART's serial output by `U10A` so the line can be held
in a break condition. `Q3`, `Q4` and `Q5` are unused. `/Mr` is tied high through `R1` (4.7k),
so the latch is not cleared by `/SYSRES`.

## Port `E9` — the baud rate generator, write only

`D0`–`D3` set the COM8116's receive divisor and `D4`–`D7` its transmit divisor, so the two
directions can run at different rates. With the 5.0688 MHz crystal the sixteen divisors give
the standard rates from 50 to 19200 baud.

## Port `EA` — UART status in, UART control out

**Read** returns the HD6402's status pins: parity error (13), framing error (14), overrun
(15), data received (19), transmit buffer empty (22) and transmit register empty (24).

**Write** sets the frame format on the HD6402's control pins: `D3` parity inhibit (35), `D4`
stop-bit select (36), `D5` and `D6` word length (37, 38), `D7` even parity (39), latched by
`CTRL_REG_LOAD` (34).

A status register that reads zero means "transmitter never empty", which is why the emulator's
previous constant `0x00` on these ports hung every driver that polled for readiness. An idle
UART must report its transmitter empty.

## Port `EB` — data

Read returns `RXBUF0`–`RXBUF7` (pins 12 down to 5); write loads `TXBUF0`–`TXBUF7` (pins 26
through 33) and pulses `TXLOAD` (23).

## The line interface

`U9` (SP3243) carries **five receivers** — `CTS`, `DSR`, `CD`, `RI`, `RXD` — and **three
transmitters** — `DTR`, `RTS`, `TXD`. The RS-232 I/O connector carries those eight signals plus
signal ground. There is no hardware handshake logic: the modem control lines are simply latched
out and buffered in, and any flow control is the software's business.

**`[unresolved]` What `J1` is.** Two readings of this sheet both name `J1`, and they cannot
both hold:

| reading | `J1` is | taken from |
|---|---|---|
| the buffer chain | where `U6A`/`U6B` drive the buffered CPU data bus | the 74LS244s |
| the line interface | the RS-232 I/O connector, eight signals plus ground | the SP3243 |

A 74LS244 carrying `D0`–`D7` does not drive an RS-232 port — the SP3243 does, as the paragraph
above says — so one of the two is a misread of the sheet. The card needs an edge connector for
the data bus regardless, because it plugs into the Expansion Interface's internal expansion
connector, which [`schematics-model-1-ei-rev-d.md`](schematics-model-1-ei-rev-d.md) sheet 4
gives as `J10` on the *Expansion Interface* side, carrying `D0`–`D7`, `/SYSRES`, `/IN`, `/OUT`
and `/INT`. Which designator the *card* gives its own edge is what is not established.

**What would settle it:** reading the connector designators off the sheet directly. This board
has no KiCad source, so nothing here can re-derive them.

Nothing an emulator does turns on the answer: the ports and the bits they carry are settled
above, and no connector name reaches software.

## What this drawing settles

1. **The Expansion Interface decodes `E8`–`EF`; the card answers on `E8`–`EB`.** Eight ports are
   decoded, four are used.
2. **`E9` is write-only.** No sense-switch read exists on this board.
3. **`E8` read drives only `D7`, `D6`, `D5`, `D4` and `D0`**; the other three bits float.
4. **An idle UART reports its transmitter empty**, so a returned `0x00` is not merely
   incomplete, it is the one value that deadlocks a polling driver.
5. **The Model I serial port cannot report itself in the `37E0` interrupt buffers.** `/INT` is
   on `J10`, so a card can pull the line, but sheet 1 of the Expansion Interface buffers only
   the timer and the floppy onto `D7`/`D6` — which is why Model I serial software polls.

## How the claims here are checked

This board has no KiCad source and no machine-readable drawing, so nothing in this document can
be re-derived by the harness. Every statement here is a reading of a hand-drawn or rasterised
scan — a single, unverifiable source, as [`sources.md`](sources.md) ranks it — and the
`[unresolved]` note above marks where that reading does not settle the question.

The values were cross-checked against a working emulator during development; that check lives in
the emulator's own test suite rather than here, because it tests the emulator and not the board.
