# Expansion Interface, Rev D — complete netlist

Generated from `TRS-80-Model-I-Expansion-Interface-Rev-D-main` by `verify/emit.py`, which exports the schematic with `kicad-cli` and parses it with the same code the claims in `verify/claims.py` use.

**185 components · 337 nets · 1346 pin connections.**

Three views of the same information: components, a connection view answering "what is this pin wired to", and a net index answering "what is on this net". The redundancy is deliberate — it is what lets the file be checked against itself.

No integrity problems: every node names a known component, every pin number is valid for that component's symbol, and the two views agree on the connection count.

## Components

| ref | value | sheet |
|---|---|---|
| `C1` | 0.1uF 50V | Capacitors |
| `C2` | 0.01uF 16V | Capacitors |
| `C3` | 0.1uF 50V | Capacitors |
| `C4` | 0.01uF 16V | Capacitors |
| `C5` | 0.1uF 50V | Capacitors |
| `C6` | 0.01uF 16V | Capacitors |
| `C7` | 0.1uF 50V | Capacitors |
| `C8` | 0.01uF 16V | Capacitors |
| `C9` | 0.1uF 50V | Capacitors |
| `C10` | 0.01uF 16V | Capacitors |
| `C11` | 0.1uF 50V | Capacitors |
| `C12` | 0.01uF 16V | Capacitors |
| `C13` | 0.1uF 50V | Capacitors |
| `C14` | 0.01uF 16V | Capacitors |
| `C15` | 0.1uF 50V | Capacitors |
| `C16` | 0.01uF 16V | Capacitors |
| `C17` | 0.1uF 50V | Capacitors |
| `C18` | 0.01uF 16V | Capacitors |
| `C19` | 0.1uF 50V | Capacitors |
| `C20` | 0.01uF 16V | Capacitors |
| `C21` | 0.1uF 50V | Capacitors |
| `C22` | 0.01uF 16V | Capacitors |
| `C23` | 0.1uF 50V | Capacitors |
| `C24` | 0.01uF 16V | Capacitors |
| `C25` | 0.1uF 50V | Capacitors |
| `C26` | 0.01uF 16V | Capacitors |
| `C27` | 0.1uF 50V | Capacitors |
| `C28` | 0.01uF 16V | Capacitors |
| `C29` | 0.1uF 50V | Capacitors |
| `C30` | 0.01uF 16V | Capacitors |
| `C31` | 0.1uF 50V | Capacitors |
| `C32` | 0.01uF 16V | Capacitors |
| `C33` | 0.1uF 50V | Capacitors |
| `C34` | 0.01uF 16V | Capacitors |
| `C35` | 0.1uF 50V | Capacitors |
| `C36` | 0.01uF 16V | Capacitors |
| `C37` | 0.1uF 50V | Capacitors |
| `C38` | 0.01uF 16V | Capacitors |
| `C39` | 0.1uF 50V | Capacitors |
| `C40` | 0.01uF 16V | Capacitors |
| `C41` | 0.1uF 50V | Capacitors |
| `C42` | 0.1uF 50V | Capacitors |
| `C43` | 10pF | Clock |
| `C44` | 75pF | Clock |
| `C45` | 0.1uF 50V | Capacitors |
| `C46` | 47uF 16V | Power |
| `C47` | 47uF 16V | Power |
| `C48` | 47uF | Power |
| `C49` | 0.1uF 50V | Capacitors |
| `C50` | 1nF | Power |
| `C51` | 0.1uF 50V | Capacitors |
| `C52` | 47uF 16V | Power |
| `C53` | 1nF | Power |
| `C54` | 0.1uF 12V | Capacitors |
| `C55` | 2200uF 35V | Power |
| `C56` | 47uF 16V | Power |
| `C57` | 10000uF 16V | Power |
| `C58` | 0.1uF 12V | Capacitors |
| `C59` | 0.1uF 12V | Capacitors |
| `C60` | 220uF 16V | Power |
| `C61` | 200pF | Line Printer |
| `C62` | 33uF | Floppy Controller |
| `C63` | 10uF 16V | Power |
| `C64` | 0.1uF 12V | Capacitors |
| `C65` | 0.1uF 12V | Capacitors |
| `C66` | 0.1uF 12V | Capacitors |
| `C67` | 0.1uF 12V | Capacitors |
| `C68` | 0.1uF 12V | Capacitors |
| `C69` | 0.1uF 12V | Capacitors |
| `C70` | 0.1uF 50V | Capacitors |
| `C71` | 0.1uF 50V | Capacitors |
| `C72` | 0.1uF 12V | Capacitors |
| `C73` | 0.1uF 12V | Capacitors |
| `C74` | 0.1uF 12V | Capacitors |
| `C75` | 0.1uF 12V | Capacitors |
| `C76` | 0.1uF 12V | Capacitors |
| `C77` | 0.1uF 12V | Capacitors |
| `C78` | 0.1uF 12V | Capacitors |
| `C79` | 0.1uF 12V | Capacitors |
| `CR1` | 1N4148 | Cassette Interface |
| `CR2` | MDA202 | Power |
| `CR3` | 1N5231 | Power |
| `CR4` | 1N4735 | Power |
| `J1` | Expansion Board Connector | Internal Expansion |
| `J2` | M1 Edge Connector | Card-Edge Interface |
| `J3` | Buffered Edge Connector | Card-Edge Interface Extension |
| `J4` | Line Printer Connector | Line Printer |
| `J5` | Shugart Floppy Disk Bus | Floppy Controller |
| `J6` | Front View 
(Cassette 1) | Cassette Interface |
| `J7` | Front View
(Cassette 2) | Cassette Interface |
| `J8` | Front View
(Cassette M1) | Cassette Interface |
| `J9` | Front View
Power | Power |
| `J10` | Internal Expansion Connector | Internal Expansion |
| `K1` | ~ | Cassette Interface |
| `Q1` | MJE2955 | Power |
| `Q2` | MJE2955 | Power |
| `Q3` | 2N3904 | Power |
| `R1` | 10M | Clock |
| `R2` | 1k | Clock |
| `R3` | 2.2k | Timer |
| `R4` | 1.2k | Power |
| `R5` | 2.2k | Power |
| `R6` | 2k | Power |
| `R7` | 1k | Power |
| `R8` | 1k | Power |
| `R9` | 3.3k | Power |
| `R10` | 3.3k | Power |
| `R11` | 12k | Power |
| `R12` | 0.33 | Power |
| `R13` | 68 | Power |
| `R14` | 4.7k | Power |
| `R15` | 1.2k | Power |
| `R16` | 4.7k |  |
| `R17` | 560 | Power |
| `R18` | 4.7k | Memory Management |
| `R19` | 33 | Memory Management |
| `R20` | 4.7k | Internal Expansion |
| `R21` | 220 | Power |
| `R22` | 150 | Floppy Controller |
| `R23` | 20k | Line Printer |
| `R24` | 4.7k |  |
| `R25` | 200k | Floppy Controller |
| `R26` | 33 | Memory Management |
| `R27` | 33 | Memory Management |
| `R28` | 10k | Floppy Controller |
| `R29` | 10k | Floppy Controller |
| `R30` | 10k | Floppy Controller |
| `R31` | 150 | Floppy Controller |
| `R32` | 150 | Floppy Controller |
| `R33` | 150 | Floppy Controller |
| `R34` | 4.7k | Line Printer |
| `R35` | 5.6 | Power |
| `S1` | ~ | Power |
| `Y1` | 4 MHz | Clock |
| `Z1` | MK4116 | RAM |
| `Z2` | MK4116 | RAM |
| `Z3` | MK4116 | RAM |
| `Z4` | MK4116 | RAM |
| `Z5` | MK4116 | RAM |
| `Z6` | MK4116 | RAM |
| `Z7` | MK4116 | RAM |
| `Z8` | MK4116 | RAM |
| `Z9` | MK4116 | RAM |
| `Z10` | MK4116 | RAM |
| `Z11` | MK4116 | RAM |
| `Z12` | MK4116 | RAM |
| `Z13` | MK4116 | RAM |
| `Z14` | MK4116 | RAM |
| `Z15` | MK4116 | RAM |
| `Z16` | MK4116 | RAM |
| `Z17` | 74LS00 | Cassette Interface |
| `Z18` | 75452 | Cassette Interface |
| `Z19` | 4049B | Clock |
| `Z20` | LM723C | Power |
| `Z21` | LM723C | Power |
| `Z22` | 74LS90 | Clock |
| `Z23` | 4518 | Timer |
| `Z24` | 4518 | Timer |
| `Z25` | 74LS74 | Clock |
| `Z26` | 74LS74 | Timer |
| `Z27` | 74LS32 | Memory Management |
| `Z28` | 74LS00 | Internal Expansion |
| `Z29` | 74LS244_Split | Memory Management |
| `Z30` | 74LS243 | Card-Edge Interface |
| `Z31` | 74LS244_Split | Memory Management |
| `Z32` | 74LS04 | Address Decoder |
| `Z33` | 74LS123 | Line Printer |
| `Z34` | 7416 |  |
| `Z35` | 74LS157 | Memory Management |
| `Z36` | 74LS157 | Memory Management |
| `Z37` | DDU-4-7835 | Card-Edge Interface |
| `Z38` | 74LS243 | Card-Edge Interface |
| `Z39` | 74LS155 | Address Decoder |
| `Z40` | 74LS139 | Address Decoder |
| `Z41` | 7416 | Internal Expansion |
| `Z42` | FD1771 | Floppy Controller |
| `Z43` | 74LS30 | Address Decoder |
| `Z44` | 74LS244 | Card-Edge Interface |
| `Z45` | 74LS244 | Card-Edge Interface |
| `Z46` | 74LS20 | Internal Expansion |
| `Z47` | 74LS175 | Floppy Controller |
| `Z48` | 74LS273 | Line Printer |
| `Z49` | 74LS367 |  |
| `Z50` | 74LS240_Split | Floppy Controller |
| `Z51` | 74LS240_Split | Floppy Controller |

## Connections

For each pin: its name, its net, and what else is on that net. Nets with more than 12 pins (power, ground, buses) are named rather than expanded.

```
C1  (0.1uF 50V, Capacitors)
   pin   1                -5V                          [net -5V, 38 pins]
   pin   2                GND                          [net GND, 227 pins]

C2  (0.01uF 16V, Capacitors)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C3  (0.1uF 50V, Capacitors)
   pin   1                -5V                          [net -5V, 38 pins]
   pin   2                GND                          [net GND, 227 pins]

C4  (0.01uF 16V, Capacitors)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C5  (0.1uF 50V, Capacitors)
   pin   1                -5V                          [net -5V, 38 pins]
   pin   2                GND                          [net GND, 227 pins]

C6  (0.01uF 16V, Capacitors)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C7  (0.1uF 50V, Capacitors)
   pin   1                -5V                          [net -5V, 38 pins]
   pin   2                GND                          [net GND, 227 pins]

C8  (0.01uF 16V, Capacitors)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C9  (0.1uF 50V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C10  (0.01uF 16V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C11  (0.1uF 50V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C12  (0.01uF 16V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C13  (0.1uF 50V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C14  (0.01uF 16V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C15  (0.1uF 50V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C16  (0.01uF 16V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C17  (0.1uF 50V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C18  (0.01uF 16V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C19  (0.1uF 50V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C20  (0.01uF 16V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C21  (0.1uF 50V, Capacitors)
   pin   1                -5V                          [net -5V, 38 pins]
   pin   2                GND                          [net GND, 227 pins]

C22  (0.01uF 16V, Capacitors)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C23  (0.1uF 50V, Capacitors)
   pin   1                -5V                          [net -5V, 38 pins]
   pin   2                GND                          [net GND, 227 pins]

C24  (0.01uF 16V, Capacitors)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C25  (0.1uF 50V, Capacitors)
   pin   1                -5V                          [net -5V, 38 pins]
   pin   2                GND                          [net GND, 227 pins]

C26  (0.01uF 16V, Capacitors)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C27  (0.1uF 50V, Capacitors)
   pin   1                -5V                          [net -5V, 38 pins]
   pin   2                GND                          [net GND, 227 pins]

C28  (0.01uF 16V, Capacitors)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C29  (0.1uF 50V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C30  (0.01uF 16V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C31  (0.1uF 50V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C32  (0.01uF 16V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C33  (0.1uF 50V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C34  (0.01uF 16V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C35  (0.1uF 50V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C36  (0.01uF 16V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C37  (0.1uF 50V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C38  (0.01uF 16V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C39  (0.1uF 50V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C40  (0.01uF 16V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C41  (0.1uF 50V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C42  (0.1uF 50V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C43  (10pF, Clock)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                Net-(C43-Pad2)               R1.1 Y1.1(1) Z19.11

C44  (75pF, Clock)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                Net-(C44-Pad2)               R2.1 Y1.2(2)

C45  (0.1uF 50V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C46  (47uF 16V, Power)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C47  (47uF 16V, Power)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C48  (47uF, Power)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C49  (0.1uF 50V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C50  (1nF, Power)
   pin   1                Net-(Z20-FC)                 Z20.13(FC)
   pin   2                Net-(Z20--)                  R7.2(2) Z20.4(-)

C51  (0.1uF 50V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C52  (47uF 16V, Power)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C53  (1nF, Power)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                Net-(Z21-FC)                 Z21.13(FC)

C54  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C55  (2200uF 35V, Power)
   pin   1                Net-(Q1-E)                   Q1.3(E) R4.1 S1.7 Z20.12(V+)
   pin   2                GND                          [net GND, 227 pins]

C56  (47uF 16V, Power)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C57  (10000uF 16V, Power)
   pin   1                Net-(Q2-E)                   Q2.3(E) R13.1 S1.10 S1.3
   pin   2                GND                          [net GND, 227 pins]

C58  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C59  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C60  (220uF 16V, Power)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                Net-(C60-Pad2)               R21.2 S1.6

C61  (200pF, Line Printer)
   pin   1                Net-(Z33A-RCext)             R23.2 Z33.15(RCext)
   pin   2                GND                          [net GND, 227 pins]

C62  (33uF, Floppy Controller)
   pin   1                Net-(Z33B-RCext)             R25.1 Z33.7(RCext)
   pin   2                GND                          [net GND, 227 pins]

C63  (10uF 16V, Power)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C64  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C65  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C66  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C67  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C68  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C69  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C70  (0.1uF 50V, Capacitors)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                -5V                          [net -5V, 38 pins]

C71  (0.1uF 50V, Capacitors)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                GND                          [net GND, 227 pins]

C72  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C73  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C74  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C75  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C76  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C77  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C78  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

C79  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                GND                          [net GND, 227 pins]

CR1  (1N4148, Cassette Interface)
   pin   1 K              +5V                          [net +5V, 105 pins]
   pin   2 A              Net-(CR1-A)                  K1.13 Z18.3(1Y)

CR2  (MDA202, Power)
   pin   1 +              Net-(CR2-+)                  S1.11 S1.2
   pin   2                Net-(CR2-Pad2)               J9.1
   pin   3                Net-(CR2-Pad3)               J9.3
   pin   4 -              Net-(CR2--)                  S1.5

CR3  (1N5231, Power)
   pin   1 K              GND                          [net GND, 227 pins]
   pin   2 A              -5V                          [net -5V, 38 pins]

CR4  (1N4735, Power)
   pin   1 K              +5V                          [net +5V, 105 pins]
   pin   2 A              GND                          [net GND, 227 pins]

J1  (Expansion Board Connector, Internal Expansion)
   pin   1 Pin_1          GND                          [net GND, 227 pins]
   pin   2 Pin_2          unconnected-(J1-Pin_2-Pad2)  (no other connection)
   pin   3 Pin_3          GND                          [net GND, 227 pins]
   pin   4 Pin_4          unconnected-(J1-Pin_4-Pad4)  (no other connection)
   pin   5 Pin_5          GND                          [net GND, 227 pins]
   pin   6 Pin_6          unconnected-(J1-Pin_6-Pad6)  (no other connection)
   pin   7 Pin_7          GND                          [net GND, 227 pins]
   pin   8 Pin_8          unconnected-(J1-Pin_8-Pad8)  (no other connection)
   pin   9 Pin_9          GND                          [net GND, 227 pins]
   pin  10 Pin_10         S0                           J10.19(Pin_19)
   pin  11 Pin_11         GND                          [net GND, 227 pins]
   pin  12 Pin_12         S1                           J10.20(Pin_20)
   pin  13 Pin_13         GND                          [net GND, 227 pins]
   pin  14 Pin_14         S2                           J10.21(Pin_21)
   pin  15 Pin_15         GND                          [net GND, 227 pins]
   pin  16 Pin_16         S3                           J10.22(Pin_22)
   pin  17 Pin_17         GND                          [net GND, 227 pins]
   pin  18 Pin_18         S4                           J10.23(Pin_23)
   pin  19 Pin_19         GND                          [net GND, 227 pins]
   pin  20 Pin_20         S5                           J10.24(Pin_24)
   pin  21 Pin_21         GND                          [net GND, 227 pins]
   pin  22 Pin_22         S6                           J10.25(Pin_25)
   pin  23 Pin_23         GND                          [net GND, 227 pins]
   pin  24 Pin_24         S7                           J10.26(Pin_26)
   pin  25 Pin_25         GND                          [net GND, 227 pins]
   pin  26 Pin_26         S8                           J10.27(Pin_27)
   pin  27 Pin_27         GND                          [net GND, 227 pins]
   pin  28 Pin_28         S9                           J10.28(Pin_28)
   pin  29 Pin_29         GND                          [net GND, 227 pins]
   pin  30 Pin_30         S10                          J10.29(Pin_29)
   pin  31 Pin_31         GND                          [net GND, 227 pins]
   pin  32 Pin_32         S11                          J10.30(Pin_30)
   pin  33 Pin_33         GND                          [net GND, 227 pins]
   pin  34 Pin_34         S12                          J10.31(Pin_31)
   pin  35 Pin_35         GND                          [net GND, 227 pins]
   pin  36 Pin_36         S13                          J10.32(Pin_32)
   pin  37 Pin_37         GND                          [net GND, 227 pins]
   pin  38 Pin_38         S14                          J10.33(Pin_33)
   pin  39 Pin_39         GND                          [net GND, 227 pins]
   pin  40 Pin_40         S15                          J10.34(Pin_34)

J2  (M1 Edge Connector, Card-Edge Interface)
   pin   1 Pin_1          ~{M1_RAS}                    Z38.3(A0)
   pin   2 Pin_2          ~{SYSRES}                    J10.6(Pin_6) J3.2(Pin_2) R28.1 Z42.19(~{MR})
   pin   3 Pin_3          unconnected-(J2-Pin_3-Pad3)  (no other connection)
   pin   4 Pin_4          M1_A10                       Z44.17(I3b)
   pin   5 Pin_5          M1_A12                       Z44.13(I1b)
   pin   6 Pin_6          M1_A13                       Z44.15(I2b)
   pin   7 Pin_7          M1_A15                       Z44.11(I0b)
   pin   8 Pin_8          GND                          [net GND, 227 pins]
   pin   9 Pin_9          M1_A11                       Z44.4(I1a)
   pin  10 Pin_10         M1_A14                       Z44.2(I0a)
   pin  11 Pin_11         M1_A8                        Z44.6(I2a)
   pin  12 Pin_12         ~{OUT}                       J10.18(Pin_18) J3.12(Pin_12)
   pin  13 Pin_13         Net-(J2-Pin_13)              Z30.4(A1)
   pin  14 Pin_14         ~{INTAK}                     J3.14(Pin_14)
   pin  15 Pin_15         Net-(J2-Pin_15)              Z30.5(A2)
   pin  16 Pin_16         unconnected-(J2-Pin_16-Pad16) (no other connection)
   pin  17 Pin_17         M1_A9                        Z44.8(I3a)
   pin  18 Pin_18         D4                           J10.7(Pin_7) J3.18(Pin_18) Z29.8 Z29.9 Z48.3(D0) Z49.3 Z51.2 Z51.3
   pin  19 Pin_19         ~{IN}                        J10.16(Pin_16) J3.19(Pin_19)
   pin  20 Pin_20         D7                           J10.5(Pin_5) J3.20(Pin_20) Z29.2 Z29.3 Z48.8(D3) Z49.11 Z49.9 Z51.4 Z51.5
   pin  21 Pin_21         ~{INT}                       J10.15(Pin_15) J3.21(Pin_21) Z34.10 Z34.12
   pin  22 Pin_22         D1                           J10.14(Pin_14) J3.22(Pin_22) Z31.6 Z31.7 Z47.5(D1) Z48.14(D5) Z50.2 Z50.3
   pin  23 Pin_23         ~{TEST}                      J3.23(Pin_23)
   pin  24 Pin_24         D6                           J10.4(Pin_4) J3.24(Pin_24) Z29.4 Z29.5 Z48.7(D2) Z49.13 Z49.7 Z51.6 Z51.7
   pin  25 Pin_25         M1_A0                        Z45.2(I0a)
   pin  26 Pin_26         D3                           J10.12(Pin_12) J3.26(Pin_26) Z31.2 Z31.3 Z47.13(D3) Z48.18(D7) Z50.4 Z50.5
   pin  27 Pin_27         M1_A1                        Z45.17(I3b)
   pin  28 Pin_28         D5                           J10.8(Pin_8) J3.28(Pin_28) Z29.6 Z29.7 Z48.4(D1) Z49.5 Z51.8 Z51.9
   pin  29 Pin_29         GND                          [net GND, 227 pins]
   pin  30 Pin_30         D0                           J10.11(Pin_11) J3.30(Pin_30) Z17.1 Z31.8 Z31.9 Z47.4(D0) Z48.13(D4) Z50.6 Z50.7
   pin  31 Pin_31         M1_A4                        Z45.4(I1a)
   pin  32 Pin_32         D2                           J10.13(Pin_13) J3.32(Pin_32) Z31.4 Z31.5 Z47.12(D2) Z48.17(D6) Z50.8 Z50.9
   pin  33 Pin_33         ~{WAIT}                      J3.33(Pin_33)
   pin  34 Pin_34         M1_A3                        Z45.15(I2b)
   pin  35 Pin_35         M1_A5                        Z45.6(I2a)
   pin  36 Pin_36         M1_A7                        Z45.13(I1b)
   pin  37 Pin_37         GND                          [net GND, 227 pins]
   pin  38 Pin_38         M1_A6                        Z45.8(I3a)
   pin  39 Pin_39         unconnected-(J2-Pin_39-Pad39) (no other connection)
   pin  40 Pin_40         M1_A2                        Z45.11(I0b)

J3  (Buffered Edge Connector, Card-Edge Interface Extension)
   pin   1 Pin_1          unconnected-(J3-Pin_1-Pad1)  (no other connection)
   pin   2 Pin_2          ~{SYSRES}                    J10.6(Pin_6) J2.2(Pin_2) R28.1 Z42.19(~{MR})
   pin   3 Pin_3          unconnected-(J3-Pin_3-Pad3)  (no other connection)
   pin   4 Pin_4          A10                          Z35.13(I1d) Z43.1 Z44.3(O3b)
   pin   5 Pin_5          A12                          Z36.6(I1b) Z43.3 Z44.7(O1b)
   pin   6 Pin_6          A13                          Z36.10(I1c) Z43.2 Z44.5(O2b)
   pin   7 Pin_7          A15                          Z40.3(A1) Z44.9(O0b)
   pin   8 Pin_8          GND                          [net GND, 227 pins]
   pin   9 Pin_9          A11                          Z36.3(I1a) Z40.13(A1) Z44.16(O1a)
   pin  10 Pin_10         A14                          Z40.2(A0) Z44.18(O0a)
   pin  11 Pin_11         A8                           Z35.6(I1b) Z43.12 Z44.14(O2a)
   pin  12 Pin_12         ~{OUT}                       J10.18(Pin_18) J2.12(Pin_12)
   pin  13 Pin_13         ~{WR}                        Z27.4 Z27.5 Z30.10(B1) Z39.15(Eb2)
   pin  14 Pin_14         ~{INTAK}                     J2.14(Pin_14)
   pin  15 Pin_15         ~{RD}                        Z30.9(B2) Z32.1 Z32.5
   pin  16 Pin_16         unconnected-(J3-Pin_16-Pad16) (no other connection)
   pin  17 Pin_17         A9                           Z35.10(I1c) Z43.4 Z44.12(O3a)
   pin  18 Pin_18         D4                           J10.7(Pin_7) J2.18(Pin_18) Z29.8 Z29.9 Z48.3(D0) Z49.3 Z51.2 Z51.3
   pin  19 Pin_19         ~{IN}                        J10.16(Pin_16) J2.19(Pin_19)
   pin  20 Pin_20         D7                           J10.5(Pin_5) J2.20(Pin_20) Z29.2 Z29.3 Z48.8(D3) Z49.11 Z49.9 Z51.4 Z51.5
   pin  21 Pin_21         ~{INT}                       J10.15(Pin_15) J2.21(Pin_21) Z34.10 Z34.12
   pin  22 Pin_22         D1                           J10.14(Pin_14) J2.22(Pin_22) Z31.6 Z31.7 Z47.5(D1) Z48.14(D5) Z50.2 Z50.3
   pin  23 Pin_23         ~{TEST}                      J2.23(Pin_23)
   pin  24 Pin_24         D6                           J10.4(Pin_4) J2.24(Pin_24) Z29.4 Z29.5 Z48.7(D2) Z49.13 Z49.7 Z51.6 Z51.7
   pin  25 Pin_25         A0                           J10.10(Pin_10) Z35.2(I0a) Z42.5(A0) Z45.18(O0a)
   pin  26 Pin_26         D3                           J10.12(Pin_12) J2.26(Pin_26) Z31.2 Z31.3 Z47.13(D3) Z48.18(D7) Z50.4 Z50.5
   pin  27 Pin_27         A1                           J10.9(Pin_9) Z35.5(I0b) Z42.6(A1) Z45.3(O3b)
   pin  28 Pin_28         D5                           J10.8(Pin_8) J2.28(Pin_28) Z29.6 Z29.7 Z48.4(D1) Z49.5 Z51.8 Z51.9
   pin  29 Pin_29         GND                          [net GND, 227 pins]
   pin  30 Pin_30         D0                           J10.11(Pin_11) J2.30(Pin_30) Z17.1 Z31.8 Z31.9 Z47.4(D0) Z48.13(D4) Z50.6 Z50.7
   pin  31 Pin_31         A4                           Z28.12 Z28.13 Z36.2(I0a) Z45.16(O1a)
   pin  32 Pin_32         D2                           J10.13(Pin_13) J2.32(Pin_32) Z31.4 Z31.5 Z47.12(D2) Z48.17(D6) Z50.8 Z50.9
   pin  33 Pin_33         ~{WAIT}                      J2.33(Pin_33)
   pin  34 Pin_34         A3                           Z35.14(I0d) Z39.3(A1) Z45.5(O2b) Z46.12
   pin  35 Pin_35         A5                           Z36.5(I0b) Z43.5 Z45.14(O2a) Z46.10
   pin  36 Pin_36         A7                           Z35.3(I1a) Z43.11 Z45.7(O1b) Z46.13
   pin  37 Pin_37         GND                          [net GND, 227 pins]
   pin  38 Pin_38         A6                           Z36.11(I0c) Z43.6 Z45.12(O3a) Z46.9
   pin  39 Pin_39         +5V                          [net +5V, 105 pins]
   pin  40 Pin_40         A2                           J10.17(Pin_17) Z35.11(I0c) Z39.13(A0) Z45.9(O0b)

J4  (Line Printer Connector, Line Printer)
   pin   1 Pin_1          ~{DATA_STROBE}               Z33.4(~{Q})
   pin   2 Pin_2          GND                          [net GND, 227 pins]
   pin   3 Pin_3          DATA1                        Z48.12(Q4)
   pin   4 Pin_4          GND                          [net GND, 227 pins]
   pin   5 Pin_5          DATA2                        Z48.15(Q5)
   pin   6 Pin_6          GND                          [net GND, 227 pins]
   pin   7 Pin_7          DATA3                        Z48.16(Q6)
   pin   8 Pin_8          GND                          [net GND, 227 pins]
   pin   9 Pin_9          DATA4                        Z48.19(Q7)
   pin  10 Pin_10         GND                          [net GND, 227 pins]
   pin  11 Pin_11         DATA5                        Z48.2(Q0)
   pin  12 Pin_12         GND                          [net GND, 227 pins]
   pin  13 Pin_13         DATA6                        Z48.5(Q1)
   pin  14 Pin_14         GND                          [net GND, 227 pins]
   pin  15 Pin_15         DATA7                        Z48.6(Q2)
   pin  16 Pin_16         GND                          [net GND, 227 pins]
   pin  17 Pin_17         DATA8                        Z48.9(Q3)
   pin  18 Pin_18         GND                          [net GND, 227 pins]
   pin  19 Pin_19         unconnected-(J4-Pin_19-Pad19) (no other connection)
   pin  20 Pin_20         GND                          [net GND, 227 pins]
   pin  21 Pin_21         ~{BUSY}                      Z49.10
   pin  22 Pin_22         GND                          [net GND, 227 pins]
   pin  23 Pin_23         ~{OUT_OF_PAPER}              Z49.6
   pin  24 Pin_24         GND                          [net GND, 227 pins]
   pin  25 Pin_25         ~{UNIT_SELECT}               Z49.4
   pin  26 Pin_26         PRIME                        (no other connection)
   pin  27 Pin_27         GND                          [net GND, 227 pins]
   pin  28 Pin_28         ~{FAULT}                     Z49.2
   pin  29 Pin_29         unconnected-(J4-Pin_29-Pad29) (no other connection)
   pin  30 Pin_30         unconnected-(J4-Pin_30-Pad30) (no other connection)
   pin  31 Pin_31         GND                          [net GND, 227 pins]
   pin  32 Pin_32         unconnected-(J4-Pin_32-Pad32) (no other connection)
   pin  33 Pin_33         GND                          [net GND, 227 pins]
   pin  34 Pin_34         GND                          [net GND, 227 pins]

J5  (Shugart Floppy Disk Bus, Floppy Controller)
   pin   1 Pin_1          GND                          [net GND, 227 pins]
   pin   2 Pin_2          unconnected-(J5-Pin_2-Pad2)  (no other connection)
   pin   3 Pin_3          GND                          [net GND, 227 pins]
   pin   4 Pin_4          unconnected-(J5-Pin_4-Pad4)  (no other connection)
   pin   5 Pin_5          GND                          [net GND, 227 pins]
   pin   6 Pin_6          unconnected-(J5-Pin_6-Pad6)  (no other connection)
   pin   7 Pin_7          GND                          [net GND, 227 pins]
   pin   8 Pin_8          ~{INDEX_PULSE}               R32.2 Z42.35(~{IP})
   pin   9 Pin_9          GND                          [net GND, 227 pins]
   pin  10 Pin_10         ~{DS0}                       Z41.8
   pin  11 Pin_11         GND                          [net GND, 227 pins]
   pin  12 Pin_12         ~{DS1}                       Z41.6
   pin  13 Pin_13         GND                          [net GND, 227 pins]
   pin  14 Pin_14         ~{DS2}                       Z41.10
   pin  15 Pin_15         GND                          [net GND, 227 pins]
   pin  16 Pin_16         ~{MOTOR_ON}                  Z41.4
   pin  17 Pin_17         GND                          [net GND, 227 pins]
   pin  18 Pin_18         ~{DIR_SEL}                   Z34.2
   pin  19 Pin_19         GND                          [net GND, 227 pins]
   pin  20 Pin_20         ~{STEP}                      Z34.4
   pin  21 Pin_21         GND                          [net GND, 227 pins]
   pin  22 Pin_22         ~{WRITE_DATA}                Z34.8
   pin  23 Pin_23         GND                          [net GND, 227 pins]
   pin  24 Pin_24         ~{WRITE_GATE}                Z34.6
   pin  25 Pin_25         GND                          [net GND, 227 pins]
   pin  26 Pin_26         ~{TRACK_ZERO}                R33.2 Z42.34(~{TR00})
   pin  27 Pin_27         GND                          [net GND, 227 pins]
   pin  28 Pin_28         ~{WRITE_PROTECT}             R31.2 Z42.36(~{WPRT})
   pin  29 Pin_29         GND                          [net GND, 227 pins]
   pin  30 Pin_30         ~{READ_DATA}                 R22.2 Z32.9
   pin  31 Pin_31         GND                          [net GND, 227 pins]
   pin  32 Pin_32         ~{DS3}                       Z41.12
   pin  33 Pin_33         GND                          [net GND, 227 pins]
   pin  34 Pin_34         unconnected-(J5-Pin_34-Pad34) (no other connection)

J6  (Front View 
(Cassette 1), Cassette Interface)
   pin   1                Net-(J6-Pad1)                K1.8
   pin   2                GND2                         J7.2 J8.2
   pin   3                Net-(J6-Pad3)                K1.7
   pin   4                Net-(J6-Pad4)                K1.6
   pin   5                Net-(J6-Pad5)                K1.5

J7  (Front View
(Cassette 2), Cassette Interface)
   pin   1                Net-(J7-Pad1)                K1.12
   pin   2                GND2                         J6.2 J8.2
   pin   3                Net-(J7-Pad3)                K1.11
   pin   4                Net-(J7-Pad4)                K1.10
   pin   5                Net-(J7-Pad5)                K1.9

J8  (Front View
(Cassette M1), Cassette Interface)
   pin   1                Net-(J8-Pad1)                K1.4
   pin   2                GND2                         J6.2 J7.2
   pin   3                Net-(J8-Pad3)                K1.3
   pin   4                Net-(J8-Pad4)                K1.2
   pin   5                Net-(J8-Pad5)                K1.1

J9  (Front View
Power, Power)
   pin   1                Net-(CR2-Pad2)               CR2.2
   pin   2                Net-(J9-Pad2)                S1.8
   pin   3                Net-(CR2-Pad3)               CR2.3
   pin   4                GND                          [net GND, 227 pins]
   pin   5                unconnected-(J9-Pad5)        (no other connection)

J10  (Internal Expansion Connector, Internal Expansion)
   pin   1 Pin_1          GND                          [net GND, 227 pins]
   pin   2 Pin_2          +5V                          [net +5V, 105 pins]
   pin   3 Pin_3          ~{E8}                        Z28.8
   pin   4 Pin_4          D6                           J2.24(Pin_24) J3.24(Pin_24) Z29.4 Z29.5 Z48.7(D2) Z49.13 Z49.7 Z51.6 Z51.7
   pin   5 Pin_5          D7                           J2.20(Pin_20) J3.20(Pin_20) Z29.2 Z29.3 Z48.8(D3) Z49.11 Z49.9 Z51.4 Z51.5
   pin   6 Pin_6          ~{SYSRES}                    J2.2(Pin_2) J3.2(Pin_2) R28.1 Z42.19(~{MR})
   pin   7 Pin_7          D4                           J2.18(Pin_18) J3.18(Pin_18) Z29.8 Z29.9 Z48.3(D0) Z49.3 Z51.2 Z51.3
   pin   8 Pin_8          D5                           J2.28(Pin_28) J3.28(Pin_28) Z29.6 Z29.7 Z48.4(D1) Z49.5 Z51.8 Z51.9
   pin   9 Pin_9          A1                           J3.27(Pin_27) Z35.5(I0b) Z42.6(A1) Z45.3(O3b)
   pin  10 Pin_10         A0                           J3.25(Pin_25) Z35.2(I0a) Z42.5(A0) Z45.18(O0a)
   pin  11 Pin_11         D0                           J2.30(Pin_30) J3.30(Pin_30) Z17.1 Z31.8 Z31.9 Z47.4(D0) Z48.13(D4) Z50.6 Z50.7
   pin  12 Pin_12         D3                           J2.26(Pin_26) J3.26(Pin_26) Z31.2 Z31.3 Z47.13(D3) Z48.18(D7) Z50.4 Z50.5
   pin  13 Pin_13         D2                           J2.32(Pin_32) J3.32(Pin_32) Z31.4 Z31.5 Z47.12(D2) Z48.17(D6) Z50.8 Z50.9
   pin  14 Pin_14         D1                           J2.22(Pin_22) J3.22(Pin_22) Z31.6 Z31.7 Z47.5(D1) Z48.14(D5) Z50.2 Z50.3
   pin  15 Pin_15         ~{INT}                       J2.21(Pin_21) J3.21(Pin_21) Z34.10 Z34.12
   pin  16 Pin_16         ~{IN}                        J2.19(Pin_19) J3.19(Pin_19)
   pin  17 Pin_17         A2                           J3.40(Pin_40) Z35.11(I0c) Z39.13(A0) Z45.9(O0b)
   pin  18 Pin_18         ~{OUT}                       J2.12(Pin_12) J3.12(Pin_12)
   pin  19 Pin_19         S0                           J1.10(Pin_10)
   pin  20 Pin_20         S1                           J1.12(Pin_12)
   pin  21 Pin_21         S2                           J1.14(Pin_14)
   pin  22 Pin_22         S3                           J1.16(Pin_16)
   pin  23 Pin_23         S4                           J1.18(Pin_18)
   pin  24 Pin_24         S5                           J1.20(Pin_20)
   pin  25 Pin_25         S6                           J1.22(Pin_22)
   pin  26 Pin_26         S7                           J1.24(Pin_24)
   pin  27 Pin_27         S8                           J1.26(Pin_26)
   pin  28 Pin_28         S9                           J1.28(Pin_28)
   pin  29 Pin_29         S10                          J1.30(Pin_30)
   pin  30 Pin_30         S11                          J1.32(Pin_32)
   pin  31 Pin_31         S12                          J1.34(Pin_34)
   pin  32 Pin_32         S13                          J1.36(Pin_36)
   pin  33 Pin_33         S14                          J1.38(Pin_38)
   pin  34 Pin_34         S15                          J1.40(Pin_40)

K1  (~, Cassette Interface)
   pin   1                Net-(J8-Pad5)                J8.5
   pin   2                Net-(J8-Pad4)                J8.4
   pin   3                Net-(J8-Pad3)                J8.3
   pin   4                Net-(J8-Pad1)                J8.1
   pin   5                Net-(J6-Pad5)                J6.5
   pin   6                Net-(J6-Pad4)                J6.4
   pin   7                Net-(J6-Pad3)                J6.3
   pin   8                Net-(J6-Pad1)                J6.1
   pin   9                Net-(J7-Pad5)                J7.5
   pin  10                Net-(J7-Pad4)                J7.4
   pin  11                Net-(J7-Pad3)                J7.3
   pin  12                Net-(J7-Pad1)                J7.1
   pin  13                Net-(CR1-A)                  CR1.2(A) Z18.3(1Y)
   pin  14                +5V                          [net +5V, 105 pins]

Q1  (MJE2955, Power)
   pin   1 B              Net-(Q1-B)                   R4.2 Z20.11(VC)
   pin   2 C              Net-(Q1-C)                   R35.2 R6.2 Z20.10(Vout)
   pin   3 E              Net-(Q1-E)                   C55.1 R4.1 S1.7 Z20.12(V+)

Q2  (MJE2955, Power)
   pin   1 B              Net-(Q2-B)                   Q3.3(C) R13.2
   pin   2 C              Net-(Q2-C)                   Q3.1(E) R12.1
   pin   3 E              Net-(Q2-E)                   C57.1 R13.1 S1.10 S1.3

Q3  (2N3904, Power)
   pin   1 E              Net-(Q2-C)                   Q2.2(C) R12.1
   pin   2 B              Net-(Q3-B)                   R17.1 Z21.10(Vout)
   pin   3 C              Net-(Q2-B)                   Q2.1(B) R13.2

R1  (10M, Clock)
   pin   1                Net-(C43-Pad2)               C43.2 Y1.1(1) Z19.11
   pin   2                Net-(R1-Pad2)                R2.2 Z19.12 Z19.14

R2  (1k, Clock)
   pin   1                Net-(C44-Pad2)               C44.2 Y1.2(2)
   pin   2                Net-(R1-Pad2)                R1.2 Z19.12 Z19.14

R3  (2.2k, Timer)
   pin   1                CLK/10                       Z22.11(Q3) Z23.2(Enable)
   pin   2                +5V                          [net +5V, 105 pins]

R4  (1.2k, Power)
   pin   1                Net-(Q1-E)                   C55.1 Q1.3(E) S1.7 Z20.12(V+)
   pin   2                Net-(Q1-B)                   Q1.1(B) Z20.11(VC)

R5  (2.2k, Power)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                Net-(R5-Pad2)                R7.1(1)

R6  (2k, Power)
   pin   1                Net-(Z20-ILIM)               R11.1 Z20.2(ILIM)
   pin   2                Net-(Q1-C)                   Q1.2(C) R35.2 Z20.10(Vout)

R7  (1k, Power)
   pin   1 1              Net-(R5-Pad2)                R5.2
   pin   2 2              Net-(Z20--)                  C50.2 Z20.4(-)
   pin   3 3              Net-(R10-Pad1)               R10.1

R8  (1k, Power)
   pin   1 1              Net-(R15-Pad1)               R15.1
   pin   2 2              Net-(Z21-+)                  Z21.5(+)
   pin   3 3              Net-(R8-Pad3)                R9.1

R9  (3.3k, Power)
   pin   1                Net-(R8-Pad3)                R8.3(3)
   pin   2                GND                          [net GND, 227 pins]

R10  (3.3k, Power)
   pin   1                Net-(R10-Pad1)               R7.3(3)
   pin   2                GND                          [net GND, 227 pins]

R11  (12k, Power)
   pin   1                Net-(Z20-ILIM)               R6.1 Z20.2(ILIM)
   pin   2                GND                          [net GND, 227 pins]

R12  (0.33, Power)
   pin   1                Net-(Q2-C)                   Q2.2(C) Q3.1(E)
   pin   2                +5V                          [net +5V, 105 pins]

R13  (68, Power)
   pin   1                Net-(Q2-E)                   C57.1 Q2.3(E) S1.10 S1.3
   pin   2                Net-(Q2-B)                   Q2.1(B) Q3.3(C)

R14  (4.7k, Power)
   pin   1                Net-(Z21-ILIM)               R17.2 Z21.2(ILIM)
   pin   2                GND                          [net GND, 227 pins]

R15  (1.2k, Power)
   pin   1                Net-(R15-Pad1)               R8.1(1)
   pin   2                Net-(Z21-VREF)               Z21.6(VREF)

R16  (4.7k, )
   pin   1                HI1                          Z25.1(~{R}) Z25.4(~{S}) Z26.1(~{R}) Z26.13(~{R})
   pin   2                +5V                          [net +5V, 105 pins]

R17  (560, Power)
   pin   1                Net-(Q3-B)                   Q3.2(B) Z21.10(Vout)
   pin   2                Net-(Z21-ILIM)               R14.1 Z21.2(ILIM)

R18  (4.7k, Memory Management)
   pin   1 R1             +5V                          [net +5V, 105 pins]
   pin   2 R1.2           Net-(R18A-R1.2)              R19.2(R1.2) Z27.3
   pin   3 R2.2           Net-(R18B-R2.2)              R19.4(R2.2) Z27.11
   pin   4 R3.2           Net-(R18C-R3.2)              R19.6(R3.2) Z27.6
   pin   5 R4.2           Net-(R18D-R4.2)              R19.8(R4.2) Z27.8

R19  (33, Memory Management)
   pin   1 R1.1           ~{LOWER}                     Z10.15(~{CAS}) Z11.15(~{CAS}) Z12.15(~{CAS}) Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z9.15(~{CAS})
   pin   2 R1.2           Net-(R18A-R1.2)              R18.2(R1.2) Z27.3
   pin   3 R2.1           ~{UPPER}                     Z1.15(~{CAS}) Z2.15(~{CAS}) Z3.15(~{CAS}) Z4.15(~{CAS}) Z5.15(~{CAS}) Z6.15(~{CAS}) Z7.15(~{CAS}) Z8.15(~{CAS})
   pin   4 R2.2           Net-(R18B-R2.2)              R18.3(R2.2) Z27.11
   pin   5 R3.1           ~{WR}                        [net ~{WR}, 17 pins]
   pin   6 R3.2           Net-(R18C-R3.2)              R18.4(R3.2) Z27.6
   pin   7 R4.1           ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   8 R4.2           Net-(R18D-R4.2)              R18.5(R4.2) Z27.8

R20  (4.7k, Internal Expansion)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                Net-(R20-Pad2)               Z28.9 Z41.2

R21  (220, Power)
   pin   1                -5V                          [net -5V, 38 pins]
   pin   2                Net-(C60-Pad2)               C60.2 S1.6

R22  (150, Floppy Controller)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                ~{READ_DATA}                 J5.30(Pin_30) Z32.9

R23  (20k, Line Printer)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                Net-(Z33A-RCext)             C61.1 Z33.15(RCext)

R24  (4.7k, )
   pin   1                HI2                          Z33.10(B) Z33.11(Clr) Z33.3(Clr)
   pin   2                +5V                          [net +5V, 105 pins]

R25  (200k, Floppy Controller)
   pin   1                Net-(Z33B-RCext)             C62.1 Z33.7(RCext)
   pin   2                +5V                          [net +5V, 105 pins]

R26  (33, Memory Management)
   pin   1 R1.1           A0                           [net A0, 17 pins]
   pin   2 R1.2           Net-(R26A-R1.2)              Z35.4(Za)
   pin   3 R2.1           A5                           [net A5, 17 pins]
   pin   4 R2.2           Net-(R26B-R2.2)              Z35.12(Zd)
   pin   5 R3.1           A2                           [net A2, 17 pins]
   pin   6 R3.2           Net-(R26C-R3.2)              Z35.7(Zb)
   pin   7 R4.1           A1                           [net A1, 17 pins]
   pin   8 R4.2           Net-(R26D-R4.2)              Z35.9(Zc)

R27  (33, Memory Management)
   pin   1 R1.1           A4                           [net A4, 17 pins]
   pin   2 R1.2           Net-(R27A-R1.2)              Z36.4(Za)
   pin   3 R2.1           unconnected-(R27B-R2.1-Pad3) (no other connection)
   pin   4 R2.2           unconnected-(R27B-R2.2-Pad4) (no other connection)
   pin   5 R3.1           A3                           [net A3, 17 pins]
   pin   6 R3.2           Net-(R27C-R3.2)              Z36.7(Zb)
   pin   7 R4.1           A6                           [net A6, 17 pins]
   pin   8 R4.2           Net-(R27D-R4.2)              Z36.9(Zc)

R28  (10k, Floppy Controller)
   pin   1                ~{SYSRES}                    J10.6(Pin_6) J2.2(Pin_2) J3.2(Pin_2) Z42.19(~{MR})
   pin   2                +5V                          [net +5V, 105 pins]

R29  (10k, Floppy Controller)
   pin   1                Net-(Z42-FDCLK)              Z42.18(~{3PM}) Z42.22(~{TEST}) Z42.25(~{XTDS}) Z42.26(FDCLK) Z42.33(~{WF}) Z42.37(~{DINT})
   pin   2                +5V                          [net +5V, 105 pins]

R30  (10k, Floppy Controller)
   pin   1                ~{INTRQ}                     Z34.11 Z42.39(~{INTRQ}) Z49.14
   pin   2                +5V                          [net +5V, 105 pins]

R31  (150, Floppy Controller)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                ~{WRITE_PROTECT}             J5.28(Pin_28) Z42.36(~{WPRT})

R32  (150, Floppy Controller)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                ~{INDEX_PULSE}               J5.8(Pin_8) Z42.35(~{IP})

R33  (150, Floppy Controller)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                ~{TRACK_ZERO}                J5.26(Pin_26) Z42.34(~{TR00})

R34  (4.7k, Line Printer)
   pin   1                +5V                          [net +5V, 105 pins]
   pin   2                Net-(Z48-~{Mr})              Z48.1(~{Mr})

R35  (5.6, Power)
   pin   1                +12V                         [net +12V, 41 pins]
   pin   2                Net-(Q1-C)                   Q1.2(C) R6.2 Z20.10(Vout)

S1  (~, Power)
   pin   1                unconnected-(S1-Pad1)        (no other connection)
   pin   2                Net-(CR2-+)                  CR2.1(+) S1.11
   pin   3                Net-(Q2-E)                   C57.1 Q2.3(E) R13.1 S1.10
   pin   4                unconnected-(S1-Pad4)        (no other connection)
   pin   5                Net-(CR2--)                  CR2.4(-)
   pin   6                Net-(C60-Pad2)               C60.2 R21.2
   pin   7                Net-(Q1-E)                   C55.1 Q1.3(E) R4.1 Z20.12(V+)
   pin   8                Net-(J9-Pad2)                J9.2
   pin   9                unconnected-(S1-Pad9)        (no other connection)
   pin  10                Net-(Q2-E)                   C57.1 Q2.3(E) R13.1 S1.3
   pin  11                Net-(CR2-+)                  CR2.1(+) S1.2
   pin  12                unconnected-(S1-Pad12)       (no other connection)

Y1  (4 MHz, Clock)
   pin   1 1              Net-(C43-Pad2)               C43.2 R1.1 Z19.11
   pin   2 2              Net-(C44-Pad2)               C44.2 R2.1

Z1  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN7                          Z29.18 Z9.2(IN)
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT7                         Z29.17 Z9.14(OUT)
   pin  15 ~{CAS}         ~{UPPER}                     R19.3(R2.1) Z2.15(~{CAS}) Z3.15(~{CAS}) Z4.15(~{CAS}) Z5.15(~{CAS}) Z6.15(~{CAS}) Z7.15(~{CAS}) Z8.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z2  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN6                          Z10.2(IN) Z29.16
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT6                         Z10.14(OUT) Z29.15
   pin  15 ~{CAS}         ~{UPPER}                     R19.3(R2.1) Z1.15(~{CAS}) Z3.15(~{CAS}) Z4.15(~{CAS}) Z5.15(~{CAS}) Z6.15(~{CAS}) Z7.15(~{CAS}) Z8.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z3  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN5                          Z11.2(IN) Z29.14
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT5                         Z11.14(OUT) Z29.13
   pin  15 ~{CAS}         ~{UPPER}                     R19.3(R2.1) Z1.15(~{CAS}) Z2.15(~{CAS}) Z4.15(~{CAS}) Z5.15(~{CAS}) Z6.15(~{CAS}) Z7.15(~{CAS}) Z8.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z4  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN4                          Z12.2(IN) Z29.12
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT4                         Z12.14(OUT) Z29.11
   pin  15 ~{CAS}         ~{UPPER}                     R19.3(R2.1) Z1.15(~{CAS}) Z2.15(~{CAS}) Z3.15(~{CAS}) Z5.15(~{CAS}) Z6.15(~{CAS}) Z7.15(~{CAS}) Z8.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z5  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN3                          Z13.2(IN) Z31.18
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT3                         Z13.14(OUT) Z31.17
   pin  15 ~{CAS}         ~{UPPER}                     R19.3(R2.1) Z1.15(~{CAS}) Z2.15(~{CAS}) Z3.15(~{CAS}) Z4.15(~{CAS}) Z6.15(~{CAS}) Z7.15(~{CAS}) Z8.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z6  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN2                          Z14.2(IN) Z31.16
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT2                         Z14.14(OUT) Z31.15
   pin  15 ~{CAS}         ~{UPPER}                     R19.3(R2.1) Z1.15(~{CAS}) Z2.15(~{CAS}) Z3.15(~{CAS}) Z4.15(~{CAS}) Z5.15(~{CAS}) Z7.15(~{CAS}) Z8.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z7  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN1                          Z15.2(IN) Z31.14
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT1                         Z15.14(OUT) Z31.13
   pin  15 ~{CAS}         ~{UPPER}                     R19.3(R2.1) Z1.15(~{CAS}) Z2.15(~{CAS}) Z3.15(~{CAS}) Z4.15(~{CAS}) Z5.15(~{CAS}) Z6.15(~{CAS}) Z8.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z8  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN0                          Z16.2(IN) Z31.12
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT0                         Z16.14(OUT) Z31.11
   pin  15 ~{CAS}         ~{UPPER}                     R19.3(R2.1) Z1.15(~{CAS}) Z2.15(~{CAS}) Z3.15(~{CAS}) Z4.15(~{CAS}) Z5.15(~{CAS}) Z6.15(~{CAS}) Z7.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z9  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN7                          Z1.2(IN) Z29.18
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT7                         Z1.14(OUT) Z29.17
   pin  15 ~{CAS}         ~{LOWER}                     R19.1(R1.1) Z10.15(~{CAS}) Z11.15(~{CAS}) Z12.15(~{CAS}) Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z10  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN6                          Z2.2(IN) Z29.16
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT6                         Z2.14(OUT) Z29.15
   pin  15 ~{CAS}         ~{LOWER}                     R19.1(R1.1) Z11.15(~{CAS}) Z12.15(~{CAS}) Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z9.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z11  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN5                          Z29.14 Z3.2(IN)
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT5                         Z29.13 Z3.14(OUT)
   pin  15 ~{CAS}         ~{LOWER}                     R19.1(R1.1) Z10.15(~{CAS}) Z12.15(~{CAS}) Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z9.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z12  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN4                          Z29.12 Z4.2(IN)
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT4                         Z29.11 Z4.14(OUT)
   pin  15 ~{CAS}         ~{LOWER}                     R19.1(R1.1) Z10.15(~{CAS}) Z11.15(~{CAS}) Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z9.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z13  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN3                          Z31.18 Z5.2(IN)
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT3                         Z31.17 Z5.14(OUT)
   pin  15 ~{CAS}         ~{LOWER}                     R19.1(R1.1) Z10.15(~{CAS}) Z11.15(~{CAS}) Z12.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z9.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z14  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN2                          Z31.16 Z6.2(IN)
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT2                         Z31.15 Z6.14(OUT)
   pin  15 ~{CAS}         ~{LOWER}                     R19.1(R1.1) Z10.15(~{CAS}) Z11.15(~{CAS}) Z12.15(~{CAS}) Z13.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z9.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z15  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN1                          Z31.14 Z7.2(IN)
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT1                         Z31.13 Z7.14(OUT)
   pin  15 ~{CAS}         ~{LOWER}                     R19.1(R1.1) Z10.15(~{CAS}) Z11.15(~{CAS}) Z12.15(~{CAS}) Z13.15(~{CAS}) Z14.15(~{CAS}) Z16.15(~{CAS}) Z9.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z16  (MK4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 IN             IN0                          Z31.12 Z8.2(IN)
   pin   3 ~{WR}          ~{WR}                        [net ~{WR}, 17 pins]
   pin   4 ~{RAS}         ~{RAS}                       [net ~{RAS}, 17 pins]
   pin   5 A0             A0                           [net A0, 17 pins]
   pin   6 A2             A2                           [net A2, 17 pins]
   pin   7 A1             A1                           [net A1, 17 pins]
   pin   8 VDD            +12V                         [net +12V, 41 pins]
   pin   9 VCC            +5V                          [net +5V, 105 pins]
   pin  10 A5             A5                           [net A5, 17 pins]
   pin  11 A4             A4                           [net A4, 17 pins]
   pin  12 A3             A3                           [net A3, 17 pins]
   pin  13 A6             A6                           [net A6, 17 pins]
   pin  14 OUT            OUT0                         Z31.11 Z8.14(OUT)
   pin  15 ~{CAS}         ~{LOWER}                     R19.1(R1.1) Z10.15(~{CAS}) Z11.15(~{CAS}) Z12.15(~{CAS}) Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z9.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 227 pins]

Z17  (74LS00, Cassette Interface)
   pin   1                D0                           J10.11(Pin_11) J2.30(Pin_30) J3.30(Pin_30) Z31.8 Z31.9 Z47.4(D0) Z48.13(D4) Z50.6 Z50.7
   pin   2                Net-(Z17-Pad13)              Z17.13 Z32.4
   pin   3                Net-(Z17-Pad12)              Z17.12 Z17.4
   pin   4                Net-(Z17-Pad12)              Z17.12 Z17.3
   pin   5                Net-(Z17-Pad5)               Z17.8
   pin   6                Net-(Z18A-1A)                Z17.9 Z18.1(1A) Z18.2(1B)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8                Net-(Z17-Pad5)               Z17.5
   pin   9                Net-(Z18A-1A)                Z17.6 Z18.1(1A) Z18.2(1B)
   pin  10                Net-(Z17-Pad10)              Z17.11
   pin  11                Net-(Z17-Pad10)              Z17.10
   pin  12                Net-(Z17-Pad12)              Z17.3 Z17.4
   pin  13                Net-(Z17-Pad13)              Z17.2 Z32.4
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z18  (75452, Cassette Interface)
   pin   1 1A             Net-(Z18A-1A)                Z17.6 Z17.9 Z18.2(1B)
   pin   2 1B             Net-(Z18A-1A)                Z17.6 Z17.9 Z18.1(1A)
   pin   3 1Y             Net-(CR1-A)                  CR1.2(A) K1.13
   pin   4 GND            GND                          [net GND, 227 pins]
   pin   5 2Y             unconnected-(Z18B-2Y-Pad5)   (no other connection)
   pin   6 2A             unconnected-(Z18B-2A-Pad6)   (no other connection)
   pin   7 2B             unconnected-(Z18B-2B-Pad7)   (no other connection)
   pin   8 VCC            +5V                          [net +5V, 105 pins]

Z19  (4049B, Clock)
   pin   1 VCC            +5V                          [net +5V, 105 pins]
   pin   2                unconnected-(Z19-Pad2)       (no other connection)
   pin   3                unconnected-(Z19-Pad3)       (no other connection)
   pin   4                unconnected-(Z19-Pad4)       (no other connection)
   pin   5                unconnected-(Z19-Pad5)       (no other connection)
   pin   6                unconnected-(Z19-Pad6)       (no other connection)
   pin   7                unconnected-(Z19-Pad7)       (no other connection)
   pin   8 VSS            GND                          [net GND, 227 pins]
   pin   9                unconnected-(Z19-Pad9)       (no other connection)
   pin  10                unconnected-(Z19-Pad10)      (no other connection)
   pin  11                Net-(C43-Pad2)               C43.2 R1.1 Y1.1(1)
   pin  12                Net-(R1-Pad2)                R1.2 R2.2 Z19.14
   pin  14                Net-(R1-Pad2)                R1.2 R2.2 Z19.12
   pin  15                Net-(Z22-CP0)                Z22.14(CP0)

Z20  (LM723C, Power)
   pin   1 NC             unconnected-(Z20-NC-Pad1)    (no other connection)
   pin   2 ILIM           Net-(Z20-ILIM)               R11.1 R6.1
   pin   3 CSEN           +12V                         [net +12V, 41 pins]
   pin   4 -              Net-(Z20--)                  C50.2 R7.2(2)
   pin   5 +              Net-(Z20-+)                  Z20.6(VREF)
   pin   6 VREF           Net-(Z20-+)                  Z20.5(+)
   pin   7 V-             GND                          [net GND, 227 pins]
   pin   8 NC             unconnected-(Z20-NC-Pad8)    (no other connection)
   pin   9 VZ             unconnected-(Z20-VZ-Pad9)    (no other connection)
   pin  10 Vout           Net-(Q1-C)                   Q1.2(C) R35.2 R6.2
   pin  11 VC             Net-(Q1-B)                   Q1.1(B) R4.2
   pin  12 V+             Net-(Q1-E)                   C55.1 Q1.3(E) R4.1 S1.7
   pin  13 FC             Net-(Z20-FC)                 C50.1
   pin  14 NC             unconnected-(Z20-NC-Pad14)   (no other connection)

Z21  (LM723C, Power)
   pin   1 NC             unconnected-(Z21-NC-Pad1)    (no other connection)
   pin   2 ILIM           Net-(Z21-ILIM)               R14.1 R17.2
   pin   3 CSEN           +5V                          [net +5V, 105 pins]
   pin   4 -              +5V                          [net +5V, 105 pins]
   pin   5 +              Net-(Z21-+)                  R8.2(2)
   pin   6 VREF           Net-(Z21-VREF)               R15.2
   pin   7 V-             GND                          [net GND, 227 pins]
   pin   8 NC             unconnected-(Z21-NC-Pad8)    (no other connection)
   pin   9 VZ             unconnected-(Z21-VZ-Pad9)    (no other connection)
   pin  10 Vout           Net-(Q3-B)                   Q3.2(B) R17.1
   pin  11 VC             +12V                         [net +12V, 41 pins]
   pin  12 V+             +12V                         [net +12V, 41 pins]
   pin  13 FC             Net-(Z21-FC)                 C53.2
   pin  14 NC             unconnected-(Z21-NC-Pad14)   (no other connection)

Z22  (74LS90, Clock)
   pin   1 CP1..3         Net-(Z22-CP1..3)             Z22.12(Q0) Z25.3(C)
   pin   2 R0(1)          GND                          [net GND, 227 pins]
   pin   3 R0(2)          GND                          [net GND, 227 pins]
   pin   5 VCC            +5V                          [net +5V, 105 pins]
   pin   6 R9(1)          GND                          [net GND, 227 pins]
   pin   7 R9(2)          GND                          [net GND, 227 pins]
   pin   8 Q2             unconnected-(Z22-Q2-Pad8)    (no other connection)
   pin   9 Q1             unconnected-(Z22-Q1-Pad9)    (no other connection)
   pin  10 GND            GND                          [net GND, 227 pins]
   pin  11 Q3             CLK/10                       R3.1 Z23.2(Enable)
   pin  12 Q0             Net-(Z22-CP1..3)             Z22.1(CP1..3) Z25.3(C)
   pin  14 CP0            Net-(Z22-CP0)                Z19.15

Z23  (4518, Timer)
   pin   1 CK             GND                          [net GND, 227 pins]
   pin   2 Enable         CLK/10                       R3.1 Z22.11(Q3)
   pin   3 Q1             unconnected-(Z23A-Q1-Pad3)   (no other connection)
   pin   4 Q2             unconnected-(Z23A-Q2-Pad4)   (no other connection)
   pin   5 Q3             unconnected-(Z23A-Q3-Pad5)   (no other connection)
   pin   6 Q4             Net-(Z23A-Q4)                Z23.10(Enable)
   pin   7 Reset          GND                          [net GND, 227 pins]
   pin   8 VSS            GND                          [net GND, 227 pins]
   pin   9 CK             GND                          [net GND, 227 pins]
   pin  10 Enable         Net-(Z23A-Q4)                Z23.6(Q4)
   pin  11 Q1             unconnected-(Z23B-Q1-Pad11)  (no other connection)
   pin  12 Q2             unconnected-(Z23B-Q2-Pad12)  (no other connection)
   pin  13 Q3             unconnected-(Z23B-Q3-Pad13)  (no other connection)
   pin  14 Q4             Net-(Z23B-Q4)                Z24.2(Enable)
   pin  15 Reset          GND                          [net GND, 227 pins]
   pin  16 VDD            +5V                          [net +5V, 105 pins]

Z24  (4518, Timer)
   pin   1 CK             GND                          [net GND, 227 pins]
   pin   2 Enable         Net-(Z23B-Q4)                Z23.14(Q4)
   pin   3 Q1             unconnected-(Z24A-Q1-Pad3)   (no other connection)
   pin   4 Q2             unconnected-(Z24A-Q2-Pad4)   (no other connection)
   pin   5 Q3             unconnected-(Z24A-Q3-Pad5)   (no other connection)
   pin   6 Q4             Net-(Z24A-Q4)                Z24.10(Enable)
   pin   7 Reset          GND                          [net GND, 227 pins]
   pin   8 VSS            GND                          [net GND, 227 pins]
   pin   9 CK             GND                          [net GND, 227 pins]
   pin  10 Enable         Net-(Z24A-Q4)                Z24.6(Q4)
   pin  11 Q1             unconnected-(Z24B-Q1-Pad11)  (no other connection)
   pin  12 Q2             unconnected-(Z24B-Q2-Pad12)  (no other connection)
   pin  13 Q3             unconnected-(Z24B-Q3-Pad13)  (no other connection)
   pin  14 Q4             Net-(Z24B-Q4)                Z26.3(C)
   pin  15 Reset          GND                          [net GND, 227 pins]
   pin  16 VDD            +5V                          [net +5V, 105 pins]

Z25  (74LS74, Clock)
   pin   1 ~{R}           HI1                          R16.1 Z25.4(~{S}) Z26.1(~{R}) Z26.13(~{R})
   pin   2 D              ~{CLK/2}                     Z25.6(~{Q}) Z42.24(CLK)
   pin   3 C              Net-(Z22-CP1..3)             Z22.1(CP1..3) Z22.12(Q0)
   pin   4 ~{S}           HI1                          R16.1 Z25.1(~{R}) Z26.1(~{R}) Z26.13(~{R})
   pin   5 Q              unconnected-(Z25A-Q-Pad5)    (no other connection)
   pin   6 ~{Q}           ~{CLK/2}                     Z25.2(D) Z42.24(CLK)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8 ~{Q}           unconnected-(Z25B-~{Q}-Pad8) (no other connection)
   pin   9 Q              unconnected-(Z25B-Q-Pad9)    (no other connection)
   pin  10 ~{S}           GND                          [net GND, 227 pins]
   pin  11 C              unconnected-(Z25B-C-Pad11)   (no other connection)
   pin  12 D              unconnected-(Z25B-D-Pad12)   (no other connection)
   pin  13 ~{R}           GND                          [net GND, 227 pins]
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z26  (74LS74, Timer)
   pin   1 ~{R}           HI1                          R16.1 Z25.1(~{R}) Z25.4(~{S}) Z26.13(~{R})
   pin   2 D              GND                          [net GND, 227 pins]
   pin   3 C              Net-(Z24B-Q4)                Z24.14(Q4)
   pin   4 ~{S}           ~{37E0_READ}                 Z26.11(C) Z39.7(Q0a) Z49.15
   pin   5 Q              Net-(Z26A-Q)                 Z26.10(~{S})
   pin   6 ~{Q}           unconnected-(Z26A-~{Q}-Pad6) (no other connection)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8 ~{Q}           unconnected-(Z26B-~{Q}-Pad8) (no other connection)
   pin   9 Q              ~{INTRQ}                     Z34.13 Z49.12
   pin  10 ~{S}           Net-(Z26A-Q)                 Z26.5(Q)
   pin  11 C              ~{37E0_READ}                 Z26.4(~{S}) Z39.7(Q0a) Z49.15
   pin  12 D              GND                          [net GND, 227 pins]
   pin  13 ~{R}           HI1                          R16.1 Z25.1(~{R}) Z25.4(~{S}) Z26.1(~{R})
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z27  (74LS32, Memory Management)
   pin   1                ~{CAS}                       Z27.12 Z38.8(B3)
   pin   2                ~{32K}                       Z28.2 Z40.6(O2)
   pin   3                Net-(R18A-R1.2)              R18.2(R1.2) R19.2(R1.2)
   pin   4                ~{WR}                        J3.13(Pin_13) Z27.5 Z30.10(B1) Z39.15(Eb2)
   pin   5                ~{WR}                        J3.13(Pin_13) Z27.4 Z30.10(B1) Z39.15(Eb2)
   pin   6                Net-(R18C-R3.2)              R18.4(R3.2) R19.6(R3.2)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8                Net-(R18D-R4.2)              R18.5(R4.2) R19.8(R4.2)
   pin   9                ~{RAS}                       Z27.10 Z38.9(B2) Z40.1(E)
   pin  10                ~{RAS}                       Z27.9 Z38.9(B2) Z40.1(E)
   pin  11                Net-(R18B-R2.2)              R18.3(R2.2) R19.4(R2.2)
   pin  12                ~{CAS}                       Z27.1 Z38.8(B3)
   pin  13                ~{48K}                       Z28.1 Z40.7(O3)
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z28  (74LS00, Internal Expansion)
   pin   1                ~{48K}                       Z27.13 Z40.7(O3)
   pin   2                ~{32K}                       Z27.2 Z40.6(O2)
   pin   3                Net-(Z28-Pad3)               Z28.4
   pin   4                Net-(Z28-Pad3)               Z28.3
   pin   5                Net-(Z28-Pad5)               Z32.2
   pin   6                Net-(Z28-Pad6)               Z29.19 Z31.19
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8                ~{E8}                        J10.3(Pin_3)
   pin   9                Net-(R20-Pad2)               R20.2 Z41.2
   pin  10                Net-(Z28-Pad10)              Z28.11
   pin  11                Net-(Z28-Pad10)              Z28.10
   pin  12                A4                           J3.31(Pin_31) Z28.13 Z36.2(I0a) Z45.16(O1a)
   pin  13                A4                           J3.31(Pin_31) Z28.12 Z36.2(I0a) Z45.16(O1a)
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z29  (74LS244_Split, Memory Management)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                D7                           J10.5(Pin_5) J2.20(Pin_20) J3.20(Pin_20) Z29.3 Z48.8(D3) Z49.11 Z49.9 Z51.4 Z51.5
   pin   3                D7                           J10.5(Pin_5) J2.20(Pin_20) J3.20(Pin_20) Z29.2 Z48.8(D3) Z49.11 Z49.9 Z51.4 Z51.5
   pin   4                D6                           J10.4(Pin_4) J2.24(Pin_24) J3.24(Pin_24) Z29.5 Z48.7(D2) Z49.13 Z49.7 Z51.6 Z51.7
   pin   5                D6                           J10.4(Pin_4) J2.24(Pin_24) J3.24(Pin_24) Z29.4 Z48.7(D2) Z49.13 Z49.7 Z51.6 Z51.7
   pin   6                D5                           J10.8(Pin_8) J2.28(Pin_28) J3.28(Pin_28) Z29.7 Z48.4(D1) Z49.5 Z51.8 Z51.9
   pin   7                D5                           J10.8(Pin_8) J2.28(Pin_28) J3.28(Pin_28) Z29.6 Z48.4(D1) Z49.5 Z51.8 Z51.9
   pin   8                D4                           J10.7(Pin_7) J2.18(Pin_18) J3.18(Pin_18) Z29.9 Z48.3(D0) Z49.3 Z51.2 Z51.3
   pin   9                D4                           J10.7(Pin_7) J2.18(Pin_18) J3.18(Pin_18) Z29.8 Z48.3(D0) Z49.3 Z51.2 Z51.3
   pin  10 GND            GND                          [net GND, 227 pins]
   pin  11                OUT4                         Z12.14(OUT) Z4.14(OUT)
   pin  12                IN4                          Z12.2(IN) Z4.2(IN)
   pin  13                OUT5                         Z11.14(OUT) Z3.14(OUT)
   pin  14                IN5                          Z11.2(IN) Z3.2(IN)
   pin  15                OUT6                         Z10.14(OUT) Z2.14(OUT)
   pin  16                IN6                          Z10.2(IN) Z2.2(IN)
   pin  17                OUT7                         Z1.14(OUT) Z9.14(OUT)
   pin  18                IN7                          Z1.2(IN) Z9.2(IN)
   pin  19                Net-(Z28-Pad6)               Z28.6 Z31.19
   pin  20 VCC            +5V                          [net +5V, 105 pins]

Z30  (74LS243, Card-Edge Interface)
   pin   1 OEa            GND                          [net GND, 227 pins]
   pin   3 A0             unconnected-(Z30-A0-Pad3)    (no other connection)
   pin   4 A1             Net-(J2-Pin_13)              J2.13(Pin_13)
   pin   5 A2             Net-(J2-Pin_15)              J2.15(Pin_15)
   pin   6 A3             unconnected-(Z30-A3-Pad6)    (no other connection)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8 B3             unconnected-(Z30-B3-Pad8)    (no other connection)
   pin   9 B2             ~{RD}                        J3.15(Pin_15) Z32.1 Z32.5
   pin  10 B1             ~{WR}                        J3.13(Pin_13) Z27.4 Z27.5 Z39.15(Eb2)
   pin  11 B0             unconnected-(Z30-B0-Pad11)   (no other connection)
   pin  13 OEb            GND                          [net GND, 227 pins]
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z31  (74LS244_Split, Memory Management)
   pin   1                GND                          [net GND, 227 pins]
   pin   2                D3                           J10.12(Pin_12) J2.26(Pin_26) J3.26(Pin_26) Z31.3 Z47.13(D3) Z48.18(D7) Z50.4 Z50.5
   pin   3                D3                           J10.12(Pin_12) J2.26(Pin_26) J3.26(Pin_26) Z31.2 Z47.13(D3) Z48.18(D7) Z50.4 Z50.5
   pin   4                D2                           J10.13(Pin_13) J2.32(Pin_32) J3.32(Pin_32) Z31.5 Z47.12(D2) Z48.17(D6) Z50.8 Z50.9
   pin   5                D2                           J10.13(Pin_13) J2.32(Pin_32) J3.32(Pin_32) Z31.4 Z47.12(D2) Z48.17(D6) Z50.8 Z50.9
   pin   6                D1                           J10.14(Pin_14) J2.22(Pin_22) J3.22(Pin_22) Z31.7 Z47.5(D1) Z48.14(D5) Z50.2 Z50.3
   pin   7                D1                           J10.14(Pin_14) J2.22(Pin_22) J3.22(Pin_22) Z31.6 Z47.5(D1) Z48.14(D5) Z50.2 Z50.3
   pin   8                D0                           J10.11(Pin_11) J2.30(Pin_30) J3.30(Pin_30) Z17.1 Z31.9 Z47.4(D0) Z48.13(D4) Z50.6 Z50.7
   pin   9                D0                           J10.11(Pin_11) J2.30(Pin_30) J3.30(Pin_30) Z17.1 Z31.8 Z47.4(D0) Z48.13(D4) Z50.6 Z50.7
   pin  10 GND            GND                          [net GND, 227 pins]
   pin  11                OUT0                         Z16.14(OUT) Z8.14(OUT)
   pin  12                IN0                          Z16.2(IN) Z8.2(IN)
   pin  13                OUT1                         Z15.14(OUT) Z7.14(OUT)
   pin  14                IN1                          Z15.2(IN) Z7.2(IN)
   pin  15                OUT2                         Z14.14(OUT) Z6.14(OUT)
   pin  16                IN2                          Z14.2(IN) Z6.2(IN)
   pin  17                OUT3                         Z13.14(OUT) Z5.14(OUT)
   pin  18                IN3                          Z13.2(IN) Z5.2(IN)
   pin  19                Net-(Z28-Pad6)               Z28.6 Z29.19
   pin  20 VCC            +5V                          [net +5V, 105 pins]

Z32  (74LS04, Address Decoder)
   pin   1                ~{RD}                        J3.15(Pin_15) Z30.9(B2) Z32.5
   pin   2                Net-(Z28-Pad5)               Z28.5
   pin   3                ~{CSW}                       Z39.10(Q1b)
   pin   4                Net-(Z17-Pad13)              Z17.13 Z17.2
   pin   5                ~{RD}                        J3.15(Pin_15) Z30.9(B2) Z32.1
   pin   6                Net-(Z39-Ea1)                Z39.1(Ea1)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8                Net-(Z42-FDDATA)             Z42.27(FDDATA)
   pin   9                ~{READ_DATA}                 J5.30(Pin_30) R22.2
   pin  10                Net-(Z35-S)                  Z35.1(S) Z36.1(S)
   pin  11                MUX                          Z37.4(Tr2)
   pin  12                unconnected-(Z32-Pad12)      (no other connection)
   pin  13                unconnected-(Z32-Pad13)      (no other connection)
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z33  (74LS123, Line Printer)
   pin   1 A              GND                          [net GND, 227 pins]
   pin   2 B              ~{37E8_WRITE}                Z39.11(Q2b) Z48.11(Cp)
   pin   3 Clr            HI2                          R24.1 Z33.10(B) Z33.11(Clr)
   pin   4 ~{Q}           ~{DATA_STROBE}               J4.1(Pin_1)
   pin   5 Q              Net-(Z33B-Q)                 Z41.3 Z47.1(~{Mr})
   pin   6 Cext           GND                          [net GND, 227 pins]
   pin   7 RCext          Net-(Z33B-RCext)             C62.1 R25.1
   pin   8 GND            GND                          [net GND, 227 pins]
   pin   9 A              ~{37E0_WRITE}                Z39.9(Q0b) Z47.9(Cp)
   pin  10 B              HI2                          R24.1 Z33.11(Clr) Z33.3(Clr)
   pin  11 Clr            HI2                          R24.1 Z33.10(B) Z33.3(Clr)
   pin  12 ~{Q}           unconnected-(Z33B-~{Q}-Pad12) (no other connection)
   pin  13 Q              unconnected-(Z33A-Q-Pad13)   (no other connection)
   pin  14 Cext           GND                          [net GND, 227 pins]
   pin  15 RCext          Net-(Z33A-RCext)             C61.1 R23.2
   pin  16 VCC            +5V                          [net +5V, 105 pins]

Z34  (7416, )
   pin   1                Net-(Z42-~{PH2}/DIRC)        Z42.16(~{PH2}/DIRC)
   pin   2                ~{DIR_SEL}                   J5.18(Pin_18)
   pin   3                Net-(Z42-~{PH1}/STEP)        Z42.15(~{PH1}/STEP)
   pin   4                ~{STEP}                      J5.20(Pin_20)
   pin   5                Net-(Z42-WG)                 Z42.30(WG)
   pin   6                ~{WRITE_GATE}                J5.24(Pin_24)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8                ~{WRITE_DATA}                J5.22(Pin_22)
   pin   9                Net-(Z42-WD)                 Z42.31(WD)
   pin  10                ~{INT}                       J10.15(Pin_15) J2.21(Pin_21) J3.21(Pin_21) Z34.12
   pin  11                ~{INTRQ}                     R30.1 Z42.39(~{INTRQ}) Z49.14
   pin  12                ~{INT}                       J10.15(Pin_15) J2.21(Pin_21) J3.21(Pin_21) Z34.10
   pin  13                ~{INTRQ}                     Z26.9(Q) Z49.12
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z35  (74LS157, Memory Management)
   pin   1 S              Net-(Z35-S)                  Z32.10 Z36.1(S)
   pin   2 I0a            A0                           J10.10(Pin_10) J3.25(Pin_25) Z42.5(A0) Z45.18(O0a)
   pin   3 I1a            A7                           J3.36(Pin_36) Z43.11 Z45.7(O1b) Z46.13
   pin   4 Za             Net-(R26A-R1.2)              R26.2(R1.2)
   pin   5 I0b            A1                           J10.9(Pin_9) J3.27(Pin_27) Z42.6(A1) Z45.3(O3b)
   pin   6 I1b            A8                           J3.11(Pin_11) Z43.12 Z44.14(O2a)
   pin   7 Zb             Net-(R26C-R3.2)              R26.6(R3.2)
   pin   8 GND            GND                          [net GND, 227 pins]
   pin   9 Zc             Net-(R26D-R4.2)              R26.8(R4.2)
   pin  10 I1c            A9                           J3.17(Pin_17) Z43.4 Z44.12(O3a)
   pin  11 I0c            A2                           J10.17(Pin_17) J3.40(Pin_40) Z39.13(A0) Z45.9(O0b)
   pin  12 Zd             Net-(R26B-R2.2)              R26.4(R2.2)
   pin  13 I1d            A10                          J3.4(Pin_4) Z43.1 Z44.3(O3b)
   pin  14 I0d            A3                           J3.34(Pin_34) Z39.3(A1) Z45.5(O2b) Z46.12
   pin  15 E              GND                          [net GND, 227 pins]
   pin  16 VCC            +5V                          [net +5V, 105 pins]

Z36  (74LS157, Memory Management)
   pin   1 S              Net-(Z35-S)                  Z32.10 Z35.1(S)
   pin   2 I0a            A4                           J3.31(Pin_31) Z28.12 Z28.13 Z45.16(O1a)
   pin   3 I1a            A11                          J3.9(Pin_9) Z40.13(A1) Z44.16(O1a)
   pin   4 Za             Net-(R27A-R1.2)              R27.2(R1.2)
   pin   5 I0b            A5                           J3.35(Pin_35) Z43.5 Z45.14(O2a) Z46.10
   pin   6 I1b            A12                          J3.5(Pin_5) Z43.3 Z44.7(O1b)
   pin   7 Zb             Net-(R27C-R3.2)              R27.6(R3.2)
   pin   8 GND            GND                          [net GND, 227 pins]
   pin   9 Zc             Net-(R27D-R4.2)              R27.8(R4.2)
   pin  10 I1c            A13                          J3.6(Pin_6) Z43.2 Z44.5(O2b)
   pin  11 I0c            A6                           J3.38(Pin_38) Z43.6 Z45.12(O3a) Z46.9
   pin  12 Zd             unconnected-(Z36-Zd-Pad12)   (no other connection)
   pin  13 I1d            unconnected-(Z36-I1d-Pad13)  (no other connection)
   pin  14 I0d            unconnected-(Z36-I0d-Pad14)  (no other connection)
   pin  15 E              GND                          [net GND, 227 pins]
   pin  16 VCC            +5V                          [net +5V, 105 pins]

Z37  (DDU-4-7835, Card-Edge Interface)
   pin   1 Input          Net-(Z37-Input)              Z38.11(B0)
   pin   4 Tr2            MUX                          Z32.11
   pin   6 Tr3            Net-(Z37-Tr3)                Z38.6(A3)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin  12 Tr1            Net-(Z37-Tr1)                Z38.5(A2)
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z38  (74LS243, Card-Edge Interface)
   pin   1 OEa            GND                          [net GND, 227 pins]
   pin   3 A0             ~{M1_RAS}                    J2.1(Pin_1)
   pin   4 A1             unconnected-(Z38-A1-Pad4)    (no other connection)
   pin   5 A2             Net-(Z37-Tr1)                Z37.12(Tr1)
   pin   6 A3             Net-(Z37-Tr3)                Z37.6(Tr3)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8 B3             ~{CAS}                       Z27.1 Z27.12
   pin   9 B2             ~{RAS}                       Z27.10 Z27.9 Z40.1(E)
   pin  10 B1             unconnected-(Z38-B1-Pad10)   (no other connection)
   pin  11 B0             Net-(Z37-Input)              Z37.1(Input)
   pin  13 OEb            GND                          [net GND, 227 pins]
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z39  (74LS155, Address Decoder)
   pin   1 Ea1            Net-(Z39-Ea1)                Z32.6
   pin   2 Ea2            Net-(Z39-Ea2)                Z39.14(Eb1) Z40.12(O0)
   pin   3 A1             A3                           J3.34(Pin_34) Z35.14(I0d) Z45.5(O2b) Z46.12
   pin   4 Q3a            ~{37EC_READ}                 Z42.4(~{RE}) Z50.19 Z51.19
   pin   5 Q2a            ~{37E8_READ}                 Z49.1
   pin   6 Q1a            unconnected-(Z39-Q1a-Pad6)   (no other connection)
   pin   7 Q0a            ~{37E0_READ}                 Z26.11(C) Z26.4(~{S}) Z49.15
   pin   8 GND            GND                          [net GND, 227 pins]
   pin   9 Q0b            ~{37E0_WRITE}                Z33.9(A) Z47.9(Cp)
   pin  10 Q1b            ~{CSW}                       Z32.3
   pin  11 Q2b            ~{37E8_WRITE}                Z33.2(B) Z48.11(Cp)
   pin  12 Q3b            ~{37EC_WRITE}                Z42.2(~{WE}) Z50.1 Z51.1
   pin  13 A0             A2                           J10.17(Pin_17) J3.40(Pin_40) Z35.11(I0c) Z45.9(O0b)
   pin  14 Eb1            Net-(Z39-Ea2)                Z39.2(Ea2) Z40.12(O0)
   pin  15 Eb2            ~{WR}                        J3.13(Pin_13) Z27.4 Z27.5 Z30.10(B1)
   pin  16 VCC            +5V                          [net +5V, 105 pins]

Z40  (74LS139, Address Decoder)
   pin   1 E              ~{RAS}                       Z27.10 Z27.9 Z38.9(B2)
   pin   2 A0             A14                          J3.10(Pin_10) Z44.18(O0a)
   pin   3 A1             A15                          J3.7(Pin_7) Z44.9(O0b)
   pin   4 O0             Net-(Z40A-O0)                Z40.15(E)
   pin   5 O1             unconnected-(Z40A-O1-Pad5)   (no other connection)
   pin   6 O2             ~{32K}                       Z27.2 Z28.2
   pin   7 O3             ~{48K}                       Z27.13 Z28.1
   pin   8 GND            GND                          [net GND, 227 pins]
   pin   9 O3             unconnected-(Z40B-O3-Pad9)   (no other connection)
   pin  10 O2             unconnected-(Z40B-O2-Pad10)  (no other connection)
   pin  11 O1             unconnected-(Z40B-O1-Pad11)  (no other connection)
   pin  12 O0             Net-(Z39-Ea2)                Z39.14(Eb1) Z39.2(Ea2)
   pin  13 A1             A11                          J3.9(Pin_9) Z36.3(I1a) Z44.16(O1a)
   pin  14 A0             Net-(Z40B-A0)                Z43.8
   pin  15 E              Net-(Z40A-O0)                Z40.4(O0)
   pin  16 VCC            +5V                          [net +5V, 105 pins]

Z41  (7416, Internal Expansion)
   pin   1                Net-(Z41-Pad1)               Z46.8
   pin   2                Net-(R20-Pad2)               R20.2 Z28.9
   pin   3                Net-(Z33B-Q)                 Z33.5(Q) Z47.1(~{Mr})
   pin   4                ~{MOTOR_ON}                  J5.16(Pin_16)
   pin   5                Net-(Z47-Q1)                 Z47.7(Q1)
   pin   6                ~{DS1}                       J5.12(Pin_12)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8                ~{DS0}                       J5.10(Pin_10)
   pin   9                Net-(Z47-Q0)                 Z47.2(Q0)
   pin  10                ~{DS2}                       J5.14(Pin_14)
   pin  11                Net-(Z47-Q2)                 Z47.10(Q2)
   pin  12                ~{DS3}                       J5.32(Pin_32)
   pin  13                Net-(Z47-Q3)                 Z47.15(Q3)
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z42  (FD1771, Floppy Controller)
   pin   1 VBB            -5V                          [net -5V, 38 pins]
   pin   2 ~{WE}          ~{37EC_WRITE}                Z39.12(Q3b) Z50.1 Z51.1
   pin   3 ~{CS}          GND                          [net GND, 227 pins]
   pin   4 ~{RE}          ~{37EC_READ}                 Z39.4(Q3a) Z50.19 Z51.19
   pin   5 A0             A0                           J10.10(Pin_10) J3.25(Pin_25) Z35.2(I0a) Z45.18(O0a)
   pin   6 A1             A1                           J10.9(Pin_9) J3.27(Pin_27) Z35.5(I0b) Z45.3(O3b)
   pin   7 DI0            Net-(Z42-DI0)                Z50.13 Z50.14
   pin   8 DI1            Net-(Z42-DI1)                Z50.17 Z50.18
   pin   9 DI2            Net-(Z42-DI2)                Z50.11 Z50.12
   pin  10 DI3            Net-(Z42-DI3)                Z50.15 Z50.16
   pin  11 DI4            Net-(Z42-DI4)                Z51.17 Z51.18
   pin  12 DI5            Net-(Z42-DI5)                Z51.11 Z51.12
   pin  13 DI6            Net-(Z42-DI6)                Z51.13 Z51.14
   pin  14 DI7            Net-(Z42-DI7)                Z51.15 Z51.16
   pin  15 ~{PH1}/STEP    Net-(Z42-~{PH1}/STEP)        Z34.3
   pin  16 ~{PH2}/DIRC    Net-(Z42-~{PH2}/DIRC)        Z34.1
   pin  17 PH3            unconnected-(Z42-PH3-Pad17)  (no other connection)
   pin  18 ~{3PM}         Net-(Z42-FDCLK)              R29.1 Z42.22(~{TEST}) Z42.25(~{XTDS}) Z42.26(FDCLK) Z42.33(~{WF}) Z42.37(~{DINT})
   pin  19 ~{MR}          ~{SYSRES}                    J10.6(Pin_6) J2.2(Pin_2) J3.2(Pin_2) R28.1
   pin  20 GND            GND                          [net GND, 227 pins]
   pin  21 VCC            +5V                          [net +5V, 105 pins]
   pin  22 ~{TEST}        Net-(Z42-FDCLK)              R29.1 Z42.18(~{3PM}) Z42.25(~{XTDS}) Z42.26(FDCLK) Z42.33(~{WF}) Z42.37(~{DINT})
   pin  23 HLT            Net-(Z42-HLT)                Z42.32(READY) Z46.6
   pin  24 CLK            ~{CLK/2}                     Z25.2(D) Z25.6(~{Q})
   pin  25 ~{XTDS}        Net-(Z42-FDCLK)              R29.1 Z42.18(~{3PM}) Z42.22(~{TEST}) Z42.26(FDCLK) Z42.33(~{WF}) Z42.37(~{DINT})
   pin  26 FDCLK          Net-(Z42-FDCLK)              R29.1 Z42.18(~{3PM}) Z42.22(~{TEST}) Z42.25(~{XTDS}) Z42.33(~{WF}) Z42.37(~{DINT})
   pin  27 FDDATA         Net-(Z42-FDDATA)             Z32.8
   pin  29 TG43           unconnected-(Z42-TG43-Pad29) (no other connection)
   pin  30 WG             Net-(Z42-WG)                 Z34.5
   pin  31 WD             Net-(Z42-WD)                 Z34.9
   pin  32 READY          Net-(Z42-HLT)                Z42.23(HLT) Z46.6
   pin  33 ~{WF}          Net-(Z42-FDCLK)              R29.1 Z42.18(~{3PM}) Z42.22(~{TEST}) Z42.25(~{XTDS}) Z42.26(FDCLK) Z42.37(~{DINT})
   pin  34 ~{TR00}        ~{TRACK_ZERO}                J5.26(Pin_26) R33.2
   pin  35 ~{IP}          ~{INDEX_PULSE}               J5.8(Pin_8) R32.2
   pin  36 ~{WPRT}        ~{WRITE_PROTECT}             J5.28(Pin_28) R31.2
   pin  37 ~{DINT}        Net-(Z42-FDCLK)              R29.1 Z42.18(~{3PM}) Z42.22(~{TEST}) Z42.25(~{XTDS}) Z42.26(FDCLK) Z42.33(~{WF})
   pin  38 DRQ            unconnected-(Z42-DRQ-Pad38)  (no other connection)
   pin  39 ~{INTRQ}       ~{INTRQ}                     R30.1 Z34.11 Z49.14
   pin  40 VDD            +12V                         [net +12V, 41 pins]

Z43  (74LS30, Address Decoder)
   pin   1                A10                          J3.4(Pin_4) Z35.13(I1d) Z44.3(O3b)
   pin   2                A13                          J3.6(Pin_6) Z36.10(I1c) Z44.5(O2b)
   pin   3                A12                          J3.5(Pin_5) Z36.6(I1b) Z44.7(O1b)
   pin   4                A9                           J3.17(Pin_17) Z35.10(I1c) Z44.12(O3a)
   pin   5                A5                           J3.35(Pin_35) Z36.5(I0b) Z45.14(O2a) Z46.10
   pin   6                A6                           J3.38(Pin_38) Z36.11(I0c) Z45.12(O3a) Z46.9
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8                Net-(Z40B-A0)                Z40.14(A0)
   pin  11                A7                           J3.36(Pin_36) Z35.3(I1a) Z45.7(O1b) Z46.13
   pin  12                A8                           J3.11(Pin_11) Z35.6(I1b) Z44.14(O2a)
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z44  (74LS244, Card-Edge Interface)
   pin   1 OEa            GND                          [net GND, 227 pins]
   pin   2 I0a            M1_A14                       J2.10(Pin_10)
   pin   3 O3b            A10                          J3.4(Pin_4) Z35.13(I1d) Z43.1
   pin   4 I1a            M1_A11                       J2.9(Pin_9)
   pin   5 O2b            A13                          J3.6(Pin_6) Z36.10(I1c) Z43.2
   pin   6 I2a            M1_A8                        J2.11(Pin_11)
   pin   7 O1b            A12                          J3.5(Pin_5) Z36.6(I1b) Z43.3
   pin   8 I3a            M1_A9                        J2.17(Pin_17)
   pin   9 O0b            A15                          J3.7(Pin_7) Z40.3(A1)
   pin  10 GND            GND                          [net GND, 227 pins]
   pin  11 I0b            M1_A15                       J2.7(Pin_7)
   pin  12 O3a            A9                           J3.17(Pin_17) Z35.10(I1c) Z43.4
   pin  13 I1b            M1_A12                       J2.5(Pin_5)
   pin  14 O2a            A8                           J3.11(Pin_11) Z35.6(I1b) Z43.12
   pin  15 I2b            M1_A13                       J2.6(Pin_6)
   pin  16 O1a            A11                          J3.9(Pin_9) Z36.3(I1a) Z40.13(A1)
   pin  17 I3b            M1_A10                       J2.4(Pin_4)
   pin  18 O0a            A14                          J3.10(Pin_10) Z40.2(A0)
   pin  19 OEb            GND                          [net GND, 227 pins]
   pin  20 VCC            +5V                          [net +5V, 105 pins]

Z45  (74LS244, Card-Edge Interface)
   pin   1 OEa            GND                          [net GND, 227 pins]
   pin   2 I0a            M1_A0                        J2.25(Pin_25)
   pin   3 O3b            A1                           J10.9(Pin_9) J3.27(Pin_27) Z35.5(I0b) Z42.6(A1)
   pin   4 I1a            M1_A4                        J2.31(Pin_31)
   pin   5 O2b            A3                           J3.34(Pin_34) Z35.14(I0d) Z39.3(A1) Z46.12
   pin   6 I2a            M1_A5                        J2.35(Pin_35)
   pin   7 O1b            A7                           J3.36(Pin_36) Z35.3(I1a) Z43.11 Z46.13
   pin   8 I3a            M1_A6                        J2.38(Pin_38)
   pin   9 O0b            A2                           J10.17(Pin_17) J3.40(Pin_40) Z35.11(I0c) Z39.13(A0)
   pin  10 GND            GND                          [net GND, 227 pins]
   pin  11 I0b            M1_A2                        J2.40(Pin_40)
   pin  12 O3a            A6                           J3.38(Pin_38) Z36.11(I0c) Z43.6 Z46.9
   pin  13 I1b            M1_A7                        J2.36(Pin_36)
   pin  14 O2a            A5                           J3.35(Pin_35) Z36.5(I0b) Z43.5 Z46.10
   pin  15 I2b            M1_A3                        J2.34(Pin_34)
   pin  16 O1a            A4                           J3.31(Pin_31) Z28.12 Z28.13 Z36.2(I0a)
   pin  17 I3b            M1_A1                        J2.27(Pin_27)
   pin  18 O0a            A0                           J10.10(Pin_10) J3.25(Pin_25) Z35.2(I0a) Z42.5(A0)
   pin  19 OEb            GND                          [net GND, 227 pins]
   pin  20 VCC            +5V                          [net +5V, 105 pins]

Z46  (74LS20, Internal Expansion)
   pin   1                Net-(Z47-~{Q0})              Z47.3(~{Q0})
   pin   2                Net-(Z47-~{Q3})              Z47.14(~{Q3})
   pin   4                Net-(Z47-~{Q1})              Z47.6(~{Q1})
   pin   5                Net-(Z47-~{Q2})              Z47.11(~{Q2})
   pin   6                Net-(Z42-HLT)                Z42.23(HLT) Z42.32(READY)
   pin   7 GND            GND                          [net GND, 227 pins]
   pin   8                Net-(Z41-Pad1)               Z41.1
   pin   9                A6                           J3.38(Pin_38) Z36.11(I0c) Z43.6 Z45.12(O3a)
   pin  10                A5                           J3.35(Pin_35) Z36.5(I0b) Z43.5 Z45.14(O2a)
   pin  12                A3                           J3.34(Pin_34) Z35.14(I0d) Z39.3(A1) Z45.5(O2b)
   pin  13                A7                           J3.36(Pin_36) Z35.3(I1a) Z43.11 Z45.7(O1b)
   pin  14 VCC            +5V                          [net +5V, 105 pins]

Z47  (74LS175, Floppy Controller)
   pin   1 ~{Mr}          Net-(Z33B-Q)                 Z33.5(Q) Z41.3
   pin   2 Q0             Net-(Z47-Q0)                 Z41.9
   pin   3 ~{Q0}          Net-(Z47-~{Q0})              Z46.1
   pin   4 D0             D0                           J10.11(Pin_11) J2.30(Pin_30) J3.30(Pin_30) Z17.1 Z31.8 Z31.9 Z48.13(D4) Z50.6 Z50.7
   pin   5 D1             D1                           J10.14(Pin_14) J2.22(Pin_22) J3.22(Pin_22) Z31.6 Z31.7 Z48.14(D5) Z50.2 Z50.3
   pin   6 ~{Q1}          Net-(Z47-~{Q1})              Z46.4
   pin   7 Q1             Net-(Z47-Q1)                 Z41.5
   pin   8 GND            GND                          [net GND, 227 pins]
   pin   9 Cp             ~{37E0_WRITE}                Z33.9(A) Z39.9(Q0b)
   pin  10 Q2             Net-(Z47-Q2)                 Z41.11
   pin  11 ~{Q2}          Net-(Z47-~{Q2})              Z46.5
   pin  12 D2             D2                           J10.13(Pin_13) J2.32(Pin_32) J3.32(Pin_32) Z31.4 Z31.5 Z48.17(D6) Z50.8 Z50.9
   pin  13 D3             D3                           J10.12(Pin_12) J2.26(Pin_26) J3.26(Pin_26) Z31.2 Z31.3 Z48.18(D7) Z50.4 Z50.5
   pin  14 ~{Q3}          Net-(Z47-~{Q3})              Z46.2
   pin  15 Q3             Net-(Z47-Q3)                 Z41.13
   pin  16 VCC            +5V                          [net +5V, 105 pins]

Z48  (74LS273, Line Printer)
   pin   1 ~{Mr}          Net-(Z48-~{Mr})              R34.2
   pin   2 Q0             DATA5                        J4.11(Pin_11)
   pin   3 D0             D4                           J10.7(Pin_7) J2.18(Pin_18) J3.18(Pin_18) Z29.8 Z29.9 Z49.3 Z51.2 Z51.3
   pin   4 D1             D5                           J10.8(Pin_8) J2.28(Pin_28) J3.28(Pin_28) Z29.6 Z29.7 Z49.5 Z51.8 Z51.9
   pin   5 Q1             DATA6                        J4.13(Pin_13)
   pin   6 Q2             DATA7                        J4.15(Pin_15)
   pin   7 D2             D6                           J10.4(Pin_4) J2.24(Pin_24) J3.24(Pin_24) Z29.4 Z29.5 Z49.13 Z49.7 Z51.6 Z51.7
   pin   8 D3             D7                           J10.5(Pin_5) J2.20(Pin_20) J3.20(Pin_20) Z29.2 Z29.3 Z49.11 Z49.9 Z51.4 Z51.5
   pin   9 Q3             DATA8                        J4.17(Pin_17)
   pin  10 GND            GND                          [net GND, 227 pins]
   pin  11 Cp             ~{37E8_WRITE}                Z33.2(B) Z39.11(Q2b)
   pin  12 Q4             DATA1                        J4.3(Pin_3)
   pin  13 D4             D0                           J10.11(Pin_11) J2.30(Pin_30) J3.30(Pin_30) Z17.1 Z31.8 Z31.9 Z47.4(D0) Z50.6 Z50.7
   pin  14 D5             D1                           J10.14(Pin_14) J2.22(Pin_22) J3.22(Pin_22) Z31.6 Z31.7 Z47.5(D1) Z50.2 Z50.3
   pin  15 Q5             DATA2                        J4.5(Pin_5)
   pin  16 Q6             DATA3                        J4.7(Pin_7)
   pin  17 D6             D2                           J10.13(Pin_13) J2.32(Pin_32) J3.32(Pin_32) Z31.4 Z31.5 Z47.12(D2) Z50.8 Z50.9
   pin  18 D7             D3                           J10.12(Pin_12) J2.26(Pin_26) J3.26(Pin_26) Z31.2 Z31.3 Z47.13(D3) Z50.4 Z50.5
   pin  19 Q7             DATA4                        J4.9(Pin_9)
   pin  20 VCC            +5V                          [net +5V, 105 pins]

Z49  (74LS367, )
   pin   1                ~{37E8_READ}                 Z39.5(Q2a)
   pin   2                ~{FAULT}                     J4.28(Pin_28)
   pin   3                D4                           J10.7(Pin_7) J2.18(Pin_18) J3.18(Pin_18) Z29.8 Z29.9 Z48.3(D0) Z51.2 Z51.3
   pin   4                ~{UNIT_SELECT}               J4.25(Pin_25)
   pin   5                D5                           J10.8(Pin_8) J2.28(Pin_28) J3.28(Pin_28) Z29.6 Z29.7 Z48.4(D1) Z51.8 Z51.9
   pin   6                ~{OUT_OF_PAPER}              J4.23(Pin_23)
   pin   7                D6                           J10.4(Pin_4) J2.24(Pin_24) J3.24(Pin_24) Z29.4 Z29.5 Z48.7(D2) Z49.13 Z51.6 Z51.7
   pin   8 GND            GND                          [net GND, 227 pins]
   pin   9                D7                           J10.5(Pin_5) J2.20(Pin_20) J3.20(Pin_20) Z29.2 Z29.3 Z48.8(D3) Z49.11 Z51.4 Z51.5
   pin  10                ~{BUSY}                      J4.21(Pin_21)
   pin  11                D7                           J10.5(Pin_5) J2.20(Pin_20) J3.20(Pin_20) Z29.2 Z29.3 Z48.8(D3) Z49.9 Z51.4 Z51.5
   pin  12                ~{INTRQ}                     Z26.9(Q) Z34.13
   pin  13                D6                           J10.4(Pin_4) J2.24(Pin_24) J3.24(Pin_24) Z29.4 Z29.5 Z48.7(D2) Z49.7 Z51.6 Z51.7
   pin  14                ~{INTRQ}                     R30.1 Z34.11 Z42.39(~{INTRQ})
   pin  15                ~{37E0_READ}                 Z26.11(C) Z26.4(~{S}) Z39.7(Q0a)
   pin  16 VCC            +5V                          [net +5V, 105 pins]

Z50  (74LS240_Split, Floppy Controller)
   pin   1                ~{37EC_WRITE}                Z39.12(Q3b) Z42.2(~{WE}) Z51.1
   pin   2                D1                           J10.14(Pin_14) J2.22(Pin_22) J3.22(Pin_22) Z31.6 Z31.7 Z47.5(D1) Z48.14(D5) Z50.3
   pin   3                D1                           J10.14(Pin_14) J2.22(Pin_22) J3.22(Pin_22) Z31.6 Z31.7 Z47.5(D1) Z48.14(D5) Z50.2
   pin   4                D3                           J10.12(Pin_12) J2.26(Pin_26) J3.26(Pin_26) Z31.2 Z31.3 Z47.13(D3) Z48.18(D7) Z50.5
   pin   5                D3                           J10.12(Pin_12) J2.26(Pin_26) J3.26(Pin_26) Z31.2 Z31.3 Z47.13(D3) Z48.18(D7) Z50.4
   pin   6                D0                           J10.11(Pin_11) J2.30(Pin_30) J3.30(Pin_30) Z17.1 Z31.8 Z31.9 Z47.4(D0) Z48.13(D4) Z50.7
   pin   7                D0                           J10.11(Pin_11) J2.30(Pin_30) J3.30(Pin_30) Z17.1 Z31.8 Z31.9 Z47.4(D0) Z48.13(D4) Z50.6
   pin   8                D2                           J10.13(Pin_13) J2.32(Pin_32) J3.32(Pin_32) Z31.4 Z31.5 Z47.12(D2) Z48.17(D6) Z50.9
   pin   9                D2                           J10.13(Pin_13) J2.32(Pin_32) J3.32(Pin_32) Z31.4 Z31.5 Z47.12(D2) Z48.17(D6) Z50.8
   pin  10 GND            GND                          [net GND, 227 pins]
   pin  11                Net-(Z42-DI2)                Z42.9(DI2) Z50.12
   pin  12                Net-(Z42-DI2)                Z42.9(DI2) Z50.11
   pin  13                Net-(Z42-DI0)                Z42.7(DI0) Z50.14
   pin  14                Net-(Z42-DI0)                Z42.7(DI0) Z50.13
   pin  15                Net-(Z42-DI3)                Z42.10(DI3) Z50.16
   pin  16                Net-(Z42-DI3)                Z42.10(DI3) Z50.15
   pin  17                Net-(Z42-DI1)                Z42.8(DI1) Z50.18
   pin  18                Net-(Z42-DI1)                Z42.8(DI1) Z50.17
   pin  19                ~{37EC_READ}                 Z39.4(Q3a) Z42.4(~{RE}) Z51.19
   pin  20 VCC            +5V                          [net +5V, 105 pins]

Z51  (74LS240_Split, Floppy Controller)
   pin   1                ~{37EC_WRITE}                Z39.12(Q3b) Z42.2(~{WE}) Z50.1
   pin   2                D4                           J10.7(Pin_7) J2.18(Pin_18) J3.18(Pin_18) Z29.8 Z29.9 Z48.3(D0) Z49.3 Z51.3
   pin   3                D4                           J10.7(Pin_7) J2.18(Pin_18) J3.18(Pin_18) Z29.8 Z29.9 Z48.3(D0) Z49.3 Z51.2
   pin   4                D7                           J10.5(Pin_5) J2.20(Pin_20) J3.20(Pin_20) Z29.2 Z29.3 Z48.8(D3) Z49.11 Z49.9 Z51.5
   pin   5                D7                           J10.5(Pin_5) J2.20(Pin_20) J3.20(Pin_20) Z29.2 Z29.3 Z48.8(D3) Z49.11 Z49.9 Z51.4
   pin   6                D6                           J10.4(Pin_4) J2.24(Pin_24) J3.24(Pin_24) Z29.4 Z29.5 Z48.7(D2) Z49.13 Z49.7 Z51.7
   pin   7                D6                           J10.4(Pin_4) J2.24(Pin_24) J3.24(Pin_24) Z29.4 Z29.5 Z48.7(D2) Z49.13 Z49.7 Z51.6
   pin   8                D5                           J10.8(Pin_8) J2.28(Pin_28) J3.28(Pin_28) Z29.6 Z29.7 Z48.4(D1) Z49.5 Z51.9
   pin   9                D5                           J10.8(Pin_8) J2.28(Pin_28) J3.28(Pin_28) Z29.6 Z29.7 Z48.4(D1) Z49.5 Z51.8
   pin  10 GND            GND                          [net GND, 227 pins]
   pin  11                Net-(Z42-DI5)                Z42.12(DI5) Z51.12
   pin  12                Net-(Z42-DI5)                Z42.12(DI5) Z51.11
   pin  13                Net-(Z42-DI6)                Z42.13(DI6) Z51.14
   pin  14                Net-(Z42-DI6)                Z42.13(DI6) Z51.13
   pin  15                Net-(Z42-DI7)                Z42.14(DI7) Z51.16
   pin  16                Net-(Z42-DI7)                Z42.14(DI7) Z51.15
   pin  17                Net-(Z42-DI4)                Z42.11(DI4) Z51.18
   pin  18                Net-(Z42-DI4)                Z42.11(DI4) Z51.17
   pin  19                ~{37EC_READ}                 Z39.4(Q3a) Z42.4(~{RE}) Z50.19
   pin  20 VCC            +5V                          [net +5V, 105 pins]

```
## Nets

```
+12V   (41 pins)
    C11      0.1uF 50V          pin   1  
    C12      0.01uF 16V         pin   1  
    C14      0.01uF 16V         pin   1  
    C15      0.1uF 50V          pin   1  
    C17      0.1uF 50V          pin   1  
    C18      0.01uF 16V         pin   1  
    C20      0.01uF 16V         pin   1  
    C29      0.1uF 50V          pin   1  
    C31      0.1uF 50V          pin   1  
    C32      0.01uF 16V         pin   1  
    C34      0.01uF 16V         pin   1  
    C35      0.1uF 50V          pin   1  
    C37      0.1uF 50V          pin   1  
    C38      0.01uF 16V         pin   1  
    C40      0.01uF 16V         pin   1  
    C48      47uF               pin   1  
    C56      47uF 16V           pin   1  
    C71      0.1uF 50V          pin   1  
    C9       0.1uF 50V          pin   1  
    R35      5.6                pin   1  
    R5       2.2k               pin   1  
    Z1       MK4116             pin   8  VDD
    Z10      MK4116             pin   8  VDD
    Z11      MK4116             pin   8  VDD
    Z12      MK4116             pin   8  VDD
    Z13      MK4116             pin   8  VDD
    Z14      MK4116             pin   8  VDD
    Z15      MK4116             pin   8  VDD
    Z16      MK4116             pin   8  VDD
    Z2       MK4116             pin   8  VDD
    Z20      LM723C             pin   3  CSEN
    Z21      LM723C             pin  11  VC
    Z21      LM723C             pin  12  V+
    Z3       MK4116             pin   8  VDD
    Z4       MK4116             pin   8  VDD
    Z42      FD1771             pin  40  VDD
    Z5       MK4116             pin   8  VDD
    Z6       MK4116             pin   8  VDD
    Z7       MK4116             pin   8  VDD
    Z8       MK4116             pin   8  VDD
    Z9       MK4116             pin   8  VDD

+5V   (105 pins)
    C10      0.01uF 16V         pin   1  
    C13      0.1uF 50V          pin   1  
    C16      0.01uF 16V         pin   1  
    C19      0.1uF 50V          pin   1  
    C30      0.01uF 16V         pin   1  
    C33      0.1uF 50V          pin   1  
    C36      0.01uF 16V         pin   1  
    C39      0.1uF 50V          pin   1  
    C41      0.1uF 50V          pin   1  
    C42      0.1uF 50V          pin   1  
    C45      0.1uF 50V          pin   1  
    C46      47uF 16V           pin   1  
    C49      0.1uF 50V          pin   1  
    C51      0.1uF 50V          pin   1  
    C52      47uF 16V           pin   1  
    C53      1nF                pin   1  
    C54      0.1uF 12V          pin   1  
    C58      0.1uF 12V          pin   1  
    C59      0.1uF 12V          pin   1  
    C64      0.1uF 12V          pin   1  
    C65      0.1uF 12V          pin   1  
    C66      0.1uF 12V          pin   1  
    C67      0.1uF 12V          pin   1  
    C68      0.1uF 12V          pin   1  
    C69      0.1uF 12V          pin   1  
    C72      0.1uF 12V          pin   1  
    C73      0.1uF 12V          pin   1  
    C74      0.1uF 12V          pin   1  
    C75      0.1uF 12V          pin   1  
    C76      0.1uF 12V          pin   1  
    C77      0.1uF 12V          pin   1  
    C78      0.1uF 12V          pin   1  
    C79      0.1uF 12V          pin   1  
    CR1      1N4148             pin   1  K
    CR4      1N4735             pin   1  K
    J10      Internal Expansion Connector pin   2  Pin_2
    J3       Buffered Edge Connector pin  39  Pin_39
    K1       ~                  pin  14  
    R12      0.33               pin   2  
    R16      4.7k               pin   2  
    R18      4.7k               pin   1  R1
    R20      4.7k               pin   1  
    R22      150                pin   1  
    R23      20k                pin   1  
    R24      4.7k               pin   2  
    R25      200k               pin   2  
    R28      10k                pin   2  
    R29      10k                pin   2  
    R3       2.2k               pin   2  
    R30      10k                pin   2  
    R31      150                pin   1  
    R32      150                pin   1  
    R33      150                pin   1  
    R34      4.7k               pin   1  
    Z1       MK4116             pin   9  VCC
    Z10      MK4116             pin   9  VCC
    Z11      MK4116             pin   9  VCC
    Z12      MK4116             pin   9  VCC
    Z13      MK4116             pin   9  VCC
    Z14      MK4116             pin   9  VCC
    Z15      MK4116             pin   9  VCC
    Z16      MK4116             pin   9  VCC
    Z17      74LS00             pin  14  VCC
    Z18      75452              pin   8  VCC
    Z19      4049B              pin   1  VCC
    Z2       MK4116             pin   9  VCC
    Z21      LM723C             pin   3  CSEN
    Z21      LM723C             pin   4  -
    Z22      74LS90             pin   5  VCC
    Z23      4518               pin  16  VDD
    Z24      4518               pin  16  VDD
    Z25      74LS74             pin  14  VCC
    Z26      74LS74             pin  14  VCC
    Z27      74LS32             pin  14  VCC
    Z28      74LS00             pin  14  VCC
    Z29      74LS244_Split      pin  20  VCC
    Z3       MK4116             pin   9  VCC
    Z30      74LS243            pin  14  VCC
    Z31      74LS244_Split      pin  20  VCC
    Z32      74LS04             pin  14  VCC
    Z33      74LS123            pin  16  VCC
    Z34      7416               pin  14  VCC
    Z35      74LS157            pin  16  VCC
    Z36      74LS157            pin  16  VCC
    Z37      DDU-4-7835         pin  14  VCC
    Z38      74LS243            pin  14  VCC
    Z39      74LS155            pin  16  VCC
    Z4       MK4116             pin   9  VCC
    Z40      74LS139            pin  16  VCC
    Z41      7416               pin  14  VCC
    Z42      FD1771             pin  21  VCC
    Z43      74LS30             pin  14  VCC
    Z44      74LS244            pin  20  VCC
    Z45      74LS244            pin  20  VCC
    Z46      74LS20             pin  14  VCC
    Z47      74LS175            pin  16  VCC
    Z48      74LS273            pin  20  VCC
    Z49      74LS367            pin  16  VCC
    Z5       MK4116             pin   9  VCC
    Z50      74LS240_Split      pin  20  VCC
    Z51      74LS240_Split      pin  20  VCC
    Z6       MK4116             pin   9  VCC
    Z7       MK4116             pin   9  VCC
    Z8       MK4116             pin   9  VCC
    Z9       MK4116             pin   9  VCC

-5V   (38 pins)
    C1       0.1uF 50V          pin   1  
    C2       0.01uF 16V         pin   2  
    C21      0.1uF 50V          pin   1  
    C22      0.01uF 16V         pin   2  
    C23      0.1uF 50V          pin   1  
    C24      0.01uF 16V         pin   2  
    C25      0.1uF 50V          pin   1  
    C26      0.01uF 16V         pin   2  
    C27      0.1uF 50V          pin   1  
    C28      0.01uF 16V         pin   2  
    C3       0.1uF 50V          pin   1  
    C4       0.01uF 16V         pin   2  
    C47      47uF 16V           pin   2  
    C5       0.1uF 50V          pin   1  
    C6       0.01uF 16V         pin   2  
    C63      10uF 16V           pin   2  
    C7       0.1uF 50V          pin   1  
    C70      0.1uF 50V          pin   2  
    C8       0.01uF 16V         pin   2  
    CR3      1N5231             pin   2  A
    R21      220                pin   1  
    Z1       MK4116             pin   1  VBB
    Z10      MK4116             pin   1  VBB
    Z11      MK4116             pin   1  VBB
    Z12      MK4116             pin   1  VBB
    Z13      MK4116             pin   1  VBB
    Z14      MK4116             pin   1  VBB
    Z15      MK4116             pin   1  VBB
    Z16      MK4116             pin   1  VBB
    Z2       MK4116             pin   1  VBB
    Z3       MK4116             pin   1  VBB
    Z4       MK4116             pin   1  VBB
    Z42      FD1771             pin   1  VBB
    Z5       MK4116             pin   1  VBB
    Z6       MK4116             pin   1  VBB
    Z7       MK4116             pin   1  VBB
    Z8       MK4116             pin   1  VBB
    Z9       MK4116             pin   1  VBB

/Address Decoder/A0   (5 pins)
    J10      Internal Expansion Connector pin  10  Pin_10
    J3       Buffered Edge Connector pin  25  Pin_25
    Z35      74LS157            pin   2  I0a
    Z42      FD1771             pin   5  A0
    Z45      74LS244            pin  18  O0a

/Address Decoder/A1   (5 pins)
    J10      Internal Expansion Connector pin   9  Pin_9
    J3       Buffered Edge Connector pin  27  Pin_27
    Z35      74LS157            pin   5  I0b
    Z42      FD1771             pin   6  A1
    Z45      74LS244            pin   3  O3b

/Address Decoder/A10   (4 pins)
    J3       Buffered Edge Connector pin   4  Pin_4
    Z35      74LS157            pin  13  I1d
    Z43      74LS30             pin   1  
    Z44      74LS244            pin   3  O3b

/Address Decoder/A11   (4 pins)
    J3       Buffered Edge Connector pin   9  Pin_9
    Z36      74LS157            pin   3  I1a
    Z40      74LS139            pin  13  A1
    Z44      74LS244            pin  16  O1a

/Address Decoder/A12   (4 pins)
    J3       Buffered Edge Connector pin   5  Pin_5
    Z36      74LS157            pin   6  I1b
    Z43      74LS30             pin   3  
    Z44      74LS244            pin   7  O1b

/Address Decoder/A13   (4 pins)
    J3       Buffered Edge Connector pin   6  Pin_6
    Z36      74LS157            pin  10  I1c
    Z43      74LS30             pin   2  
    Z44      74LS244            pin   5  O2b

/Address Decoder/A14   (3 pins)
    J3       Buffered Edge Connector pin  10  Pin_10
    Z40      74LS139            pin   2  A0
    Z44      74LS244            pin  18  O0a

/Address Decoder/A15   (3 pins)
    J3       Buffered Edge Connector pin   7  Pin_7
    Z40      74LS139            pin   3  A1
    Z44      74LS244            pin   9  O0b

/Address Decoder/A2   (5 pins)
    J10      Internal Expansion Connector pin  17  Pin_17
    J3       Buffered Edge Connector pin  40  Pin_40
    Z35      74LS157            pin  11  I0c
    Z39      74LS155            pin  13  A0
    Z45      74LS244            pin   9  O0b

/Address Decoder/A3   (5 pins)
    J3       Buffered Edge Connector pin  34  Pin_34
    Z35      74LS157            pin  14  I0d
    Z39      74LS155            pin   3  A1
    Z45      74LS244            pin   5  O2b
    Z46      74LS20             pin  12  

/Address Decoder/A4   (5 pins)
    J3       Buffered Edge Connector pin  31  Pin_31
    Z28      74LS00             pin  12  
    Z28      74LS00             pin  13  
    Z36      74LS157            pin   2  I0a
    Z45      74LS244            pin  16  O1a

/Address Decoder/A5   (5 pins)
    J3       Buffered Edge Connector pin  35  Pin_35
    Z36      74LS157            pin   5  I0b
    Z43      74LS30             pin   5  
    Z45      74LS244            pin  14  O2a
    Z46      74LS20             pin  10  

/Address Decoder/A6   (5 pins)
    J3       Buffered Edge Connector pin  38  Pin_38
    Z36      74LS157            pin  11  I0c
    Z43      74LS30             pin   6  
    Z45      74LS244            pin  12  O3a
    Z46      74LS20             pin   9  

/Address Decoder/A7   (5 pins)
    J3       Buffered Edge Connector pin  36  Pin_36
    Z35      74LS157            pin   3  I1a
    Z43      74LS30             pin  11  
    Z45      74LS244            pin   7  O1b
    Z46      74LS20             pin  13  

/Address Decoder/A8   (4 pins)
    J3       Buffered Edge Connector pin  11  Pin_11
    Z35      74LS157            pin   6  I1b
    Z43      74LS30             pin  12  
    Z44      74LS244            pin  14  O2a

/Address Decoder/A9   (4 pins)
    J3       Buffered Edge Connector pin  17  Pin_17
    Z35      74LS157            pin  10  I1c
    Z43      74LS30             pin   4  
    Z44      74LS244            pin  12  O3a

/Address Decoder/~{32K}   (3 pins)
    Z27      74LS32             pin   2  
    Z28      74LS00             pin   2  
    Z40      74LS139            pin   6  O2

/Address Decoder/~{37E0_READ}   (4 pins)
    Z26      74LS74             pin   4  ~{S}
    Z26      74LS74             pin  11  C
    Z39      74LS155            pin   7  Q0a
    Z49      74LS367            pin  15  

/Address Decoder/~{37E0_WRITE}   (3 pins)
    Z33      74LS123            pin   9  A
    Z39      74LS155            pin   9  Q0b
    Z47      74LS175            pin   9  Cp

/Address Decoder/~{37E8_READ}   (2 pins)
    Z39      74LS155            pin   5  Q2a
    Z49      74LS367            pin   1  

/Address Decoder/~{37E8_WRITE}   (3 pins)
    Z33      74LS123            pin   2  B
    Z39      74LS155            pin  11  Q2b
    Z48      74LS273            pin  11  Cp

/Address Decoder/~{37EC_READ}   (4 pins)
    Z39      74LS155            pin   4  Q3a
    Z42      FD1771             pin   4  ~{RE}
    Z50      74LS240_Split      pin  19  
    Z51      74LS240_Split      pin  19  

/Address Decoder/~{37EC_WRITE}   (4 pins)
    Z39      74LS155            pin  12  Q3b
    Z42      FD1771             pin   2  ~{WE}
    Z50      74LS240_Split      pin   1  
    Z51      74LS240_Split      pin   1  

/Address Decoder/~{48K}   (3 pins)
    Z27      74LS32             pin  13  
    Z28      74LS00             pin   1  
    Z40      74LS139            pin   7  O3

/Address Decoder/~{CSW}   (2 pins)
    Z32      74LS04             pin   3  
    Z39      74LS155            pin  10  Q1b

/Address Decoder/~{RAS}   (4 pins)
    Z27      74LS32             pin   9  
    Z27      74LS32             pin  10  
    Z38      74LS243            pin   9  B2
    Z40      74LS139            pin   1  E

/Address Decoder/~{RD}   (4 pins)
    J3       Buffered Edge Connector pin  15  Pin_15
    Z30      74LS243            pin   9  B2
    Z32      74LS04             pin   1  
    Z32      74LS04             pin   5  

/Address Decoder/~{WR}   (5 pins)
    J3       Buffered Edge Connector pin  13  Pin_13
    Z27      74LS32             pin   4  
    Z27      74LS32             pin   5  
    Z30      74LS243            pin  10  B1
    Z39      74LS155            pin  15  Eb2

/Card-Edge Interface Extension/D0   (10 pins)
    J10      Internal Expansion Connector pin  11  Pin_11
    J2       M1 Edge Connector  pin  30  Pin_30
    J3       Buffered Edge Connector pin  30  Pin_30
    Z17      74LS00             pin   1  
    Z31      74LS244_Split      pin   8  
    Z31      74LS244_Split      pin   9  
    Z47      74LS175            pin   4  D0
    Z48      74LS273            pin  13  D4
    Z50      74LS240_Split      pin   6  
    Z50      74LS240_Split      pin   7  

/Card-Edge Interface Extension/D1   (9 pins)
    J10      Internal Expansion Connector pin  14  Pin_14
    J2       M1 Edge Connector  pin  22  Pin_22
    J3       Buffered Edge Connector pin  22  Pin_22
    Z31      74LS244_Split      pin   6  
    Z31      74LS244_Split      pin   7  
    Z47      74LS175            pin   5  D1
    Z48      74LS273            pin  14  D5
    Z50      74LS240_Split      pin   2  
    Z50      74LS240_Split      pin   3  

/Card-Edge Interface Extension/D2   (9 pins)
    J10      Internal Expansion Connector pin  13  Pin_13
    J2       M1 Edge Connector  pin  32  Pin_32
    J3       Buffered Edge Connector pin  32  Pin_32
    Z31      74LS244_Split      pin   4  
    Z31      74LS244_Split      pin   5  
    Z47      74LS175            pin  12  D2
    Z48      74LS273            pin  17  D6
    Z50      74LS240_Split      pin   8  
    Z50      74LS240_Split      pin   9  

/Card-Edge Interface Extension/D3   (9 pins)
    J10      Internal Expansion Connector pin  12  Pin_12
    J2       M1 Edge Connector  pin  26  Pin_26
    J3       Buffered Edge Connector pin  26  Pin_26
    Z31      74LS244_Split      pin   2  
    Z31      74LS244_Split      pin   3  
    Z47      74LS175            pin  13  D3
    Z48      74LS273            pin  18  D7
    Z50      74LS240_Split      pin   4  
    Z50      74LS240_Split      pin   5  

/Card-Edge Interface Extension/D4   (9 pins)
    J10      Internal Expansion Connector pin   7  Pin_7
    J2       M1 Edge Connector  pin  18  Pin_18
    J3       Buffered Edge Connector pin  18  Pin_18
    Z29      74LS244_Split      pin   8  
    Z29      74LS244_Split      pin   9  
    Z48      74LS273            pin   3  D0
    Z49      74LS367            pin   3  
    Z51      74LS240_Split      pin   2  
    Z51      74LS240_Split      pin   3  

/Card-Edge Interface Extension/D5   (9 pins)
    J10      Internal Expansion Connector pin   8  Pin_8
    J2       M1 Edge Connector  pin  28  Pin_28
    J3       Buffered Edge Connector pin  28  Pin_28
    Z29      74LS244_Split      pin   6  
    Z29      74LS244_Split      pin   7  
    Z48      74LS273            pin   4  D1
    Z49      74LS367            pin   5  
    Z51      74LS240_Split      pin   8  
    Z51      74LS240_Split      pin   9  

/Card-Edge Interface Extension/D6   (10 pins)
    J10      Internal Expansion Connector pin   4  Pin_4
    J2       M1 Edge Connector  pin  24  Pin_24
    J3       Buffered Edge Connector pin  24  Pin_24
    Z29      74LS244_Split      pin   4  
    Z29      74LS244_Split      pin   5  
    Z48      74LS273            pin   7  D2
    Z49      74LS367            pin   7  
    Z49      74LS367            pin  13  
    Z51      74LS240_Split      pin   6  
    Z51      74LS240_Split      pin   7  

/Card-Edge Interface Extension/D7   (10 pins)
    J10      Internal Expansion Connector pin   5  Pin_5
    J2       M1 Edge Connector  pin  20  Pin_20
    J3       Buffered Edge Connector pin  20  Pin_20
    Z29      74LS244_Split      pin   2  
    Z29      74LS244_Split      pin   3  
    Z48      74LS273            pin   8  D3
    Z49      74LS367            pin   9  
    Z49      74LS367            pin  11  
    Z51      74LS240_Split      pin   4  
    Z51      74LS240_Split      pin   5  

/Card-Edge Interface Extension/~{INTAK}   (2 pins)
    J2       M1 Edge Connector  pin  14  Pin_14
    J3       Buffered Edge Connector pin  14  Pin_14

/Card-Edge Interface Extension/~{INT}   (5 pins)
    J10      Internal Expansion Connector pin  15  Pin_15
    J2       M1 Edge Connector  pin  21  Pin_21
    J3       Buffered Edge Connector pin  21  Pin_21
    Z34      7416               pin  10  
    Z34      7416               pin  12  

/Card-Edge Interface Extension/~{IN}   (3 pins)
    J10      Internal Expansion Connector pin  16  Pin_16
    J2       M1 Edge Connector  pin  19  Pin_19
    J3       Buffered Edge Connector pin  19  Pin_19

/Card-Edge Interface Extension/~{OUT}   (3 pins)
    J10      Internal Expansion Connector pin  18  Pin_18
    J2       M1 Edge Connector  pin  12  Pin_12
    J3       Buffered Edge Connector pin  12  Pin_12

/Card-Edge Interface Extension/~{SYSRES}   (5 pins)
    J10      Internal Expansion Connector pin   6  Pin_6
    J2       M1 Edge Connector  pin   2  Pin_2
    J3       Buffered Edge Connector pin   2  Pin_2
    R28      10k                pin   1  
    Z42      FD1771             pin  19  ~{MR}

/Card-Edge Interface Extension/~{TEST}   (2 pins)
    J2       M1 Edge Connector  pin  23  Pin_23
    J3       Buffered Edge Connector pin  23  Pin_23

/Card-Edge Interface Extension/~{WAIT}   (2 pins)
    J2       M1 Edge Connector  pin  33  Pin_33
    J3       Buffered Edge Connector pin  33  Pin_33

/Card-Edge Interface/M1_A0   (2 pins)
    J2       M1 Edge Connector  pin  25  Pin_25
    Z45      74LS244            pin   2  I0a

/Card-Edge Interface/M1_A1   (2 pins)
    J2       M1 Edge Connector  pin  27  Pin_27
    Z45      74LS244            pin  17  I3b

/Card-Edge Interface/M1_A10   (2 pins)
    J2       M1 Edge Connector  pin   4  Pin_4
    Z44      74LS244            pin  17  I3b

/Card-Edge Interface/M1_A11   (2 pins)
    J2       M1 Edge Connector  pin   9  Pin_9
    Z44      74LS244            pin   4  I1a

/Card-Edge Interface/M1_A12   (2 pins)
    J2       M1 Edge Connector  pin   5  Pin_5
    Z44      74LS244            pin  13  I1b

/Card-Edge Interface/M1_A13   (2 pins)
    J2       M1 Edge Connector  pin   6  Pin_6
    Z44      74LS244            pin  15  I2b

/Card-Edge Interface/M1_A14   (2 pins)
    J2       M1 Edge Connector  pin  10  Pin_10
    Z44      74LS244            pin   2  I0a

/Card-Edge Interface/M1_A15   (2 pins)
    J2       M1 Edge Connector  pin   7  Pin_7
    Z44      74LS244            pin  11  I0b

/Card-Edge Interface/M1_A2   (2 pins)
    J2       M1 Edge Connector  pin  40  Pin_40
    Z45      74LS244            pin  11  I0b

/Card-Edge Interface/M1_A3   (2 pins)
    J2       M1 Edge Connector  pin  34  Pin_34
    Z45      74LS244            pin  15  I2b

/Card-Edge Interface/M1_A4   (2 pins)
    J2       M1 Edge Connector  pin  31  Pin_31
    Z45      74LS244            pin   4  I1a

/Card-Edge Interface/M1_A5   (2 pins)
    J2       M1 Edge Connector  pin  35  Pin_35
    Z45      74LS244            pin   6  I2a

/Card-Edge Interface/M1_A6   (2 pins)
    J2       M1 Edge Connector  pin  38  Pin_38
    Z45      74LS244            pin   8  I3a

/Card-Edge Interface/M1_A7   (2 pins)
    J2       M1 Edge Connector  pin  36  Pin_36
    Z45      74LS244            pin  13  I1b

/Card-Edge Interface/M1_A8   (2 pins)
    J2       M1 Edge Connector  pin  11  Pin_11
    Z44      74LS244            pin   6  I2a

/Card-Edge Interface/M1_A9   (2 pins)
    J2       M1 Edge Connector  pin  17  Pin_17
    Z44      74LS244            pin   8  I3a

/Card-Edge Interface/MUX   (2 pins)
    Z32      74LS04             pin  11  
    Z37      DDU-4-7835         pin   4  Tr2

/Card-Edge Interface/~{CAS}   (3 pins)
    Z27      74LS32             pin   1  
    Z27      74LS32             pin  12  
    Z38      74LS243            pin   8  B3

/Card-Edge Interface/~{M1_RAS}   (2 pins)
    J2       M1 Edge Connector  pin   1  Pin_1
    Z38      74LS243            pin   3  A0

/Clock/CLK/10   (3 pins)
    R3       2.2k               pin   1  
    Z22      74LS90             pin  11  Q3
    Z23      4518               pin   2  Enable

/Clock/~{CLK/2}   (3 pins)
    Z25      74LS74             pin   2  D
    Z25      74LS74             pin   6  ~{Q}
    Z42      FD1771             pin  24  CLK

/Floppy Controller/~{DIR_SEL}   (2 pins)
    J5       Shugart Floppy Disk Bus pin  18  Pin_18
    Z34      7416               pin   2  

/Floppy Controller/~{DS0}   (2 pins)
    J5       Shugart Floppy Disk Bus pin  10  Pin_10
    Z41      7416               pin   8  

/Floppy Controller/~{DS1}   (2 pins)
    J5       Shugart Floppy Disk Bus pin  12  Pin_12
    Z41      7416               pin   6  

/Floppy Controller/~{DS2}   (2 pins)
    J5       Shugart Floppy Disk Bus pin  14  Pin_14
    Z41      7416               pin  10  

/Floppy Controller/~{DS3}   (2 pins)
    J5       Shugart Floppy Disk Bus pin  32  Pin_32
    Z41      7416               pin  12  

/Floppy Controller/~{INDEX_PULSE}   (3 pins)
    J5       Shugart Floppy Disk Bus pin   8  Pin_8
    R32      150                pin   2  
    Z42      FD1771             pin  35  ~{IP}

/Floppy Controller/~{INTRQ}   (4 pins)
    R30      10k                pin   1  
    Z34      7416               pin  11  
    Z42      FD1771             pin  39  ~{INTRQ}
    Z49      74LS367            pin  14  

/Floppy Controller/~{MOTOR_ON}   (2 pins)
    J5       Shugart Floppy Disk Bus pin  16  Pin_16
    Z41      7416               pin   4  

/Floppy Controller/~{READ_DATA}   (3 pins)
    J5       Shugart Floppy Disk Bus pin  30  Pin_30
    R22      150                pin   2  
    Z32      74LS04             pin   9  

/Floppy Controller/~{STEP}   (2 pins)
    J5       Shugart Floppy Disk Bus pin  20  Pin_20
    Z34      7416               pin   4  

/Floppy Controller/~{TRACK_ZERO}   (3 pins)
    J5       Shugart Floppy Disk Bus pin  26  Pin_26
    R33      150                pin   2  
    Z42      FD1771             pin  34  ~{TR00}

/Floppy Controller/~{WRITE_DATA}   (2 pins)
    J5       Shugart Floppy Disk Bus pin  22  Pin_22
    Z34      7416               pin   8  

/Floppy Controller/~{WRITE_GATE}   (2 pins)
    J5       Shugart Floppy Disk Bus pin  24  Pin_24
    Z34      7416               pin   6  

/Floppy Controller/~{WRITE_PROTECT}   (3 pins)
    J5       Shugart Floppy Disk Bus pin  28  Pin_28
    R31      150                pin   2  
    Z42      FD1771             pin  36  ~{WPRT}

/Internal Expansion/S0   (2 pins)
    J1       Expansion Board Connector pin  10  Pin_10
    J10      Internal Expansion Connector pin  19  Pin_19

/Internal Expansion/S1   (2 pins)
    J1       Expansion Board Connector pin  12  Pin_12
    J10      Internal Expansion Connector pin  20  Pin_20

/Internal Expansion/S10   (2 pins)
    J1       Expansion Board Connector pin  30  Pin_30
    J10      Internal Expansion Connector pin  29  Pin_29

/Internal Expansion/S11   (2 pins)
    J1       Expansion Board Connector pin  32  Pin_32
    J10      Internal Expansion Connector pin  30  Pin_30

/Internal Expansion/S12   (2 pins)
    J1       Expansion Board Connector pin  34  Pin_34
    J10      Internal Expansion Connector pin  31  Pin_31

/Internal Expansion/S13   (2 pins)
    J1       Expansion Board Connector pin  36  Pin_36
    J10      Internal Expansion Connector pin  32  Pin_32

/Internal Expansion/S14   (2 pins)
    J1       Expansion Board Connector pin  38  Pin_38
    J10      Internal Expansion Connector pin  33  Pin_33

/Internal Expansion/S15   (2 pins)
    J1       Expansion Board Connector pin  40  Pin_40
    J10      Internal Expansion Connector pin  34  Pin_34

/Internal Expansion/S2   (2 pins)
    J1       Expansion Board Connector pin  14  Pin_14
    J10      Internal Expansion Connector pin  21  Pin_21

/Internal Expansion/S3   (2 pins)
    J1       Expansion Board Connector pin  16  Pin_16
    J10      Internal Expansion Connector pin  22  Pin_22

/Internal Expansion/S4   (2 pins)
    J1       Expansion Board Connector pin  18  Pin_18
    J10      Internal Expansion Connector pin  23  Pin_23

/Internal Expansion/S5   (2 pins)
    J1       Expansion Board Connector pin  20  Pin_20
    J10      Internal Expansion Connector pin  24  Pin_24

/Internal Expansion/S6   (2 pins)
    J1       Expansion Board Connector pin  22  Pin_22
    J10      Internal Expansion Connector pin  25  Pin_25

/Internal Expansion/S7   (2 pins)
    J1       Expansion Board Connector pin  24  Pin_24
    J10      Internal Expansion Connector pin  26  Pin_26

/Internal Expansion/S8   (2 pins)
    J1       Expansion Board Connector pin  26  Pin_26
    J10      Internal Expansion Connector pin  27  Pin_27

/Internal Expansion/S9   (2 pins)
    J1       Expansion Board Connector pin  28  Pin_28
    J10      Internal Expansion Connector pin  28  Pin_28

/Internal Expansion/~{E8}   (2 pins)
    J10      Internal Expansion Connector pin   3  Pin_3
    Z28      74LS00             pin   8  

/Line Printer/DATA1   (2 pins)
    J4       Line Printer Connector pin   3  Pin_3
    Z48      74LS273            pin  12  Q4

/Line Printer/DATA2   (2 pins)
    J4       Line Printer Connector pin   5  Pin_5
    Z48      74LS273            pin  15  Q5

/Line Printer/DATA3   (2 pins)
    J4       Line Printer Connector pin   7  Pin_7
    Z48      74LS273            pin  16  Q6

/Line Printer/DATA4   (2 pins)
    J4       Line Printer Connector pin   9  Pin_9
    Z48      74LS273            pin  19  Q7

/Line Printer/DATA5   (2 pins)
    J4       Line Printer Connector pin  11  Pin_11
    Z48      74LS273            pin   2  Q0

/Line Printer/DATA6   (2 pins)
    J4       Line Printer Connector pin  13  Pin_13
    Z48      74LS273            pin   5  Q1

/Line Printer/DATA7   (2 pins)
    J4       Line Printer Connector pin  15  Pin_15
    Z48      74LS273            pin   6  Q2

/Line Printer/DATA8   (2 pins)
    J4       Line Printer Connector pin  17  Pin_17
    Z48      74LS273            pin   9  Q3

/Line Printer/PRIME   (1 pins)
    J4       Line Printer Connector pin  26  Pin_26

/Line Printer/~{BUSY}   (2 pins)
    J4       Line Printer Connector pin  21  Pin_21
    Z49      74LS367            pin  10  

/Line Printer/~{DATA_STROBE}   (2 pins)
    J4       Line Printer Connector pin   1  Pin_1
    Z33      74LS123            pin   4  ~{Q}

/Line Printer/~{FAULT}   (2 pins)
    J4       Line Printer Connector pin  28  Pin_28
    Z49      74LS367            pin   2  

/Line Printer/~{OUT_OF_PAPER}   (2 pins)
    J4       Line Printer Connector pin  23  Pin_23
    Z49      74LS367            pin   6  

/Line Printer/~{UNIT_SELECT}   (2 pins)
    J4       Line Printer Connector pin  25  Pin_25
    Z49      74LS367            pin   4  

/Memory Management/RAM/A0   (17 pins)
    R26      33                 pin   1  R1.1
    Z1       MK4116             pin   5  A0
    Z10      MK4116             pin   5  A0
    Z11      MK4116             pin   5  A0
    Z12      MK4116             pin   5  A0
    Z13      MK4116             pin   5  A0
    Z14      MK4116             pin   5  A0
    Z15      MK4116             pin   5  A0
    Z16      MK4116             pin   5  A0
    Z2       MK4116             pin   5  A0
    Z3       MK4116             pin   5  A0
    Z4       MK4116             pin   5  A0
    Z5       MK4116             pin   5  A0
    Z6       MK4116             pin   5  A0
    Z7       MK4116             pin   5  A0
    Z8       MK4116             pin   5  A0
    Z9       MK4116             pin   5  A0

/Memory Management/RAM/A1   (17 pins)
    R26      33                 pin   7  R4.1
    Z1       MK4116             pin   7  A1
    Z10      MK4116             pin   7  A1
    Z11      MK4116             pin   7  A1
    Z12      MK4116             pin   7  A1
    Z13      MK4116             pin   7  A1
    Z14      MK4116             pin   7  A1
    Z15      MK4116             pin   7  A1
    Z16      MK4116             pin   7  A1
    Z2       MK4116             pin   7  A1
    Z3       MK4116             pin   7  A1
    Z4       MK4116             pin   7  A1
    Z5       MK4116             pin   7  A1
    Z6       MK4116             pin   7  A1
    Z7       MK4116             pin   7  A1
    Z8       MK4116             pin   7  A1
    Z9       MK4116             pin   7  A1

/Memory Management/RAM/A2   (17 pins)
    R26      33                 pin   5  R3.1
    Z1       MK4116             pin   6  A2
    Z10      MK4116             pin   6  A2
    Z11      MK4116             pin   6  A2
    Z12      MK4116             pin   6  A2
    Z13      MK4116             pin   6  A2
    Z14      MK4116             pin   6  A2
    Z15      MK4116             pin   6  A2
    Z16      MK4116             pin   6  A2
    Z2       MK4116             pin   6  A2
    Z3       MK4116             pin   6  A2
    Z4       MK4116             pin   6  A2
    Z5       MK4116             pin   6  A2
    Z6       MK4116             pin   6  A2
    Z7       MK4116             pin   6  A2
    Z8       MK4116             pin   6  A2
    Z9       MK4116             pin   6  A2

/Memory Management/RAM/A3   (17 pins)
    R27      33                 pin   5  R3.1
    Z1       MK4116             pin  12  A3
    Z10      MK4116             pin  12  A3
    Z11      MK4116             pin  12  A3
    Z12      MK4116             pin  12  A3
    Z13      MK4116             pin  12  A3
    Z14      MK4116             pin  12  A3
    Z15      MK4116             pin  12  A3
    Z16      MK4116             pin  12  A3
    Z2       MK4116             pin  12  A3
    Z3       MK4116             pin  12  A3
    Z4       MK4116             pin  12  A3
    Z5       MK4116             pin  12  A3
    Z6       MK4116             pin  12  A3
    Z7       MK4116             pin  12  A3
    Z8       MK4116             pin  12  A3
    Z9       MK4116             pin  12  A3

/Memory Management/RAM/A4   (17 pins)
    R27      33                 pin   1  R1.1
    Z1       MK4116             pin  11  A4
    Z10      MK4116             pin  11  A4
    Z11      MK4116             pin  11  A4
    Z12      MK4116             pin  11  A4
    Z13      MK4116             pin  11  A4
    Z14      MK4116             pin  11  A4
    Z15      MK4116             pin  11  A4
    Z16      MK4116             pin  11  A4
    Z2       MK4116             pin  11  A4
    Z3       MK4116             pin  11  A4
    Z4       MK4116             pin  11  A4
    Z5       MK4116             pin  11  A4
    Z6       MK4116             pin  11  A4
    Z7       MK4116             pin  11  A4
    Z8       MK4116             pin  11  A4
    Z9       MK4116             pin  11  A4

/Memory Management/RAM/A5   (17 pins)
    R26      33                 pin   3  R2.1
    Z1       MK4116             pin  10  A5
    Z10      MK4116             pin  10  A5
    Z11      MK4116             pin  10  A5
    Z12      MK4116             pin  10  A5
    Z13      MK4116             pin  10  A5
    Z14      MK4116             pin  10  A5
    Z15      MK4116             pin  10  A5
    Z16      MK4116             pin  10  A5
    Z2       MK4116             pin  10  A5
    Z3       MK4116             pin  10  A5
    Z4       MK4116             pin  10  A5
    Z5       MK4116             pin  10  A5
    Z6       MK4116             pin  10  A5
    Z7       MK4116             pin  10  A5
    Z8       MK4116             pin  10  A5
    Z9       MK4116             pin  10  A5

/Memory Management/RAM/A6   (17 pins)
    R27      33                 pin   7  R4.1
    Z1       MK4116             pin  13  A6
    Z10      MK4116             pin  13  A6
    Z11      MK4116             pin  13  A6
    Z12      MK4116             pin  13  A6
    Z13      MK4116             pin  13  A6
    Z14      MK4116             pin  13  A6
    Z15      MK4116             pin  13  A6
    Z16      MK4116             pin  13  A6
    Z2       MK4116             pin  13  A6
    Z3       MK4116             pin  13  A6
    Z4       MK4116             pin  13  A6
    Z5       MK4116             pin  13  A6
    Z6       MK4116             pin  13  A6
    Z7       MK4116             pin  13  A6
    Z8       MK4116             pin  13  A6
    Z9       MK4116             pin  13  A6

/Memory Management/RAM/IN0   (3 pins)
    Z16      MK4116             pin   2  IN
    Z31      74LS244_Split      pin  12  
    Z8       MK4116             pin   2  IN

/Memory Management/RAM/IN1   (3 pins)
    Z15      MK4116             pin   2  IN
    Z31      74LS244_Split      pin  14  
    Z7       MK4116             pin   2  IN

/Memory Management/RAM/IN2   (3 pins)
    Z14      MK4116             pin   2  IN
    Z31      74LS244_Split      pin  16  
    Z6       MK4116             pin   2  IN

/Memory Management/RAM/IN3   (3 pins)
    Z13      MK4116             pin   2  IN
    Z31      74LS244_Split      pin  18  
    Z5       MK4116             pin   2  IN

/Memory Management/RAM/IN4   (3 pins)
    Z12      MK4116             pin   2  IN
    Z29      74LS244_Split      pin  12  
    Z4       MK4116             pin   2  IN

/Memory Management/RAM/IN5   (3 pins)
    Z11      MK4116             pin   2  IN
    Z29      74LS244_Split      pin  14  
    Z3       MK4116             pin   2  IN

/Memory Management/RAM/IN6   (3 pins)
    Z10      MK4116             pin   2  IN
    Z2       MK4116             pin   2  IN
    Z29      74LS244_Split      pin  16  

/Memory Management/RAM/IN7   (3 pins)
    Z1       MK4116             pin   2  IN
    Z29      74LS244_Split      pin  18  
    Z9       MK4116             pin   2  IN

/Memory Management/RAM/OUT0   (3 pins)
    Z16      MK4116             pin  14  OUT
    Z31      74LS244_Split      pin  11  
    Z8       MK4116             pin  14  OUT

/Memory Management/RAM/OUT1   (3 pins)
    Z15      MK4116             pin  14  OUT
    Z31      74LS244_Split      pin  13  
    Z7       MK4116             pin  14  OUT

/Memory Management/RAM/OUT2   (3 pins)
    Z14      MK4116             pin  14  OUT
    Z31      74LS244_Split      pin  15  
    Z6       MK4116             pin  14  OUT

/Memory Management/RAM/OUT3   (3 pins)
    Z13      MK4116             pin  14  OUT
    Z31      74LS244_Split      pin  17  
    Z5       MK4116             pin  14  OUT

/Memory Management/RAM/OUT4   (3 pins)
    Z12      MK4116             pin  14  OUT
    Z29      74LS244_Split      pin  11  
    Z4       MK4116             pin  14  OUT

/Memory Management/RAM/OUT5   (3 pins)
    Z11      MK4116             pin  14  OUT
    Z29      74LS244_Split      pin  13  
    Z3       MK4116             pin  14  OUT

/Memory Management/RAM/OUT6   (3 pins)
    Z10      MK4116             pin  14  OUT
    Z2       MK4116             pin  14  OUT
    Z29      74LS244_Split      pin  15  

/Memory Management/RAM/OUT7   (3 pins)
    Z1       MK4116             pin  14  OUT
    Z29      74LS244_Split      pin  17  
    Z9       MK4116             pin  14  OUT

/Memory Management/RAM/~{LOWER}   (9 pins)
    R19      33                 pin   1  R1.1
    Z10      MK4116             pin  15  ~{CAS}
    Z11      MK4116             pin  15  ~{CAS}
    Z12      MK4116             pin  15  ~{CAS}
    Z13      MK4116             pin  15  ~{CAS}
    Z14      MK4116             pin  15  ~{CAS}
    Z15      MK4116             pin  15  ~{CAS}
    Z16      MK4116             pin  15  ~{CAS}
    Z9       MK4116             pin  15  ~{CAS}

/Memory Management/RAM/~{RAS}   (17 pins)
    R19      33                 pin   7  R4.1
    Z1       MK4116             pin   4  ~{RAS}
    Z10      MK4116             pin   4  ~{RAS}
    Z11      MK4116             pin   4  ~{RAS}
    Z12      MK4116             pin   4  ~{RAS}
    Z13      MK4116             pin   4  ~{RAS}
    Z14      MK4116             pin   4  ~{RAS}
    Z15      MK4116             pin   4  ~{RAS}
    Z16      MK4116             pin   4  ~{RAS}
    Z2       MK4116             pin   4  ~{RAS}
    Z3       MK4116             pin   4  ~{RAS}
    Z4       MK4116             pin   4  ~{RAS}
    Z5       MK4116             pin   4  ~{RAS}
    Z6       MK4116             pin   4  ~{RAS}
    Z7       MK4116             pin   4  ~{RAS}
    Z8       MK4116             pin   4  ~{RAS}
    Z9       MK4116             pin   4  ~{RAS}

/Memory Management/RAM/~{UPPER}   (9 pins)
    R19      33                 pin   3  R2.1
    Z1       MK4116             pin  15  ~{CAS}
    Z2       MK4116             pin  15  ~{CAS}
    Z3       MK4116             pin  15  ~{CAS}
    Z4       MK4116             pin  15  ~{CAS}
    Z5       MK4116             pin  15  ~{CAS}
    Z6       MK4116             pin  15  ~{CAS}
    Z7       MK4116             pin  15  ~{CAS}
    Z8       MK4116             pin  15  ~{CAS}

/Memory Management/RAM/~{WR}   (17 pins)
    R19      33                 pin   5  R3.1
    Z1       MK4116             pin   3  ~{WR}
    Z10      MK4116             pin   3  ~{WR}
    Z11      MK4116             pin   3  ~{WR}
    Z12      MK4116             pin   3  ~{WR}
    Z13      MK4116             pin   3  ~{WR}
    Z14      MK4116             pin   3  ~{WR}
    Z15      MK4116             pin   3  ~{WR}
    Z16      MK4116             pin   3  ~{WR}
    Z2       MK4116             pin   3  ~{WR}
    Z3       MK4116             pin   3  ~{WR}
    Z4       MK4116             pin   3  ~{WR}
    Z5       MK4116             pin   3  ~{WR}
    Z6       MK4116             pin   3  ~{WR}
    Z7       MK4116             pin   3  ~{WR}
    Z8       MK4116             pin   3  ~{WR}
    Z9       MK4116             pin   3  ~{WR}

/Timer/~{INTRQ}   (3 pins)
    Z26      74LS74             pin   9  Q
    Z34      7416               pin  13  
    Z49      74LS367            pin  12  

GND   (227 pins)
    C1       0.1uF 50V          pin   2  
    C10      0.01uF 16V         pin   2  
    C11      0.1uF 50V          pin   2  
    C12      0.01uF 16V         pin   2  
    C13      0.1uF 50V          pin   2  
    C14      0.01uF 16V         pin   2  
    C15      0.1uF 50V          pin   2  
    C16      0.01uF 16V         pin   2  
    C17      0.1uF 50V          pin   2  
    C18      0.01uF 16V         pin   2  
    C19      0.1uF 50V          pin   2  
    C2       0.01uF 16V         pin   1  
    C20      0.01uF 16V         pin   2  
    C21      0.1uF 50V          pin   2  
    C22      0.01uF 16V         pin   1  
    C23      0.1uF 50V          pin   2  
    C24      0.01uF 16V         pin   1  
    C25      0.1uF 50V          pin   2  
    C26      0.01uF 16V         pin   1  
    C27      0.1uF 50V          pin   2  
    C28      0.01uF 16V         pin   1  
    C29      0.1uF 50V          pin   2  
    C3       0.1uF 50V          pin   2  
    C30      0.01uF 16V         pin   2  
    C31      0.1uF 50V          pin   2  
    C32      0.01uF 16V         pin   2  
    C33      0.1uF 50V          pin   2  
    C34      0.01uF 16V         pin   2  
    C35      0.1uF 50V          pin   2  
    C36      0.01uF 16V         pin   2  
    C37      0.1uF 50V          pin   2  
    C38      0.01uF 16V         pin   2  
    C39      0.1uF 50V          pin   2  
    C4       0.01uF 16V         pin   1  
    C40      0.01uF 16V         pin   2  
    C41      0.1uF 50V          pin   2  
    C42      0.1uF 50V          pin   2  
    C43      10pF               pin   1  
    C44      75pF               pin   1  
    C45      0.1uF 50V          pin   2  
    C46      47uF 16V           pin   2  
    C47      47uF 16V           pin   1  
    C48      47uF               pin   2  
    C49      0.1uF 50V          pin   2  
    C5       0.1uF 50V          pin   2  
    C51      0.1uF 50V          pin   2  
    C52      47uF 16V           pin   2  
    C54      0.1uF 12V          pin   2  
    C55      2200uF 35V         pin   2  
    C56      47uF 16V           pin   2  
    C57      10000uF 16V        pin   2  
    C58      0.1uF 12V          pin   2  
    C59      0.1uF 12V          pin   2  
    C6       0.01uF 16V         pin   1  
    C60      220uF 16V          pin   1  
    C61      200pF              pin   2  
    C62      33uF               pin   2  
    C63      10uF 16V           pin   1  
    C64      0.1uF 12V          pin   2  
    C65      0.1uF 12V          pin   2  
    C66      0.1uF 12V          pin   2  
    C67      0.1uF 12V          pin   2  
    C68      0.1uF 12V          pin   2  
    C69      0.1uF 12V          pin   2  
    C7       0.1uF 50V          pin   2  
    C70      0.1uF 50V          pin   1  
    C71      0.1uF 50V          pin   2  
    C72      0.1uF 12V          pin   2  
    C73      0.1uF 12V          pin   2  
    C74      0.1uF 12V          pin   2  
    C75      0.1uF 12V          pin   2  
    C76      0.1uF 12V          pin   2  
    C77      0.1uF 12V          pin   2  
    C78      0.1uF 12V          pin   2  
    C79      0.1uF 12V          pin   2  
    C8       0.01uF 16V         pin   1  
    C9       0.1uF 50V          pin   2  
    CR3      1N5231             pin   1  K
    CR4      1N4735             pin   2  A
    J1       Expansion Board Connector pin   1  Pin_1
    J1       Expansion Board Connector pin   3  Pin_3
    J1       Expansion Board Connector pin   5  Pin_5
    J1       Expansion Board Connector pin   7  Pin_7
    J1       Expansion Board Connector pin   9  Pin_9
    J1       Expansion Board Connector pin  11  Pin_11
    J1       Expansion Board Connector pin  13  Pin_13
    J1       Expansion Board Connector pin  15  Pin_15
    J1       Expansion Board Connector pin  17  Pin_17
    J1       Expansion Board Connector pin  19  Pin_19
    J1       Expansion Board Connector pin  21  Pin_21
    J1       Expansion Board Connector pin  23  Pin_23
    J1       Expansion Board Connector pin  25  Pin_25
    J1       Expansion Board Connector pin  27  Pin_27
    J1       Expansion Board Connector pin  29  Pin_29
    J1       Expansion Board Connector pin  31  Pin_31
    J1       Expansion Board Connector pin  33  Pin_33
    J1       Expansion Board Connector pin  35  Pin_35
    J1       Expansion Board Connector pin  37  Pin_37
    J1       Expansion Board Connector pin  39  Pin_39
    J10      Internal Expansion Connector pin   1  Pin_1
    J2       M1 Edge Connector  pin   8  Pin_8
    J2       M1 Edge Connector  pin  29  Pin_29
    J2       M1 Edge Connector  pin  37  Pin_37
    J3       Buffered Edge Connector pin   8  Pin_8
    J3       Buffered Edge Connector pin  29  Pin_29
    J3       Buffered Edge Connector pin  37  Pin_37
    J4       Line Printer Connector pin   2  Pin_2
    J4       Line Printer Connector pin   4  Pin_4
    J4       Line Printer Connector pin   6  Pin_6
    J4       Line Printer Connector pin   8  Pin_8
    J4       Line Printer Connector pin  10  Pin_10
    J4       Line Printer Connector pin  12  Pin_12
    J4       Line Printer Connector pin  14  Pin_14
    J4       Line Printer Connector pin  16  Pin_16
    J4       Line Printer Connector pin  18  Pin_18
    J4       Line Printer Connector pin  20  Pin_20
    J4       Line Printer Connector pin  22  Pin_22
    J4       Line Printer Connector pin  24  Pin_24
    J4       Line Printer Connector pin  27  Pin_27
    J4       Line Printer Connector pin  31  Pin_31
    J4       Line Printer Connector pin  33  Pin_33
    J4       Line Printer Connector pin  34  Pin_34
    J5       Shugart Floppy Disk Bus pin   1  Pin_1
    J5       Shugart Floppy Disk Bus pin   3  Pin_3
    J5       Shugart Floppy Disk Bus pin   5  Pin_5
    J5       Shugart Floppy Disk Bus pin   7  Pin_7
    J5       Shugart Floppy Disk Bus pin   9  Pin_9
    J5       Shugart Floppy Disk Bus pin  11  Pin_11
    J5       Shugart Floppy Disk Bus pin  13  Pin_13
    J5       Shugart Floppy Disk Bus pin  15  Pin_15
    J5       Shugart Floppy Disk Bus pin  17  Pin_17
    J5       Shugart Floppy Disk Bus pin  19  Pin_19
    J5       Shugart Floppy Disk Bus pin  21  Pin_21
    J5       Shugart Floppy Disk Bus pin  23  Pin_23
    J5       Shugart Floppy Disk Bus pin  25  Pin_25
    J5       Shugart Floppy Disk Bus pin  27  Pin_27
    J5       Shugart Floppy Disk Bus pin  29  Pin_29
    J5       Shugart Floppy Disk Bus pin  31  Pin_31
    J5       Shugart Floppy Disk Bus pin  33  Pin_33
    J9       Front View
Power   pin   4  
    R10      3.3k               pin   2  
    R11      12k                pin   2  
    R14      4.7k               pin   2  
    R9       3.3k               pin   2  
    Z1       MK4116             pin  16  VSS
    Z10      MK4116             pin  16  VSS
    Z11      MK4116             pin  16  VSS
    Z12      MK4116             pin  16  VSS
    Z13      MK4116             pin  16  VSS
    Z14      MK4116             pin  16  VSS
    Z15      MK4116             pin  16  VSS
    Z16      MK4116             pin  16  VSS
    Z17      74LS00             pin   7  GND
    Z18      75452              pin   4  GND
    Z19      4049B              pin   8  VSS
    Z2       MK4116             pin  16  VSS
    Z20      LM723C             pin   7  V-
    Z21      LM723C             pin   7  V-
    Z22      74LS90             pin   2  R0(1)
    Z22      74LS90             pin   3  R0(2)
    Z22      74LS90             pin   6  R9(1)
    Z22      74LS90             pin   7  R9(2)
    Z22      74LS90             pin  10  GND
    Z23      4518               pin   1  CK
    Z23      4518               pin   7  Reset
    Z23      4518               pin   8  VSS
    Z23      4518               pin   9  CK
    Z23      4518               pin  15  Reset
    Z24      4518               pin   1  CK
    Z24      4518               pin   7  Reset
    Z24      4518               pin   8  VSS
    Z24      4518               pin   9  CK
    Z24      4518               pin  15  Reset
    Z25      74LS74             pin   7  GND
    Z25      74LS74             pin  10  ~{S}
    Z25      74LS74             pin  13  ~{R}
    Z26      74LS74             pin   2  D
    Z26      74LS74             pin   7  GND
    Z26      74LS74             pin  12  D
    Z27      74LS32             pin   7  GND
    Z28      74LS00             pin   7  GND
    Z29      74LS244_Split      pin   1  
    Z29      74LS244_Split      pin  10  GND
    Z3       MK4116             pin  16  VSS
    Z30      74LS243            pin   1  OEa
    Z30      74LS243            pin   7  GND
    Z30      74LS243            pin  13  OEb
    Z31      74LS244_Split      pin   1  
    Z31      74LS244_Split      pin  10  GND
    Z32      74LS04             pin   7  GND
    Z33      74LS123            pin   1  A
    Z33      74LS123            pin   6  Cext
    Z33      74LS123            pin   8  GND
    Z33      74LS123            pin  14  Cext
    Z34      7416               pin   7  GND
    Z35      74LS157            pin   8  GND
    Z35      74LS157            pin  15  E
    Z36      74LS157            pin   8  GND
    Z36      74LS157            pin  15  E
    Z37      DDU-4-7835         pin   7  GND
    Z38      74LS243            pin   1  OEa
    Z38      74LS243            pin   7  GND
    Z38      74LS243            pin  13  OEb
    Z39      74LS155            pin   8  GND
    Z4       MK4116             pin  16  VSS
    Z40      74LS139            pin   8  GND
    Z41      7416               pin   7  GND
    Z42      FD1771             pin   3  ~{CS}
    Z42      FD1771             pin  20  GND
    Z43      74LS30             pin   7  GND
    Z44      74LS244            pin   1  OEa
    Z44      74LS244            pin  10  GND
    Z44      74LS244            pin  19  OEb
    Z45      74LS244            pin   1  OEa
    Z45      74LS244            pin  10  GND
    Z45      74LS244            pin  19  OEb
    Z46      74LS20             pin   7  GND
    Z47      74LS175            pin   8  GND
    Z48      74LS273            pin  10  GND
    Z49      74LS367            pin   8  GND
    Z5       MK4116             pin  16  VSS
    Z50      74LS240_Split      pin  10  GND
    Z51      74LS240_Split      pin  10  GND
    Z6       MK4116             pin  16  VSS
    Z7       MK4116             pin  16  VSS
    Z8       MK4116             pin  16  VSS
    Z9       MK4116             pin  16  VSS

GND2   (3 pins)
    J6       Front View 
(Cassette 1) pin   2  
    J7       Front View
(Cassette 2) pin   2  
    J8       Front View
(Cassette M1) pin   2  

HI1   (5 pins)
    R16      4.7k               pin   1  
    Z25      74LS74             pin   1  ~{R}
    Z25      74LS74             pin   4  ~{S}
    Z26      74LS74             pin   1  ~{R}
    Z26      74LS74             pin  13  ~{R}

HI2   (4 pins)
    R24      4.7k               pin   1  
    Z33      74LS123            pin   3  Clr
    Z33      74LS123            pin  10  B
    Z33      74LS123            pin  11  Clr

Net-(C43-Pad2)   (4 pins)
    C43      10pF               pin   2  
    R1       10M                pin   1  
    Y1       4 MHz              pin   1  1
    Z19      4049B              pin  11  

Net-(C44-Pad2)   (3 pins)
    C44      75pF               pin   2  
    R2       1k                 pin   1  
    Y1       4 MHz              pin   2  2

Net-(C60-Pad2)   (3 pins)
    C60      220uF 16V          pin   2  
    R21      220                pin   2  
    S1       ~                  pin   6  

Net-(CR1-A)   (3 pins)
    CR1      1N4148             pin   2  A
    K1       ~                  pin  13  
    Z18      75452              pin   3  1Y

Net-(CR2-+)   (3 pins)
    CR2      MDA202             pin   1  +
    S1       ~                  pin   2  
    S1       ~                  pin  11  

Net-(CR2--)   (2 pins)
    CR2      MDA202             pin   4  -
    S1       ~                  pin   5  

Net-(CR2-Pad2)   (2 pins)
    CR2      MDA202             pin   2  
    J9       Front View
Power   pin   1  

Net-(CR2-Pad3)   (2 pins)
    CR2      MDA202             pin   3  
    J9       Front View
Power   pin   3  

Net-(J2-Pin_13)   (2 pins)
    J2       M1 Edge Connector  pin  13  Pin_13
    Z30      74LS243            pin   4  A1

Net-(J2-Pin_15)   (2 pins)
    J2       M1 Edge Connector  pin  15  Pin_15
    Z30      74LS243            pin   5  A2

Net-(J6-Pad1)   (2 pins)
    J6       Front View 
(Cassette 1) pin   1  
    K1       ~                  pin   8  

Net-(J6-Pad3)   (2 pins)
    J6       Front View 
(Cassette 1) pin   3  
    K1       ~                  pin   7  

Net-(J6-Pad4)   (2 pins)
    J6       Front View 
(Cassette 1) pin   4  
    K1       ~                  pin   6  

Net-(J6-Pad5)   (2 pins)
    J6       Front View 
(Cassette 1) pin   5  
    K1       ~                  pin   5  

Net-(J7-Pad1)   (2 pins)
    J7       Front View
(Cassette 2) pin   1  
    K1       ~                  pin  12  

Net-(J7-Pad3)   (2 pins)
    J7       Front View
(Cassette 2) pin   3  
    K1       ~                  pin  11  

Net-(J7-Pad4)   (2 pins)
    J7       Front View
(Cassette 2) pin   4  
    K1       ~                  pin  10  

Net-(J7-Pad5)   (2 pins)
    J7       Front View
(Cassette 2) pin   5  
    K1       ~                  pin   9  

Net-(J8-Pad1)   (2 pins)
    J8       Front View
(Cassette M1) pin   1  
    K1       ~                  pin   4  

Net-(J8-Pad3)   (2 pins)
    J8       Front View
(Cassette M1) pin   3  
    K1       ~                  pin   3  

Net-(J8-Pad4)   (2 pins)
    J8       Front View
(Cassette M1) pin   4  
    K1       ~                  pin   2  

Net-(J8-Pad5)   (2 pins)
    J8       Front View
(Cassette M1) pin   5  
    K1       ~                  pin   1  

Net-(J9-Pad2)   (2 pins)
    J9       Front View
Power   pin   2  
    S1       ~                  pin   8  

Net-(Q1-B)   (3 pins)
    Q1       MJE2955            pin   1  B
    R4       1.2k               pin   2  
    Z20      LM723C             pin  11  VC

Net-(Q1-C)   (4 pins)
    Q1       MJE2955            pin   2  C
    R35      5.6                pin   2  
    R6       2k                 pin   2  
    Z20      LM723C             pin  10  Vout

Net-(Q1-E)   (5 pins)
    C55      2200uF 35V         pin   1  
    Q1       MJE2955            pin   3  E
    R4       1.2k               pin   1  
    S1       ~                  pin   7  
    Z20      LM723C             pin  12  V+

Net-(Q2-B)   (3 pins)
    Q2       MJE2955            pin   1  B
    Q3       2N3904             pin   3  C
    R13      68                 pin   2  

Net-(Q2-C)   (3 pins)
    Q2       MJE2955            pin   2  C
    Q3       2N3904             pin   1  E
    R12      0.33               pin   1  

Net-(Q2-E)   (5 pins)
    C57      10000uF 16V        pin   1  
    Q2       MJE2955            pin   3  E
    R13      68                 pin   1  
    S1       ~                  pin   3  
    S1       ~                  pin  10  

Net-(Q3-B)   (3 pins)
    Q3       2N3904             pin   2  B
    R17      560                pin   1  
    Z21      LM723C             pin  10  Vout

Net-(R1-Pad2)   (4 pins)
    R1       10M                pin   2  
    R2       1k                 pin   2  
    Z19      4049B              pin  12  
    Z19      4049B              pin  14  

Net-(R10-Pad1)   (2 pins)
    R10      3.3k               pin   1  
    R7       1k                 pin   3  3

Net-(R15-Pad1)   (2 pins)
    R15      1.2k               pin   1  
    R8       1k                 pin   1  1

Net-(R18A-R1.2)   (3 pins)
    R18      4.7k               pin   2  R1.2
    R19      33                 pin   2  R1.2
    Z27      74LS32             pin   3  

Net-(R18B-R2.2)   (3 pins)
    R18      4.7k               pin   3  R2.2
    R19      33                 pin   4  R2.2
    Z27      74LS32             pin  11  

Net-(R18C-R3.2)   (3 pins)
    R18      4.7k               pin   4  R3.2
    R19      33                 pin   6  R3.2
    Z27      74LS32             pin   6  

Net-(R18D-R4.2)   (3 pins)
    R18      4.7k               pin   5  R4.2
    R19      33                 pin   8  R4.2
    Z27      74LS32             pin   8  

Net-(R20-Pad2)   (3 pins)
    R20      4.7k               pin   2  
    Z28      74LS00             pin   9  
    Z41      7416               pin   2  

Net-(R26A-R1.2)   (2 pins)
    R26      33                 pin   2  R1.2
    Z35      74LS157            pin   4  Za

Net-(R26B-R2.2)   (2 pins)
    R26      33                 pin   4  R2.2
    Z35      74LS157            pin  12  Zd

Net-(R26C-R3.2)   (2 pins)
    R26      33                 pin   6  R3.2
    Z35      74LS157            pin   7  Zb

Net-(R26D-R4.2)   (2 pins)
    R26      33                 pin   8  R4.2
    Z35      74LS157            pin   9  Zc

Net-(R27A-R1.2)   (2 pins)
    R27      33                 pin   2  R1.2
    Z36      74LS157            pin   4  Za

Net-(R27C-R3.2)   (2 pins)
    R27      33                 pin   6  R3.2
    Z36      74LS157            pin   7  Zb

Net-(R27D-R4.2)   (2 pins)
    R27      33                 pin   8  R4.2
    Z36      74LS157            pin   9  Zc

Net-(R5-Pad2)   (2 pins)
    R5       2.2k               pin   2  
    R7       1k                 pin   1  1

Net-(R8-Pad3)   (2 pins)
    R8       1k                 pin   3  3
    R9       3.3k               pin   1  

Net-(Z17-Pad10)   (2 pins)
    Z17      74LS00             pin  10  
    Z17      74LS00             pin  11  

Net-(Z17-Pad12)   (3 pins)
    Z17      74LS00             pin   3  
    Z17      74LS00             pin   4  
    Z17      74LS00             pin  12  

Net-(Z17-Pad13)   (3 pins)
    Z17      74LS00             pin   2  
    Z17      74LS00             pin  13  
    Z32      74LS04             pin   4  

Net-(Z17-Pad5)   (2 pins)
    Z17      74LS00             pin   5  
    Z17      74LS00             pin   8  

Net-(Z18A-1A)   (4 pins)
    Z17      74LS00             pin   6  
    Z17      74LS00             pin   9  
    Z18      75452              pin   1  1A
    Z18      75452              pin   2  1B

Net-(Z20-+)   (2 pins)
    Z20      LM723C             pin   5  +
    Z20      LM723C             pin   6  VREF

Net-(Z20--)   (3 pins)
    C50      1nF                pin   2  
    R7       1k                 pin   2  2
    Z20      LM723C             pin   4  -

Net-(Z20-FC)   (2 pins)
    C50      1nF                pin   1  
    Z20      LM723C             pin  13  FC

Net-(Z20-ILIM)   (3 pins)
    R11      12k                pin   1  
    R6       2k                 pin   1  
    Z20      LM723C             pin   2  ILIM

Net-(Z21-+)   (2 pins)
    R8       1k                 pin   2  2
    Z21      LM723C             pin   5  +

Net-(Z21-FC)   (2 pins)
    C53      1nF                pin   2  
    Z21      LM723C             pin  13  FC

Net-(Z21-ILIM)   (3 pins)
    R14      4.7k               pin   1  
    R17      560                pin   2  
    Z21      LM723C             pin   2  ILIM

Net-(Z21-VREF)   (2 pins)
    R15      1.2k               pin   2  
    Z21      LM723C             pin   6  VREF

Net-(Z22-CP0)   (2 pins)
    Z19      4049B              pin  15  
    Z22      74LS90             pin  14  CP0

Net-(Z22-CP1..3)   (3 pins)
    Z22      74LS90             pin   1  CP1..3
    Z22      74LS90             pin  12  Q0
    Z25      74LS74             pin   3  C

Net-(Z23A-Q4)   (2 pins)
    Z23      4518               pin   6  Q4
    Z23      4518               pin  10  Enable

Net-(Z23B-Q4)   (2 pins)
    Z23      4518               pin  14  Q4
    Z24      4518               pin   2  Enable

Net-(Z24A-Q4)   (2 pins)
    Z24      4518               pin   6  Q4
    Z24      4518               pin  10  Enable

Net-(Z24B-Q4)   (2 pins)
    Z24      4518               pin  14  Q4
    Z26      74LS74             pin   3  C

Net-(Z26A-Q)   (2 pins)
    Z26      74LS74             pin   5  Q
    Z26      74LS74             pin  10  ~{S}

Net-(Z28-Pad10)   (2 pins)
    Z28      74LS00             pin  10  
    Z28      74LS00             pin  11  

Net-(Z28-Pad3)   (2 pins)
    Z28      74LS00             pin   3  
    Z28      74LS00             pin   4  

Net-(Z28-Pad5)   (2 pins)
    Z28      74LS00             pin   5  
    Z32      74LS04             pin   2  

Net-(Z28-Pad6)   (3 pins)
    Z28      74LS00             pin   6  
    Z29      74LS244_Split      pin  19  
    Z31      74LS244_Split      pin  19  

Net-(Z33A-RCext)   (3 pins)
    C61      200pF              pin   1  
    R23      20k                pin   2  
    Z33      74LS123            pin  15  RCext

Net-(Z33B-Q)   (3 pins)
    Z33      74LS123            pin   5  Q
    Z41      7416               pin   3  
    Z47      74LS175            pin   1  ~{Mr}

Net-(Z33B-RCext)   (3 pins)
    C62      33uF               pin   1  
    R25      200k               pin   1  
    Z33      74LS123            pin   7  RCext

Net-(Z35-S)   (3 pins)
    Z32      74LS04             pin  10  
    Z35      74LS157            pin   1  S
    Z36      74LS157            pin   1  S

Net-(Z37-Input)   (2 pins)
    Z37      DDU-4-7835         pin   1  Input
    Z38      74LS243            pin  11  B0

Net-(Z37-Tr1)   (2 pins)
    Z37      DDU-4-7835         pin  12  Tr1
    Z38      74LS243            pin   5  A2

Net-(Z37-Tr3)   (2 pins)
    Z37      DDU-4-7835         pin   6  Tr3
    Z38      74LS243            pin   6  A3

Net-(Z39-Ea1)   (2 pins)
    Z32      74LS04             pin   6  
    Z39      74LS155            pin   1  Ea1

Net-(Z39-Ea2)   (3 pins)
    Z39      74LS155            pin   2  Ea2
    Z39      74LS155            pin  14  Eb1
    Z40      74LS139            pin  12  O0

Net-(Z40A-O0)   (2 pins)
    Z40      74LS139            pin   4  O0
    Z40      74LS139            pin  15  E

Net-(Z40B-A0)   (2 pins)
    Z40      74LS139            pin  14  A0
    Z43      74LS30             pin   8  

Net-(Z41-Pad1)   (2 pins)
    Z41      7416               pin   1  
    Z46      74LS20             pin   8  

Net-(Z42-DI0)   (3 pins)
    Z42      FD1771             pin   7  DI0
    Z50      74LS240_Split      pin  13  
    Z50      74LS240_Split      pin  14  

Net-(Z42-DI1)   (3 pins)
    Z42      FD1771             pin   8  DI1
    Z50      74LS240_Split      pin  17  
    Z50      74LS240_Split      pin  18  

Net-(Z42-DI2)   (3 pins)
    Z42      FD1771             pin   9  DI2
    Z50      74LS240_Split      pin  11  
    Z50      74LS240_Split      pin  12  

Net-(Z42-DI3)   (3 pins)
    Z42      FD1771             pin  10  DI3
    Z50      74LS240_Split      pin  15  
    Z50      74LS240_Split      pin  16  

Net-(Z42-DI4)   (3 pins)
    Z42      FD1771             pin  11  DI4
    Z51      74LS240_Split      pin  17  
    Z51      74LS240_Split      pin  18  

Net-(Z42-DI5)   (3 pins)
    Z42      FD1771             pin  12  DI5
    Z51      74LS240_Split      pin  11  
    Z51      74LS240_Split      pin  12  

Net-(Z42-DI6)   (3 pins)
    Z42      FD1771             pin  13  DI6
    Z51      74LS240_Split      pin  13  
    Z51      74LS240_Split      pin  14  

Net-(Z42-DI7)   (3 pins)
    Z42      FD1771             pin  14  DI7
    Z51      74LS240_Split      pin  15  
    Z51      74LS240_Split      pin  16  

Net-(Z42-FDCLK)   (7 pins)
    R29      10k                pin   1  
    Z42      FD1771             pin  18  ~{3PM}
    Z42      FD1771             pin  22  ~{TEST}
    Z42      FD1771             pin  25  ~{XTDS}
    Z42      FD1771             pin  26  FDCLK
    Z42      FD1771             pin  33  ~{WF}
    Z42      FD1771             pin  37  ~{DINT}

Net-(Z42-FDDATA)   (2 pins)
    Z32      74LS04             pin   8  
    Z42      FD1771             pin  27  FDDATA

Net-(Z42-HLT)   (3 pins)
    Z42      FD1771             pin  23  HLT
    Z42      FD1771             pin  32  READY
    Z46      74LS20             pin   6  

Net-(Z42-WD)   (2 pins)
    Z34      7416               pin   9  
    Z42      FD1771             pin  31  WD

Net-(Z42-WG)   (2 pins)
    Z34      7416               pin   5  
    Z42      FD1771             pin  30  WG

Net-(Z42-~{PH1}/STEP)   (2 pins)
    Z34      7416               pin   3  
    Z42      FD1771             pin  15  ~{PH1}/STEP

Net-(Z42-~{PH2}/DIRC)   (2 pins)
    Z34      7416               pin   1  
    Z42      FD1771             pin  16  ~{PH2}/DIRC

Net-(Z47-Q0)   (2 pins)
    Z41      7416               pin   9  
    Z47      74LS175            pin   2  Q0

Net-(Z47-Q1)   (2 pins)
    Z41      7416               pin   5  
    Z47      74LS175            pin   7  Q1

Net-(Z47-Q2)   (2 pins)
    Z41      7416               pin  11  
    Z47      74LS175            pin  10  Q2

Net-(Z47-Q3)   (2 pins)
    Z41      7416               pin  13  
    Z47      74LS175            pin  15  Q3

Net-(Z47-~{Q0})   (2 pins)
    Z46      74LS20             pin   1  
    Z47      74LS175            pin   3  ~{Q0}

Net-(Z47-~{Q1})   (2 pins)
    Z46      74LS20             pin   4  
    Z47      74LS175            pin   6  ~{Q1}

Net-(Z47-~{Q2})   (2 pins)
    Z46      74LS20             pin   5  
    Z47      74LS175            pin  11  ~{Q2}

Net-(Z47-~{Q3})   (2 pins)
    Z46      74LS20             pin   2  
    Z47      74LS175            pin  14  ~{Q3}

Net-(Z48-~{Mr})   (2 pins)
    R34      4.7k               pin   2  
    Z48      74LS273            pin   1  ~{Mr}

unconnected-(J1-Pin_2-Pad2)   (1 pins)
    J1       Expansion Board Connector pin   2  Pin_2

unconnected-(J1-Pin_4-Pad4)   (1 pins)
    J1       Expansion Board Connector pin   4  Pin_4

unconnected-(J1-Pin_6-Pad6)   (1 pins)
    J1       Expansion Board Connector pin   6  Pin_6

unconnected-(J1-Pin_8-Pad8)   (1 pins)
    J1       Expansion Board Connector pin   8  Pin_8

unconnected-(J2-Pin_16-Pad16)   (1 pins)
    J2       M1 Edge Connector  pin  16  Pin_16

unconnected-(J2-Pin_3-Pad3)   (1 pins)
    J2       M1 Edge Connector  pin   3  Pin_3

unconnected-(J2-Pin_39-Pad39)   (1 pins)
    J2       M1 Edge Connector  pin  39  Pin_39

unconnected-(J3-Pin_1-Pad1)   (1 pins)
    J3       Buffered Edge Connector pin   1  Pin_1

unconnected-(J3-Pin_16-Pad16)   (1 pins)
    J3       Buffered Edge Connector pin  16  Pin_16

unconnected-(J3-Pin_3-Pad3)   (1 pins)
    J3       Buffered Edge Connector pin   3  Pin_3

unconnected-(J4-Pin_19-Pad19)   (1 pins)
    J4       Line Printer Connector pin  19  Pin_19

unconnected-(J4-Pin_29-Pad29)   (1 pins)
    J4       Line Printer Connector pin  29  Pin_29

unconnected-(J4-Pin_30-Pad30)   (1 pins)
    J4       Line Printer Connector pin  30  Pin_30

unconnected-(J4-Pin_32-Pad32)   (1 pins)
    J4       Line Printer Connector pin  32  Pin_32

unconnected-(J5-Pin_2-Pad2)   (1 pins)
    J5       Shugart Floppy Disk Bus pin   2  Pin_2

unconnected-(J5-Pin_34-Pad34)   (1 pins)
    J5       Shugart Floppy Disk Bus pin  34  Pin_34

unconnected-(J5-Pin_4-Pad4)   (1 pins)
    J5       Shugart Floppy Disk Bus pin   4  Pin_4

unconnected-(J5-Pin_6-Pad6)   (1 pins)
    J5       Shugart Floppy Disk Bus pin   6  Pin_6

unconnected-(J9-Pad5)   (1 pins)
    J9       Front View
Power   pin   5  

unconnected-(R27B-R2.1-Pad3)   (1 pins)
    R27      33                 pin   3  R2.1

unconnected-(R27B-R2.2-Pad4)   (1 pins)
    R27      33                 pin   4  R2.2

unconnected-(S1-Pad1)   (1 pins)
    S1       ~                  pin   1  

unconnected-(S1-Pad12)   (1 pins)
    S1       ~                  pin  12  

unconnected-(S1-Pad4)   (1 pins)
    S1       ~                  pin   4  

unconnected-(S1-Pad9)   (1 pins)
    S1       ~                  pin   9  

unconnected-(Z18B-2A-Pad6)   (1 pins)
    Z18      75452              pin   6  2A

unconnected-(Z18B-2B-Pad7)   (1 pins)
    Z18      75452              pin   7  2B

unconnected-(Z18B-2Y-Pad5)   (1 pins)
    Z18      75452              pin   5  2Y

unconnected-(Z19-Pad10)   (1 pins)
    Z19      4049B              pin  10  

unconnected-(Z19-Pad2)   (1 pins)
    Z19      4049B              pin   2  

unconnected-(Z19-Pad3)   (1 pins)
    Z19      4049B              pin   3  

unconnected-(Z19-Pad4)   (1 pins)
    Z19      4049B              pin   4  

unconnected-(Z19-Pad5)   (1 pins)
    Z19      4049B              pin   5  

unconnected-(Z19-Pad6)   (1 pins)
    Z19      4049B              pin   6  

unconnected-(Z19-Pad7)   (1 pins)
    Z19      4049B              pin   7  

unconnected-(Z19-Pad9)   (1 pins)
    Z19      4049B              pin   9  

unconnected-(Z20-NC-Pad1)   (1 pins)
    Z20      LM723C             pin   1  NC

unconnected-(Z20-NC-Pad14)   (1 pins)
    Z20      LM723C             pin  14  NC

unconnected-(Z20-NC-Pad8)   (1 pins)
    Z20      LM723C             pin   8  NC

unconnected-(Z20-VZ-Pad9)   (1 pins)
    Z20      LM723C             pin   9  VZ

unconnected-(Z21-NC-Pad1)   (1 pins)
    Z21      LM723C             pin   1  NC

unconnected-(Z21-NC-Pad14)   (1 pins)
    Z21      LM723C             pin  14  NC

unconnected-(Z21-NC-Pad8)   (1 pins)
    Z21      LM723C             pin   8  NC

unconnected-(Z21-VZ-Pad9)   (1 pins)
    Z21      LM723C             pin   9  VZ

unconnected-(Z22-Q1-Pad9)   (1 pins)
    Z22      74LS90             pin   9  Q1

unconnected-(Z22-Q2-Pad8)   (1 pins)
    Z22      74LS90             pin   8  Q2

unconnected-(Z23A-Q1-Pad3)   (1 pins)
    Z23      4518               pin   3  Q1

unconnected-(Z23A-Q2-Pad4)   (1 pins)
    Z23      4518               pin   4  Q2

unconnected-(Z23A-Q3-Pad5)   (1 pins)
    Z23      4518               pin   5  Q3

unconnected-(Z23B-Q1-Pad11)   (1 pins)
    Z23      4518               pin  11  Q1

unconnected-(Z23B-Q2-Pad12)   (1 pins)
    Z23      4518               pin  12  Q2

unconnected-(Z23B-Q3-Pad13)   (1 pins)
    Z23      4518               pin  13  Q3

unconnected-(Z24A-Q1-Pad3)   (1 pins)
    Z24      4518               pin   3  Q1

unconnected-(Z24A-Q2-Pad4)   (1 pins)
    Z24      4518               pin   4  Q2

unconnected-(Z24A-Q3-Pad5)   (1 pins)
    Z24      4518               pin   5  Q3

unconnected-(Z24B-Q1-Pad11)   (1 pins)
    Z24      4518               pin  11  Q1

unconnected-(Z24B-Q2-Pad12)   (1 pins)
    Z24      4518               pin  12  Q2

unconnected-(Z24B-Q3-Pad13)   (1 pins)
    Z24      4518               pin  13  Q3

unconnected-(Z25A-Q-Pad5)   (1 pins)
    Z25      74LS74             pin   5  Q

unconnected-(Z25B-C-Pad11)   (1 pins)
    Z25      74LS74             pin  11  C

unconnected-(Z25B-D-Pad12)   (1 pins)
    Z25      74LS74             pin  12  D

unconnected-(Z25B-Q-Pad9)   (1 pins)
    Z25      74LS74             pin   9  Q

unconnected-(Z25B-~{Q}-Pad8)   (1 pins)
    Z25      74LS74             pin   8  ~{Q}

unconnected-(Z26A-~{Q}-Pad6)   (1 pins)
    Z26      74LS74             pin   6  ~{Q}

unconnected-(Z26B-~{Q}-Pad8)   (1 pins)
    Z26      74LS74             pin   8  ~{Q}

unconnected-(Z30-A0-Pad3)   (1 pins)
    Z30      74LS243            pin   3  A0

unconnected-(Z30-A3-Pad6)   (1 pins)
    Z30      74LS243            pin   6  A3

unconnected-(Z30-B0-Pad11)   (1 pins)
    Z30      74LS243            pin  11  B0

unconnected-(Z30-B3-Pad8)   (1 pins)
    Z30      74LS243            pin   8  B3

unconnected-(Z32-Pad12)   (1 pins)
    Z32      74LS04             pin  12  

unconnected-(Z32-Pad13)   (1 pins)
    Z32      74LS04             pin  13  

unconnected-(Z33A-Q-Pad13)   (1 pins)
    Z33      74LS123            pin  13  Q

unconnected-(Z33B-~{Q}-Pad12)   (1 pins)
    Z33      74LS123            pin  12  ~{Q}

unconnected-(Z36-I0d-Pad14)   (1 pins)
    Z36      74LS157            pin  14  I0d

unconnected-(Z36-I1d-Pad13)   (1 pins)
    Z36      74LS157            pin  13  I1d

unconnected-(Z36-Zd-Pad12)   (1 pins)
    Z36      74LS157            pin  12  Zd

unconnected-(Z38-A1-Pad4)   (1 pins)
    Z38      74LS243            pin   4  A1

unconnected-(Z38-B1-Pad10)   (1 pins)
    Z38      74LS243            pin  10  B1

unconnected-(Z39-Q1a-Pad6)   (1 pins)
    Z39      74LS155            pin   6  Q1a

unconnected-(Z40A-O1-Pad5)   (1 pins)
    Z40      74LS139            pin   5  O1

unconnected-(Z40B-O1-Pad11)   (1 pins)
    Z40      74LS139            pin  11  O1

unconnected-(Z40B-O2-Pad10)   (1 pins)
    Z40      74LS139            pin  10  O2

unconnected-(Z40B-O3-Pad9)   (1 pins)
    Z40      74LS139            pin   9  O3

unconnected-(Z42-DRQ-Pad38)   (1 pins)
    Z42      FD1771             pin  38  DRQ

unconnected-(Z42-PH3-Pad17)   (1 pins)
    Z42      FD1771             pin  17  PH3

unconnected-(Z42-TG43-Pad29)   (1 pins)
    Z42      FD1771             pin  29  TG43

```
