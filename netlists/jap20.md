# Japanese Model I main board, Jap20 — complete netlist

Generated from `TRS-80-Model-I-Jap20-E1-main` by `verify/emit.py`, which exports the schematic with `kicad-cli` and parses it with the same code the claims in `verify/claims.py` use.

**253 components · 410 nets · 1543 pin connections.**

Three views of the same information: components, a connection view answering "what is this pin wired to", and a net index answering "what is on this net". The redundancy is deliberate — it is what lets the file be checked against itself.

No integrity problems: every node names a known component, every pin number is valid for that component's symbol, and the two views agree on the connection count.

## Components

| ref | value | sheet |
|---|---|---|
| `C1` | 10uF 16V | Cassette Interface |
| `C2` | 0.1uF 12V | Cassette Interface |
| `C3` | 0.01uF 24V | Video Mixer |
| `C4` | 10uF 16V | Video Mixer |
| `C5` | 220uF 16V | Power |
| `C6` | 10uF 16V | Power |
| `C7` | 0.01uF 24V | Power |
| `C8` | 0.1uF 12V | Capacitors |
| `C9` | 2200uF 35V | Power |
| `C10` | 10000uF 16V | Power |
| `C11` | 1nF | Power |
| `C12` | 10uF 16V | Power |
| `C13` | 0.01uF 24V | Power |
| `C14` | 10uF 16V | Power |
| `C15` | 0.01uF 24V | Power |
| `C16` | 1nF | Power |
| `C17` | 220pF | Cassette Interface |
| `C18` | 220pF | Cassette Interface |
| `C19` | 100uF 16V | Cassette Interface |
| `C20` | 0.1uF 12V | Capacitors |
| `C22` | 0.1uF 12V | Capacitors |
| `C23` | 0.1uF 12V | Capacitors |
| `C24` | 0.1uF 12V | Capacitors |
| `C25` | 0.1uF 12V | Capacitors |
| `C26` | 0.1uF 12V | Capacitors |
| `C27` | 0.1uF 25V | Capacitors |
| `C28` | 0.1uF 12V | Capacitors |
| `C29` | 0.1uF 12V | Capacitors |
| `C30` | 0.1uF 25V | Capacitors |
| `C31` | 0.1uF 12V | Capacitors |
| `C32` | 0.1uF 12V | Capacitors |
| `C33` | 0.1uF 25V | Capacitors |
| `C34` | 0.1uF 12V | Capacitors |
| `C35` | 0.1uF 12V | Capacitors |
| `C36` | 0.1uF 25V | Capacitors |
| `C37` | 0.1uF 12V | Capacitors |
| `C38` | 0.1uF 12V | Capacitors |
| `C39` | 0.1uF 12V | Capacitors |
| `C40` | 10uF 16V | CPU |
| `C41` | 0.1uF 12V | Cassette Interface |
| `C43` | 100pF | Video Mixer |
| `C44` | 0.1uF 12V | Capacitors |
| `C45` | 0.1uF 12V | Capacitors |
| `C46` | 0.1uF 12V | Capacitors |
| `C47` | 0.1uF 12V | Capacitors |
| `C48` | 1nF | Cassette Interface |
| `C49` | 0.1uF 12V | Capacitors |
| `C50` | 2.7nF | Cassette Interface |
| `C51` | 0.1uF 12V | Capacitors |
| `C52` | 0.1uF 12V | Capacitors |
| `C53` | 0.1uF 12V | Capacitors |
| `C54` | 0.1uF 12V | Capacitors |
| `C55` | 0.1uF 12V | Capacitors |
| `C56` | 0.1uF 12V | Capacitors |
| `C57` | 1nF | CPU |
| `C58` | 0.1uF 12V | Capacitors |
| `C59` | 0.1uF 12V | Capacitors |
| `C60` | 47pF | Clock |
| `C63` | 0.1uF 12V | Capacitors |
| `C64` | 0.1uF 12V | Capacitors |
| `C65` | 0.1uF 12V | Capacitors |
| `C66` | 0.1uF 12V | Capacitors |
| `C67` | 0.1uF 12V | Capacitors |
| `C68` | 0.1uF 12V | Capacitors |
| `C69` | 0.1uF 12V | Capacitors |
| `C70` | 22uF 16V | CPU |
| `C71` | 0.1uF 12V | Capacitors |
| `C72` | 0.1uF 12V | Capacitors |
| `CN1` | Connection Mainboard Side | Keyboard |
| `CN2` | Conn_01x09 | Keyboard ROM Selector |
| `CR1` | MDA202 | Power |
| `CR2` | 1N4735 | Power |
| `CR3` | 1N5231 | Power |
| `CR4` | 1N4148 | Cassette Interface |
| `CR5` | 1N4148 | Cassette Interface |
| `CR6` | 1N4148 | Cassette Interface |
| `CR7` | 1N4148 | Cassette Interface |
| `CR8` | 1N4148 | Cassette Interface |
| `J1` | Front View | Power |
| `J2` | Front View | Video Mixer |
| `J3` | Front View | Cassette Interface |
| `J4` | Edge Connector | Card-Edge Interface |
| `JP1` | TRS80_Model_I_Jumper_2_Jap | Address Decoder |
| `JP2` | TRS80_Model_I_Jumper_2_Jap | Address Decoder |
| `JP3` | TRS80_Model_I_Jumper_2_Jap | Address Decoder |
| `JP4` | TRS80_Model_I_Jumper_3_Jap | Cassette Interface |
| `JP5` | TRS80_Model_I_Jumper_3_Jap | Cassette Interface |
| `JP6` | TRS80_Model_I_Jumper_3_Jap | Video Counter |
| `JP7` | TRS80_Model_I_Jumper_3_Jap | Video Sync |
| `JP8` | TRS80_Model_I_Jumper_3_Jap | Video Sync |
| `JP9` | TRS80_Model_I_Jumper_2_Jap | Video Mixer |
| `JP10` | TRS80_Model_I_Jumper_3_Jap | Video Counter |
| `K1` | Relay_SPDT | Cassette Interface |
| `Q1` | C1815 | Video Mixer |
| `Q2` | A1015 | Video Mixer |
| `Q3` | TIP29A | Power |
| `Q4` | 2N6594 | Power |
| `Q5` | A1015 | Power |
| `Q6` | MJE34 | Power |
| `R1` | 100 | Cassette Interface |
| `R2` | 1.2k | Cassette Interface |
| `R3` | 7.5k | Cassette Interface |
| `R4` | 7.5k | Cassette Interface |
| `R5` | 220k | Cassette Interface |
| `R6` | 75 | Video Mixer |
| `R7` | 47 | Video Mixer |
| `R8` | 330 | Video Mixer |
| `R9` | 120 | Video Mixer |
| `R10` | 270 | Video Mixer |
| `R11` | 10k | Video Mixer |
| `R12` | 220 | Power |
| `R13` | 68 | Power |
| `R14` | 2.7k | Power |
| `R15` | 750 | Power |
| `R16` | 0.33 | Power |
| `R17` | 1k | Power |
| `R18` | 1.2k | Power |
| `R19` | 1.2k | Power |
| `R20` | 100k | Power |
| `R21` | 3.3k | Power |
| `R22` | 1.5k | Power |
| `R23` | 1k | Power |
| `R24` | 3.3k | Power |
| `R25` | 3.3k | Power |
| `R26` | 2.2k | Power |
| `R27` | 12k | Power |
| `R28` | 1.2k | Power |
| `R29` | 2k | Power |
| `R30` | 5.6 | Power |
| `R31` | 10k | CPU |
| `R32` | 100 | CPU |
| `R33` | 1M | Cassette Interface |
| `R34` | 10k | Cassette Interface |
| `R35` | 680k | Cassette Interface |
| `R36` | 1.8M | Cassette Interface |
| `R37` | 220 | Cassette Interface |
| `R38` | 360k | Cassette Interface |
| `R39` | 10 | Cassette Interface |
| `R40` | 4.7k | Cassette Interface |
| `R41` | 4.7k | Card-Edge Interface |
| `R42` | 360k | Cassette Interface |
| `R43` | 560k | Cassette Interface |
| `R44` | 470k | Cassette Interface |
| `R45` | 470k | Cassette Interface |
| `R46` | 470k | Cassette Interface |
| `R47` | 470k | Cassette Interface |
| `R48` | 4.7k | Video Access Multiplexer |
| `R49` | 10k | CPU |
| `R50` | 470k | Cassette Interface |
| `R51` | 1M | Cassette Interface |
| `R52` | 8.2k | Cassette Interface |
| `R53` | 8.2k | Cassette Interface |
| `R54` | 4.7k |  |
| `R55` | 4.7k | Card-Edge Interface |
| `R56` | 910 | Clock |
| `R57` | 910 | Clock |
| `R64` | 4.7k | Video Sync |
| `R65` | 4.7k | Cassette Interface |
| `R66` | 4.7k | Video Latch |
| `R67` | 4.7k | Cassette Interface |
| `R68` | 4.7k | Video Generator |
| `R69` | 4.7k | RAM |
| `R70` | 4.7k | Address Decoder |
| `R71` | 4.7k | Address Decoder |
| `R72` | 4.7k | Address Decoder |
| `R74` | 4.7k |  |
| `R75` | 330 | CPU |
| `R76` | 4.7k | RAM |
| `R77` | 4.7k | Card-Edge Interface |
| `R101` | 330 | RAM |
| `R102` | 330 | RAM |
| `R103` | 330 | RAM |
| `R104` | 330 | RAM |
| `R105` | 330 | RAM |
| `R106` | 330 | RAM |
| `R107` | 330 | RAM |
| `R108` | 330 | RAM |
| `R109` | 330 | RAM |
| `R110` | 330 | RAM |
| `RP1` | 4.7k | CPU Gating |
| `RP2` | 4.7k | RAM-ROM Interface |
| `S1` | ~ | Power |
| `S2` | Reset | CPU |
| `TP1` | ~ | Power |
| `Y1` | 10.6445 MHz | Clock |
| `Z1` | LM723C | Power |
| `Z2` | LM723C | Power |
| `Z3` | 75452 | Cassette Interface |
| `Z4` | 74LS175 | Cassette Interface |
| `Z5` | 74LS10 | Video Counter |
| `Z6` | 74LS92 | Video Mode |
| `Z7` | 74LS93 | Video Counter |
| `Z8` | 74LS157 | Video Access Multiplexer |
| `Z9` | SRAM_2114 | Video RAM |
| `Z10` | SRAM_2114 | Video RAM |
| `Z11` | 74LS174 | Video Latch |
| `Z12` | 74LS245 | Video RAM |
| `Z13` | 74LS157 | RAM |
| `Z14` | 74LS157 | RAM |
| `Z15` | DRAM_4116 | RAM |
| `Z16` | DRAM_4116 | RAM |
| `Z17` | DRAM_4116 | RAM |
| `Z18` | DRAM_4116 | RAM |
| `Z19` | DRAM_4116 | RAM |
| `Z20` | DRAM_4116 | RAM |
| `Z21` | DRAM_4116 | RAM |
| `Z22` | DRAM_4116 | RAM |
| `Z23` | 74LS245 | CPU Gating |
| `Z24` | 74LS367 | RAM-ROM Interface |
| `Z25` | LM3900 | Cassette Interface |
| `Z26` | 74LS14 | Video Counter |
| `Z27` | 74LS157 | Video Mode |
| `Z28` | 74LS93 | Video Counter |
| `Z29` | 74LS157 | Video Access Multiplexer |
| `Z30` | 74LS367 | CPU Gating |
| `Z31` | 74LS132 | Cassette Interface |
| `Z32` | 74C00 | Video Sync |
| `Z33` | 74LS04 | Video Sync |
| `Z34` | 74LS93 | Video Counter |
| `Z35` | 74LS93 | Video Counter |
| `Z36` | 74LS157 | Video Access Multiplexer |
| `Z37` | MCM6670 | Video Generator |
| `Z38` | MCM6670 | Video Generator |
| `Z39` | 74LS153 | Video Generator |
| `Z40` | 74LS32 | Address Decoder |
| `Z41` | 74LS30 | Cassette Interface |
| `Z42` | 2364_20L | ROM |
| `Z43` | 2332_20L_21L | ROM |
| `Z44` | 74LS00 | CPU |
| `Z45` | 74LS02 | CPU |
| `Z46` | 74LS04 |  |
| `Z47` | 74LS132 | CPU |
| `Z48` | Z80CPU | CPU |
| `Z49` | 74LS244 | CPU Gating |
| `Z50` | 7404 | Clock |
| `Z51` | 74LS08 | Video RAM |
| `Z52` | 74LS08 | Video Sync |
| `Z53` | 74LS74 | Cassette Interface |
| `Z54` | 74LS02 | Video Latch |
| `Z55` | 74LS20 | Video Generator |
| `Z56` | 74LS175 | Video Latch |
| `Z57` | 74LS166 | Video Generator |
| `Z58` | 74LS166 | Video Generator |
| `Z59` | 74LS367 | RAM |
| `Z60` | 74LS11 | Address Decoder |
| `Z61` | 74LS139 | Address Decoder |
| `Z62` | 74LS74 | CPU |
| `Z63` | 74LS74 | CPU |
| `Z64` | 74LS32 | CPU |
| `Z65` | 74LS92 | Clock |
| `Z66` | 74LS367 | CPU |
| `Z67` | 74LS32 | CPU |
| `Z68` | 74LS244 | CPU Gating |

## Connections

For each pin: its name, its net, and what else is on that net. Nets with more than 12 pins (power, ground, buses) are named rather than expanded.

```
C1  (10uF 16V, Cassette Interface)
   pin   1                Net-(C1-Pad1)                R33.1 R34.1 R35.1 R36.2
   pin   2                GND                          [net GND, 176 pins]

C2  (0.1uF 12V, Cassette Interface)
   pin   1                Net-(C2-Pad1)                R1.1
   pin   2                Net-(C2-Pad2)                J3.3 K1.3

C3  (0.01uF 24V, Video Mixer)
   pin   1                Net-(Q1-C)                   C4.1 Q1.2(C) R7.2
   pin   2                GND                          [net GND, 176 pins]

C4  (10uF 16V, Video Mixer)
   pin   1                Net-(Q1-C)                   C3.1 Q1.2(C) R7.2
   pin   2                GND                          [net GND, 176 pins]

C5  (220uF 16V, Power)
   pin   1                GND                          [net GND, 176 pins]
   pin   2                Net-(C5-Pad2)                R12.2 S1.10

C6  (10uF 16V, Power)
   pin   1                GND                          [net GND, 176 pins]
   pin   2                -5V                          [net -5V, 18 pins]

C7  (0.01uF 24V, Power)
   pin   1                -5V                          [net -5V, 18 pins]
   pin   2                GND                          [net GND, 176 pins]

C8  (0.1uF 12V, Capacitors)
   pin   1                -5V                          [net -5V, 18 pins]
   pin   2                GND                          [net GND, 176 pins]

C9  (2200uF 35V, Power)
   pin   1                Net-(Q6-E)                   Q6.3(E) R28.1 S1.3 Z2.12(V+)
   pin   2                GND                          [net GND, 176 pins]

C10  (10000uF 16V, Power)
   pin   1                Net-(Q4-E)                   Q4.2(E) R13.1 S1.6 S1.7
   pin   2                GND                          [net GND, 176 pins]

C11  (1nF, Power)
   pin   1                Net-(Z1--)                   R19.2 Z1.4(-)
   pin   2                Net-(Z1-FC)                  Z1.13(FC)

C12  (10uF 16V, Power)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C13  (0.01uF 24V, Power)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C14  (10uF 16V, Power)
   pin   1                +12V                         [net +12V, 20 pins]
   pin   2                GND                          [net GND, 176 pins]

C15  (0.01uF 24V, Power)
   pin   1                +12V                         [net +12V, 20 pins]
   pin   2                GND                          [net GND, 176 pins]

C16  (1nF, Power)
   pin   1                Net-(Z2-FC)                  Z2.13(FC)
   pin   2                Net-(Z2--)                   R23.2(2) Z2.4(-)

C17  (220pF, Cassette Interface)
   pin   1                CASSIN                       J3.4 R37.2
   pin   2                Net-(C17-Pad2)               C18.1 R42.1

C18  (220pF, Cassette Interface)
   pin   1                Net-(C17-Pad2)               C17.2 R42.1
   pin   2                Net-(C18-Pad2)               R38.1

C19  (100uF 16V, Cassette Interface)
   pin   1                GND                          [net GND, 176 pins]
   pin   2                Net-(Z25E-V+)                R39.1 Z25.14(V+)

C20  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C22  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C23  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C24  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C25  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C26  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C27  (0.1uF 25V, Capacitors)
   pin   1                +12V                         [net +12V, 20 pins]
   pin   2                GND                          [net GND, 176 pins]

C28  (0.1uF 12V, Capacitors)
   pin   1                -5V                          [net -5V, 18 pins]
   pin   2                GND                          [net GND, 176 pins]

C29  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C30  (0.1uF 25V, Capacitors)
   pin   1                +12V                         [net +12V, 20 pins]
   pin   2                GND                          [net GND, 176 pins]

C31  (0.1uF 12V, Capacitors)
   pin   1                -5V                          [net -5V, 18 pins]
   pin   2                GND                          [net GND, 176 pins]

C32  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C33  (0.1uF 25V, Capacitors)
   pin   1                +12V                         [net +12V, 20 pins]
   pin   2                GND                          [net GND, 176 pins]

C34  (0.1uF 12V, Capacitors)
   pin   1                -5V                          [net -5V, 18 pins]
   pin   2                GND                          [net GND, 176 pins]

C35  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C36  (0.1uF 25V, Capacitors)
   pin   1                +12V                         [net +12V, 20 pins]
   pin   2                GND                          [net GND, 176 pins]

C37  (0.1uF 12V, Capacitors)
   pin   1                -5V                          [net -5V, 18 pins]
   pin   2                GND                          [net GND, 176 pins]

C38  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C39  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C40  (10uF 16V, CPU)
   pin   1                Net-(C40-Pad1)               R31.2 R32.1 Z47.4
   pin   2                GND                          [net GND, 176 pins]

C41  (0.1uF 12V, Cassette Interface)
   pin   1                GND                          [net GND, 176 pins]
   pin   2                Net-(CR8-K)                  CR8.1(K) R47.1

C43  (100pF, Video Mixer)
   pin   1                Net-(Q2-B)                   Q2.3(B) R11.2
   pin   2                SYNC                         R11.1 Z32.3

C44  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C45  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C46  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C47  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C48  (1nF, Cassette Interface)
   pin   1                GND                          [net GND, 176 pins]
   pin   2                Net-(CR5-K)                  CR5.1(K) CR6.1(K) R50.1

C49  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C50  (2.7nF, Cassette Interface)
   pin   1                Net-(C50-Pad1)               R52.1 R53.2 Z31.10
   pin   2                Net-(C50-Pad2)               Z25.9

C51  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C52  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C53  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C54  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C55  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C56  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C57  (1nF, CPU)
   pin   1                GND                          [net GND, 176 pins]
   pin   2                Net-(C57-Pad2)               Z45.11 Z45.8 Z45.9 Z47.6

C58  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C59  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C60  (47pF, Clock)
   pin   1                Net-(C60-Pad1)               R57.1 Z50.3
   pin   2                Net-(C60-Pad2)               R56.2 Z50.6 Z50.9

C63  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C64  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C65  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C66  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C67  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C68  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C69  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C70  (22uF 16V, CPU)
   pin   1                Net-(C70-Pad1)               R49.2 Z47.1 Z47.2
   pin   2                GND                          [net GND, 176 pins]

C71  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

C72  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                GND                          [net GND, 176 pins]

CN1  (Connection Mainboard Side, Keyboard)
   pin   1 Pin_1          +5V                          [net +5V, 138 pins]
   pin   2 Pin_2          A4                           J4.31(Pin_31) Z13.2(I0a) Z29.11(I0c) Z41.11 Z42.4(A4) Z43.4(A4) Z68.5(O2b)
   pin   3 Pin_3          A5                           J4.35(Pin_35) Z13.5(I0b) Z29.2(I0a) Z41.12 Z42.3(A5) Z43.3(A5) Z68.16(O1a)
   pin   4 Pin_4          A1                           J4.27(Pin_27) Z14.5(I0b) Z36.2(I0a) Z41.5 Z42.7(A1) Z43.7(A1) Z68.12(O3a)
   pin   5 Pin_5          A0                           J4.25(Pin_25) Z14.2(I0a) Z36.11(I0c) Z41.6 Z42.8(A0) Z43.8(A0) Z68.9(O0b)
   pin   6 Pin_6          A2                           J4.40(Pin_40) Z14.11(I0c) Z36.14(I0d) Z41.4 Z42.6(A2) Z43.6(A2) Z68.7(O1b)
   pin   7 Pin_7          A6                           J4.38(Pin_38) Z13.11(I0c) Z41.2 Z42.2(A6) Z43.2(A6) Z68.3(O3b) Z8.11(I0c)
   pin   8 Pin_8          A7                           J4.36(Pin_36) Z14.3(I1a) Z41.1 Z42.1(A7) Z43.1(A7) Z68.18(O0a) Z8.14(I0d)
   pin   9 Pin_9          A3                           J4.34(Pin_34) Z14.14(I0d) Z36.5(I0b) Z41.3 Z42.5(A3) Z43.5(A3) Z68.14(O2a)
   pin  10 Pin_10         ~{KYBD}                      Z60.4 Z61.10(O2)
   pin  11 Pin_11         KBD0                         RP2.3(R2) Z22.14(OUT) Z24.14 Z42.9(D0) Z43.9(D0)
   pin  12 Pin_12         KBD1                         RP2.2(R1) Z21.14(OUT) Z24.2 Z42.10(D1) Z43.10(D1)
   pin  13 Pin_13         KBD2                         RP2.5(R4) Z20.14(OUT) Z24.12 Z42.11(D2) Z43.11(D2)
   pin  14 Pin_14         KBD3                         RP2.7(R6) Z19.14(OUT) Z30.12 Z42.13(D3) Z43.13(D3)
   pin  15 Pin_15         KBD4                         RP2.9(R8) Z18.14(OUT) Z30.14 Z42.14(D4) Z43.14(D4)
   pin  16 Pin_16         KBD5                         RP2.8(R7) Z17.14(OUT) Z24.10 Z42.15(D5) Z43.15(D5)
   pin  17 Pin_17         KBD6                         RP2.6(R5) Z16.14(OUT) Z24.6 Z42.16(D6) Z43.16(D6)
   pin  18 Pin_18         KBD7                         RP2.4(R3) Z15.14(OUT) Z24.4 Z42.17(D7) Z43.17(D7)
   pin  19 Pin_19         GND                          [net GND, 176 pins]

CN2  (Conn_01x09, Keyboard ROM Selector)
   pin   1 Pin_1          A8                           J4.11(Pin_11) Z14.6(I1b) Z42.23(A8) Z43.23(A8) Z49.14(O2a) Z8.2(I0a)
   pin   2 Pin_2          A9                           J4.17(Pin_17) Z14.10(I1c) Z42.22(A9) Z43.22(A9) Z49.16(O1a) Z8.5(I0b)
   pin   3 Pin_3          A10                          J4.4(Pin_4) Z14.13(I1d) Z42.19(A10) Z43.19(A10) Z49.18(O0a) Z61.14(A0)
   pin   4 Pin_4          A11                          J4.9(Pin_9) Z13.3(I1a) Z42.18(A11) Z43.18(A11) Z49.3(O3b) Z61.13(A1)
   pin   5 Pin_5          ~{CS1}                       Z60.10 Z60.11 Z61.4(O0)
   pin   6 Pin_6          ~{CS2}                       JP1.1(A) Z61.5(O1)
   pin   7 Pin_7          ~{CS3}                       JP2.1(A) Z61.6(O2)
   pin   8 Pin_8          ~{CS4}                       JP3.1(A) Z61.12(O0)
   pin   9 Pin_9          ~{SYSRES}                    J4.2(Pin_2) Z45.13

CR1  (MDA202, Power)
   pin   1 +              Net-(CR1-+)                  S1.4 S1.5 S1.8 S1.9
   pin   2                Net-(CR1-Pad2)               J1.3
   pin   3                Net-(CR1-Pad3)               J1.1
   pin   4 -              Net-(CR1--)                  S1.11 S1.12

CR2  (1N4735, Power)
   pin   1 K              +5V                          [net +5V, 138 pins]
   pin   2 A              GND                          [net GND, 176 pins]

CR3  (1N5231, Power)
   pin   1 K              GND                          [net GND, 176 pins]
   pin   2 A              -5V                          [net -5V, 18 pins]

CR4  (1N4148, Cassette Interface)
   pin   1 K              +5V                          [net +5V, 138 pins]
   pin   2 A              Net-(CR4-A)                  K1.2 Z3.5(2Y)

CR5  (1N4148, Cassette Interface)
   pin   1 K              Net-(CR5-K)                  C48.2 CR6.1(K) R50.1
   pin   2 A              Net-(CR5-A)                  R42.2 R43.1 R44.1 Z25.4

CR6  (1N4148, Cassette Interface)
   pin   1 K              Net-(CR5-K)                  C48.2 CR5.1(K) R50.1
   pin   2 A              Net-(CR6-A)                  R45.2 Z25.5

CR7  (1N4148, Cassette Interface)
   pin   1 K              Net-(CR7-K)                  CR8.2(A)
   pin   2 A              Net-(CR7-A)                  R46.1 R51.2 Z25.10

CR8  (1N4148, Cassette Interface)
   pin   1 K              Net-(CR8-K)                  C41.2 R47.1
   pin   2 A              Net-(CR7-K)                  CR7.1(K)

J1  (Front View, Power)
   pin   1                Net-(CR1-Pad3)               CR1.3
   pin   2                Net-(J1-Pad2)                S1.1 S1.2
   pin   3                Net-(CR1-Pad2)               CR1.2
   pin   4                GND                          [net GND, 176 pins]
   pin   5                unconnected-(J1-Pad5)        (no other connection)

J2  (Front View, Video Mixer)
   pin   1                Net-(JP9-B)                  JP9.2(B)
   pin   2                unconnected-(J2-Pad2)        (no other connection)
   pin   3                unconnected-(J2-Pad3)        (no other connection)
   pin   4                Net-(Q1-E)                   Q1.1(E) R6.1
   pin   5                GND                          [net GND, 176 pins]

J3  (Front View, Cassette Interface)
   pin   1                Net-(J3-Pad1)                K1.4 R1.2
   pin   2                GND                          [net GND, 176 pins]
   pin   3                Net-(C2-Pad2)                C2.2 K1.3
   pin   4                CASSIN                       C17.1 R37.2
   pin   5                CASSOUT                      R2.2 R3.2 R4.1

J4  (Edge Connector, Card-Edge Interface)
   pin   1 Pin_1          ~{RAS}                       Z64.4 Z66.12 Z66.3
   pin   2 Pin_2          ~{SYSRES}                    CN2.9(Pin_9) Z45.13
   pin   3 Pin_3          ~{CAS}                       Z59.14 Z66.7
   pin   4 Pin_4          A10                          CN2.3(Pin_3) Z14.13(I1d) Z42.19(A10) Z43.19(A10) Z49.18(O0a) Z61.14(A0)
   pin   5 Pin_5          A12                          Z13.6(I1b) Z42.21(A12) Z43.21(~{CE2}) Z49.5(O2b) Z61.2(A0)
   pin   6 Pin_6          A13                          Z13.10(I1c) Z49.7(O1b) Z61.3(A1)
   pin   7 Pin_7          A15                          Z49.9(O0b) Z64.5
   pin   8 Pin_8          GND                          [net GND, 176 pins]
   pin   9 Pin_9          A11                          CN2.4(Pin_4) Z13.3(I1a) Z42.18(A11) Z43.18(A11) Z49.3(O3b) Z61.13(A1)
   pin  10 Pin_10         A14                          Z44.12 Z44.13 Z49.12(O3a) Z64.1
   pin  11 Pin_11         A8                           CN2.1(Pin_1) Z14.6(I1b) Z42.23(A8) Z43.23(A8) Z49.14(O2a) Z8.2(I0a)
   pin  12 Pin_12         ~{OUT}                       Z30.7 Z40.5
   pin  13 Pin_13         ~{WR}                        R110.2 Z29.14(I0d) Z30.3
   pin  14 Pin_14         ~{INTAK}                     Z64.8
   pin  15 Pin_15         ~{RD}                        Z29.5(I0b) Z30.5 Z40.10
   pin  16 Pin_16         MUX                          Z13.1(S) Z14.1(S) Z66.5
   pin  17 Pin_17         A9                           CN2.2(Pin_2) Z14.10(I1c) Z42.22(A9) Z43.22(A9) Z49.16(O1a) Z8.5(I0b)
   pin  18 Pin_18         D4                           RP1.2(R1) Z12.16(B2) Z18.2(IN) Z23.12(B6) Z30.13
   pin  19 Pin_19         ~{IN}                        Z30.9 Z40.1
   pin  20 Pin_20         D7                           RP1.3(R2) Z12.13(B5) Z15.2(IN) Z23.16(B2) Z24.5 Z53.2(D) Z59.5
   pin  21 Pin_21         ~{INT}                       R77.2 Z48.16(~{INT})
   pin  22 Pin_22         D1                           RP1.4(R3) Z12.11(B7) Z21.2(IN) Z23.18(B0) Z24.3 Z4.12(D2)
   pin  23 Pin_23         ~{TEST}                      R55.2 Z46.11 Z47.10 Z48.25(~{BUSRQ})
   pin  24 Pin_24         D6                           RP1.5(R4) Z12.14(B4) Z16.2(IN) Z23.14(B4) Z24.7 Z59.3
   pin  25 Pin_25         A0                           CN1.5(Pin_5) Z14.2(I0a) Z36.11(I0c) Z41.6 Z42.8(A0) Z43.8(A0) Z68.9(O0b)
   pin  26 Pin_26         D3                           RP1.9(R8) Z12.17(B1) Z19.2(IN) Z23.11(B7) Z30.11 Z4.5(D1)
   pin  27 Pin_27         A1                           CN1.4(Pin_4) Z14.5(I0b) Z36.2(I0a) Z41.5 Z42.7(A1) Z43.7(A1) Z68.12(O3a)
   pin  28 Pin_28         D5                           RP1.6(R5) Z12.15(B3) Z17.2(IN) Z23.13(B5) Z24.9
   pin  29 Pin_29         GND                          [net GND, 176 pins]
   pin  30 Pin_30         D0                           RP1.7(R6) Z12.12(B6) Z22.2(IN) Z23.17(B1) Z24.13 Z4.13(D3)
   pin  31 Pin_31         A4                           CN1.2(Pin_2) Z13.2(I0a) Z29.11(I0c) Z41.11 Z42.4(A4) Z43.4(A4) Z68.5(O2b)
   pin  32 Pin_32         D2                           RP1.8(R7) Z12.18(B0) Z20.2(IN) Z23.15(B3) Z24.11 Z4.4(D0)
   pin  33 Pin_33         ~{WAIT}                      R41.2 Z48.24(~{WAIT})
   pin  34 Pin_34         A3                           CN1.9(Pin_9) Z14.14(I0d) Z36.5(I0b) Z41.3 Z42.5(A3) Z43.5(A3) Z68.14(O2a)
   pin  35 Pin_35         A5                           CN1.3(Pin_3) Z13.5(I0b) Z29.2(I0a) Z41.12 Z42.3(A5) Z43.3(A5) Z68.16(O1a)
   pin  36 Pin_36         A7                           CN1.8(Pin_8) Z14.3(I1a) Z41.1 Z42.1(A7) Z43.1(A7) Z68.18(O0a) Z8.14(I0d)
   pin  37 Pin_37         GND                          [net GND, 176 pins]
   pin  38 Pin_38         A6                           CN1.7(Pin_7) Z13.11(I0c) Z41.2 Z42.2(A6) Z43.2(A6) Z68.3(O3b) Z8.11(I0c)
   pin  39 Pin_39         GND                          [net GND, 176 pins]
   pin  40 Pin_40         A2                           CN1.6(Pin_6) Z14.11(I0c) Z36.14(I0d) Z41.4 Z42.6(A2) Z43.6(A2) Z68.7(O1b)

JP1  (TRS80_Model_I_Jumper_2_Jap, Address Decoder)
   pin   1 A              ~{CS2}                       CN2.6(Pin_6) Z61.5(O1)
   pin   2 B              Net-(JP1-B)                  R71.1 Z60.9

JP2  (TRS80_Model_I_Jumper_2_Jap, Address Decoder)
   pin   1 A              ~{CS3}                       CN2.7(Pin_7) Z61.6(O2)
   pin   2 B              ~{ROMB}                      R72.1 Z43.20(~{CE1}) Z60.2

JP3  (TRS80_Model_I_Jumper_2_Jap, Address Decoder)
   pin   1 A              ~{CS4}                       CN2.8(Pin_8) Z61.12(O0)
   pin   2 B              Net-(JP3-B)                  R70.1 Z60.5

JP4  (TRS80_Model_I_Jumper_3_Jap, Cassette Interface)
   pin   1 A              Net-(JP4-A-Pad1)             R65.1
   pin   2 B              Net-(JP4-B)                  Z53.4(~{S})
   pin   3 A              GND                          [net GND, 176 pins]

JP5  (TRS80_Model_I_Jumper_3_Jap, Cassette Interface)
   pin   1 A              GND                          [net GND, 176 pins]
   pin   2 B              Net-(JP5-B)                  Z53.1(~{R})
   pin   3 A              Net-(JP5-A-Pad3)             R67.1

JP6  (TRS80_Model_I_Jumper_3_Jap, Video Counter)
   pin   1 A              R2                           JP8.3(A) Z7.9(Q1) Z8.3(I1a)
   pin   2 B              Net-(JP6-B)                  Z5.2
   pin   3 A              R3                           Z7.8(Q2) Z8.6(I1b)

JP7  (TRS80_Model_I_Jumper_3_Jap, Video Sync)
   pin   1 A              R1                           Z33.11 Z5.13 Z7.1(CP1..3) Z7.12(Q0) Z8.13(I1d)
   pin   2 B              Net-(JP7-B)                  Z52.1
   pin   3 A              Net-(JP7-A-Pad3)             Z33.10

JP8  (TRS80_Model_I_Jumper_3_Jap, Video Sync)
   pin   1 A              Net-(JP8-A-Pad1)             R64.2
   pin   2 B              Net-(JP8-B)                  Z52.10
   pin   3 A              R2                           JP6.1(A) Z7.9(Q1) Z8.3(I1a)

JP9  (TRS80_Model_I_Jumper_2_Jap, Video Mixer)
   pin   1 A              +5V                          [net +5V, 138 pins]
   pin   2 B              Net-(JP9-B)                  J2.1

JP10  (TRS80_Model_I_Jumper_3_Jap, Video Counter)
   pin   1 A              L2                           Z35.8(Q2) Z37.8(R2) Z38.8(R2) Z39.14(S0) Z5.3
   pin   2 B              Net-(JP10-B)                 Z5.4
   pin   3 A              Net-(JP10-A-Pad3)            Z46.4

K1  (Relay_SPDT, Cassette Interface)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(CR4-A)                  CR4.2(A) Z3.5(2Y)
   pin   3                Net-(C2-Pad2)                C2.2 J3.3
   pin   4                Net-(J3-Pad1)                J3.1 R1.2
   pin   5                unconnected-(K1-Pad5)        (no other connection)

Q1  (C1815, Video Mixer)
   pin   1 E              Net-(Q1-E)                   J2.4 R6.1
   pin   2 C              Net-(Q1-C)                   C3.1 C4.1 R7.2
   pin   3 B              Net-(Q1-B)                   R10.2 R8.1 R9.1

Q2  (A1015, Video Mixer)
   pin   1 E              +5V                          [net +5V, 138 pins]
   pin   2 C              Net-(Q2-C)                   R10.1
   pin   3 B              Net-(Q2-B)                   C43.1 R11.2

Q3  (TIP29A, Power)
   pin   1 B              Net-(Q3-B)                   R14.1 Z1.10(Vout)
   pin   2 C              Net-(Q3-C)                   Q4.1(B) R13.2
   pin   3 E              Net-(Q3-E)                   Q4.3(C) R14.2 R15.1 R16.1

Q4  (2N6594, Power)
   pin   1 B              Net-(Q3-C)                   Q3.2(C) R13.2
   pin   2 E              Net-(Q4-E)                   C10.1 R13.1 S1.6 S1.7
   pin   3 C              Net-(Q3-E)                   Q3.3(E) R14.2 R15.1 R16.1

Q5  (A1015, Power)
   pin   1 E              Net-(Q5-E)                   R17.2(2) Z1.5(+)
   pin   2 C              Net-(Q5-C)                   R21.2
   pin   3 B              Net-(Q5-B)                   R20.1

Q6  (MJE34, Power)
   pin   1 B              Net-(Q6-B)                   R28.2 Z2.11(VC)
   pin   2 C              Net-(Q6-C)                   R29.1 R30.2 Z2.10(Vout)
   pin   3 E              Net-(Q6-E)                   C9.1 R28.1 S1.3 Z2.12(V+)

R1  (100, Cassette Interface)
   pin   1                Net-(C2-Pad1)                C2.1
   pin   2                Net-(J3-Pad1)                J3.1 K1.4

R2  (1.2k, Cassette Interface)
   pin   1                GND                          [net GND, 176 pins]
   pin   2                CASSOUT                      J3.5 R3.2 R4.1

R3  (7.5k, Cassette Interface)
   pin   1                Net-(Z4-Q3)                  Z4.15(Q3)
   pin   2                CASSOUT                      J3.5 R2.2 R4.1

R4  (7.5k, Cassette Interface)
   pin   1                CASSOUT                      J3.5 R2.2 R3.2
   pin   2                Net-(Z4-~{Q2})               R5.1 Z4.11(~{Q2})

R5  (220k, Cassette Interface)
   pin   1                Net-(Z4-~{Q2})               R4.2 Z4.11(~{Q2})
   pin   2                +5V                          [net +5V, 138 pins]

R6  (75, Video Mixer)
   pin   1                Net-(Q1-E)                   J2.4 Q1.1(E)
   pin   2                GND                          [net GND, 176 pins]

R7  (47, Video Mixer)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(Q1-C)                   C3.1 C4.1 Q1.2(C)

R8  (330, Video Mixer)
   pin   1                Net-(Q1-B)                   Q1.3(B) R10.2 R9.1
   pin   2                GND                          [net GND, 176 pins]

R9  (120, Video Mixer)
   pin   1                Net-(Q1-B)                   Q1.3(B) R10.2 R8.1
   pin   2                Net-(Z3A-1Y)                 Z3.3(1Y)

R10  (270, Video Mixer)
   pin   1                Net-(Q2-C)                   Q2.2(C)
   pin   2                Net-(Q1-B)                   Q1.3(B) R8.1 R9.1

R11  (10k, Video Mixer)
   pin   1                SYNC                         C43.2 Z32.3
   pin   2                Net-(Q2-B)                   C43.1 Q2.3(B)

R12  (220, Power)
   pin   1                -5V                          [net -5V, 18 pins]
   pin   2                Net-(C5-Pad2)                C5.2 S1.10

R13  (68, Power)
   pin   1                Net-(Q4-E)                   C10.1 Q4.2(E) S1.6 S1.7
   pin   2                Net-(Q3-C)                   Q3.2(C) Q4.1(B)

R14  (2.7k, Power)
   pin   1                Net-(Q3-B)                   Q3.1(B) Z1.10(Vout)
   pin   2                Net-(Q3-E)                   Q3.3(E) Q4.3(C) R15.1 R16.1

R15  (750, Power)
   pin   1                Net-(Q3-E)                   Q3.3(E) Q4.3(C) R14.2 R16.1
   pin   2                Net-(Z1-ILIM)                R21.1 Z1.2(ILIM)

R16  (0.33, Power)
   pin   1                Net-(Q3-E)                   Q3.3(E) Q4.3(C) R14.2 R15.1
   pin   2                +5V                          [net +5V, 138 pins]

R17  (1k, Power)
   pin   1 1              Net-(R17-Pad1)               R18.1
   pin   2 2              Net-(Q5-E)                   Q5.1(E) Z1.5(+)
   pin   3 3              Net-(R17-Pad3)               R24.1

R18  (1.2k, Power)
   pin   1                Net-(R17-Pad1)               R17.1(1)
   pin   2                Net-(Z1-VREF)                Z1.6(VREF)

R19  (1.2k, Power)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(Z1--)                   C11.1 Z1.4(-)

R20  (100k, Power)
   pin   1                Net-(Q5-B)                   Q5.3(B)
   pin   2                +5V                          [net +5V, 138 pins]

R21  (3.3k, Power)
   pin   1                Net-(Z1-ILIM)                R15.2 Z1.2(ILIM)
   pin   2                Net-(Q5-C)                   Q5.2(C)

R22  (1.5k, Power)
   pin   1                Net-(Z2-VREF)                Z2.6(VREF)
   pin   2                Net-(Z2-+)                   Z2.5(+)

R23  (1k, Power)
   pin   1 1              Net-(R23-Pad1)               R25.1
   pin   2 2              Net-(Z2--)                   C16.2 Z2.4(-)
   pin   3 3              Net-(R23-Pad3)               R26.2

R24  (3.3k, Power)
   pin   1                Net-(R17-Pad3)               R17.3(3)
   pin   2                GND                          [net GND, 176 pins]

R25  (3.3k, Power)
   pin   1                Net-(R23-Pad1)               R23.1(1)
   pin   2                GND                          [net GND, 176 pins]

R26  (2.2k, Power)
   pin   1                +12V                         [net +12V, 20 pins]
   pin   2                Net-(R23-Pad3)               R23.3(3)

R27  (12k, Power)
   pin   1                Net-(Z2-ILIM)                R29.2 Z2.2(ILIM)
   pin   2                GND                          [net GND, 176 pins]

R28  (1.2k, Power)
   pin   1                Net-(Q6-E)                   C9.1 Q6.3(E) S1.3 Z2.12(V+)
   pin   2                Net-(Q6-B)                   Q6.1(B) Z2.11(VC)

R29  (2k, Power)
   pin   1                Net-(Q6-C)                   Q6.2(C) R30.2 Z2.10(Vout)
   pin   2                Net-(Z2-ILIM)                R27.1 Z2.2(ILIM)

R30  (5.6, Power)
   pin   1                +12V                         [net +12V, 20 pins]
   pin   2                Net-(Q6-C)                   Q6.2(C) R29.1 Z2.10(Vout)

R31  (10k, CPU)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(C40-Pad1)               C40.1 R32.1 Z47.4

R32  (100, CPU)
   pin   1                Net-(C40-Pad1)               C40.1 R31.2 Z47.4
   pin   2                Net-(R32-Pad2)               S2.4

R33  (1M, Cassette Interface)
   pin   1                Net-(C1-Pad1)                C1.1 R34.1 R35.1 R36.2
   pin   2                Net-(Z25D-+)                 Z25.12(+)

R34  (10k, Cassette Interface)
   pin   1                Net-(C1-Pad1)                C1.1 R33.1 R35.1 R36.2
   pin   2                +5V                          [net +5V, 138 pins]

R35  (680k, Cassette Interface)
   pin   1                Net-(C1-Pad1)                C1.1 R33.1 R34.1 R36.2
   pin   2                Net-(Z25A-+)                 Z25.1(+)

R36  (1.8M, Cassette Interface)
   pin   1                Net-(Z25B-+)                 R38.2 Z25.2(+)
   pin   2                Net-(C1-Pad1)                C1.1 R33.1 R34.1 R35.1

R37  (220, Cassette Interface)
   pin   1                GND                          [net GND, 176 pins]
   pin   2                CASSIN                       C17.1 J3.4

R38  (360k, Cassette Interface)
   pin   1                Net-(C18-Pad2)               C18.2
   pin   2                Net-(Z25B-+)                 R36.1 Z25.2(+)

R39  (10, Cassette Interface)
   pin   1                Net-(Z25E-V+)                C19.2 Z25.14(V+)
   pin   2                +5V                          [net +5V, 138 pins]

R40  (4.7k, Cassette Interface)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(Z4-~{Mr})               Z4.1(~{Mr})

R41  (4.7k, Card-Edge Interface)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                ~{WAIT}                      J4.33(Pin_33) Z48.24(~{WAIT})

R42  (360k, Cassette Interface)
   pin   1                Net-(C17-Pad2)               C17.2 C18.1
   pin   2                Net-(CR5-A)                  CR5.2(A) R43.1 R44.1 Z25.4

R43  (560k, Cassette Interface)
   pin   1                Net-(CR5-A)                  CR5.2(A) R42.2 R44.1 Z25.4
   pin   2                Net-(Z25B--)                 Z25.3(-)

R44  (470k, Cassette Interface)
   pin   1                Net-(CR5-A)                  CR5.2(A) R42.2 R43.1 Z25.4
   pin   2                Net-(Z25A--)                 R45.1 Z25.6(-)

R45  (470k, Cassette Interface)
   pin   1                Net-(Z25A--)                 R44.2 Z25.6(-)
   pin   2                Net-(CR6-A)                  CR6.2(A) Z25.5

R46  (470k, Cassette Interface)
   pin   1                Net-(CR7-A)                  CR7.2(A) R51.2 Z25.10
   pin   2                Net-(Z25C-+)                 Z25.13(+)

R47  (470k, Cassette Interface)
   pin   1                Net-(CR8-K)                  C41.2 CR8.1(K)
   pin   2                Net-(Z25C--)                 Z25.8(-)

R48  (4.7k, Video Access Multiplexer)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(Z29-I1b)                Z29.13(I1d) Z29.6(I1b)

R49  (10k, CPU)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(C70-Pad1)               C70.1 Z47.1 Z47.2

R50  (470k, Cassette Interface)
   pin   1                Net-(CR5-K)                  C48.2 CR5.1(K) CR6.1(K)
   pin   2                Net-(Z25D--)                 R51.1 Z25.11(-)

R51  (1M, Cassette Interface)
   pin   1                Net-(Z25D--)                 R50.2 Z25.11(-)
   pin   2                Net-(CR7-A)                  CR7.2(A) R46.1 Z25.10

R52  (8.2k, Cassette Interface)
   pin   1                Net-(C50-Pad1)               C50.1 R53.2 Z31.10
   pin   2                +5V                          [net +5V, 138 pins]

R53  (8.2k, Cassette Interface)
   pin   1                GND                          [net GND, 176 pins]
   pin   2                Net-(C50-Pad1)               C50.1 R52.1 Z31.10

R54  (4.7k, )
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(R54-Pad2)               Z46.9

R55  (4.7k, Card-Edge Interface)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                ~{TEST}                      J4.23(Pin_23) Z46.11 Z47.10 Z48.25(~{BUSRQ})

R56  (910, Clock)
   pin   1                Net-(R56-Pad1)               Y1.2(2) Z50.5
   pin   2                Net-(C60-Pad2)               C60.2 Z50.6 Z50.9

R57  (910, Clock)
   pin   1                Net-(C60-Pad1)               C60.1 Z50.3
   pin   2                Net-(R57-Pad2)               Y1.1(1) Z50.4

R64  (4.7k, Video Sync)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(JP8-A-Pad1)             JP8.1(A)

R65  (4.7k, Cassette Interface)
   pin   1                Net-(JP4-A-Pad1)             JP4.1(A)
   pin   2                +5V                          [net +5V, 138 pins]

R66  (4.7k, Video Latch)
   pin   1                Net-(Z53B-~{R})              Z53.13(~{R})
   pin   2                +5V                          [net +5V, 138 pins]

R67  (4.7k, Cassette Interface)
   pin   1                Net-(JP5-A-Pad3)             JP5.3(A)
   pin   2                +5V                          [net +5V, 138 pins]

R68  (4.7k, Video Generator)
   pin   1                Net-(Z57-Clr)                Z57.9(Clr) Z58.9(Clr)
   pin   2                +5V                          [net +5V, 138 pins]

R69  (4.7k, RAM)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(R101-Pad2)              R101.2 Z59.13

R70  (4.7k, Address Decoder)
   pin   1                Net-(JP3-B)                  JP3.2(B) Z60.5
   pin   2                +5V                          [net +5V, 138 pins]

R71  (4.7k, Address Decoder)
   pin   1                Net-(JP1-B)                  JP1.2(B) Z60.9
   pin   2                +5V                          [net +5V, 138 pins]

R72  (4.7k, Address Decoder)
   pin   1                ~{ROMB}                      JP2.2(B) Z43.20(~{CE1}) Z60.2
   pin   2                +5V                          [net +5V, 138 pins]

R74  (4.7k, )
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                HI                           Z62.10(~{S}) Z62.4(~{S}) Z63.10(~{S}) Z63.4(~{S})

R75  (330, CPU)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                ZCLK                         Z48.6(~{CLK}) Z66.13

R76  (4.7k, RAM)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                Net-(R109-Pad2)              R109.2 Z66.11

R77  (4.7k, Card-Edge Interface)
   pin   1                +5V                          [net +5V, 138 pins]
   pin   2                ~{INT}                       J4.21(Pin_21) Z48.16(~{INT})

R101  (330, RAM)
   pin   1                Net-(Z15-~{CAS})             Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z21.15(~{CAS}) Z22.15(~{CAS})
   pin   2                Net-(R101-Pad2)              R69.2 Z59.13

R102  (330, RAM)
   pin   1                Net-(Z15-A6)                 Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z21.13(A6) Z22.13(A6)
   pin   2                Net-(Z13-Zc)                 Z13.9(Zc)

R103  (330, RAM)
   pin   1                Net-(Z15-A3)                 Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z21.12(A3) Z22.12(A3)
   pin   2                Net-(Z14-Zd)                 Z14.12(Zd)

R104  (330, RAM)
   pin   1                Net-(Z15-A0)                 Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z21.5(A0) Z22.5(A0)
   pin   2                Net-(Z14-Za)                 Z14.4(Za)

R105  (330, RAM)
   pin   1                Net-(Z15-A4)                 Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z21.11(A4) Z22.11(A4)
   pin   2                Net-(Z13-Za)                 Z13.4(Za)

R106  (330, RAM)
   pin   1                Net-(Z15-A5)                 Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z21.10(A5) Z22.10(A5)
   pin   2                Net-(Z13-Zb)                 Z13.7(Zb)

R107  (330, RAM)
   pin   1                Net-(Z15-A1)                 Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z21.7(A1) Z22.7(A1)
   pin   2                Net-(Z14-Zb)                 Z14.7(Zb)

R108  (330, RAM)
   pin   1                Net-(Z15-A2)                 Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z21.6(A2) Z22.6(A2)
   pin   2                Net-(Z14-Zc)                 Z14.9(Zc)

R109  (330, RAM)
   pin   1                Net-(Z15-~{RAS})             Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z21.4(~{RAS}) Z22.4(~{RAS})
   pin   2                Net-(R109-Pad2)              R76.2 Z66.11

R110  (330, RAM)
   pin   1                Net-(Z15-~{WR})              Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z21.3(~{WR}) Z22.3(~{WR})
   pin   2                ~{WR}                        J4.13(Pin_13) Z29.14(I0d) Z30.3

RP1  (4.7k, CPU Gating)
   pin   1 common         +5V                          [net +5V, 138 pins]
   pin   2 R1             D4                           J4.18(Pin_18) Z12.16(B2) Z18.2(IN) Z23.12(B6) Z30.13
   pin   3 R2             D7                           J4.20(Pin_20) Z12.13(B5) Z15.2(IN) Z23.16(B2) Z24.5 Z53.2(D) Z59.5
   pin   4 R3             D1                           J4.22(Pin_22) Z12.11(B7) Z21.2(IN) Z23.18(B0) Z24.3 Z4.12(D2)
   pin   5 R4             D6                           J4.24(Pin_24) Z12.14(B4) Z16.2(IN) Z23.14(B4) Z24.7 Z59.3
   pin   6 R5             D5                           J4.28(Pin_28) Z12.15(B3) Z17.2(IN) Z23.13(B5) Z24.9
   pin   7 R6             D0                           J4.30(Pin_30) Z12.12(B6) Z22.2(IN) Z23.17(B1) Z24.13 Z4.13(D3)
   pin   8 R7             D2                           J4.32(Pin_32) Z12.18(B0) Z20.2(IN) Z23.15(B3) Z24.11 Z4.4(D0)
   pin   9 R8             D3                           J4.26(Pin_26) Z12.17(B1) Z19.2(IN) Z23.11(B7) Z30.11 Z4.5(D1)

RP2  (4.7k, RAM-ROM Interface)
   pin   1 common         +5V                          [net +5V, 138 pins]
   pin   2 R1             KBD1                         CN1.12(Pin_12) Z21.14(OUT) Z24.2 Z42.10(D1) Z43.10(D1)
   pin   3 R2             KBD0                         CN1.11(Pin_11) Z22.14(OUT) Z24.14 Z42.9(D0) Z43.9(D0)
   pin   4 R3             KBD7                         CN1.18(Pin_18) Z15.14(OUT) Z24.4 Z42.17(D7) Z43.17(D7)
   pin   5 R4             KBD2                         CN1.13(Pin_13) Z20.14(OUT) Z24.12 Z42.11(D2) Z43.11(D2)
   pin   6 R5             KBD6                         CN1.17(Pin_17) Z16.14(OUT) Z24.6 Z42.16(D6) Z43.16(D6)
   pin   7 R6             KBD3                         CN1.14(Pin_14) Z19.14(OUT) Z30.12 Z42.13(D3) Z43.13(D3)
   pin   8 R7             KBD5                         CN1.16(Pin_16) Z17.14(OUT) Z24.10 Z42.15(D5) Z43.15(D5)
   pin   9 R8             KBD4                         CN1.15(Pin_15) Z18.14(OUT) Z30.14 Z42.14(D4) Z43.14(D4)

S1  (~, Power)
   pin   1                Net-(J1-Pad2)                J1.2 S1.2
   pin   2                Net-(J1-Pad2)                J1.2 S1.1
   pin   3                Net-(Q6-E)                   C9.1 Q6.3(E) R28.1 Z2.12(V+)
   pin   4                Net-(CR1-+)                  CR1.1(+) S1.5 S1.8 S1.9
   pin   5                Net-(CR1-+)                  CR1.1(+) S1.4 S1.8 S1.9
   pin   6                Net-(Q4-E)                   C10.1 Q4.2(E) R13.1 S1.7
   pin   7                Net-(Q4-E)                   C10.1 Q4.2(E) R13.1 S1.6
   pin   8                Net-(CR1-+)                  CR1.1(+) S1.4 S1.5 S1.9
   pin   9                Net-(CR1-+)                  CR1.1(+) S1.4 S1.5 S1.8
   pin  10                Net-(C5-Pad2)                C5.2 R12.2
   pin  11                Net-(CR1--)                  CR1.4(-) S1.12
   pin  12                Net-(CR1--)                  CR1.4(-) S1.11

S2  (Reset, CPU)
   pin   1                unconnected-(S2-Pad1)        (no other connection)
   pin   2                unconnected-(S2-Pad2)        (no other connection)
   pin   3                unconnected-(S2-Pad3)        (no other connection)
   pin   4                Net-(R32-Pad2)               R32.2
   pin   5                GND                          [net GND, 176 pins]
   pin   6                GND                          [net GND, 176 pins]

TP1  (~, Power)
   pin   1                +12V                         [net +12V, 20 pins]
   pin   2                -5V                          [net -5V, 18 pins]
   pin   3                +5V                          [net +5V, 138 pins]
   pin   4                GND                          [net GND, 176 pins]

Y1  (10.6445 MHz, Clock)
   pin   1 1              Net-(R57-Pad2)               R57.2 Z50.4
   pin   2 2              Net-(R56-Pad1)               R56.1 Z50.5

Z1  (LM723C, Power)
   pin   1 NC             unconnected-(Z1-NC-Pad1)     (no other connection)
   pin   2 ILIM           Net-(Z1-ILIM)                R15.2 R21.1
   pin   3 CSEN           +5V                          [net +5V, 138 pins]
   pin   4 -              Net-(Z1--)                   C11.1 R19.2
   pin   5 +              Net-(Q5-E)                   Q5.1(E) R17.2(2)
   pin   6 VREF           Net-(Z1-VREF)                R18.2
   pin   7 V-             GND                          [net GND, 176 pins]
   pin   8 NC             unconnected-(Z1-NC-Pad8)     (no other connection)
   pin   9 VZ             unconnected-(Z1-VZ-Pad9)     (no other connection)
   pin  10 Vout           Net-(Q3-B)                   Q3.1(B) R14.1
   pin  11 VC             +12V                         [net +12V, 20 pins]
   pin  12 V+             +12V                         [net +12V, 20 pins]
   pin  13 FC             Net-(Z1-FC)                  C11.2
   pin  14 NC             unconnected-(Z1-NC-Pad14)    (no other connection)

Z2  (LM723C, Power)
   pin   1 NC             unconnected-(Z2-NC-Pad1)     (no other connection)
   pin   2 ILIM           Net-(Z2-ILIM)                R27.1 R29.2
   pin   3 CSEN           +12V                         [net +12V, 20 pins]
   pin   4 -              Net-(Z2--)                   C16.2 R23.2(2)
   pin   5 +              Net-(Z2-+)                   R22.2
   pin   6 VREF           Net-(Z2-VREF)                R22.1
   pin   7 V-             GND                          [net GND, 176 pins]
   pin   8 NC             unconnected-(Z2-NC-Pad8)     (no other connection)
   pin   9 VZ             unconnected-(Z2-VZ-Pad9)     (no other connection)
   pin  10 Vout           Net-(Q6-C)                   Q6.2(C) R29.1 R30.2
   pin  11 VC             Net-(Q6-B)                   Q6.1(B) R28.2
   pin  12 V+             Net-(Q6-E)                   C9.1 Q6.3(E) R28.1 S1.3
   pin  13 FC             Net-(Z2-FC)                  C16.1
   pin  14 NC             unconnected-(Z2-NC-Pad14)    (no other connection)

Z3  (75452, Cassette Interface)
   pin   1 1A             PIXEL                        Z3.2(1B) Z54.13
   pin   2 1B             PIXEL                        Z3.1(1A) Z54.13
   pin   3 1Y             Net-(Z3A-1Y)                 R9.2
   pin   4 GND            GND                          [net GND, 176 pins]
   pin   5 2Y             Net-(CR4-A)                  CR4.2(A) K1.2
   pin   6 2A             Net-(Z3B-2A)                 Z3.7(2B) Z4.2(Q0)
   pin   7 2B             Net-(Z3B-2A)                 Z3.6(2A) Z4.2(Q0)
   pin   8 VCC            +5V                          [net +5V, 138 pins]

Z4  (74LS175, Cassette Interface)
   pin   1 ~{Mr}          Net-(Z4-~{Mr})               R40.2
   pin   2 Q0             Net-(Z3B-2A)                 Z3.6(2A) Z3.7(2B)
   pin   3 ~{Q0}          unconnected-(Z4-~{Q0}-Pad3)  (no other connection)
   pin   4 D0             D2                           J4.32(Pin_32) RP1.8(R7) Z12.18(B0) Z20.2(IN) Z23.15(B3) Z24.11
   pin   5 D1             D3                           J4.26(Pin_26) RP1.9(R8) Z12.17(B1) Z19.2(IN) Z23.11(B7) Z30.11
   pin   6 ~{Q1}          MODESEL                      Z27.1(S) Z59.2
   pin   7 Q1             unconnected-(Z4-Q1-Pad7)     (no other connection)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Cp             ~{OUTSIG}                    Z31.5 Z40.6 Z53.3(C)
   pin  10 Q2             unconnected-(Z4-Q2-Pad10)    (no other connection)
   pin  11 ~{Q2}          Net-(Z4-~{Q2})               R4.2 R5.1
   pin  12 D2             D1                           J4.22(Pin_22) RP1.4(R3) Z12.11(B7) Z21.2(IN) Z23.18(B0) Z24.3
   pin  13 D3             D0                           J4.30(Pin_30) RP1.7(R6) Z12.12(B6) Z22.2(IN) Z23.17(B1) Z24.13
   pin  14 ~{Q3}          unconnected-(Z4-~{Q3}-Pad14) (no other connection)
   pin  15 Q3             Net-(Z4-Q3)                  R3.1
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z5  (74LS10, Video Counter)
   pin   1                VDRV                         Z44.2 Z52.2 Z54.2 Z7.11(Q3)
   pin   2                Net-(JP6-B)                  JP6.2(B)
   pin   3                L2                           JP10.1(A) Z35.8(Q2) Z37.8(R2) Z38.8(R2) Z39.14(S0)
   pin   4                Net-(JP10-B)                 JP10.2(B)
   pin   5                L3                           Z34.14(CP0) Z35.11(Q3) Z39.2(S1) Z52.12 Z56.12(D2)
   pin   6                Net-(Z26-Pad1)               Z26.1
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                Net-(Z26-Pad13)              Z26.13
   pin   9                HDRV                         Z28.11(Q3) Z35.14(CP0) Z54.3 Z62.1(~{R})
   pin  10                C4                           Z28.9(Q1) Z29.10(I1c) Z51.13
   pin  11                C5                           Z28.8(Q2) Z29.3(I1a)
   pin  12                Net-(Z26-Pad11)              Z26.11
   pin  13                R1                           JP7.1(A) Z33.11 Z7.1(CP1..3) Z7.12(Q0) Z8.13(I1d)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z6  (74LS92, Video Mode)
   pin   1 CP1..3         Net-(Z6-CP1..3)              Z31.13 Z6.12(Q0)
   pin   5 VCC            +5V                          [net +5V, 138 pins]
   pin   6 R0(1)          ~{CLK_EN}                    Z46.8 Z6.7(R0(2)) Z65.6(R0(1)) Z65.7(R0(2))
   pin   7 R0(2)          ~{CLK_EN}                    Z46.8 Z6.6(R0(1)) Z65.6(R0(1)) Z65.7(R0(2))
   pin   8 Q3             Net-(Z27-I1b)                Z27.10(I1c) Z27.6(I1b)
   pin   9 Q2             Net-(Z27-I0c)                Z27.11(I0c) Z31.12
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 Q1             unconnected-(Z6-Q1-Pad11)    (no other connection)
   pin  12 Q0             Net-(Z6-CP1..3)              Z31.13 Z6.1(CP1..3)
   pin  14 CP0            SHIFT                        Z27.4(Za) Z50.13

Z7  (74LS93, Video Counter)
   pin   1 CP1..3         R1                           JP7.1(A) Z33.11 Z5.13 Z7.12(Q0) Z8.13(I1d)
   pin   2 R0(1)          Net-(Z7-R0(1))               Z26.10 Z7.3(R0(2))
   pin   3 R0(2)          Net-(Z7-R0(1))               Z26.10 Z7.2(R0(1))
   pin   5 VCC            +5V                          [net +5V, 138 pins]
   pin   8 Q2             R3                           JP6.3(A) Z8.6(I1b)
   pin   9 Q1             R2                           JP6.1(A) JP8.3(A) Z8.3(I1a)
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 Q3             VDRV                         Z44.2 Z5.1 Z52.2 Z54.2
   pin  12 Q0             R1                           JP7.1(A) Z33.11 Z5.13 Z7.1(CP1..3) Z8.13(I1d)
   pin  14 CP0            R0                           Z33.13 Z34.12(Q0) Z44.1 Z8.10(I1c)

Z8  (74LS157, Video Access Multiplexer)
   pin   1 S              ~{VID}                       Z29.1(S) Z36.1(S) Z53.10(~{S}) Z61.9(O3)
   pin   2 I0a            A8                           CN2.1(Pin_1) J4.11(Pin_11) Z14.6(I1b) Z42.23(A8) Z43.23(A8) Z49.14(O2a)
   pin   3 I1a            R2                           JP6.1(A) JP8.3(A) Z7.9(Q1)
   pin   4 Za             VA8                          Z10.16(A8) Z9.16(A8)
   pin   5 I0b            A9                           CN2.2(Pin_2) J4.17(Pin_17) Z14.10(I1c) Z42.22(A9) Z43.22(A9) Z49.16(O1a)
   pin   6 I1b            R3                           JP6.3(A) Z7.8(Q2)
   pin   7 Zb             VA9                          Z10.15(A9) Z9.15(A9)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Zc             VA6                          Z10.1(A6) Z9.1(A6)
   pin  10 I1c            R0                           Z33.13 Z34.12(Q0) Z44.1 Z7.14(CP0)
   pin  11 I0c            A6                           CN1.7(Pin_7) J4.38(Pin_38) Z13.11(I0c) Z41.2 Z42.2(A6) Z43.2(A6) Z68.3(O3b)
   pin  12 Zd             VA7                          Z10.17(A7) Z9.17(A7)
   pin  13 I1d            R1                           JP7.1(A) Z33.11 Z5.13 Z7.1(CP1..3) Z7.12(Q0)
   pin  14 I0d            A7                           CN1.8(Pin_8) J4.36(Pin_36) Z14.3(I1a) Z41.1 Z42.1(A7) Z43.1(A7) Z68.18(O0a)
   pin  15 E              GND                          [net GND, 176 pins]
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z9  (SRAM_2114, Video RAM)
   pin   1 A6             VA6                          Z10.1(A6) Z8.9(Zc)
   pin   2 A5             VA5                          Z10.2(A5) Z29.4(Za)
   pin   3 A4             VA4                          Z10.3(A4) Z29.9(Zc)
   pin   4 A3             VA3                          Z10.4(A3) Z36.7(Zb)
   pin   5 A0             VA0                          Z10.5(A0) Z36.9(Zc)
   pin   6 A1             VA1                          Z10.6(A1) Z36.4(Za)
   pin   7 A2             VA2                          Z10.7(A2) Z36.12(Zd)
   pin   8 ~{CE}          GND                          [net GND, 176 pins]
   pin   9 VSS            GND                          [net GND, 176 pins]
   pin  10 ~{WR}          ~{VWR}                       Z10.10(~{WR}) Z29.12(Zd) Z40.12 Z40.13 Z51.2
   pin  11 D3             VD7                          Z12.7(A5) Z56.4(D0)
   pin  12 D2             VD6                          Z12.6(A4) Z56.13(D3)
   pin  13 D1             VD5                          Z11.11(D3) Z12.5(A3)
   pin  14 D0             VD4                          Z11.4(D1) Z12.4(A2)
   pin  15 A9             VA9                          Z10.15(A9) Z8.7(Zb)
   pin  16 A8             VA8                          Z10.16(A8) Z8.4(Za)
   pin  17 A7             VA7                          Z10.17(A7) Z8.12(Zd)
   pin  18 VCC            +5V                          [net +5V, 138 pins]

Z10  (SRAM_2114, Video RAM)
   pin   1 A6             VA6                          Z8.9(Zc) Z9.1(A6)
   pin   2 A5             VA5                          Z29.4(Za) Z9.2(A5)
   pin   3 A4             VA4                          Z29.9(Zc) Z9.3(A4)
   pin   4 A3             VA3                          Z36.7(Zb) Z9.4(A3)
   pin   5 A0             VA0                          Z36.9(Zc) Z9.5(A0)
   pin   6 A1             VA1                          Z36.4(Za) Z9.6(A1)
   pin   7 A2             VA2                          Z36.12(Zd) Z9.7(A2)
   pin   8 ~{CE}          GND                          [net GND, 176 pins]
   pin   9 VSS            GND                          [net GND, 176 pins]
   pin  10 ~{WR}          ~{VWR}                       Z29.12(Zd) Z40.12 Z40.13 Z51.2 Z9.10(~{WR})
   pin  11 D3             VD3                          Z11.6(D2) Z12.3(A1)
   pin  12 D2             VD2                          Z11.3(D0) Z12.2(A0)
   pin  13 D1             VD1                          Z11.13(D4) Z12.9(A7)
   pin  14 D0             VD0                          Z11.14(D5) Z12.8(A6)
   pin  15 A9             VA9                          Z8.7(Zb) Z9.15(A9)
   pin  16 A8             VA8                          Z8.4(Za) Z9.16(A8)
   pin  17 A7             VA7                          Z8.12(Zd) Z9.17(A7)
   pin  18 VCC            +5V                          [net +5V, 138 pins]

Z11  (74LS174, Video Latch)
   pin   1 ~{Mr}          ~{VCLR}                      Z53.8(~{Q}) Z56.1(~{Mr})
   pin   2 Q0             LB2                          Z37.5(A2) Z38.5(A2) Z39.5(I1a)
   pin   3 D0             VD2                          Z10.12(D2) Z12.2(A0)
   pin   4 D1             VD4                          Z12.4(A2) Z9.14(D0)
   pin   5 Q1             LB4                          Z37.3(A4) Z38.3(A4) Z39.4(I2a)
   pin   6 D2             VD3                          Z10.11(D3) Z12.3(A1)
   pin   7 Q2             LB3                          Z37.4(A3) Z38.4(A3) Z39.11(I1b)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Cp             ~{LATCH}                     Z31.11 Z50.11 Z53.11(C) Z56.9(Cp)
   pin  10 Q3             LB5                          Z37.2(A5) Z38.2(A5) Z39.12(I2b)
   pin  11 D3             VD5                          Z12.5(A3) Z9.13(D1)
   pin  12 Q4             LB1                          Z37.6(A1) Z38.6(A1) Z39.10(I0b)
   pin  13 D4             VD1                          Z10.13(D1) Z12.9(A7)
   pin  14 D5             VD0                          Z10.14(D0) Z12.8(A6)
   pin  15 Q5             LB0                          Z37.7(A0) Z38.7(A0) Z39.6(I0a)
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z12  (74LS245, Video RAM)
   pin   1 A->B           Net-(Z12-A->B)               Z40.11
   pin   2 A0             VD2                          Z10.12(D2) Z11.3(D0)
   pin   3 A1             VD3                          Z10.11(D3) Z11.6(D2)
   pin   4 A2             VD4                          Z11.4(D1) Z9.14(D0)
   pin   5 A3             VD5                          Z11.11(D3) Z9.13(D1)
   pin   6 A4             VD6                          Z56.13(D3) Z9.12(D2)
   pin   7 A5             VD7                          Z56.4(D0) Z9.11(D3)
   pin   8 A6             VD0                          Z10.14(D0) Z11.14(D5)
   pin   9 A7             VD1                          Z10.13(D1) Z11.13(D4)
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 B7             D1                           J4.22(Pin_22) RP1.4(R3) Z21.2(IN) Z23.18(B0) Z24.3 Z4.12(D2)
   pin  12 B6             D0                           J4.30(Pin_30) RP1.7(R6) Z22.2(IN) Z23.17(B1) Z24.13 Z4.13(D3)
   pin  13 B5             D7                           J4.20(Pin_20) RP1.3(R2) Z15.2(IN) Z23.16(B2) Z24.5 Z53.2(D) Z59.5
   pin  14 B4             D6                           J4.24(Pin_24) RP1.5(R4) Z16.2(IN) Z23.14(B4) Z24.7 Z59.3
   pin  15 B3             D5                           J4.28(Pin_28) RP1.6(R5) Z17.2(IN) Z23.13(B5) Z24.9
   pin  16 B2             D4                           J4.18(Pin_18) RP1.2(R1) Z18.2(IN) Z23.12(B6) Z30.13
   pin  17 B1             D3                           J4.26(Pin_26) RP1.9(R8) Z19.2(IN) Z23.11(B7) Z30.11 Z4.5(D1)
   pin  18 B0             D2                           J4.32(Pin_32) RP1.8(R7) Z20.2(IN) Z23.15(B3) Z24.11 Z4.4(D0)
   pin  19 CE             Net-(Z12-CE)                 Z51.3
   pin  20 VCC            +5V                          [net +5V, 138 pins]

Z13  (74LS157, RAM)
   pin   1 S              MUX                          J4.16(Pin_16) Z14.1(S) Z66.5
   pin   2 I0a            A4                           CN1.2(Pin_2) J4.31(Pin_31) Z29.11(I0c) Z41.11 Z42.4(A4) Z43.4(A4) Z68.5(O2b)
   pin   3 I1a            A11                          CN2.4(Pin_4) J4.9(Pin_9) Z42.18(A11) Z43.18(A11) Z49.3(O3b) Z61.13(A1)
   pin   4 Za             Net-(Z13-Za)                 R105.2
   pin   5 I0b            A5                           CN1.3(Pin_3) J4.35(Pin_35) Z29.2(I0a) Z41.12 Z42.3(A5) Z43.3(A5) Z68.16(O1a)
   pin   6 I1b            A12                          J4.5(Pin_5) Z42.21(A12) Z43.21(~{CE2}) Z49.5(O2b) Z61.2(A0)
   pin   7 Zb             Net-(Z13-Zb)                 R106.2
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Zc             Net-(Z13-Zc)                 R102.2
   pin  10 I1c            A13                          J4.6(Pin_6) Z49.7(O1b) Z61.3(A1)
   pin  11 I0c            A6                           CN1.7(Pin_7) J4.38(Pin_38) Z41.2 Z42.2(A6) Z43.2(A6) Z68.3(O3b) Z8.11(I0c)
   pin  12 Zd             unconnected-(Z13-Zd-Pad12)   (no other connection)
   pin  13 I1d            unconnected-(Z13-I1d-Pad13)  (no other connection)
   pin  14 I0d            unconnected-(Z13-I0d-Pad14)  (no other connection)
   pin  15 E              GND                          [net GND, 176 pins]
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z14  (74LS157, RAM)
   pin   1 S              MUX                          J4.16(Pin_16) Z13.1(S) Z66.5
   pin   2 I0a            A0                           CN1.5(Pin_5) J4.25(Pin_25) Z36.11(I0c) Z41.6 Z42.8(A0) Z43.8(A0) Z68.9(O0b)
   pin   3 I1a            A7                           CN1.8(Pin_8) J4.36(Pin_36) Z41.1 Z42.1(A7) Z43.1(A7) Z68.18(O0a) Z8.14(I0d)
   pin   4 Za             Net-(Z14-Za)                 R104.2
   pin   5 I0b            A1                           CN1.4(Pin_4) J4.27(Pin_27) Z36.2(I0a) Z41.5 Z42.7(A1) Z43.7(A1) Z68.12(O3a)
   pin   6 I1b            A8                           CN2.1(Pin_1) J4.11(Pin_11) Z42.23(A8) Z43.23(A8) Z49.14(O2a) Z8.2(I0a)
   pin   7 Zb             Net-(Z14-Zb)                 R107.2
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Zc             Net-(Z14-Zc)                 R108.2
   pin  10 I1c            A9                           CN2.2(Pin_2) J4.17(Pin_17) Z42.22(A9) Z43.22(A9) Z49.16(O1a) Z8.5(I0b)
   pin  11 I0c            A2                           CN1.6(Pin_6) J4.40(Pin_40) Z36.14(I0d) Z41.4 Z42.6(A2) Z43.6(A2) Z68.7(O1b)
   pin  12 Zd             Net-(Z14-Zd)                 R103.2
   pin  13 I1d            A10                          CN2.3(Pin_3) J4.4(Pin_4) Z42.19(A10) Z43.19(A10) Z49.18(O0a) Z61.14(A0)
   pin  14 I0d            A3                           CN1.9(Pin_9) J4.34(Pin_34) Z36.5(I0b) Z41.3 Z42.5(A3) Z43.5(A3) Z68.14(O2a)
   pin  15 E              GND                          [net GND, 176 pins]
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z15  (DRAM_4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 18 pins]
   pin   2 IN             D7                           J4.20(Pin_20) RP1.3(R2) Z12.13(B5) Z23.16(B2) Z24.5 Z53.2(D) Z59.5
   pin   3 ~{WR}          Net-(Z15-~{WR})              R110.1 Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z21.3(~{WR}) Z22.3(~{WR})
   pin   4 ~{RAS}         Net-(Z15-~{RAS})             R109.1 Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z21.4(~{RAS}) Z22.4(~{RAS})
   pin   5 A0             Net-(Z15-A0)                 R104.1 Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z21.5(A0) Z22.5(A0)
   pin   6 A2             Net-(Z15-A2)                 R108.1 Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z21.6(A2) Z22.6(A2)
   pin   7 A1             Net-(Z15-A1)                 R107.1 Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z21.7(A1) Z22.7(A1)
   pin   8 VDD            +12V                         [net +12V, 20 pins]
   pin   9 VCC            +5V                          [net +5V, 138 pins]
   pin  10 A5             Net-(Z15-A5)                 R106.1 Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z21.10(A5) Z22.10(A5)
   pin  11 A4             Net-(Z15-A4)                 R105.1 Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z21.11(A4) Z22.11(A4)
   pin  12 A3             Net-(Z15-A3)                 R103.1 Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z21.12(A3) Z22.12(A3)
   pin  13 A6             Net-(Z15-A6)                 R102.1 Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z21.13(A6) Z22.13(A6)
   pin  14 OUT            KBD7                         CN1.18(Pin_18) RP2.4(R3) Z24.4 Z42.17(D7) Z43.17(D7)
   pin  15 ~{CAS}         Net-(Z15-~{CAS})             R101.1 Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z21.15(~{CAS}) Z22.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 176 pins]

Z16  (DRAM_4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 18 pins]
   pin   2 IN             D6                           J4.24(Pin_24) RP1.5(R4) Z12.14(B4) Z23.14(B4) Z24.7 Z59.3
   pin   3 ~{WR}          Net-(Z15-~{WR})              R110.1 Z15.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z21.3(~{WR}) Z22.3(~{WR})
   pin   4 ~{RAS}         Net-(Z15-~{RAS})             R109.1 Z15.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z21.4(~{RAS}) Z22.4(~{RAS})
   pin   5 A0             Net-(Z15-A0)                 R104.1 Z15.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z21.5(A0) Z22.5(A0)
   pin   6 A2             Net-(Z15-A2)                 R108.1 Z15.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z21.6(A2) Z22.6(A2)
   pin   7 A1             Net-(Z15-A1)                 R107.1 Z15.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z21.7(A1) Z22.7(A1)
   pin   8 VDD            +12V                         [net +12V, 20 pins]
   pin   9 VCC            +5V                          [net +5V, 138 pins]
   pin  10 A5             Net-(Z15-A5)                 R106.1 Z15.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z21.10(A5) Z22.10(A5)
   pin  11 A4             Net-(Z15-A4)                 R105.1 Z15.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z21.11(A4) Z22.11(A4)
   pin  12 A3             Net-(Z15-A3)                 R103.1 Z15.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z21.12(A3) Z22.12(A3)
   pin  13 A6             Net-(Z15-A6)                 R102.1 Z15.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z21.13(A6) Z22.13(A6)
   pin  14 OUT            KBD6                         CN1.17(Pin_17) RP2.6(R5) Z24.6 Z42.16(D6) Z43.16(D6)
   pin  15 ~{CAS}         Net-(Z15-~{CAS})             R101.1 Z15.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z21.15(~{CAS}) Z22.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 176 pins]

Z17  (DRAM_4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 18 pins]
   pin   2 IN             D5                           J4.28(Pin_28) RP1.6(R5) Z12.15(B3) Z23.13(B5) Z24.9
   pin   3 ~{WR}          Net-(Z15-~{WR})              R110.1 Z15.3(~{WR}) Z16.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z21.3(~{WR}) Z22.3(~{WR})
   pin   4 ~{RAS}         Net-(Z15-~{RAS})             R109.1 Z15.4(~{RAS}) Z16.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z21.4(~{RAS}) Z22.4(~{RAS})
   pin   5 A0             Net-(Z15-A0)                 R104.1 Z15.5(A0) Z16.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z21.5(A0) Z22.5(A0)
   pin   6 A2             Net-(Z15-A2)                 R108.1 Z15.6(A2) Z16.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z21.6(A2) Z22.6(A2)
   pin   7 A1             Net-(Z15-A1)                 R107.1 Z15.7(A1) Z16.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z21.7(A1) Z22.7(A1)
   pin   8 VDD            +12V                         [net +12V, 20 pins]
   pin   9 VCC            +5V                          [net +5V, 138 pins]
   pin  10 A5             Net-(Z15-A5)                 R106.1 Z15.10(A5) Z16.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z21.10(A5) Z22.10(A5)
   pin  11 A4             Net-(Z15-A4)                 R105.1 Z15.11(A4) Z16.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z21.11(A4) Z22.11(A4)
   pin  12 A3             Net-(Z15-A3)                 R103.1 Z15.12(A3) Z16.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z21.12(A3) Z22.12(A3)
   pin  13 A6             Net-(Z15-A6)                 R102.1 Z15.13(A6) Z16.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z21.13(A6) Z22.13(A6)
   pin  14 OUT            KBD5                         CN1.16(Pin_16) RP2.8(R7) Z24.10 Z42.15(D5) Z43.15(D5)
   pin  15 ~{CAS}         Net-(Z15-~{CAS})             R101.1 Z15.15(~{CAS}) Z16.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z21.15(~{CAS}) Z22.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 176 pins]

Z18  (DRAM_4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 18 pins]
   pin   2 IN             D4                           J4.18(Pin_18) RP1.2(R1) Z12.16(B2) Z23.12(B6) Z30.13
   pin   3 ~{WR}          Net-(Z15-~{WR})              R110.1 Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z21.3(~{WR}) Z22.3(~{WR})
   pin   4 ~{RAS}         Net-(Z15-~{RAS})             R109.1 Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z21.4(~{RAS}) Z22.4(~{RAS})
   pin   5 A0             Net-(Z15-A0)                 R104.1 Z15.5(A0) Z16.5(A0) Z17.5(A0) Z19.5(A0) Z20.5(A0) Z21.5(A0) Z22.5(A0)
   pin   6 A2             Net-(Z15-A2)                 R108.1 Z15.6(A2) Z16.6(A2) Z17.6(A2) Z19.6(A2) Z20.6(A2) Z21.6(A2) Z22.6(A2)
   pin   7 A1             Net-(Z15-A1)                 R107.1 Z15.7(A1) Z16.7(A1) Z17.7(A1) Z19.7(A1) Z20.7(A1) Z21.7(A1) Z22.7(A1)
   pin   8 VDD            +12V                         [net +12V, 20 pins]
   pin   9 VCC            +5V                          [net +5V, 138 pins]
   pin  10 A5             Net-(Z15-A5)                 R106.1 Z15.10(A5) Z16.10(A5) Z17.10(A5) Z19.10(A5) Z20.10(A5) Z21.10(A5) Z22.10(A5)
   pin  11 A4             Net-(Z15-A4)                 R105.1 Z15.11(A4) Z16.11(A4) Z17.11(A4) Z19.11(A4) Z20.11(A4) Z21.11(A4) Z22.11(A4)
   pin  12 A3             Net-(Z15-A3)                 R103.1 Z15.12(A3) Z16.12(A3) Z17.12(A3) Z19.12(A3) Z20.12(A3) Z21.12(A3) Z22.12(A3)
   pin  13 A6             Net-(Z15-A6)                 R102.1 Z15.13(A6) Z16.13(A6) Z17.13(A6) Z19.13(A6) Z20.13(A6) Z21.13(A6) Z22.13(A6)
   pin  14 OUT            KBD4                         CN1.15(Pin_15) RP2.9(R8) Z30.14 Z42.14(D4) Z43.14(D4)
   pin  15 ~{CAS}         Net-(Z15-~{CAS})             R101.1 Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z21.15(~{CAS}) Z22.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 176 pins]

Z19  (DRAM_4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 18 pins]
   pin   2 IN             D3                           J4.26(Pin_26) RP1.9(R8) Z12.17(B1) Z23.11(B7) Z30.11 Z4.5(D1)
   pin   3 ~{WR}          Net-(Z15-~{WR})              R110.1 Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z20.3(~{WR}) Z21.3(~{WR}) Z22.3(~{WR})
   pin   4 ~{RAS}         Net-(Z15-~{RAS})             R109.1 Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z20.4(~{RAS}) Z21.4(~{RAS}) Z22.4(~{RAS})
   pin   5 A0             Net-(Z15-A0)                 R104.1 Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z20.5(A0) Z21.5(A0) Z22.5(A0)
   pin   6 A2             Net-(Z15-A2)                 R108.1 Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z20.6(A2) Z21.6(A2) Z22.6(A2)
   pin   7 A1             Net-(Z15-A1)                 R107.1 Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z20.7(A1) Z21.7(A1) Z22.7(A1)
   pin   8 VDD            +12V                         [net +12V, 20 pins]
   pin   9 VCC            +5V                          [net +5V, 138 pins]
   pin  10 A5             Net-(Z15-A5)                 R106.1 Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z20.10(A5) Z21.10(A5) Z22.10(A5)
   pin  11 A4             Net-(Z15-A4)                 R105.1 Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z20.11(A4) Z21.11(A4) Z22.11(A4)
   pin  12 A3             Net-(Z15-A3)                 R103.1 Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z20.12(A3) Z21.12(A3) Z22.12(A3)
   pin  13 A6             Net-(Z15-A6)                 R102.1 Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z20.13(A6) Z21.13(A6) Z22.13(A6)
   pin  14 OUT            KBD3                         CN1.14(Pin_14) RP2.7(R6) Z30.12 Z42.13(D3) Z43.13(D3)
   pin  15 ~{CAS}         Net-(Z15-~{CAS})             R101.1 Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z20.15(~{CAS}) Z21.15(~{CAS}) Z22.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 176 pins]

Z20  (DRAM_4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 18 pins]
   pin   2 IN             D2                           J4.32(Pin_32) RP1.8(R7) Z12.18(B0) Z23.15(B3) Z24.11 Z4.4(D0)
   pin   3 ~{WR}          Net-(Z15-~{WR})              R110.1 Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z21.3(~{WR}) Z22.3(~{WR})
   pin   4 ~{RAS}         Net-(Z15-~{RAS})             R109.1 Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z21.4(~{RAS}) Z22.4(~{RAS})
   pin   5 A0             Net-(Z15-A0)                 R104.1 Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z21.5(A0) Z22.5(A0)
   pin   6 A2             Net-(Z15-A2)                 R108.1 Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z21.6(A2) Z22.6(A2)
   pin   7 A1             Net-(Z15-A1)                 R107.1 Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z21.7(A1) Z22.7(A1)
   pin   8 VDD            +12V                         [net +12V, 20 pins]
   pin   9 VCC            +5V                          [net +5V, 138 pins]
   pin  10 A5             Net-(Z15-A5)                 R106.1 Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z21.10(A5) Z22.10(A5)
   pin  11 A4             Net-(Z15-A4)                 R105.1 Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z21.11(A4) Z22.11(A4)
   pin  12 A3             Net-(Z15-A3)                 R103.1 Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z21.12(A3) Z22.12(A3)
   pin  13 A6             Net-(Z15-A6)                 R102.1 Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z21.13(A6) Z22.13(A6)
   pin  14 OUT            KBD2                         CN1.13(Pin_13) RP2.5(R4) Z24.12 Z42.11(D2) Z43.11(D2)
   pin  15 ~{CAS}         Net-(Z15-~{CAS})             R101.1 Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z21.15(~{CAS}) Z22.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 176 pins]

Z21  (DRAM_4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 18 pins]
   pin   2 IN             D1                           J4.22(Pin_22) RP1.4(R3) Z12.11(B7) Z23.18(B0) Z24.3 Z4.12(D2)
   pin   3 ~{WR}          Net-(Z15-~{WR})              R110.1 Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z22.3(~{WR})
   pin   4 ~{RAS}         Net-(Z15-~{RAS})             R109.1 Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z22.4(~{RAS})
   pin   5 A0             Net-(Z15-A0)                 R104.1 Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z22.5(A0)
   pin   6 A2             Net-(Z15-A2)                 R108.1 Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z22.6(A2)
   pin   7 A1             Net-(Z15-A1)                 R107.1 Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z22.7(A1)
   pin   8 VDD            +12V                         [net +12V, 20 pins]
   pin   9 VCC            +5V                          [net +5V, 138 pins]
   pin  10 A5             Net-(Z15-A5)                 R106.1 Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z22.10(A5)
   pin  11 A4             Net-(Z15-A4)                 R105.1 Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z22.11(A4)
   pin  12 A3             Net-(Z15-A3)                 R103.1 Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z22.12(A3)
   pin  13 A6             Net-(Z15-A6)                 R102.1 Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z22.13(A6)
   pin  14 OUT            KBD1                         CN1.12(Pin_12) RP2.2(R1) Z24.2 Z42.10(D1) Z43.10(D1)
   pin  15 ~{CAS}         Net-(Z15-~{CAS})             R101.1 Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z22.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 176 pins]

Z22  (DRAM_4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 18 pins]
   pin   2 IN             D0                           J4.30(Pin_30) RP1.7(R6) Z12.12(B6) Z23.17(B1) Z24.13 Z4.13(D3)
   pin   3 ~{WR}          Net-(Z15-~{WR})              R110.1 Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z21.3(~{WR})
   pin   4 ~{RAS}         Net-(Z15-~{RAS})             R109.1 Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z21.4(~{RAS})
   pin   5 A0             Net-(Z15-A0)                 R104.1 Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z21.5(A0)
   pin   6 A2             Net-(Z15-A2)                 R108.1 Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z21.6(A2)
   pin   7 A1             Net-(Z15-A1)                 R107.1 Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z21.7(A1)
   pin   8 VDD            +12V                         [net +12V, 20 pins]
   pin   9 VCC            +5V                          [net +5V, 138 pins]
   pin  10 A5             Net-(Z15-A5)                 R106.1 Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z21.10(A5)
   pin  11 A4             Net-(Z15-A4)                 R105.1 Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z21.11(A4)
   pin  12 A3             Net-(Z15-A3)                 R103.1 Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z21.12(A3)
   pin  13 A6             Net-(Z15-A6)                 R102.1 Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z21.13(A6)
   pin  14 OUT            KBD0                         CN1.11(Pin_11) RP2.3(R2) Z24.14 Z42.9(D0) Z43.9(D0)
   pin  15 ~{CAS}         Net-(Z15-~{CAS})             R101.1 Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z21.15(~{CAS})
   pin  16 VSS            GND                          [net GND, 176 pins]

Z23  (74LS245, CPU Gating)
   pin   1 A->B           ~{DBIN}                      Z47.11
   pin   2 A0             ZD1                          Z48.15(D1)
   pin   3 A1             ZD0                          Z48.14(D0)
   pin   4 A2             ZD7                          Z48.13(D7)
   pin   5 A3             ZD2                          Z48.12(D2)
   pin   6 A4             ZD6                          Z48.10(D6)
   pin   7 A5             ZD5                          Z48.9(D5)
   pin   8 A6             ZD4                          Z48.7(D4)
   pin   9 A7             ZD3                          Z48.8(D3)
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 B7             D3                           J4.26(Pin_26) RP1.9(R8) Z12.17(B1) Z19.2(IN) Z30.11 Z4.5(D1)
   pin  12 B6             D4                           J4.18(Pin_18) RP1.2(R1) Z12.16(B2) Z18.2(IN) Z30.13
   pin  13 B5             D5                           J4.28(Pin_28) RP1.6(R5) Z12.15(B3) Z17.2(IN) Z24.9
   pin  14 B4             D6                           J4.24(Pin_24) RP1.5(R4) Z12.14(B4) Z16.2(IN) Z24.7 Z59.3
   pin  15 B3             D2                           J4.32(Pin_32) RP1.8(R7) Z12.18(B0) Z20.2(IN) Z24.11 Z4.4(D0)
   pin  16 B2             D7                           J4.20(Pin_20) RP1.3(R2) Z12.13(B5) Z15.2(IN) Z24.5 Z53.2(D) Z59.5
   pin  17 B1             D0                           J4.30(Pin_30) RP1.7(R6) Z12.12(B6) Z22.2(IN) Z24.13 Z4.13(D3)
   pin  18 B0             D1                           J4.22(Pin_22) RP1.4(R3) Z12.11(B7) Z21.2(IN) Z24.3 Z4.12(D2)
   pin  19 CE             GND                          [net GND, 176 pins]
   pin  20 VCC            +5V                          [net +5V, 138 pins]

Z24  (74LS367, RAM-ROM Interface)
   pin   1                ~{MEM}                       Z24.15 Z30.15 Z40.8
   pin   2                KBD1                         CN1.12(Pin_12) RP2.2(R1) Z21.14(OUT) Z42.10(D1) Z43.10(D1)
   pin   3                D1                           J4.22(Pin_22) RP1.4(R3) Z12.11(B7) Z21.2(IN) Z23.18(B0) Z4.12(D2)
   pin   4                KBD7                         CN1.18(Pin_18) RP2.4(R3) Z15.14(OUT) Z42.17(D7) Z43.17(D7)
   pin   5                D7                           J4.20(Pin_20) RP1.3(R2) Z12.13(B5) Z15.2(IN) Z23.16(B2) Z53.2(D) Z59.5
   pin   6                KBD6                         CN1.17(Pin_17) RP2.6(R5) Z16.14(OUT) Z42.16(D6) Z43.16(D6)
   pin   7                D6                           J4.24(Pin_24) RP1.5(R4) Z12.14(B4) Z16.2(IN) Z23.14(B4) Z59.3
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9                D5                           J4.28(Pin_28) RP1.6(R5) Z12.15(B3) Z17.2(IN) Z23.13(B5)
   pin  10                KBD5                         CN1.16(Pin_16) RP2.8(R7) Z17.14(OUT) Z42.15(D5) Z43.15(D5)
   pin  11                D2                           J4.32(Pin_32) RP1.8(R7) Z12.18(B0) Z20.2(IN) Z23.15(B3) Z4.4(D0)
   pin  12                KBD2                         CN1.13(Pin_13) RP2.5(R4) Z20.14(OUT) Z42.11(D2) Z43.11(D2)
   pin  13                D0                           J4.30(Pin_30) RP1.7(R6) Z12.12(B6) Z22.2(IN) Z23.17(B1) Z4.13(D3)
   pin  14                KBD0                         CN1.11(Pin_11) RP2.3(R2) Z22.14(OUT) Z42.9(D0) Z43.9(D0)
   pin  15                ~{MEM}                       Z24.1 Z30.15 Z40.8
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z25  (LM3900, Cassette Interface)
   pin   1 +              Net-(Z25A-+)                 R35.2
   pin   2 +              Net-(Z25B-+)                 R36.1 R38.2
   pin   3 -              Net-(Z25B--)                 R43.2
   pin   4                Net-(CR5-A)                  CR5.2(A) R42.2 R43.1 R44.1
   pin   5                Net-(CR6-A)                  CR6.2(A) R45.2
   pin   6 -              Net-(Z25A--)                 R44.2 R45.1
   pin   7 V-             GND                          [net GND, 176 pins]
   pin   8 -              Net-(Z25C--)                 R47.2
   pin   9                Net-(C50-Pad2)               C50.2
   pin  10                Net-(CR7-A)                  CR7.2(A) R46.1 R51.2
   pin  11 -              Net-(Z25D--)                 R50.2 R51.1
   pin  12 +              Net-(Z25D-+)                 R33.2
   pin  13 +              Net-(Z25C-+)                 R46.2
   pin  14 V+             Net-(Z25E-V+)                C19.2 R39.1

Z26  (74LS14, Video Counter)
   pin   1                Net-(Z26-Pad1)               Z5.6
   pin   2                Net-(Z35-R0(1))              Z35.2(R0(1)) Z35.3(R0(2))
   pin   3                unconnected-(Z26-Pad3)       (no other connection)
   pin   4                unconnected-(Z26-Pad4)       (no other connection)
   pin   5                unconnected-(Z26-Pad5)       (no other connection)
   pin   6                unconnected-(Z26-Pad6)       (no other connection)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                unconnected-(Z26-Pad8)       (no other connection)
   pin   9                unconnected-(Z26-Pad9)       (no other connection)
   pin  10                Net-(Z7-R0(1))               Z7.2(R0(1)) Z7.3(R0(2))
   pin  11                Net-(Z26-Pad11)              Z5.12
   pin  12                Net-(Z28-R0(1))              Z28.2(R0(1)) Z28.3(R0(2))
   pin  13                Net-(Z26-Pad13)              Z5.8
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z27  (74LS157, Video Mode)
   pin   1 S              MODESEL                      Z4.6(~{Q1}) Z59.2
   pin   2 I0a            CLK_DIV2                     Z65.12(Q0)
   pin   3 I1a            CLK                          Z50.8 Z62.11(C) Z63.11(C) Z63.3(C) Z65.1(CP1..3) Z65.14(CP0)
   pin   4 Za             SHIFT                        Z50.13 Z6.14(CP0)
   pin   5 I0b            GND                          [net GND, 176 pins]
   pin   6 I1b            Net-(Z27-I1b)                Z27.10(I1c) Z6.8(Q3)
   pin   7 Zb             C0                           Z36.10(I1c)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Zc             DOT_CLK                      Z34.1(CP1..3)
   pin  10 I1c            Net-(Z27-I1b)                Z27.6(I1b) Z6.8(Q3)
   pin  11 I0c            Net-(Z27-I0c)                Z31.12 Z6.9(Q2)
   pin  12 Zd             HCLK                         Z62.3(C)
   pin  13 I1d            C1                           Z34.9(Q1) Z36.3(I1a)
   pin  14 I0d            C2                           Z28.14(CP0) Z34.8(Q2) Z36.13(I1d)
   pin  15 E              GND                          [net GND, 176 pins]
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z28  (74LS93, Video Counter)
   pin   1 CP1..3         C3                           Z28.12(Q0) Z36.6(I1b) Z46.1
   pin   2 R0(1)          Net-(Z28-R0(1))              Z26.12 Z28.3(R0(2))
   pin   3 R0(2)          Net-(Z28-R0(1))              Z26.12 Z28.2(R0(1))
   pin   5 VCC            +5V                          [net +5V, 138 pins]
   pin   8 Q2             C5                           Z29.3(I1a) Z5.11
   pin   9 Q1             C4                           Z29.10(I1c) Z5.10 Z51.13
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 Q3             HDRV                         Z35.14(CP0) Z5.9 Z54.3 Z62.1(~{R})
   pin  12 Q0             C3                           Z28.1(CP1..3) Z36.6(I1b) Z46.1
   pin  14 CP0            C2                           Z27.14(I0d) Z34.8(Q2) Z36.13(I1d)

Z29  (74LS157, Video Access Multiplexer)
   pin   1 S              ~{VID}                       Z36.1(S) Z53.10(~{S}) Z61.9(O3) Z8.1(S)
   pin   2 I0a            A5                           CN1.3(Pin_3) J4.35(Pin_35) Z13.5(I0b) Z41.12 Z42.3(A5) Z43.3(A5) Z68.16(O1a)
   pin   3 I1a            C5                           Z28.8(Q2) Z5.11
   pin   4 Za             VA5                          Z10.2(A5) Z9.2(A5)
   pin   5 I0b            ~{RD}                        J4.15(Pin_15) Z30.5 Z40.10
   pin   6 I1b            Net-(Z29-I1b)                R48.2 Z29.13(I1d)
   pin   7 Zb             ~{VRD}                       Z51.1
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Zc             VA4                          Z10.3(A4) Z9.3(A4)
   pin  10 I1c            C4                           Z28.9(Q1) Z5.10 Z51.13
   pin  11 I0c            A4                           CN1.2(Pin_2) J4.31(Pin_31) Z13.2(I0a) Z41.11 Z42.4(A4) Z43.4(A4) Z68.5(O2b)
   pin  12 Zd             ~{VWR}                       Z10.10(~{WR}) Z40.12 Z40.13 Z51.2 Z9.10(~{WR})
   pin  13 I1d            Net-(Z29-I1b)                R48.2 Z29.6(I1b)
   pin  14 I0d            ~{WR}                        J4.13(Pin_13) R110.2 Z30.3
   pin  15 E              GND                          [net GND, 176 pins]
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z30  (74LS367, CPU Gating)
   pin   1                Net-(Z49-OEa)                Z46.10 Z49.1(OEa) Z49.19(OEb) Z66.1 Z68.1(OEa) Z68.19(OEb)
   pin   2                ~{ZWR}                       Z67.3
   pin   3                ~{WR}                        J4.13(Pin_13) R110.2 Z29.14(I0d)
   pin   4                ~{ZRD}                       Z67.11
   pin   5                ~{RD}                        J4.15(Pin_15) Z29.5(I0b) Z40.10
   pin   6                ~{ZOUT}                      Z67.6
   pin   7                ~{OUT}                       J4.12(Pin_12) Z40.5
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9                ~{IN}                        J4.19(Pin_19) Z40.1
   pin  10                ~{ZIN}                       Z67.8
   pin  11                D3                           J4.26(Pin_26) RP1.9(R8) Z12.17(B1) Z19.2(IN) Z23.11(B7) Z4.5(D1)
   pin  12                KBD3                         CN1.14(Pin_14) RP2.7(R6) Z19.14(OUT) Z42.13(D3) Z43.13(D3)
   pin  13                D4                           J4.18(Pin_18) RP1.2(R1) Z12.16(B2) Z18.2(IN) Z23.12(B6)
   pin  14                KBD4                         CN1.15(Pin_15) RP2.9(R8) Z18.14(OUT) Z42.14(D4) Z43.14(D4)
   pin  15                ~{MEM}                       Z24.1 Z24.15 Z40.8
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z31  (74LS132, Cassette Interface)
   pin   1                unconnected-(Z31-Pad1)       (no other connection)
   pin   2                unconnected-(Z31-Pad2)       (no other connection)
   pin   3                unconnected-(Z31-Pad3)       (no other connection)
   pin   4                Net-(Z31-Pad4)               Z31.8 Z59.4
   pin   5                ~{OUTSIG}                    Z4.9(Cp) Z40.6 Z53.3(C)
   pin   6                Net-(Z31-Pad6)               Z31.9
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                Net-(Z31-Pad4)               Z31.4 Z59.4
   pin   9                Net-(Z31-Pad6)               Z31.6
   pin  10                Net-(C50-Pad1)               C50.1 R52.1 R53.2
   pin  11                ~{LATCH}                     Z11.9(Cp) Z50.11 Z53.11(C) Z56.9(Cp)
   pin  12                Net-(Z27-I0c)                Z27.11(I0c) Z6.9(Q2)
   pin  13                Net-(Z6-CP1..3)              Z6.1(CP1..3) Z6.12(Q0)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z32  (74C00, Video Sync)
   pin   1                Net-(Z32-Pad1)               Z32.6
   pin   2                Net-(Z32-Pad2)               Z32.8
   pin   3                SYNC                         C43.2 R11.1
   pin   4                Net-(Z32-Pad10)              Z32.10 Z32.11
   pin   5                Net-(Z62A-Q)                 Z32.13 Z62.5(Q)
   pin   6                Net-(Z32-Pad1)               Z32.1
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                Net-(Z32-Pad2)               Z32.2
   pin   9                Net-(Z32-Pad12)              Z32.12 Z52.8
   pin  10                Net-(Z32-Pad10)              Z32.11 Z32.4
   pin  11                Net-(Z32-Pad10)              Z32.10 Z32.4
   pin  12                Net-(Z32-Pad12)              Z32.9 Z52.8
   pin  13                Net-(Z62A-Q)                 Z32.5 Z62.5(Q)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z33  (74LS04, Video Sync)
   pin   1                unconnected-(Z33-Pad1)       (no other connection)
   pin   2                unconnected-(Z33-Pad2)       (no other connection)
   pin   3                unconnected-(Z33-Pad3)       (no other connection)
   pin   4                unconnected-(Z33-Pad4)       (no other connection)
   pin   5                unconnected-(Z33-Pad5)       (no other connection)
   pin   6                unconnected-(Z33-Pad6)       (no other connection)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                unconnected-(Z33-Pad8)       (no other connection)
   pin   9                unconnected-(Z33-Pad9)       (no other connection)
   pin  10                Net-(JP7-A-Pad3)             JP7.3(A)
   pin  11                R1                           JP7.1(A) Z5.13 Z7.1(CP1..3) Z7.12(Q0) Z8.13(I1d)
   pin  12                Net-(Z33-Pad12)              Z52.13
   pin  13                R0                           Z34.12(Q0) Z44.1 Z7.14(CP0) Z8.10(I1c)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z34  (74LS93, Video Counter)
   pin   1 CP1..3         DOT_CLK                      Z27.9(Zc)
   pin   2 R0(1)          GND                          [net GND, 176 pins]
   pin   3 R0(2)          GND                          [net GND, 176 pins]
   pin   5 VCC            +5V                          [net +5V, 138 pins]
   pin   8 Q2             C2                           Z27.14(I0d) Z28.14(CP0) Z36.13(I1d)
   pin   9 Q1             C1                           Z27.13(I1d) Z36.3(I1a)
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 Q3             unconnected-(Z34-Q3-Pad11)   (no other connection)
   pin  12 Q0             R0                           Z33.13 Z44.1 Z7.14(CP0) Z8.10(I1c)
   pin  14 CP0            L3                           Z35.11(Q3) Z39.2(S1) Z5.5 Z52.12 Z56.12(D2)

Z35  (74LS93, Video Counter)
   pin   1 CP1..3         L0                           Z35.12(Q0) Z37.11(R0) Z38.11(R0) Z45.2
   pin   2 R0(1)          Net-(Z35-R0(1))              Z26.2 Z35.3(R0(2))
   pin   3 R0(2)          Net-(Z35-R0(1))              Z26.2 Z35.2(R0(1))
   pin   5 VCC            +5V                          [net +5V, 138 pins]
   pin   8 Q2             L2                           JP10.1(A) Z37.8(R2) Z38.8(R2) Z39.14(S0) Z5.3
   pin   9 Q1             L1                           Z37.10(R1) Z38.10(R1)
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 Q3             L3                           Z34.14(CP0) Z39.2(S1) Z5.5 Z52.12 Z56.12(D2)
   pin  12 Q0             L0                           Z35.1(CP1..3) Z37.11(R0) Z38.11(R0) Z45.2
   pin  14 CP0            HDRV                         Z28.11(Q3) Z5.9 Z54.3 Z62.1(~{R})

Z36  (74LS157, Video Access Multiplexer)
   pin   1 S              ~{VID}                       Z29.1(S) Z53.10(~{S}) Z61.9(O3) Z8.1(S)
   pin   2 I0a            A1                           CN1.4(Pin_4) J4.27(Pin_27) Z14.5(I0b) Z41.5 Z42.7(A1) Z43.7(A1) Z68.12(O3a)
   pin   3 I1a            C1                           Z27.13(I1d) Z34.9(Q1)
   pin   4 Za             VA1                          Z10.6(A1) Z9.6(A1)
   pin   5 I0b            A3                           CN1.9(Pin_9) J4.34(Pin_34) Z14.14(I0d) Z41.3 Z42.5(A3) Z43.5(A3) Z68.14(O2a)
   pin   6 I1b            C3                           Z28.1(CP1..3) Z28.12(Q0) Z46.1
   pin   7 Zb             VA3                          Z10.4(A3) Z9.4(A3)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Zc             VA0                          Z10.5(A0) Z9.5(A0)
   pin  10 I1c            C0                           Z27.7(Zb)
   pin  11 I0c            A0                           CN1.5(Pin_5) J4.25(Pin_25) Z14.2(I0a) Z41.6 Z42.8(A0) Z43.8(A0) Z68.9(O0b)
   pin  12 Zd             VA2                          Z10.7(A2) Z9.7(A2)
   pin  13 I1d            C2                           Z27.14(I0d) Z28.14(CP0) Z34.8(Q2)
   pin  14 I0d            A2                           CN1.6(Pin_6) J4.40(Pin_40) Z14.11(I0c) Z41.4 Z42.6(A2) Z43.6(A2) Z68.7(O1b)
   pin  15 E              GND                          [net GND, 176 pins]
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z37  (MCM6670, Video Generator)
   pin   1 A6             LB6                          Z38.1(A6) Z56.15(Q3)
   pin   2 A5             LB5                          Z11.10(Q3) Z38.2(A5) Z39.12(I2b)
   pin   3 A4             LB4                          Z11.5(Q1) Z38.3(A4) Z39.4(I2a)
   pin   4 A3             LB3                          Z11.7(Q2) Z38.4(A3) Z39.11(I1b)
   pin   5 A2             LB2                          Z11.2(Q0) Z38.5(A2) Z39.5(I1a)
   pin   6 A1             LB1                          Z11.12(Q4) Z38.6(A1) Z39.10(I0b)
   pin   7 A0             LB0                          Z11.15(Q5) Z38.7(A0) Z39.6(I0a)
   pin   8 R2             L2                           JP10.1(A) Z35.8(Q2) Z38.8(R2) Z39.14(S0) Z5.3
   pin   9 GND            GND                          [net GND, 176 pins]
   pin  10 R1             L1                           Z35.9(Q1) Z38.10(R1)
   pin  11 R0             L0                           Z35.1(CP1..3) Z35.12(Q0) Z38.11(R0) Z45.2
   pin  12 D0             Net-(Z37-D0)                 Z38.12(D0) Z57.4(C)
   pin  13 D1             Net-(Z37-D1)                 Z38.13(D1) Z57.5(D)
   pin  14 D2             Net-(Z37-D2)                 Z38.14(D2) Z57.10(E)
   pin  15 D3             Net-(Z37-D3)                 Z38.15(D3) Z57.11(F)
   pin  16 D4             Net-(Z37-D4)                 Z38.16(D4) Z57.12(G)
   pin  17 ~{CS}          ~{CGA}                       Z53.5(Q)
   pin  18 VCC            +5V                          [net +5V, 138 pins]

Z38  (MCM6670, Video Generator)
   pin   1 A6             LB6                          Z37.1(A6) Z56.15(Q3)
   pin   2 A5             LB5                          Z11.10(Q3) Z37.2(A5) Z39.12(I2b)
   pin   3 A4             LB4                          Z11.5(Q1) Z37.3(A4) Z39.4(I2a)
   pin   4 A3             LB3                          Z11.7(Q2) Z37.4(A3) Z39.11(I1b)
   pin   5 A2             LB2                          Z11.2(Q0) Z37.5(A2) Z39.5(I1a)
   pin   6 A1             LB1                          Z11.12(Q4) Z37.6(A1) Z39.10(I0b)
   pin   7 A0             LB0                          Z11.15(Q5) Z37.7(A0) Z39.6(I0a)
   pin   8 R2             L2                           JP10.1(A) Z35.8(Q2) Z37.8(R2) Z39.14(S0) Z5.3
   pin   9 GND            GND                          [net GND, 176 pins]
   pin  10 R1             L1                           Z35.9(Q1) Z37.10(R1)
   pin  11 R0             L0                           Z35.1(CP1..3) Z35.12(Q0) Z37.11(R0) Z45.2
   pin  12 D0             Net-(Z37-D0)                 Z37.12(D0) Z57.4(C)
   pin  13 D1             Net-(Z37-D1)                 Z37.13(D1) Z57.5(D)
   pin  14 D2             Net-(Z37-D2)                 Z37.14(D2) Z57.10(E)
   pin  15 D3             Net-(Z37-D3)                 Z37.15(D3) Z57.11(F)
   pin  16 D4             Net-(Z37-D4)                 Z37.16(D4) Z57.12(G)
   pin  17 ~{CS}          ~{CGB}                       Z53.6(~{Q})
   pin  18 VCC            +5V                          [net +5V, 138 pins]

Z39  (74LS153, Video Generator)
   pin   1 Ea             GND                          [net GND, 176 pins]
   pin   2 S1             L3                           Z34.14(CP0) Z35.11(Q3) Z5.5 Z52.12 Z56.12(D2)
   pin   3 I3a            unconnected-(Z39-I3a-Pad3)   (no other connection)
   pin   4 I2a            LB4                          Z11.5(Q1) Z37.3(A4) Z38.3(A4)
   pin   5 I1a            LB2                          Z11.2(Q0) Z37.5(A2) Z38.5(A2)
   pin   6 I0a            LB0                          Z11.15(Q5) Z37.7(A0) Z38.7(A0)
   pin   7 Za             Net-(Z39-Za)                 Z58.11(F) Z58.12(G) Z58.14(H)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Zb             Net-(Z39-Zb)                 Z58.10(E) Z58.4(C) Z58.5(D)
   pin  10 I0b            LB1                          Z11.12(Q4) Z37.6(A1) Z38.6(A1)
   pin  11 I1b            LB3                          Z11.7(Q2) Z37.4(A3) Z38.4(A3)
   pin  12 I2b            LB5                          Z11.10(Q3) Z37.2(A5) Z38.2(A5)
   pin  13 I3b            unconnected-(Z39-I3b-Pad13)  (no other connection)
   pin  14 S0             L2                           JP10.1(A) Z35.8(Q2) Z37.8(R2) Z38.8(R2) Z5.3
   pin  15 Eb             GND                          [net GND, 176 pins]
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z40  (74LS32, Address Decoder)
   pin   1                ~{IN}                        J4.19(Pin_19) Z30.9
   pin   2                Net-(Z40-Pad2)               Z40.4 Z41.8
   pin   3                ~{INSIG}                     Z59.1
   pin   4                Net-(Z40-Pad2)               Z40.2 Z41.8
   pin   5                ~{OUT}                       J4.12(Pin_12) Z30.7
   pin   6                ~{OUTSIG}                    Z31.5 Z4.9(Cp) Z53.3(C)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                ~{MEM}                       Z24.1 Z24.15 Z30.15
   pin   9                Net-(Z40-Pad9)               Z60.12
   pin  10                ~{RD}                        J4.15(Pin_15) Z29.5(I0b) Z30.5
   pin  11                Net-(Z12-A->B)               Z12.1(A->B)
   pin  12                ~{VWR}                       Z10.10(~{WR}) Z29.12(Zd) Z40.13 Z51.2 Z9.10(~{WR})
   pin  13                ~{VWR}                       Z10.10(~{WR}) Z29.12(Zd) Z40.12 Z51.2 Z9.10(~{WR})
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z41  (74LS30, Cassette Interface)
   pin   1                A7                           CN1.8(Pin_8) J4.36(Pin_36) Z14.3(I1a) Z42.1(A7) Z43.1(A7) Z68.18(O0a) Z8.14(I0d)
   pin   2                A6                           CN1.7(Pin_7) J4.38(Pin_38) Z13.11(I0c) Z42.2(A6) Z43.2(A6) Z68.3(O3b) Z8.11(I0c)
   pin   3                A3                           CN1.9(Pin_9) J4.34(Pin_34) Z14.14(I0d) Z36.5(I0b) Z42.5(A3) Z43.5(A3) Z68.14(O2a)
   pin   4                A2                           CN1.6(Pin_6) J4.40(Pin_40) Z14.11(I0c) Z36.14(I0d) Z42.6(A2) Z43.6(A2) Z68.7(O1b)
   pin   5                A1                           CN1.4(Pin_4) J4.27(Pin_27) Z14.5(I0b) Z36.2(I0a) Z42.7(A1) Z43.7(A1) Z68.12(O3a)
   pin   6                A0                           CN1.5(Pin_5) J4.25(Pin_25) Z14.2(I0a) Z36.11(I0c) Z42.8(A0) Z43.8(A0) Z68.9(O0b)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                Net-(Z40-Pad2)               Z40.2 Z40.4
   pin  11                A4                           CN1.2(Pin_2) J4.31(Pin_31) Z13.2(I0a) Z29.11(I0c) Z42.4(A4) Z43.4(A4) Z68.5(O2b)
   pin  12                A5                           CN1.3(Pin_3) J4.35(Pin_35) Z13.5(I0b) Z29.2(I0a) Z42.3(A5) Z43.3(A5) Z68.16(O1a)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z42  (2364_20L, ROM)
   pin   1 A7             A7                           CN1.8(Pin_8) J4.36(Pin_36) Z14.3(I1a) Z41.1 Z43.1(A7) Z68.18(O0a) Z8.14(I0d)
   pin   2 A6             A6                           CN1.7(Pin_7) J4.38(Pin_38) Z13.11(I0c) Z41.2 Z43.2(A6) Z68.3(O3b) Z8.11(I0c)
   pin   3 A5             A5                           CN1.3(Pin_3) J4.35(Pin_35) Z13.5(I0b) Z29.2(I0a) Z41.12 Z43.3(A5) Z68.16(O1a)
   pin   4 A4             A4                           CN1.2(Pin_2) J4.31(Pin_31) Z13.2(I0a) Z29.11(I0c) Z41.11 Z43.4(A4) Z68.5(O2b)
   pin   5 A3             A3                           CN1.9(Pin_9) J4.34(Pin_34) Z14.14(I0d) Z36.5(I0b) Z41.3 Z43.5(A3) Z68.14(O2a)
   pin   6 A2             A2                           CN1.6(Pin_6) J4.40(Pin_40) Z14.11(I0c) Z36.14(I0d) Z41.4 Z43.6(A2) Z68.7(O1b)
   pin   7 A1             A1                           CN1.4(Pin_4) J4.27(Pin_27) Z14.5(I0b) Z36.2(I0a) Z41.5 Z43.7(A1) Z68.12(O3a)
   pin   8 A0             A0                           CN1.5(Pin_5) J4.25(Pin_25) Z14.2(I0a) Z36.11(I0c) Z41.6 Z43.8(A0) Z68.9(O0b)
   pin   9 D0             KBD0                         CN1.11(Pin_11) RP2.3(R2) Z22.14(OUT) Z24.14 Z43.9(D0)
   pin  10 D1             KBD1                         CN1.12(Pin_12) RP2.2(R1) Z21.14(OUT) Z24.2 Z43.10(D1)
   pin  11 D2             KBD2                         CN1.13(Pin_13) RP2.5(R4) Z20.14(OUT) Z24.12 Z43.11(D2)
   pin  12 GND            GND                          [net GND, 176 pins]
   pin  13 D3             KBD3                         CN1.14(Pin_14) RP2.7(R6) Z19.14(OUT) Z30.12 Z43.13(D3)
   pin  14 D4             KBD4                         CN1.15(Pin_15) RP2.9(R8) Z18.14(OUT) Z30.14 Z43.14(D4)
   pin  15 D5             KBD5                         CN1.16(Pin_16) RP2.8(R7) Z17.14(OUT) Z24.10 Z43.15(D5)
   pin  16 D6             KBD6                         CN1.17(Pin_17) RP2.6(R5) Z16.14(OUT) Z24.6 Z43.16(D6)
   pin  17 D7             KBD7                         CN1.18(Pin_18) RP2.4(R3) Z15.14(OUT) Z24.4 Z43.17(D7)
   pin  18 A11            A11                          CN2.4(Pin_4) J4.9(Pin_9) Z13.3(I1a) Z43.18(A11) Z49.3(O3b) Z61.13(A1)
   pin  19 A10            A10                          CN2.3(Pin_3) J4.4(Pin_4) Z14.13(I1d) Z43.19(A10) Z49.18(O0a) Z61.14(A0)
   pin  20 ~{OE}          ~{ROMA}                      Z60.13 Z60.8
   pin  21 A12            A12                          J4.5(Pin_5) Z13.6(I1b) Z43.21(~{CE2}) Z49.5(O2b) Z61.2(A0)
   pin  22 A9             A9                           CN2.2(Pin_2) J4.17(Pin_17) Z14.10(I1c) Z43.22(A9) Z49.16(O1a) Z8.5(I0b)
   pin  23 A8             A8                           CN2.1(Pin_1) J4.11(Pin_11) Z14.6(I1b) Z43.23(A8) Z49.14(O2a) Z8.2(I0a)
   pin  24 VCC            +5V                          [net +5V, 138 pins]

Z43  (2332_20L_21L, ROM)
   pin   1 A7             A7                           CN1.8(Pin_8) J4.36(Pin_36) Z14.3(I1a) Z41.1 Z42.1(A7) Z68.18(O0a) Z8.14(I0d)
   pin   2 A6             A6                           CN1.7(Pin_7) J4.38(Pin_38) Z13.11(I0c) Z41.2 Z42.2(A6) Z68.3(O3b) Z8.11(I0c)
   pin   3 A5             A5                           CN1.3(Pin_3) J4.35(Pin_35) Z13.5(I0b) Z29.2(I0a) Z41.12 Z42.3(A5) Z68.16(O1a)
   pin   4 A4             A4                           CN1.2(Pin_2) J4.31(Pin_31) Z13.2(I0a) Z29.11(I0c) Z41.11 Z42.4(A4) Z68.5(O2b)
   pin   5 A3             A3                           CN1.9(Pin_9) J4.34(Pin_34) Z14.14(I0d) Z36.5(I0b) Z41.3 Z42.5(A3) Z68.14(O2a)
   pin   6 A2             A2                           CN1.6(Pin_6) J4.40(Pin_40) Z14.11(I0c) Z36.14(I0d) Z41.4 Z42.6(A2) Z68.7(O1b)
   pin   7 A1             A1                           CN1.4(Pin_4) J4.27(Pin_27) Z14.5(I0b) Z36.2(I0a) Z41.5 Z42.7(A1) Z68.12(O3a)
   pin   8 A0             A0                           CN1.5(Pin_5) J4.25(Pin_25) Z14.2(I0a) Z36.11(I0c) Z41.6 Z42.8(A0) Z68.9(O0b)
   pin   9 D0             KBD0                         CN1.11(Pin_11) RP2.3(R2) Z22.14(OUT) Z24.14 Z42.9(D0)
   pin  10 D1             KBD1                         CN1.12(Pin_12) RP2.2(R1) Z21.14(OUT) Z24.2 Z42.10(D1)
   pin  11 D2             KBD2                         CN1.13(Pin_13) RP2.5(R4) Z20.14(OUT) Z24.12 Z42.11(D2)
   pin  12 GND            GND                          [net GND, 176 pins]
   pin  13 D3             KBD3                         CN1.14(Pin_14) RP2.7(R6) Z19.14(OUT) Z30.12 Z42.13(D3)
   pin  14 D4             KBD4                         CN1.15(Pin_15) RP2.9(R8) Z18.14(OUT) Z30.14 Z42.14(D4)
   pin  15 D5             KBD5                         CN1.16(Pin_16) RP2.8(R7) Z17.14(OUT) Z24.10 Z42.15(D5)
   pin  16 D6             KBD6                         CN1.17(Pin_17) RP2.6(R5) Z16.14(OUT) Z24.6 Z42.16(D6)
   pin  17 D7             KBD7                         CN1.18(Pin_18) RP2.4(R3) Z15.14(OUT) Z24.4 Z42.17(D7)
   pin  18 A11            A11                          CN2.4(Pin_4) J4.9(Pin_9) Z13.3(I1a) Z42.18(A11) Z49.3(O3b) Z61.13(A1)
   pin  19 A10            A10                          CN2.3(Pin_3) J4.4(Pin_4) Z14.13(I1d) Z42.19(A10) Z49.18(O0a) Z61.14(A0)
   pin  20 ~{CE1}         ~{ROMB}                      JP2.2(B) R72.1 Z60.2
   pin  21 ~{CE2}         A12                          J4.5(Pin_5) Z13.6(I1b) Z42.21(A12) Z49.5(O2b) Z61.2(A0)
   pin  22 A9             A9                           CN2.2(Pin_2) J4.17(Pin_17) Z14.10(I1c) Z42.22(A9) Z49.16(O1a) Z8.5(I0b)
   pin  23 A8             A8                           CN2.1(Pin_1) J4.11(Pin_11) Z14.6(I1b) Z42.23(A8) Z49.14(O2a) Z8.2(I0a)
   pin  24 VCC            +5V                          [net +5V, 138 pins]

Z44  (74LS00, CPU)
   pin   1                R0                           Z33.13 Z34.12(Q0) Z7.14(CP0) Z8.10(I1c)
   pin   2                VDRV                         Z5.1 Z52.2 Z54.2 Z7.11(Q3)
   pin   3                Net-(Z44-Pad3)               Z45.3
   pin   4                unconnected-(Z44-Pad4)       (no other connection)
   pin   5                unconnected-(Z44-Pad5)       (no other connection)
   pin   6                unconnected-(Z44-Pad6)       (no other connection)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                MREQ                         Z62.13(~{R}) Z63.1(~{R}) Z63.13(~{R}) Z63.2(D)
   pin   9                Net-(Z48-~{WR})              Z48.22(~{WR}) Z67.1 Z67.4
   pin  10                Net-(Z48-~{RD})              Z47.9 Z48.21(~{RD}) Z67.10 Z67.12
   pin  11                Net-(Z44-Pad11)              Z64.12
   pin  12                A14                          J4.10(Pin_10) Z44.13 Z49.12(O3a) Z64.1
   pin  13                A14                          J4.10(Pin_10) Z44.12 Z49.12(O3a) Z64.1
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z45  (74LS02, CPU)
   pin   1                Net-(Z45-Pad1)               Z46.3
   pin   2                L0                           Z35.1(CP1..3) Z35.12(Q0) Z37.11(R0) Z38.11(R0)
   pin   3                Net-(Z44-Pad3)               Z44.3
   pin   4                unconnected-(Z45-Pad4)       (no other connection)
   pin   5                unconnected-(Z45-Pad5)       (no other connection)
   pin   6                unconnected-(Z45-Pad6)       (no other connection)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                Net-(C57-Pad2)               C57.2 Z45.11 Z45.9 Z47.6
   pin   9                Net-(C57-Pad2)               C57.2 Z45.11 Z45.8 Z47.6
   pin  10                Net-(Z48-~{NMI})             Z48.17(~{NMI})
   pin  11                Net-(C57-Pad2)               C57.2 Z45.8 Z45.9 Z47.6
   pin  12                Net-(Z45-Pad12)              Z46.13 Z47.3
   pin  13                ~{SYSRES}                    CN2.9(Pin_9) J4.2(Pin_2)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z46  (74LS04, )
   pin   1                C3                           Z28.1(CP1..3) Z28.12(Q0) Z36.6(I1b)
   pin   2                Net-(Z46-Pad2)               Z51.12
   pin   3                Net-(Z45-Pad1)               Z45.1
   pin   4                Net-(JP10-A-Pad3)            JP10.3(A)
   pin   5                unconnected-(Z46-Pad5)       (no other connection)
   pin   6                unconnected-(Z46-Pad6)       (no other connection)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                ~{CLK_EN}                    Z6.6(R0(1)) Z6.7(R0(2)) Z65.6(R0(1)) Z65.7(R0(2))
   pin   9                Net-(R54-Pad2)               R54.2
   pin  10                Net-(Z49-OEa)                Z30.1 Z49.1(OEa) Z49.19(OEb) Z66.1 Z68.1(OEa) Z68.19(OEb)
   pin  11                ~{TEST}                      J4.23(Pin_23) R55.2 Z47.10 Z48.25(~{BUSRQ})
   pin  12                Net-(Z48-~{RESET})           Z48.26(~{RESET})
   pin  13                Net-(Z45-Pad12)              Z45.12 Z47.3
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z47  (74LS132, CPU)
   pin   1                Net-(C70-Pad1)               C70.1 R49.2 Z47.2
   pin   2                Net-(C70-Pad1)               C70.1 R49.2 Z47.1
   pin   3                Net-(Z45-Pad12)              Z45.12 Z46.13
   pin   4                Net-(C40-Pad1)               C40.1 R31.2 R32.1
   pin   5                Net-(Z48-~{HALT})            Z48.18(~{HALT})
   pin   6                Net-(C57-Pad2)               C57.2 Z45.11 Z45.8 Z45.9
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                Net-(Z47-Pad12)              Z47.12 Z47.13
   pin   9                Net-(Z48-~{RD})              Z44.10 Z48.21(~{RD}) Z67.10 Z67.12
   pin  10                ~{TEST}                      J4.23(Pin_23) R55.2 Z46.11 Z48.25(~{BUSRQ})
   pin  11                ~{DBIN}                      Z23.1(A->B)
   pin  12                Net-(Z47-Pad12)              Z47.13 Z47.8
   pin  13                Net-(Z47-Pad12)              Z47.12 Z47.8
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z48  (Z80CPU, CPU)
   pin   1 A11            ZA11                         Z49.17(I3b)
   pin   2 A12            ZA12                         Z49.15(I2b)
   pin   3 A13            ZA13                         Z49.13(I1b)
   pin   4 A14            ZA14                         Z49.8(I3a)
   pin   5 A15            ZA15                         Z49.11(I0b)
   pin   6 ~{CLK}         ZCLK                         R75.2 Z66.13
   pin   7 D4             ZD4                          Z23.8(A6)
   pin   8 D3             ZD3                          Z23.9(A7)
   pin   9 D5             ZD5                          Z23.7(A5)
   pin  10 D6             ZD6                          Z23.6(A4)
   pin  11 VCC            +5V                          [net +5V, 138 pins]
   pin  12 D2             ZD2                          Z23.5(A3)
   pin  13 D7             ZD7                          Z23.4(A2)
   pin  14 D0             ZD0                          Z23.3(A1)
   pin  15 D1             ZD1                          Z23.2(A0)
   pin  16 ~{INT}         ~{INT}                       J4.21(Pin_21) R77.2
   pin  17 ~{NMI}         Net-(Z48-~{NMI})             Z45.10
   pin  18 ~{HALT}        Net-(Z48-~{HALT})            Z47.5
   pin  19 ~{MREQ}        ~{ZRAS}                      Z66.2 Z67.13 Z67.2
   pin  20 ~{IORQ}        Net-(Z48-~{IORQ})            Z64.9 Z67.5 Z67.9
   pin  21 ~{RD}          Net-(Z48-~{RD})              Z44.10 Z47.9 Z67.10 Z67.12
   pin  22 ~{WR}          Net-(Z48-~{WR})              Z44.9 Z67.1 Z67.4
   pin  23 ~{BUSACK}      unconnected-(Z48-~{BUSACK}-Pad23) (no other connection)
   pin  24 ~{WAIT}        ~{WAIT}                      J4.33(Pin_33) R41.2
   pin  25 ~{BUSRQ}       ~{TEST}                      J4.23(Pin_23) R55.2 Z46.11 Z47.10
   pin  26 ~{RESET}       Net-(Z48-~{RESET})           Z46.12
   pin  27 ~{M1}          Net-(Z48-~{M1})              Z64.10
   pin  28 ~{RFSH}        unconnected-(Z48-~{RFSH}-Pad28) (no other connection)
   pin  29 GND            GND                          [net GND, 176 pins]
   pin  30 A0             ZA0                          Z68.11(I0b)
   pin  31 A1             ZA1                          Z68.8(I3a)
   pin  32 A2             ZA2                          Z68.13(I1b)
   pin  33 A3             ZA3                          Z68.6(I2a)
   pin  34 A4             ZA4                          Z68.15(I2b)
   pin  35 A5             ZA5                          Z68.4(I1a)
   pin  36 A6             ZA6                          Z68.17(I3b)
   pin  37 A7             ZA7                          Z68.2(I0a)
   pin  38 A8             ZA8                          Z49.6(I2a)
   pin  39 A9             ZA9                          Z49.4(I1a)
   pin  40 A10            ZA10                         Z49.2(I0a)

Z49  (74LS244, CPU Gating)
   pin   1 OEa            Net-(Z49-OEa)                Z30.1 Z46.10 Z49.19(OEb) Z66.1 Z68.1(OEa) Z68.19(OEb)
   pin   2 I0a            ZA10                         Z48.40(A10)
   pin   3 O3b            A11                          CN2.4(Pin_4) J4.9(Pin_9) Z13.3(I1a) Z42.18(A11) Z43.18(A11) Z61.13(A1)
   pin   4 I1a            ZA9                          Z48.39(A9)
   pin   5 O2b            A12                          J4.5(Pin_5) Z13.6(I1b) Z42.21(A12) Z43.21(~{CE2}) Z61.2(A0)
   pin   6 I2a            ZA8                          Z48.38(A8)
   pin   7 O1b            A13                          J4.6(Pin_6) Z13.10(I1c) Z61.3(A1)
   pin   8 I3a            ZA14                         Z48.4(A14)
   pin   9 O0b            A15                          J4.7(Pin_7) Z64.5
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 I0b            ZA15                         Z48.5(A15)
   pin  12 O3a            A14                          J4.10(Pin_10) Z44.12 Z44.13 Z64.1
   pin  13 I1b            ZA13                         Z48.3(A13)
   pin  14 O2a            A8                           CN2.1(Pin_1) J4.11(Pin_11) Z14.6(I1b) Z42.23(A8) Z43.23(A8) Z8.2(I0a)
   pin  15 I2b            ZA12                         Z48.2(A12)
   pin  16 O1a            A9                           CN2.2(Pin_2) J4.17(Pin_17) Z14.10(I1c) Z42.22(A9) Z43.22(A9) Z8.5(I0b)
   pin  17 I3b            ZA11                         Z48.1(A11)
   pin  18 O0a            A10                          CN2.3(Pin_3) J4.4(Pin_4) Z14.13(I1d) Z42.19(A10) Z43.19(A10) Z61.14(A0)
   pin  19 OEb            Net-(Z49-OEa)                Z30.1 Z46.10 Z49.1(OEa) Z66.1 Z68.1(OEa) Z68.19(OEb)
   pin  20 VCC            +5V                          [net +5V, 138 pins]

Z50  (7404, Clock)
   pin   1                unconnected-(Z50-Pad1)       (no other connection)
   pin   2                unconnected-(Z50-Pad2)       (no other connection)
   pin   3                Net-(C60-Pad1)               C60.1 R57.1
   pin   4                Net-(R57-Pad2)               R57.2 Y1.1(1)
   pin   5                Net-(R56-Pad1)               R56.1 Y1.2(2)
   pin   6                Net-(C60-Pad2)               C60.2 R56.2 Z50.9
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                CLK                          Z27.3(I1a) Z62.11(C) Z63.11(C) Z63.3(C) Z65.1(CP1..3) Z65.14(CP0)
   pin   9                Net-(C60-Pad2)               C60.2 R56.2 Z50.6
   pin  10                Net-(Z50-Pad10)              Z55.12 Z55.4
   pin  11                ~{LATCH}                     Z11.9(Cp) Z31.11 Z53.11(C) Z56.9(Cp)
   pin  12                Net-(Z57-Clk)                Z57.7(Clk) Z58.7(Clk)
   pin  13                SHIFT                        Z27.4(Za) Z6.14(CP0)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z51  (74LS08, Video RAM)
   pin   1                ~{VRD}                       Z29.7(Zb)
   pin   2                ~{VWR}                       Z10.10(~{WR}) Z29.12(Zd) Z40.12 Z40.13 Z9.10(~{WR})
   pin   3                Net-(Z12-CE)                 Z12.19(CE)
   pin   4                unconnected-(Z51-Pad4)       (no other connection)
   pin   5                unconnected-(Z51-Pad5)       (no other connection)
   pin   6                unconnected-(Z51-Pad6)       (no other connection)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                unconnected-(Z51-Pad8)       (no other connection)
   pin   9                unconnected-(Z51-Pad9)       (no other connection)
   pin  10                unconnected-(Z51-Pad10)      (no other connection)
   pin  11                Net-(Z62A-D)                 Z62.2(D)
   pin  12                Net-(Z46-Pad2)               Z46.2
   pin  13                C4                           Z28.9(Q1) Z29.10(I1c) Z5.10
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z52  (74LS08, Video Sync)
   pin   1                Net-(JP7-B)                  JP7.2(B)
   pin   2                VDRV                         Z44.2 Z5.1 Z54.2 Z7.11(Q3)
   pin   3                Net-(Z52-Pad3)               Z52.4
   pin   4                Net-(Z52-Pad3)               Z52.3
   pin   5                Net-(Z52-Pad11)              Z52.11
   pin   6                Net-(Z52-Pad6)               Z52.9
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                Net-(Z32-Pad12)              Z32.12 Z32.9
   pin   9                Net-(Z52-Pad6)               Z52.6
   pin  10                Net-(JP8-B)                  JP8.2(B)
   pin  11                Net-(Z52-Pad11)              Z52.5
   pin  12                L3                           Z34.14(CP0) Z35.11(Q3) Z39.2(S1) Z5.5 Z56.12(D2)
   pin  13                Net-(Z33-Pad12)              Z33.12
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z53  (74LS74, Cassette Interface)
   pin   1 ~{R}           Net-(JP5-B)                  JP5.2(B)
   pin   2 D              D7                           J4.20(Pin_20) RP1.3(R2) Z12.13(B5) Z15.2(IN) Z23.16(B2) Z24.5 Z59.5
   pin   3 C              ~{OUTSIG}                    Z31.5 Z4.9(Cp) Z40.6
   pin   4 ~{S}           Net-(JP4-B)                  JP4.2(B)
   pin   5 Q              ~{CGA}                       Z37.17(~{CS})
   pin   6 ~{Q}           ~{CGB}                       Z38.17(~{CS})
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8 ~{Q}           ~{VCLR}                      Z11.1(~{Mr}) Z56.1(~{Mr})
   pin   9 Q              unconnected-(Z53B-Q-Pad9)    (no other connection)
   pin  10 ~{S}           ~{VID}                       Z29.1(S) Z36.1(S) Z61.9(O3) Z8.1(S)
   pin  11 C              ~{LATCH}                     Z11.9(Cp) Z31.11 Z50.11 Z56.9(Cp)
   pin  12 D              GND                          [net GND, 176 pins]
   pin  13 ~{R}           Net-(Z53B-~{R})              R66.1
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z54  (74LS02, Video Latch)
   pin   1                Net-(Z56-D1)                 Z56.5(D1)
   pin   2                VDRV                         Z44.2 Z5.1 Z52.2 Z7.11(Q3)
   pin   3                HDRV                         Z28.11(Q3) Z35.14(CP0) Z5.9 Z62.1(~{R})
   pin   4                unconnected-(Z54-Pad4)       (no other connection)
   pin   5                unconnected-(Z54-Pad5)       (no other connection)
   pin   6                unconnected-(Z54-Pad6)       (no other connection)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                unconnected-(Z54-Pad8)       (no other connection)
   pin   9                unconnected-(Z54-Pad9)       (no other connection)
   pin  10                unconnected-(Z54-Pad10)      (no other connection)
   pin  11                Net-(Z57-Qh)                 Z57.13(Qh)
   pin  12                Net-(Z58-Qh)                 Z58.13(Qh)
   pin  13                PIXEL                        Z3.1(1A) Z3.2(1B)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z55  (74LS20, Video Generator)
   pin   1                ~{CHARGAP}                   Z56.11(~{Q2})
   pin   2                ~{GRAPHICS}                  Z56.3(~{Q0})
   pin   4                Net-(Z50-Pad10)              Z50.10 Z55.12
   pin   5                ~{BLANK}                     Z55.10 Z55.9 Z56.7(Q1)
   pin   6                Net-(Z57-PE)                 Z57.15(PE)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                Net-(Z58-PE)                 Z58.15(PE)
   pin   9                ~{BLANK}                     Z55.10 Z55.5 Z56.7(Q1)
   pin  10                ~{BLANK}                     Z55.5 Z55.9 Z56.7(Q1)
   pin  12                Net-(Z50-Pad10)              Z50.10 Z55.4
   pin  13                GRAPHICS                     Z56.2(Q0)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z56  (74LS175, Video Latch)
   pin   1 ~{Mr}          ~{VCLR}                      Z11.1(~{Mr}) Z53.8(~{Q})
   pin   2 Q0             GRAPHICS                     Z55.13
   pin   3 ~{Q0}          ~{GRAPHICS}                  Z55.2
   pin   4 D0             VD7                          Z12.7(A5) Z9.11(D3)
   pin   5 D1             Net-(Z56-D1)                 Z54.1
   pin   6 ~{Q1}          unconnected-(Z56-~{Q1}-Pad6) (no other connection)
   pin   7 Q1             ~{BLANK}                     Z55.10 Z55.5 Z55.9
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Cp             ~{LATCH}                     Z11.9(Cp) Z31.11 Z50.11 Z53.11(C)
   pin  10 Q2             unconnected-(Z56-Q2-Pad10)   (no other connection)
   pin  11 ~{Q2}          ~{CHARGAP}                   Z55.1
   pin  12 D2             L3                           Z34.14(CP0) Z35.11(Q3) Z39.2(S1) Z5.5 Z52.12
   pin  13 D3             VD6                          Z12.6(A4) Z9.12(D2)
   pin  14 ~{Q3}          unconnected-(Z56-~{Q3}-Pad14) (no other connection)
   pin  15 Q3             LB6                          Z37.1(A6) Z38.1(A6)
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z57  (74LS166, Video Generator)
   pin   1 Ds             GND                          [net GND, 176 pins]
   pin   2 A              GND                          [net GND, 176 pins]
   pin   3 B              GND                          [net GND, 176 pins]
   pin   4 C              Net-(Z37-D0)                 Z37.12(D0) Z38.12(D0)
   pin   5 D              Net-(Z37-D1)                 Z37.13(D1) Z38.13(D1)
   pin   6 CE             GND                          [net GND, 176 pins]
   pin   7 Clk            Net-(Z57-Clk)                Z50.12 Z58.7(Clk)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Clr            Net-(Z57-Clr)                R68.1 Z58.9(Clr)
   pin  10 E              Net-(Z37-D2)                 Z37.14(D2) Z38.14(D2)
   pin  11 F              Net-(Z37-D3)                 Z37.15(D3) Z38.15(D3)
   pin  12 G              Net-(Z37-D4)                 Z37.16(D4) Z38.16(D4)
   pin  13 Qh             Net-(Z57-Qh)                 Z54.11
   pin  14 H              GND                          [net GND, 176 pins]
   pin  15 PE             Net-(Z57-PE)                 Z55.6
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z58  (74LS166, Video Generator)
   pin   1 Ds             GND                          [net GND, 176 pins]
   pin   2 A              GND                          [net GND, 176 pins]
   pin   3 B              GND                          [net GND, 176 pins]
   pin   4 C              Net-(Z39-Zb)                 Z39.9(Zb) Z58.10(E) Z58.5(D)
   pin   5 D              Net-(Z39-Zb)                 Z39.9(Zb) Z58.10(E) Z58.4(C)
   pin   6 CE             GND                          [net GND, 176 pins]
   pin   7 Clk            Net-(Z57-Clk)                Z50.12 Z57.7(Clk)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 Clr            Net-(Z57-Clr)                R68.1 Z57.9(Clr)
   pin  10 E              Net-(Z39-Zb)                 Z39.9(Zb) Z58.4(C) Z58.5(D)
   pin  11 F              Net-(Z39-Za)                 Z39.7(Za) Z58.12(G) Z58.14(H)
   pin  12 G              Net-(Z39-Za)                 Z39.7(Za) Z58.11(F) Z58.14(H)
   pin  13 Qh             Net-(Z58-Qh)                 Z54.12
   pin  14 H              Net-(Z39-Za)                 Z39.7(Za) Z58.11(F) Z58.12(G)
   pin  15 PE             Net-(Z58-PE)                 Z55.8
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z59  (74LS367, RAM)
   pin   1                ~{INSIG}                     Z40.3
   pin   2                MODESEL                      Z27.1(S) Z4.6(~{Q1})
   pin   3                D6                           J4.24(Pin_24) RP1.5(R4) Z12.14(B4) Z16.2(IN) Z23.14(B4) Z24.7
   pin   4                Net-(Z31-Pad4)               Z31.4 Z31.8
   pin   5                D7                           J4.20(Pin_20) RP1.3(R2) Z12.13(B5) Z15.2(IN) Z23.16(B2) Z24.5 Z53.2(D)
   pin   6                unconnected-(Z59-Pad6)       (no other connection)
   pin   7                unconnected-(Z59-Pad7)       (no other connection)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9                unconnected-(Z59-Pad9)       (no other connection)
   pin  10                unconnected-(Z59-Pad10)      (no other connection)
   pin  11                unconnected-(Z59-Pad11)      (no other connection)
   pin  12                unconnected-(Z59-Pad12)      (no other connection)
   pin  13                Net-(R101-Pad2)              R101.2 R69.2
   pin  14                ~{CAS}                       J4.3(Pin_3) Z66.7
   pin  15                ~{RAM}                       Z60.3 Z64.11
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z60  (74LS11, Address Decoder)
   pin   1                Net-(Z60-Pad1)               Z60.6
   pin   2                ~{ROMB}                      JP2.2(B) R72.1 Z43.20(~{CE1})
   pin   3                ~{RAM}                       Z59.15 Z64.11
   pin   4                ~{KYBD}                      CN1.10(Pin_10) Z61.10(O2)
   pin   5                Net-(JP3-B)                  JP3.2(B) R70.1
   pin   6                Net-(Z60-Pad1)               Z60.1
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                ~{ROMA}                      Z42.20(~{OE}) Z60.13
   pin   9                Net-(JP1-B)                  JP1.2(B) R71.1
   pin  10                ~{CS1}                       CN2.5(Pin_5) Z60.11 Z61.4(O0)
   pin  11                ~{CS1}                       CN2.5(Pin_5) Z60.10 Z61.4(O0)
   pin  12                Net-(Z40-Pad9)               Z40.9
   pin  13                ~{ROMA}                      Z42.20(~{OE}) Z60.8
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z61  (74LS139, Address Decoder)
   pin   1 E              Net-(Z61A-E)                 Z64.3
   pin   2 A0             A12                          J4.5(Pin_5) Z13.6(I1b) Z42.21(A12) Z43.21(~{CE2}) Z49.5(O2b)
   pin   3 A1             A13                          J4.6(Pin_6) Z13.10(I1c) Z49.7(O1b)
   pin   4 O0             ~{CS1}                       CN2.5(Pin_5) Z60.10 Z60.11
   pin   5 O1             ~{CS2}                       CN2.6(Pin_6) JP1.1(A)
   pin   6 O2             ~{CS3}                       CN2.7(Pin_7) JP2.1(A)
   pin   7 O3             Net-(Z61A-O3)                Z61.15(E)
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9 O3             ~{VID}                       Z29.1(S) Z36.1(S) Z53.10(~{S}) Z8.1(S)
   pin  10 O2             ~{KYBD}                      CN1.10(Pin_10) Z60.4
   pin  11 O1             unconnected-(Z61B-O1-Pad11)  (no other connection)
   pin  12 O0             ~{CS4}                       CN2.8(Pin_8) JP3.1(A)
   pin  13 A1             A11                          CN2.4(Pin_4) J4.9(Pin_9) Z13.3(I1a) Z42.18(A11) Z43.18(A11) Z49.3(O3b)
   pin  14 A0             A10                          CN2.3(Pin_3) J4.4(Pin_4) Z14.13(I1d) Z42.19(A10) Z43.19(A10) Z49.18(O0a)
   pin  15 E              Net-(Z61A-O3)                Z61.7(O3)
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z62  (74LS74, CPU)
   pin   1 ~{R}           HDRV                         Z28.11(Q3) Z35.14(CP0) Z5.9 Z54.3
   pin   2 D              Net-(Z62A-D)                 Z51.11
   pin   3 C              HCLK                         Z27.12(Zd)
   pin   4 ~{S}           HI                           R74.2 Z62.10(~{S}) Z63.10(~{S}) Z63.4(~{S})
   pin   5 Q              Net-(Z62A-Q)                 Z32.13 Z32.5
   pin   6 ~{Q}           unconnected-(Z62A-~{Q}-Pad6) (no other connection)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8 ~{Q}           ~{ZCAS}                      Z66.6
   pin   9 Q              unconnected-(Z62B-Q-Pad9)    (no other connection)
   pin  10 ~{S}           HI                           R74.2 Z62.4(~{S}) Z63.10(~{S}) Z63.4(~{S})
   pin  11 C              CLK                          Z27.3(I1a) Z50.8 Z63.11(C) Z63.3(C) Z65.1(CP1..3) Z65.14(CP0)
   pin  12 D              ZMUX                         Z63.9(Q) Z66.4
   pin  13 ~{R}           MREQ                         Z44.8 Z63.1(~{R}) Z63.13(~{R}) Z63.2(D)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z63  (74LS74, CPU)
   pin   1 ~{R}           MREQ                         Z44.8 Z62.13(~{R}) Z63.13(~{R}) Z63.2(D)
   pin   2 D              MREQ                         Z44.8 Z62.13(~{R}) Z63.1(~{R}) Z63.13(~{R})
   pin   3 C              CLK                          Z27.3(I1a) Z50.8 Z62.11(C) Z63.11(C) Z65.1(CP1..3) Z65.14(CP0)
   pin   4 ~{S}           HI                           R74.2 Z62.10(~{S}) Z62.4(~{S}) Z63.10(~{S})
   pin   5 Q              Net-(Z63A-Q)                 Z63.12(D)
   pin   6 ~{Q}           unconnected-(Z63A-~{Q}-Pad6) (no other connection)
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8 ~{Q}           unconnected-(Z63B-~{Q}-Pad8) (no other connection)
   pin   9 Q              ZMUX                         Z62.12(D) Z66.4
   pin  10 ~{S}           HI                           R74.2 Z62.10(~{S}) Z62.4(~{S}) Z63.4(~{S})
   pin  11 C              CLK                          Z27.3(I1a) Z50.8 Z62.11(C) Z63.3(C) Z65.1(CP1..3) Z65.14(CP0)
   pin  12 D              Net-(Z63A-Q)                 Z63.5(Q)
   pin  13 ~{R}           MREQ                         Z44.8 Z62.13(~{R}) Z63.1(~{R}) Z63.2(D)
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z64  (74LS32, CPU)
   pin   1                A14                          J4.10(Pin_10) Z44.12 Z44.13 Z49.12(O3a)
   pin   2                Net-(Z64-Pad13)              Z64.13 Z64.6
   pin   3                Net-(Z61A-E)                 Z61.1(E)
   pin   4                ~{RAS}                       J4.1(Pin_1) Z66.12 Z66.3
   pin   5                A15                          J4.7(Pin_7) Z49.9(O0b)
   pin   6                Net-(Z64-Pad13)              Z64.13 Z64.2
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                ~{INTAK}                     J4.14(Pin_14)
   pin   9                Net-(Z48-~{IORQ})            Z48.20(~{IORQ}) Z67.5 Z67.9
   pin  10                Net-(Z48-~{M1})              Z48.27(~{M1})
   pin  11                ~{RAM}                       Z59.15 Z60.3
   pin  12                Net-(Z44-Pad11)              Z44.11
   pin  13                Net-(Z64-Pad13)              Z64.2 Z64.6
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z65  (74LS92, Clock)
   pin   1 CP1..3         CLK                          Z27.3(I1a) Z50.8 Z62.11(C) Z63.11(C) Z63.3(C) Z65.14(CP0)
   pin   5 VCC            +5V                          [net +5V, 138 pins]
   pin   6 R0(1)          ~{CLK_EN}                    Z46.8 Z6.6(R0(1)) Z6.7(R0(2)) Z65.7(R0(2))
   pin   7 R0(2)          ~{CLK_EN}                    Z46.8 Z6.6(R0(1)) Z6.7(R0(2)) Z65.6(R0(1))
   pin   8 Q3             CLK_DIV6                     Z66.14
   pin   9 Q2             unconnected-(Z65-Q2-Pad9)    (no other connection)
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 Q1             unconnected-(Z65-Q1-Pad11)   (no other connection)
   pin  12 Q0             CLK_DIV2                     Z27.2(I0a)
   pin  14 CP0            CLK                          Z27.3(I1a) Z50.8 Z62.11(C) Z63.11(C) Z63.3(C) Z65.1(CP1..3)

Z66  (74LS367, CPU)
   pin   1                Net-(Z49-OEa)                Z30.1 Z46.10 Z49.1(OEa) Z49.19(OEb) Z68.1(OEa) Z68.19(OEb)
   pin   2                ~{ZRAS}                      Z48.19(~{MREQ}) Z67.13 Z67.2
   pin   3                ~{RAS}                       J4.1(Pin_1) Z64.4 Z66.12
   pin   4                ZMUX                         Z62.12(D) Z63.9(Q)
   pin   5                MUX                          J4.16(Pin_16) Z13.1(S) Z14.1(S)
   pin   6                ~{ZCAS}                      Z62.8(~{Q})
   pin   7                ~{CAS}                       J4.3(Pin_3) Z59.14
   pin   8 GND            GND                          [net GND, 176 pins]
   pin   9                unconnected-(Z66-Pad9)       (no other connection)
   pin  10                unconnected-(Z66-Pad10)      (no other connection)
   pin  11                Net-(R109-Pad2)              R109.2 R76.2
   pin  12                ~{RAS}                       J4.1(Pin_1) Z64.4 Z66.3
   pin  13                ZCLK                         R75.2 Z48.6(~{CLK})
   pin  14                CLK_DIV6                     Z65.8(Q3)
   pin  15                GND                          [net GND, 176 pins]
   pin  16 VCC            +5V                          [net +5V, 138 pins]

Z67  (74LS32, CPU)
   pin   1                Net-(Z48-~{WR})              Z44.9 Z48.22(~{WR}) Z67.4
   pin   2                ~{ZRAS}                      Z48.19(~{MREQ}) Z66.2 Z67.13
   pin   3                ~{ZWR}                       Z30.2
   pin   4                Net-(Z48-~{WR})              Z44.9 Z48.22(~{WR}) Z67.1
   pin   5                Net-(Z48-~{IORQ})            Z48.20(~{IORQ}) Z64.9 Z67.9
   pin   6                ~{ZOUT}                      Z30.6
   pin   7 GND            GND                          [net GND, 176 pins]
   pin   8                ~{ZIN}                       Z30.10
   pin   9                Net-(Z48-~{IORQ})            Z48.20(~{IORQ}) Z64.9 Z67.5
   pin  10                Net-(Z48-~{RD})              Z44.10 Z47.9 Z48.21(~{RD}) Z67.12
   pin  11                ~{ZRD}                       Z30.4
   pin  12                Net-(Z48-~{RD})              Z44.10 Z47.9 Z48.21(~{RD}) Z67.10
   pin  13                ~{ZRAS}                      Z48.19(~{MREQ}) Z66.2 Z67.2
   pin  14 VCC            +5V                          [net +5V, 138 pins]

Z68  (74LS244, CPU Gating)
   pin   1 OEa            Net-(Z49-OEa)                Z30.1 Z46.10 Z49.1(OEa) Z49.19(OEb) Z66.1 Z68.19(OEb)
   pin   2 I0a            ZA7                          Z48.37(A7)
   pin   3 O3b            A6                           CN1.7(Pin_7) J4.38(Pin_38) Z13.11(I0c) Z41.2 Z42.2(A6) Z43.2(A6) Z8.11(I0c)
   pin   4 I1a            ZA5                          Z48.35(A5)
   pin   5 O2b            A4                           CN1.2(Pin_2) J4.31(Pin_31) Z13.2(I0a) Z29.11(I0c) Z41.11 Z42.4(A4) Z43.4(A4)
   pin   6 I2a            ZA3                          Z48.33(A3)
   pin   7 O1b            A2                           CN1.6(Pin_6) J4.40(Pin_40) Z14.11(I0c) Z36.14(I0d) Z41.4 Z42.6(A2) Z43.6(A2)
   pin   8 I3a            ZA1                          Z48.31(A1)
   pin   9 O0b            A0                           CN1.5(Pin_5) J4.25(Pin_25) Z14.2(I0a) Z36.11(I0c) Z41.6 Z42.8(A0) Z43.8(A0)
   pin  10 GND            GND                          [net GND, 176 pins]
   pin  11 I0b            ZA0                          Z48.30(A0)
   pin  12 O3a            A1                           CN1.4(Pin_4) J4.27(Pin_27) Z14.5(I0b) Z36.2(I0a) Z41.5 Z42.7(A1) Z43.7(A1)
   pin  13 I1b            ZA2                          Z48.32(A2)
   pin  14 O2a            A3                           CN1.9(Pin_9) J4.34(Pin_34) Z14.14(I0d) Z36.5(I0b) Z41.3 Z42.5(A3) Z43.5(A3)
   pin  15 I2b            ZA4                          Z48.34(A4)
   pin  16 O1a            A5                           CN1.3(Pin_3) J4.35(Pin_35) Z13.5(I0b) Z29.2(I0a) Z41.12 Z42.3(A5) Z43.3(A5)
   pin  17 I3b            ZA6                          Z48.36(A6)
   pin  18 O0a            A7                           CN1.8(Pin_8) J4.36(Pin_36) Z14.3(I1a) Z41.1 Z42.1(A7) Z43.1(A7) Z8.14(I0d)
   pin  19 OEb            Net-(Z49-OEa)                Z30.1 Z46.10 Z49.1(OEa) Z49.19(OEb) Z66.1 Z68.1(OEa)
   pin  20 VCC            +5V                          [net +5V, 138 pins]

```
## Nets

```
+12V   (20 pins)
    C14      10uF 16V           pin   1  
    C15      0.01uF 24V         pin   1  
    C27      0.1uF 25V          pin   1  
    C30      0.1uF 25V          pin   1  
    C33      0.1uF 25V          pin   1  
    C36      0.1uF 25V          pin   1  
    R26      2.2k               pin   1  
    R30      5.6                pin   1  
    TP1      ~                  pin   1  
    Z1       LM723C             pin  11  VC
    Z1       LM723C             pin  12  V+
    Z15      DRAM_4116          pin   8  VDD
    Z16      DRAM_4116          pin   8  VDD
    Z17      DRAM_4116          pin   8  VDD
    Z18      DRAM_4116          pin   8  VDD
    Z19      DRAM_4116          pin   8  VDD
    Z2       LM723C             pin   3  CSEN
    Z20      DRAM_4116          pin   8  VDD
    Z21      DRAM_4116          pin   8  VDD
    Z22      DRAM_4116          pin   8  VDD

+5V   (138 pins)
    C12      10uF 16V           pin   1  
    C13      0.01uF 24V         pin   1  
    C20      0.1uF 12V          pin   1  
    C22      0.1uF 12V          pin   1  
    C23      0.1uF 12V          pin   1  
    C24      0.1uF 12V          pin   1  
    C25      0.1uF 12V          pin   1  
    C26      0.1uF 12V          pin   1  
    C29      0.1uF 12V          pin   1  
    C32      0.1uF 12V          pin   1  
    C35      0.1uF 12V          pin   1  
    C38      0.1uF 12V          pin   1  
    C39      0.1uF 12V          pin   1  
    C44      0.1uF 12V          pin   1  
    C45      0.1uF 12V          pin   1  
    C46      0.1uF 12V          pin   1  
    C47      0.1uF 12V          pin   1  
    C49      0.1uF 12V          pin   1  
    C51      0.1uF 12V          pin   1  
    C52      0.1uF 12V          pin   1  
    C53      0.1uF 12V          pin   1  
    C54      0.1uF 12V          pin   1  
    C55      0.1uF 12V          pin   1  
    C56      0.1uF 12V          pin   1  
    C58      0.1uF 12V          pin   1  
    C59      0.1uF 12V          pin   1  
    C63      0.1uF 12V          pin   1  
    C64      0.1uF 12V          pin   1  
    C65      0.1uF 12V          pin   1  
    C66      0.1uF 12V          pin   1  
    C67      0.1uF 12V          pin   1  
    C68      0.1uF 12V          pin   1  
    C69      0.1uF 12V          pin   1  
    C71      0.1uF 12V          pin   1  
    C72      0.1uF 12V          pin   1  
    CN1      Connection Mainboard Side pin   1  Pin_1
    CR2      1N4735             pin   1  K
    CR4      1N4148             pin   1  K
    JP9      TRS80_Model_I_Jumper_2_Jap pin   1  A
    K1       Relay_SPDT         pin   1  
    Q2       A1015              pin   1  E
    R16      0.33               pin   2  
    R19      1.2k               pin   1  
    R20      100k               pin   2  
    R31      10k                pin   1  
    R34      10k                pin   2  
    R39      10                 pin   2  
    R40      4.7k               pin   1  
    R41      4.7k               pin   1  
    R48      4.7k               pin   1  
    R49      10k                pin   1  
    R5       220k               pin   2  
    R52      8.2k               pin   2  
    R54      4.7k               pin   1  
    R55      4.7k               pin   1  
    R64      4.7k               pin   1  
    R65      4.7k               pin   2  
    R66      4.7k               pin   2  
    R67      4.7k               pin   2  
    R68      4.7k               pin   2  
    R69      4.7k               pin   1  
    R7       47                 pin   1  
    R70      4.7k               pin   2  
    R71      4.7k               pin   2  
    R72      4.7k               pin   2  
    R74      4.7k               pin   1  
    R75      330                pin   1  
    R76      4.7k               pin   1  
    R77      4.7k               pin   1  
    RP1      4.7k               pin   1  common
    RP2      4.7k               pin   1  common
    TP1      ~                  pin   3  
    Z1       LM723C             pin   3  CSEN
    Z10      SRAM_2114          pin  18  VCC
    Z11      74LS174            pin  16  VCC
    Z12      74LS245            pin  20  VCC
    Z13      74LS157            pin  16  VCC
    Z14      74LS157            pin  16  VCC
    Z15      DRAM_4116          pin   9  VCC
    Z16      DRAM_4116          pin   9  VCC
    Z17      DRAM_4116          pin   9  VCC
    Z18      DRAM_4116          pin   9  VCC
    Z19      DRAM_4116          pin   9  VCC
    Z20      DRAM_4116          pin   9  VCC
    Z21      DRAM_4116          pin   9  VCC
    Z22      DRAM_4116          pin   9  VCC
    Z23      74LS245            pin  20  VCC
    Z24      74LS367            pin  16  VCC
    Z26      74LS14             pin  14  VCC
    Z27      74LS157            pin  16  VCC
    Z28      74LS93             pin   5  VCC
    Z29      74LS157            pin  16  VCC
    Z3       75452              pin   8  VCC
    Z30      74LS367            pin  16  VCC
    Z31      74LS132            pin  14  VCC
    Z32      74C00              pin  14  VCC
    Z33      74LS04             pin  14  VCC
    Z34      74LS93             pin   5  VCC
    Z35      74LS93             pin   5  VCC
    Z36      74LS157            pin  16  VCC
    Z37      MCM6670            pin  18  VCC
    Z38      MCM6670            pin  18  VCC
    Z39      74LS153            pin  16  VCC
    Z4       74LS175            pin  16  VCC
    Z40      74LS32             pin  14  VCC
    Z41      74LS30             pin  14  VCC
    Z42      2364_20L           pin  24  VCC
    Z43      2332_20L_21L       pin  24  VCC
    Z44      74LS00             pin  14  VCC
    Z45      74LS02             pin  14  VCC
    Z46      74LS04             pin  14  VCC
    Z47      74LS132            pin  14  VCC
    Z48      Z80CPU             pin  11  VCC
    Z49      74LS244            pin  20  VCC
    Z5       74LS10             pin  14  VCC
    Z50      7404               pin  14  VCC
    Z51      74LS08             pin  14  VCC
    Z52      74LS08             pin  14  VCC
    Z53      74LS74             pin  14  VCC
    Z54      74LS02             pin  14  VCC
    Z55      74LS20             pin  14  VCC
    Z56      74LS175            pin  16  VCC
    Z57      74LS166            pin  16  VCC
    Z58      74LS166            pin  16  VCC
    Z59      74LS367            pin  16  VCC
    Z6       74LS92             pin   5  VCC
    Z60      74LS11             pin  14  VCC
    Z61      74LS139            pin  16  VCC
    Z62      74LS74             pin  14  VCC
    Z63      74LS74             pin  14  VCC
    Z64      74LS32             pin  14  VCC
    Z65      74LS92             pin   5  VCC
    Z66      74LS367            pin  16  VCC
    Z67      74LS32             pin  14  VCC
    Z68      74LS244            pin  20  VCC
    Z7       74LS93             pin   5  VCC
    Z8       74LS157            pin  16  VCC
    Z9       SRAM_2114          pin  18  VCC

-5V   (18 pins)
    C28      0.1uF 12V          pin   1  
    C31      0.1uF 12V          pin   1  
    C34      0.1uF 12V          pin   1  
    C37      0.1uF 12V          pin   1  
    C6       10uF 16V           pin   2  
    C7       0.01uF 24V         pin   1  
    C8       0.1uF 12V          pin   1  
    CR3      1N5231             pin   2  A
    R12      220                pin   1  
    TP1      ~                  pin   2  
    Z15      DRAM_4116          pin   1  VBB
    Z16      DRAM_4116          pin   1  VBB
    Z17      DRAM_4116          pin   1  VBB
    Z18      DRAM_4116          pin   1  VBB
    Z19      DRAM_4116          pin   1  VBB
    Z20      DRAM_4116          pin   1  VBB
    Z21      DRAM_4116          pin   1  VBB
    Z22      DRAM_4116          pin   1  VBB

/A0   (8 pins)
    CN1      Connection Mainboard Side pin   5  Pin_5
    J4       Edge Connector     pin  25  Pin_25
    Z14      74LS157            pin   2  I0a
    Z36      74LS157            pin  11  I0c
    Z41      74LS30             pin   6  
    Z42      2364_20L           pin   8  A0
    Z43      2332_20L_21L       pin   8  A0
    Z68      74LS244            pin   9  O0b

/A1   (8 pins)
    CN1      Connection Mainboard Side pin   4  Pin_4
    J4       Edge Connector     pin  27  Pin_27
    Z14      74LS157            pin   5  I0b
    Z36      74LS157            pin   2  I0a
    Z41      74LS30             pin   5  
    Z42      2364_20L           pin   7  A1
    Z43      2332_20L_21L       pin   7  A1
    Z68      74LS244            pin  12  O3a

/A10   (7 pins)
    CN2      Conn_01x09         pin   3  Pin_3
    J4       Edge Connector     pin   4  Pin_4
    Z14      74LS157            pin  13  I1d
    Z42      2364_20L           pin  19  A10
    Z43      2332_20L_21L       pin  19  A10
    Z49      74LS244            pin  18  O0a
    Z61      74LS139            pin  14  A0

/A11   (7 pins)
    CN2      Conn_01x09         pin   4  Pin_4
    J4       Edge Connector     pin   9  Pin_9
    Z13      74LS157            pin   3  I1a
    Z42      2364_20L           pin  18  A11
    Z43      2332_20L_21L       pin  18  A11
    Z49      74LS244            pin   3  O3b
    Z61      74LS139            pin  13  A1

/A12   (6 pins)
    J4       Edge Connector     pin   5  Pin_5
    Z13      74LS157            pin   6  I1b
    Z42      2364_20L           pin  21  A12
    Z43      2332_20L_21L       pin  21  ~{CE2}
    Z49      74LS244            pin   5  O2b
    Z61      74LS139            pin   2  A0

/A13   (4 pins)
    J4       Edge Connector     pin   6  Pin_6
    Z13      74LS157            pin  10  I1c
    Z49      74LS244            pin   7  O1b
    Z61      74LS139            pin   3  A1

/A14   (5 pins)
    J4       Edge Connector     pin  10  Pin_10
    Z44      74LS00             pin  12  
    Z44      74LS00             pin  13  
    Z49      74LS244            pin  12  O3a
    Z64      74LS32             pin   1  

/A15   (3 pins)
    J4       Edge Connector     pin   7  Pin_7
    Z49      74LS244            pin   9  O0b
    Z64      74LS32             pin   5  

/A2   (8 pins)
    CN1      Connection Mainboard Side pin   6  Pin_6
    J4       Edge Connector     pin  40  Pin_40
    Z14      74LS157            pin  11  I0c
    Z36      74LS157            pin  14  I0d
    Z41      74LS30             pin   4  
    Z42      2364_20L           pin   6  A2
    Z43      2332_20L_21L       pin   6  A2
    Z68      74LS244            pin   7  O1b

/A3   (8 pins)
    CN1      Connection Mainboard Side pin   9  Pin_9
    J4       Edge Connector     pin  34  Pin_34
    Z14      74LS157            pin  14  I0d
    Z36      74LS157            pin   5  I0b
    Z41      74LS30             pin   3  
    Z42      2364_20L           pin   5  A3
    Z43      2332_20L_21L       pin   5  A3
    Z68      74LS244            pin  14  O2a

/A4   (8 pins)
    CN1      Connection Mainboard Side pin   2  Pin_2
    J4       Edge Connector     pin  31  Pin_31
    Z13      74LS157            pin   2  I0a
    Z29      74LS157            pin  11  I0c
    Z41      74LS30             pin  11  
    Z42      2364_20L           pin   4  A4
    Z43      2332_20L_21L       pin   4  A4
    Z68      74LS244            pin   5  O2b

/A5   (8 pins)
    CN1      Connection Mainboard Side pin   3  Pin_3
    J4       Edge Connector     pin  35  Pin_35
    Z13      74LS157            pin   5  I0b
    Z29      74LS157            pin   2  I0a
    Z41      74LS30             pin  12  
    Z42      2364_20L           pin   3  A5
    Z43      2332_20L_21L       pin   3  A5
    Z68      74LS244            pin  16  O1a

/A6   (8 pins)
    CN1      Connection Mainboard Side pin   7  Pin_7
    J4       Edge Connector     pin  38  Pin_38
    Z13      74LS157            pin  11  I0c
    Z41      74LS30             pin   2  
    Z42      2364_20L           pin   2  A6
    Z43      2332_20L_21L       pin   2  A6
    Z68      74LS244            pin   3  O3b
    Z8       74LS157            pin  11  I0c

/A7   (8 pins)
    CN1      Connection Mainboard Side pin   8  Pin_8
    J4       Edge Connector     pin  36  Pin_36
    Z14      74LS157            pin   3  I1a
    Z41      74LS30             pin   1  
    Z42      2364_20L           pin   1  A7
    Z43      2332_20L_21L       pin   1  A7
    Z68      74LS244            pin  18  O0a
    Z8       74LS157            pin  14  I0d

/A8   (7 pins)
    CN2      Conn_01x09         pin   1  Pin_1
    J4       Edge Connector     pin  11  Pin_11
    Z14      74LS157            pin   6  I1b
    Z42      2364_20L           pin  23  A8
    Z43      2332_20L_21L       pin  23  A8
    Z49      74LS244            pin  14  O2a
    Z8       74LS157            pin   2  I0a

/A9   (7 pins)
    CN2      Conn_01x09         pin   2  Pin_2
    J4       Edge Connector     pin  17  Pin_17
    Z14      74LS157            pin  10  I1c
    Z42      2364_20L           pin  22  A9
    Z43      2332_20L_21L       pin  22  A9
    Z49      74LS244            pin  16  O1a
    Z8       74LS157            pin   5  I0b

/Address Decoder/~{CS1}   (4 pins)
    CN2      Conn_01x09         pin   5  Pin_5
    Z60      74LS11             pin  10  
    Z60      74LS11             pin  11  
    Z61      74LS139            pin   4  O0

/Address Decoder/~{CS2}   (3 pins)
    CN2      Conn_01x09         pin   6  Pin_6
    JP1      TRS80_Model_I_Jumper_2_Jap pin   1  A
    Z61      74LS139            pin   5  O1

/Address Decoder/~{CS3}   (3 pins)
    CN2      Conn_01x09         pin   7  Pin_7
    JP2      TRS80_Model_I_Jumper_2_Jap pin   1  A
    Z61      74LS139            pin   6  O2

/Address Decoder/~{CS4}   (3 pins)
    CN2      Conn_01x09         pin   8  Pin_8
    JP3      TRS80_Model_I_Jumper_2_Jap pin   1  A
    Z61      74LS139            pin  12  O0

/Address Decoder/~{KYBD}   (3 pins)
    CN1      Connection Mainboard Side pin  10  Pin_10
    Z60      74LS11             pin   4  
    Z61      74LS139            pin  10  O2

/Address Decoder/~{MEM}   (4 pins)
    Z24      74LS367            pin   1  
    Z24      74LS367            pin  15  
    Z30      74LS367            pin  15  
    Z40      74LS32             pin   8  

/Address Decoder/~{RAM}   (3 pins)
    Z59      74LS367            pin  15  
    Z60      74LS11             pin   3  
    Z64      74LS32             pin  11  

/Address Decoder/~{RAS}   (4 pins)
    J4       Edge Connector     pin   1  Pin_1
    Z64      74LS32             pin   4  
    Z66      74LS367            pin   3  
    Z66      74LS367            pin  12  

/Address Decoder/~{RD}   (4 pins)
    J4       Edge Connector     pin  15  Pin_15
    Z29      74LS157            pin   5  I0b
    Z30      74LS367            pin   5  
    Z40      74LS32             pin  10  

/Address Decoder/~{ROMA}   (3 pins)
    Z42      2364_20L           pin  20  ~{OE}
    Z60      74LS11             pin   8  
    Z60      74LS11             pin  13  

/Address Decoder/~{ROMB}   (4 pins)
    JP2      TRS80_Model_I_Jumper_2_Jap pin   2  B
    R72      4.7k               pin   1  
    Z43      2332_20L_21L       pin  20  ~{CE1}
    Z60      74LS11             pin   2  

/Address Decoder/~{VID}   (5 pins)
    Z29      74LS157            pin   1  S
    Z36      74LS157            pin   1  S
    Z53      74LS74             pin  10  ~{S}
    Z61      74LS139            pin   9  O3
    Z8       74LS157            pin   1  S

/CPU Gating/MUX   (4 pins)
    J4       Edge Connector     pin  16  Pin_16
    Z13      74LS157            pin   1  S
    Z14      74LS157            pin   1  S
    Z66      74LS367            pin   5  

/CPU Gating/ZA0   (2 pins)
    Z48      Z80CPU             pin  30  A0
    Z68      74LS244            pin  11  I0b

/CPU Gating/ZA1   (2 pins)
    Z48      Z80CPU             pin  31  A1
    Z68      74LS244            pin   8  I3a

/CPU Gating/ZA10   (2 pins)
    Z48      Z80CPU             pin  40  A10
    Z49      74LS244            pin   2  I0a

/CPU Gating/ZA11   (2 pins)
    Z48      Z80CPU             pin   1  A11
    Z49      74LS244            pin  17  I3b

/CPU Gating/ZA12   (2 pins)
    Z48      Z80CPU             pin   2  A12
    Z49      74LS244            pin  15  I2b

/CPU Gating/ZA13   (2 pins)
    Z48      Z80CPU             pin   3  A13
    Z49      74LS244            pin  13  I1b

/CPU Gating/ZA14   (2 pins)
    Z48      Z80CPU             pin   4  A14
    Z49      74LS244            pin   8  I3a

/CPU Gating/ZA15   (2 pins)
    Z48      Z80CPU             pin   5  A15
    Z49      74LS244            pin  11  I0b

/CPU Gating/ZA2   (2 pins)
    Z48      Z80CPU             pin  32  A2
    Z68      74LS244            pin  13  I1b

/CPU Gating/ZA3   (2 pins)
    Z48      Z80CPU             pin  33  A3
    Z68      74LS244            pin   6  I2a

/CPU Gating/ZA4   (2 pins)
    Z48      Z80CPU             pin  34  A4
    Z68      74LS244            pin  15  I2b

/CPU Gating/ZA5   (2 pins)
    Z48      Z80CPU             pin  35  A5
    Z68      74LS244            pin   4  I1a

/CPU Gating/ZA6   (2 pins)
    Z48      Z80CPU             pin  36  A6
    Z68      74LS244            pin  17  I3b

/CPU Gating/ZA7   (2 pins)
    Z48      Z80CPU             pin  37  A7
    Z68      74LS244            pin   2  I0a

/CPU Gating/ZA8   (2 pins)
    Z48      Z80CPU             pin  38  A8
    Z49      74LS244            pin   6  I2a

/CPU Gating/ZA9   (2 pins)
    Z48      Z80CPU             pin  39  A9
    Z49      74LS244            pin   4  I1a

/CPU Gating/ZD0   (2 pins)
    Z23      74LS245            pin   3  A1
    Z48      Z80CPU             pin  14  D0

/CPU Gating/ZD1   (2 pins)
    Z23      74LS245            pin   2  A0
    Z48      Z80CPU             pin  15  D1

/CPU Gating/ZD2   (2 pins)
    Z23      74LS245            pin   5  A3
    Z48      Z80CPU             pin  12  D2

/CPU Gating/ZD3   (2 pins)
    Z23      74LS245            pin   9  A7
    Z48      Z80CPU             pin   8  D3

/CPU Gating/ZD4   (2 pins)
    Z23      74LS245            pin   8  A6
    Z48      Z80CPU             pin   7  D4

/CPU Gating/ZD5   (2 pins)
    Z23      74LS245            pin   7  A5
    Z48      Z80CPU             pin   9  D5

/CPU Gating/ZD6   (2 pins)
    Z23      74LS245            pin   6  A4
    Z48      Z80CPU             pin  10  D6

/CPU Gating/ZD7   (2 pins)
    Z23      74LS245            pin   4  A2
    Z48      Z80CPU             pin  13  D7

/CPU Gating/ZMUX   (3 pins)
    Z62      74LS74             pin  12  D
    Z63      74LS74             pin   9  Q
    Z66      74LS367            pin   4  

/CPU Gating/~{CAS}   (3 pins)
    J4       Edge Connector     pin   3  Pin_3
    Z59      74LS367            pin  14  
    Z66      74LS367            pin   7  

/CPU Gating/~{DBIN}   (2 pins)
    Z23      74LS245            pin   1  A->B
    Z47      74LS132            pin  11  

/CPU Gating/~{IN}   (3 pins)
    J4       Edge Connector     pin  19  Pin_19
    Z30      74LS367            pin   9  
    Z40      74LS32             pin   1  

/CPU Gating/~{OUT}   (3 pins)
    J4       Edge Connector     pin  12  Pin_12
    Z30      74LS367            pin   7  
    Z40      74LS32             pin   5  

/CPU Gating/~{TEST}   (5 pins)
    J4       Edge Connector     pin  23  Pin_23
    R55      4.7k               pin   2  
    Z46      74LS04             pin  11  
    Z47      74LS132            pin  10  
    Z48      Z80CPU             pin  25  ~{BUSRQ}

/CPU Gating/~{WR}   (4 pins)
    J4       Edge Connector     pin  13  Pin_13
    R110     330                pin   2  
    Z29      74LS157            pin  14  I0d
    Z30      74LS367            pin   3  

/CPU Gating/~{ZCAS}   (2 pins)
    Z62      74LS74             pin   8  ~{Q}
    Z66      74LS367            pin   6  

/CPU Gating/~{ZIN}   (2 pins)
    Z30      74LS367            pin  10  
    Z67      74LS32             pin   8  

/CPU Gating/~{ZOUT}   (2 pins)
    Z30      74LS367            pin   6  
    Z67      74LS32             pin   6  

/CPU Gating/~{ZRAS}   (4 pins)
    Z48      Z80CPU             pin  19  ~{MREQ}
    Z66      74LS367            pin   2  
    Z67      74LS32             pin   2  
    Z67      74LS32             pin  13  

/CPU Gating/~{ZRD}   (2 pins)
    Z30      74LS367            pin   4  
    Z67      74LS32             pin  11  

/CPU Gating/~{ZWR}   (2 pins)
    Z30      74LS367            pin   2  
    Z67      74LS32             pin   3  

/CPU/CLK   (7 pins)
    Z27      74LS157            pin   3  I1a
    Z50      7404               pin   8  
    Z62      74LS74             pin  11  C
    Z63      74LS74             pin   3  C
    Z63      74LS74             pin  11  C
    Z65      74LS92             pin   1  CP1..3
    Z65      74LS92             pin  14  CP0

/CPU/CLK_DIV6   (2 pins)
    Z65      74LS92             pin   8  Q3
    Z66      74LS367            pin  14  

/CPU/HI   (5 pins)
    R74      4.7k               pin   2  
    Z62      74LS74             pin   4  ~{S}
    Z62      74LS74             pin  10  ~{S}
    Z63      74LS74             pin   4  ~{S}
    Z63      74LS74             pin  10  ~{S}

/CPU/MREQ   (5 pins)
    Z44      74LS00             pin   8  
    Z62      74LS74             pin  13  ~{R}
    Z63      74LS74             pin   1  ~{R}
    Z63      74LS74             pin   2  D
    Z63      74LS74             pin  13  ~{R}

/CPU/ZCLK   (3 pins)
    R75      330                pin   2  
    Z48      Z80CPU             pin   6  ~{CLK}
    Z66      74LS367            pin  13  

/CPU/~{INTAK}   (2 pins)
    J4       Edge Connector     pin  14  Pin_14
    Z64      74LS32             pin   8  

/CPU/~{INT}   (3 pins)
    J4       Edge Connector     pin  21  Pin_21
    R77      4.7k               pin   2  
    Z48      Z80CPU             pin  16  ~{INT}

/CPU/~{SYSRES}   (3 pins)
    CN2      Conn_01x09         pin   9  Pin_9
    J4       Edge Connector     pin   2  Pin_2
    Z45      74LS02             pin  13  

/CPU/~{WAIT}   (3 pins)
    J4       Edge Connector     pin  33  Pin_33
    R41      4.7k               pin   2  
    Z48      Z80CPU             pin  24  ~{WAIT}

/Cassette Interface/CASSIN   (3 pins)
    C17      220pF              pin   1  
    J3       Front View         pin   4  
    R37      220                pin   2  

/Cassette Interface/CASSOUT   (4 pins)
    J3       Front View         pin   5  
    R2       1.2k               pin   2  
    R3       7.5k               pin   2  
    R4       7.5k               pin   1  

/Cassette Interface/MODESEL   (3 pins)
    Z27      74LS157            pin   1  S
    Z4       74LS175            pin   6  ~{Q1}
    Z59      74LS367            pin   2  

/Cassette Interface/~{CGA}   (2 pins)
    Z37      MCM6670            pin  17  ~{CS}
    Z53      74LS74             pin   5  Q

/Cassette Interface/~{CGB}   (2 pins)
    Z38      MCM6670            pin  17  ~{CS}
    Z53      74LS74             pin   6  ~{Q}

/Cassette Interface/~{INSIG}   (2 pins)
    Z40      74LS32             pin   3  
    Z59      74LS367            pin   1  

/Cassette Interface/~{OUTSIG}   (4 pins)
    Z31      74LS132            pin   5  
    Z4       74LS175            pin   9  Cp
    Z40      74LS32             pin   6  
    Z53      74LS74             pin   3  C

/Clock/CLK_DIV2   (2 pins)
    Z27      74LS157            pin   2  I0a
    Z65      74LS92             pin  12  Q0

/Clock/~{CLK_EN}   (5 pins)
    Z46      74LS04             pin   8  
    Z6       74LS92             pin   6  R0(1)
    Z6       74LS92             pin   7  R0(2)
    Z65      74LS92             pin   6  R0(1)
    Z65      74LS92             pin   7  R0(2)

/D0   (7 pins)
    J4       Edge Connector     pin  30  Pin_30
    RP1      4.7k               pin   7  R6
    Z12      74LS245            pin  12  B6
    Z22      DRAM_4116          pin   2  IN
    Z23      74LS245            pin  17  B1
    Z24      74LS367            pin  13  
    Z4       74LS175            pin  13  D3

/D1   (7 pins)
    J4       Edge Connector     pin  22  Pin_22
    RP1      4.7k               pin   4  R3
    Z12      74LS245            pin  11  B7
    Z21      DRAM_4116          pin   2  IN
    Z23      74LS245            pin  18  B0
    Z24      74LS367            pin   3  
    Z4       74LS175            pin  12  D2

/D2   (7 pins)
    J4       Edge Connector     pin  32  Pin_32
    RP1      4.7k               pin   8  R7
    Z12      74LS245            pin  18  B0
    Z20      DRAM_4116          pin   2  IN
    Z23      74LS245            pin  15  B3
    Z24      74LS367            pin  11  
    Z4       74LS175            pin   4  D0

/D3   (7 pins)
    J4       Edge Connector     pin  26  Pin_26
    RP1      4.7k               pin   9  R8
    Z12      74LS245            pin  17  B1
    Z19      DRAM_4116          pin   2  IN
    Z23      74LS245            pin  11  B7
    Z30      74LS367            pin  11  
    Z4       74LS175            pin   5  D1

/D4   (6 pins)
    J4       Edge Connector     pin  18  Pin_18
    RP1      4.7k               pin   2  R1
    Z12      74LS245            pin  16  B2
    Z18      DRAM_4116          pin   2  IN
    Z23      74LS245            pin  12  B6
    Z30      74LS367            pin  13  

/D5   (6 pins)
    J4       Edge Connector     pin  28  Pin_28
    RP1      4.7k               pin   6  R5
    Z12      74LS245            pin  15  B3
    Z17      DRAM_4116          pin   2  IN
    Z23      74LS245            pin  13  B5
    Z24      74LS367            pin   9  

/D6   (7 pins)
    J4       Edge Connector     pin  24  Pin_24
    RP1      4.7k               pin   5  R4
    Z12      74LS245            pin  14  B4
    Z16      DRAM_4116          pin   2  IN
    Z23      74LS245            pin  14  B4
    Z24      74LS367            pin   7  
    Z59      74LS367            pin   3  

/D7   (8 pins)
    J4       Edge Connector     pin  20  Pin_20
    RP1      4.7k               pin   3  R2
    Z12      74LS245            pin  13  B5
    Z15      DRAM_4116          pin   2  IN
    Z23      74LS245            pin  16  B2
    Z24      74LS367            pin   5  
    Z53      74LS74             pin   2  D
    Z59      74LS367            pin   5  

/Keyboard/KBD0   (6 pins)
    CN1      Connection Mainboard Side pin  11  Pin_11
    RP2      4.7k               pin   3  R2
    Z22      DRAM_4116          pin  14  OUT
    Z24      74LS367            pin  14  
    Z42      2364_20L           pin   9  D0
    Z43      2332_20L_21L       pin   9  D0

/Keyboard/KBD1   (6 pins)
    CN1      Connection Mainboard Side pin  12  Pin_12
    RP2      4.7k               pin   2  R1
    Z21      DRAM_4116          pin  14  OUT
    Z24      74LS367            pin   2  
    Z42      2364_20L           pin  10  D1
    Z43      2332_20L_21L       pin  10  D1

/Keyboard/KBD2   (6 pins)
    CN1      Connection Mainboard Side pin  13  Pin_13
    RP2      4.7k               pin   5  R4
    Z20      DRAM_4116          pin  14  OUT
    Z24      74LS367            pin  12  
    Z42      2364_20L           pin  11  D2
    Z43      2332_20L_21L       pin  11  D2

/Keyboard/KBD3   (6 pins)
    CN1      Connection Mainboard Side pin  14  Pin_14
    RP2      4.7k               pin   7  R6
    Z19      DRAM_4116          pin  14  OUT
    Z30      74LS367            pin  12  
    Z42      2364_20L           pin  13  D3
    Z43      2332_20L_21L       pin  13  D3

/Keyboard/KBD4   (6 pins)
    CN1      Connection Mainboard Side pin  15  Pin_15
    RP2      4.7k               pin   9  R8
    Z18      DRAM_4116          pin  14  OUT
    Z30      74LS367            pin  14  
    Z42      2364_20L           pin  14  D4
    Z43      2332_20L_21L       pin  14  D4

/Keyboard/KBD5   (6 pins)
    CN1      Connection Mainboard Side pin  16  Pin_16
    RP2      4.7k               pin   8  R7
    Z17      DRAM_4116          pin  14  OUT
    Z24      74LS367            pin  10  
    Z42      2364_20L           pin  15  D5
    Z43      2332_20L_21L       pin  15  D5

/Keyboard/KBD6   (6 pins)
    CN1      Connection Mainboard Side pin  17  Pin_17
    RP2      4.7k               pin   6  R5
    Z16      DRAM_4116          pin  14  OUT
    Z24      74LS367            pin   6  
    Z42      2364_20L           pin  16  D6
    Z43      2332_20L_21L       pin  16  D6

/Keyboard/KBD7   (6 pins)
    CN1      Connection Mainboard Side pin  18  Pin_18
    RP2      4.7k               pin   4  R3
    Z15      DRAM_4116          pin  14  OUT
    Z24      74LS367            pin   4  
    Z42      2364_20L           pin  17  D7
    Z43      2332_20L_21L       pin  17  D7

/Video/Video Access Multiplexer/C0   (2 pins)
    Z27      74LS157            pin   7  Zb
    Z36      74LS157            pin  10  I1c

/Video/Video Access Multiplexer/C1   (3 pins)
    Z27      74LS157            pin  13  I1d
    Z34      74LS93             pin   9  Q1
    Z36      74LS157            pin   3  I1a

/Video/Video Access Multiplexer/C2   (4 pins)
    Z27      74LS157            pin  14  I0d
    Z28      74LS93             pin  14  CP0
    Z34      74LS93             pin   8  Q2
    Z36      74LS157            pin  13  I1d

/Video/Video Access Multiplexer/C3   (4 pins)
    Z28      74LS93             pin   1  CP1..3
    Z28      74LS93             pin  12  Q0
    Z36      74LS157            pin   6  I1b
    Z46      74LS04             pin   1  

/Video/Video Access Multiplexer/C4   (4 pins)
    Z28      74LS93             pin   9  Q1
    Z29      74LS157            pin  10  I1c
    Z5       74LS10             pin  10  
    Z51      74LS08             pin  13  

/Video/Video Access Multiplexer/C5   (3 pins)
    Z28      74LS93             pin   8  Q2
    Z29      74LS157            pin   3  I1a
    Z5       74LS10             pin  11  

/Video/Video Access Multiplexer/R0   (5 pins)
    Z33      74LS04             pin  13  
    Z34      74LS93             pin  12  Q0
    Z44      74LS00             pin   1  
    Z7       74LS93             pin  14  CP0
    Z8       74LS157            pin  10  I1c

/Video/Video Access Multiplexer/R1   (6 pins)
    JP7      TRS80_Model_I_Jumper_3_Jap pin   1  A
    Z33      74LS04             pin  11  
    Z5       74LS10             pin  13  
    Z7       74LS93             pin   1  CP1..3
    Z7       74LS93             pin  12  Q0
    Z8       74LS157            pin  13  I1d

/Video/Video Access Multiplexer/R2   (4 pins)
    JP6      TRS80_Model_I_Jumper_3_Jap pin   1  A
    JP8      TRS80_Model_I_Jumper_3_Jap pin   3  A
    Z7       74LS93             pin   9  Q1
    Z8       74LS157            pin   3  I1a

/Video/Video Access Multiplexer/R3   (3 pins)
    JP6      TRS80_Model_I_Jumper_3_Jap pin   3  A
    Z7       74LS93             pin   8  Q2
    Z8       74LS157            pin   6  I1b

/Video/Video Access Multiplexer/VA0   (3 pins)
    Z10      SRAM_2114          pin   5  A0
    Z36      74LS157            pin   9  Zc
    Z9       SRAM_2114          pin   5  A0

/Video/Video Access Multiplexer/VA1   (3 pins)
    Z10      SRAM_2114          pin   6  A1
    Z36      74LS157            pin   4  Za
    Z9       SRAM_2114          pin   6  A1

/Video/Video Access Multiplexer/VA2   (3 pins)
    Z10      SRAM_2114          pin   7  A2
    Z36      74LS157            pin  12  Zd
    Z9       SRAM_2114          pin   7  A2

/Video/Video Access Multiplexer/VA3   (3 pins)
    Z10      SRAM_2114          pin   4  A3
    Z36      74LS157            pin   7  Zb
    Z9       SRAM_2114          pin   4  A3

/Video/Video Access Multiplexer/VA4   (3 pins)
    Z10      SRAM_2114          pin   3  A4
    Z29      74LS157            pin   9  Zc
    Z9       SRAM_2114          pin   3  A4

/Video/Video Access Multiplexer/VA5   (3 pins)
    Z10      SRAM_2114          pin   2  A5
    Z29      74LS157            pin   4  Za
    Z9       SRAM_2114          pin   2  A5

/Video/Video Access Multiplexer/VA6   (3 pins)
    Z10      SRAM_2114          pin   1  A6
    Z8       74LS157            pin   9  Zc
    Z9       SRAM_2114          pin   1  A6

/Video/Video Access Multiplexer/VA7   (3 pins)
    Z10      SRAM_2114          pin  17  A7
    Z8       74LS157            pin  12  Zd
    Z9       SRAM_2114          pin  17  A7

/Video/Video Access Multiplexer/VA8   (3 pins)
    Z10      SRAM_2114          pin  16  A8
    Z8       74LS157            pin   4  Za
    Z9       SRAM_2114          pin  16  A8

/Video/Video Access Multiplexer/VA9   (3 pins)
    Z10      SRAM_2114          pin  15  A9
    Z8       74LS157            pin   7  Zb
    Z9       SRAM_2114          pin  15  A9

/Video/Video Access Multiplexer/~{VRD}   (2 pins)
    Z29      74LS157            pin   7  Zb
    Z51      74LS08             pin   1  

/Video/Video Access Multiplexer/~{VWR}   (6 pins)
    Z10      SRAM_2114          pin  10  ~{WR}
    Z29      74LS157            pin  12  Zd
    Z40      74LS32             pin  12  
    Z40      74LS32             pin  13  
    Z51      74LS08             pin   2  
    Z9       SRAM_2114          pin  10  ~{WR}

/Video/Video Counter/DOT_CLK   (2 pins)
    Z27      74LS157            pin   9  Zc
    Z34      74LS93             pin   1  CP1..3

/Video/Video Counter/HDRV   (5 pins)
    Z28      74LS93             pin  11  Q3
    Z35      74LS93             pin  14  CP0
    Z5       74LS10             pin   9  
    Z54      74LS02             pin   3  
    Z62      74LS74             pin   1  ~{R}

/Video/Video Counter/L0   (5 pins)
    Z35      74LS93             pin   1  CP1..3
    Z35      74LS93             pin  12  Q0
    Z37      MCM6670            pin  11  R0
    Z38      MCM6670            pin  11  R0
    Z45      74LS02             pin   2  

/Video/Video Counter/L1   (3 pins)
    Z35      74LS93             pin   9  Q1
    Z37      MCM6670            pin  10  R1
    Z38      MCM6670            pin  10  R1

/Video/Video Counter/L2   (6 pins)
    JP10     TRS80_Model_I_Jumper_3_Jap pin   1  A
    Z35      74LS93             pin   8  Q2
    Z37      MCM6670            pin   8  R2
    Z38      MCM6670            pin   8  R2
    Z39      74LS153            pin  14  S0
    Z5       74LS10             pin   3  

/Video/Video Counter/L3   (6 pins)
    Z34      74LS93             pin  14  CP0
    Z35      74LS93             pin  11  Q3
    Z39      74LS153            pin   2  S1
    Z5       74LS10             pin   5  
    Z52      74LS08             pin  12  
    Z56      74LS175            pin  12  D2

/Video/Video Counter/VDRV   (5 pins)
    Z44      74LS00             pin   2  
    Z5       74LS10             pin   1  
    Z52      74LS08             pin   2  
    Z54      74LS02             pin   2  
    Z7       74LS93             pin  11  Q3

/Video/Video Generator/GRAPHICS   (2 pins)
    Z55      74LS20             pin  13  
    Z56      74LS175            pin   2  Q0

/Video/Video Generator/LB0   (4 pins)
    Z11      74LS174            pin  15  Q5
    Z37      MCM6670            pin   7  A0
    Z38      MCM6670            pin   7  A0
    Z39      74LS153            pin   6  I0a

/Video/Video Generator/LB1   (4 pins)
    Z11      74LS174            pin  12  Q4
    Z37      MCM6670            pin   6  A1
    Z38      MCM6670            pin   6  A1
    Z39      74LS153            pin  10  I0b

/Video/Video Generator/LB2   (4 pins)
    Z11      74LS174            pin   2  Q0
    Z37      MCM6670            pin   5  A2
    Z38      MCM6670            pin   5  A2
    Z39      74LS153            pin   5  I1a

/Video/Video Generator/LB3   (4 pins)
    Z11      74LS174            pin   7  Q2
    Z37      MCM6670            pin   4  A3
    Z38      MCM6670            pin   4  A3
    Z39      74LS153            pin  11  I1b

/Video/Video Generator/LB4   (4 pins)
    Z11      74LS174            pin   5  Q1
    Z37      MCM6670            pin   3  A4
    Z38      MCM6670            pin   3  A4
    Z39      74LS153            pin   4  I2a

/Video/Video Generator/LB5   (4 pins)
    Z11      74LS174            pin  10  Q3
    Z37      MCM6670            pin   2  A5
    Z38      MCM6670            pin   2  A5
    Z39      74LS153            pin  12  I2b

/Video/Video Generator/LB6   (3 pins)
    Z37      MCM6670            pin   1  A6
    Z38      MCM6670            pin   1  A6
    Z56      74LS175            pin  15  Q3

/Video/Video Generator/PIXEL   (3 pins)
    Z3       75452              pin   1  1A
    Z3       75452              pin   2  1B
    Z54      74LS02             pin  13  

/Video/Video Generator/SHIFT   (3 pins)
    Z27      74LS157            pin   4  Za
    Z50      7404               pin  13  
    Z6       74LS92             pin  14  CP0

/Video/Video Generator/~{BLANK}   (4 pins)
    Z55      74LS20             pin   5  
    Z55      74LS20             pin   9  
    Z55      74LS20             pin  10  
    Z56      74LS175            pin   7  Q1

/Video/Video Generator/~{CHARGAP}   (2 pins)
    Z55      74LS20             pin   1  
    Z56      74LS175            pin  11  ~{Q2}

/Video/Video Generator/~{GRAPHICS}   (2 pins)
    Z55      74LS20             pin   2  
    Z56      74LS175            pin   3  ~{Q0}

/Video/Video Generator/~{LATCH}   (5 pins)
    Z11      74LS174            pin   9  Cp
    Z31      74LS132            pin  11  
    Z50      7404               pin  11  
    Z53      74LS74             pin  11  C
    Z56      74LS175            pin   9  Cp

/Video/Video Latch/VD0   (3 pins)
    Z10      SRAM_2114          pin  14  D0
    Z11      74LS174            pin  14  D5
    Z12      74LS245            pin   8  A6

/Video/Video Latch/VD1   (3 pins)
    Z10      SRAM_2114          pin  13  D1
    Z11      74LS174            pin  13  D4
    Z12      74LS245            pin   9  A7

/Video/Video Latch/VD2   (3 pins)
    Z10      SRAM_2114          pin  12  D2
    Z11      74LS174            pin   3  D0
    Z12      74LS245            pin   2  A0

/Video/Video Latch/VD3   (3 pins)
    Z10      SRAM_2114          pin  11  D3
    Z11      74LS174            pin   6  D2
    Z12      74LS245            pin   3  A1

/Video/Video Latch/VD4   (3 pins)
    Z11      74LS174            pin   4  D1
    Z12      74LS245            pin   4  A2
    Z9       SRAM_2114          pin  14  D0

/Video/Video Latch/VD5   (3 pins)
    Z11      74LS174            pin  11  D3
    Z12      74LS245            pin   5  A3
    Z9       SRAM_2114          pin  13  D1

/Video/Video Latch/VD6   (3 pins)
    Z12      74LS245            pin   6  A4
    Z56      74LS175            pin  13  D3
    Z9       SRAM_2114          pin  12  D2

/Video/Video Latch/VD7   (3 pins)
    Z12      74LS245            pin   7  A5
    Z56      74LS175            pin   4  D0
    Z9       SRAM_2114          pin  11  D3

/Video/Video Latch/~{VCLR}   (3 pins)
    Z11      74LS174            pin   1  ~{Mr}
    Z53      74LS74             pin   8  ~{Q}
    Z56      74LS175            pin   1  ~{Mr}

/Video/Video Mixer/SYNC   (3 pins)
    C43      100pF              pin   2  
    R11      10k                pin   1  
    Z32      74C00              pin   3  

/Video/Video Mode/HCLK   (2 pins)
    Z27      74LS157            pin  12  Zd
    Z62      74LS74             pin   3  C

GND   (176 pins)
    C1       10uF 16V           pin   2  
    C10      10000uF 16V        pin   2  
    C12      10uF 16V           pin   2  
    C13      0.01uF 24V         pin   2  
    C14      10uF 16V           pin   2  
    C15      0.01uF 24V         pin   2  
    C19      100uF 16V          pin   1  
    C20      0.1uF 12V          pin   2  
    C22      0.1uF 12V          pin   2  
    C23      0.1uF 12V          pin   2  
    C24      0.1uF 12V          pin   2  
    C25      0.1uF 12V          pin   2  
    C26      0.1uF 12V          pin   2  
    C27      0.1uF 25V          pin   2  
    C28      0.1uF 12V          pin   2  
    C29      0.1uF 12V          pin   2  
    C3       0.01uF 24V         pin   2  
    C30      0.1uF 25V          pin   2  
    C31      0.1uF 12V          pin   2  
    C32      0.1uF 12V          pin   2  
    C33      0.1uF 25V          pin   2  
    C34      0.1uF 12V          pin   2  
    C35      0.1uF 12V          pin   2  
    C36      0.1uF 25V          pin   2  
    C37      0.1uF 12V          pin   2  
    C38      0.1uF 12V          pin   2  
    C39      0.1uF 12V          pin   2  
    C4       10uF 16V           pin   2  
    C40      10uF 16V           pin   2  
    C41      0.1uF 12V          pin   1  
    C44      0.1uF 12V          pin   2  
    C45      0.1uF 12V          pin   2  
    C46      0.1uF 12V          pin   2  
    C47      0.1uF 12V          pin   2  
    C48      1nF                pin   1  
    C49      0.1uF 12V          pin   2  
    C5       220uF 16V          pin   1  
    C51      0.1uF 12V          pin   2  
    C52      0.1uF 12V          pin   2  
    C53      0.1uF 12V          pin   2  
    C54      0.1uF 12V          pin   2  
    C55      0.1uF 12V          pin   2  
    C56      0.1uF 12V          pin   2  
    C57      1nF                pin   1  
    C58      0.1uF 12V          pin   2  
    C59      0.1uF 12V          pin   2  
    C6       10uF 16V           pin   1  
    C63      0.1uF 12V          pin   2  
    C64      0.1uF 12V          pin   2  
    C65      0.1uF 12V          pin   2  
    C66      0.1uF 12V          pin   2  
    C67      0.1uF 12V          pin   2  
    C68      0.1uF 12V          pin   2  
    C69      0.1uF 12V          pin   2  
    C7       0.01uF 24V         pin   2  
    C70      22uF 16V           pin   2  
    C71      0.1uF 12V          pin   2  
    C72      0.1uF 12V          pin   2  
    C8       0.1uF 12V          pin   2  
    C9       2200uF 35V         pin   2  
    CN1      Connection Mainboard Side pin  19  Pin_19
    CR2      1N4735             pin   2  A
    CR3      1N5231             pin   1  K
    J1       Front View         pin   4  
    J2       Front View         pin   5  
    J3       Front View         pin   2  
    J4       Edge Connector     pin   8  Pin_8
    J4       Edge Connector     pin  29  Pin_29
    J4       Edge Connector     pin  37  Pin_37
    J4       Edge Connector     pin  39  Pin_39
    JP4      TRS80_Model_I_Jumper_3_Jap pin   3  A
    JP5      TRS80_Model_I_Jumper_3_Jap pin   1  A
    R2       1.2k               pin   1  
    R24      3.3k               pin   2  
    R25      3.3k               pin   2  
    R27      12k                pin   2  
    R37      220                pin   1  
    R53      8.2k               pin   1  
    R6       75                 pin   2  
    R8       330                pin   2  
    S2       Reset              pin   5  
    S2       Reset              pin   6  
    TP1      ~                  pin   4  
    Z1       LM723C             pin   7  V-
    Z10      SRAM_2114          pin   8  ~{CE}
    Z10      SRAM_2114          pin   9  VSS
    Z11      74LS174            pin   8  GND
    Z12      74LS245            pin  10  GND
    Z13      74LS157            pin   8  GND
    Z13      74LS157            pin  15  E
    Z14      74LS157            pin   8  GND
    Z14      74LS157            pin  15  E
    Z15      DRAM_4116          pin  16  VSS
    Z16      DRAM_4116          pin  16  VSS
    Z17      DRAM_4116          pin  16  VSS
    Z18      DRAM_4116          pin  16  VSS
    Z19      DRAM_4116          pin  16  VSS
    Z2       LM723C             pin   7  V-
    Z20      DRAM_4116          pin  16  VSS
    Z21      DRAM_4116          pin  16  VSS
    Z22      DRAM_4116          pin  16  VSS
    Z23      74LS245            pin  10  GND
    Z23      74LS245            pin  19  CE
    Z24      74LS367            pin   8  GND
    Z25      LM3900             pin   7  V-
    Z26      74LS14             pin   7  GND
    Z27      74LS157            pin   5  I0b
    Z27      74LS157            pin   8  GND
    Z27      74LS157            pin  15  E
    Z28      74LS93             pin  10  GND
    Z29      74LS157            pin   8  GND
    Z29      74LS157            pin  15  E
    Z3       75452              pin   4  GND
    Z30      74LS367            pin   8  GND
    Z31      74LS132            pin   7  GND
    Z32      74C00              pin   7  GND
    Z33      74LS04             pin   7  GND
    Z34      74LS93             pin   2  R0(1)
    Z34      74LS93             pin   3  R0(2)
    Z34      74LS93             pin  10  GND
    Z35      74LS93             pin  10  GND
    Z36      74LS157            pin   8  GND
    Z36      74LS157            pin  15  E
    Z37      MCM6670            pin   9  GND
    Z38      MCM6670            pin   9  GND
    Z39      74LS153            pin   1  Ea
    Z39      74LS153            pin   8  GND
    Z39      74LS153            pin  15  Eb
    Z4       74LS175            pin   8  GND
    Z40      74LS32             pin   7  GND
    Z41      74LS30             pin   7  GND
    Z42      2364_20L           pin  12  GND
    Z43      2332_20L_21L       pin  12  GND
    Z44      74LS00             pin   7  GND
    Z45      74LS02             pin   7  GND
    Z46      74LS04             pin   7  GND
    Z47      74LS132            pin   7  GND
    Z48      Z80CPU             pin  29  GND
    Z49      74LS244            pin  10  GND
    Z5       74LS10             pin   7  GND
    Z50      7404               pin   7  GND
    Z51      74LS08             pin   7  GND
    Z52      74LS08             pin   7  GND
    Z53      74LS74             pin   7  GND
    Z53      74LS74             pin  12  D
    Z54      74LS02             pin   7  GND
    Z55      74LS20             pin   7  GND
    Z56      74LS175            pin   8  GND
    Z57      74LS166            pin   1  Ds
    Z57      74LS166            pin   2  A
    Z57      74LS166            pin   3  B
    Z57      74LS166            pin   6  CE
    Z57      74LS166            pin   8  GND
    Z57      74LS166            pin  14  H
    Z58      74LS166            pin   1  Ds
    Z58      74LS166            pin   2  A
    Z58      74LS166            pin   3  B
    Z58      74LS166            pin   6  CE
    Z58      74LS166            pin   8  GND
    Z59      74LS367            pin   8  GND
    Z6       74LS92             pin  10  GND
    Z60      74LS11             pin   7  GND
    Z61      74LS139            pin   8  GND
    Z62      74LS74             pin   7  GND
    Z63      74LS74             pin   7  GND
    Z64      74LS32             pin   7  GND
    Z65      74LS92             pin  10  GND
    Z66      74LS367            pin   8  GND
    Z66      74LS367            pin  15  
    Z67      74LS32             pin   7  GND
    Z68      74LS244            pin  10  GND
    Z7       74LS93             pin  10  GND
    Z8       74LS157            pin   8  GND
    Z8       74LS157            pin  15  E
    Z9       SRAM_2114          pin   8  ~{CE}
    Z9       SRAM_2114          pin   9  VSS

Net-(C1-Pad1)   (5 pins)
    C1       10uF 16V           pin   1  
    R33      1M                 pin   1  
    R34      10k                pin   1  
    R35      680k               pin   1  
    R36      1.8M               pin   2  

Net-(C17-Pad2)   (3 pins)
    C17      220pF              pin   2  
    C18      220pF              pin   1  
    R42      360k               pin   1  

Net-(C18-Pad2)   (2 pins)
    C18      220pF              pin   2  
    R38      360k               pin   1  

Net-(C2-Pad1)   (2 pins)
    C2       0.1uF 12V          pin   1  
    R1       100                pin   1  

Net-(C2-Pad2)   (3 pins)
    C2       0.1uF 12V          pin   2  
    J3       Front View         pin   3  
    K1       Relay_SPDT         pin   3  

Net-(C40-Pad1)   (4 pins)
    C40      10uF 16V           pin   1  
    R31      10k                pin   2  
    R32      100                pin   1  
    Z47      74LS132            pin   4  

Net-(C5-Pad2)   (3 pins)
    C5       220uF 16V          pin   2  
    R12      220                pin   2  
    S1       ~                  pin  10  

Net-(C50-Pad1)   (4 pins)
    C50      2.7nF              pin   1  
    R52      8.2k               pin   1  
    R53      8.2k               pin   2  
    Z31      74LS132            pin  10  

Net-(C50-Pad2)   (2 pins)
    C50      2.7nF              pin   2  
    Z25      LM3900             pin   9  

Net-(C57-Pad2)   (5 pins)
    C57      1nF                pin   2  
    Z45      74LS02             pin   8  
    Z45      74LS02             pin   9  
    Z45      74LS02             pin  11  
    Z47      74LS132            pin   6  

Net-(C60-Pad1)   (3 pins)
    C60      47pF               pin   1  
    R57      910                pin   1  
    Z50      7404               pin   3  

Net-(C60-Pad2)   (4 pins)
    C60      47pF               pin   2  
    R56      910                pin   2  
    Z50      7404               pin   6  
    Z50      7404               pin   9  

Net-(C70-Pad1)   (4 pins)
    C70      22uF 16V           pin   1  
    R49      10k                pin   2  
    Z47      74LS132            pin   1  
    Z47      74LS132            pin   2  

Net-(CR1-+)   (5 pins)
    CR1      MDA202             pin   1  +
    S1       ~                  pin   4  
    S1       ~                  pin   5  
    S1       ~                  pin   8  
    S1       ~                  pin   9  

Net-(CR1--)   (3 pins)
    CR1      MDA202             pin   4  -
    S1       ~                  pin  11  
    S1       ~                  pin  12  

Net-(CR1-Pad2)   (2 pins)
    CR1      MDA202             pin   2  
    J1       Front View         pin   3  

Net-(CR1-Pad3)   (2 pins)
    CR1      MDA202             pin   3  
    J1       Front View         pin   1  

Net-(CR4-A)   (3 pins)
    CR4      1N4148             pin   2  A
    K1       Relay_SPDT         pin   2  
    Z3       75452              pin   5  2Y

Net-(CR5-A)   (5 pins)
    CR5      1N4148             pin   2  A
    R42      360k               pin   2  
    R43      560k               pin   1  
    R44      470k               pin   1  
    Z25      LM3900             pin   4  

Net-(CR5-K)   (4 pins)
    C48      1nF                pin   2  
    CR5      1N4148             pin   1  K
    CR6      1N4148             pin   1  K
    R50      470k               pin   1  

Net-(CR6-A)   (3 pins)
    CR6      1N4148             pin   2  A
    R45      470k               pin   2  
    Z25      LM3900             pin   5  

Net-(CR7-A)   (4 pins)
    CR7      1N4148             pin   2  A
    R46      470k               pin   1  
    R51      1M                 pin   2  
    Z25      LM3900             pin  10  

Net-(CR7-K)   (2 pins)
    CR7      1N4148             pin   1  K
    CR8      1N4148             pin   2  A

Net-(CR8-K)   (3 pins)
    C41      0.1uF 12V          pin   2  
    CR8      1N4148             pin   1  K
    R47      470k               pin   1  

Net-(J1-Pad2)   (3 pins)
    J1       Front View         pin   2  
    S1       ~                  pin   1  
    S1       ~                  pin   2  

Net-(J3-Pad1)   (3 pins)
    J3       Front View         pin   1  
    K1       Relay_SPDT         pin   4  
    R1       100                pin   2  

Net-(JP1-B)   (3 pins)
    JP1      TRS80_Model_I_Jumper_2_Jap pin   2  B
    R71      4.7k               pin   1  
    Z60      74LS11             pin   9  

Net-(JP10-A-Pad3)   (2 pins)
    JP10     TRS80_Model_I_Jumper_3_Jap pin   3  A
    Z46      74LS04             pin   4  

Net-(JP10-B)   (2 pins)
    JP10     TRS80_Model_I_Jumper_3_Jap pin   2  B
    Z5       74LS10             pin   4  

Net-(JP3-B)   (3 pins)
    JP3      TRS80_Model_I_Jumper_2_Jap pin   2  B
    R70      4.7k               pin   1  
    Z60      74LS11             pin   5  

Net-(JP4-A-Pad1)   (2 pins)
    JP4      TRS80_Model_I_Jumper_3_Jap pin   1  A
    R65      4.7k               pin   1  

Net-(JP4-B)   (2 pins)
    JP4      TRS80_Model_I_Jumper_3_Jap pin   2  B
    Z53      74LS74             pin   4  ~{S}

Net-(JP5-A-Pad3)   (2 pins)
    JP5      TRS80_Model_I_Jumper_3_Jap pin   3  A
    R67      4.7k               pin   1  

Net-(JP5-B)   (2 pins)
    JP5      TRS80_Model_I_Jumper_3_Jap pin   2  B
    Z53      74LS74             pin   1  ~{R}

Net-(JP6-B)   (2 pins)
    JP6      TRS80_Model_I_Jumper_3_Jap pin   2  B
    Z5       74LS10             pin   2  

Net-(JP7-A-Pad3)   (2 pins)
    JP7      TRS80_Model_I_Jumper_3_Jap pin   3  A
    Z33      74LS04             pin  10  

Net-(JP7-B)   (2 pins)
    JP7      TRS80_Model_I_Jumper_3_Jap pin   2  B
    Z52      74LS08             pin   1  

Net-(JP8-A-Pad1)   (2 pins)
    JP8      TRS80_Model_I_Jumper_3_Jap pin   1  A
    R64      4.7k               pin   2  

Net-(JP8-B)   (2 pins)
    JP8      TRS80_Model_I_Jumper_3_Jap pin   2  B
    Z52      74LS08             pin  10  

Net-(JP9-B)   (2 pins)
    J2       Front View         pin   1  
    JP9      TRS80_Model_I_Jumper_2_Jap pin   2  B

Net-(Q1-B)   (4 pins)
    Q1       C1815              pin   3  B
    R10      270                pin   2  
    R8       330                pin   1  
    R9       120                pin   1  

Net-(Q1-C)   (4 pins)
    C3       0.01uF 24V         pin   1  
    C4       10uF 16V           pin   1  
    Q1       C1815              pin   2  C
    R7       47                 pin   2  

Net-(Q1-E)   (3 pins)
    J2       Front View         pin   4  
    Q1       C1815              pin   1  E
    R6       75                 pin   1  

Net-(Q2-B)   (3 pins)
    C43      100pF              pin   1  
    Q2       A1015              pin   3  B
    R11      10k                pin   2  

Net-(Q2-C)   (2 pins)
    Q2       A1015              pin   2  C
    R10      270                pin   1  

Net-(Q3-B)   (3 pins)
    Q3       TIP29A             pin   1  B
    R14      2.7k               pin   1  
    Z1       LM723C             pin  10  Vout

Net-(Q3-C)   (3 pins)
    Q3       TIP29A             pin   2  C
    Q4       2N6594             pin   1  B
    R13      68                 pin   2  

Net-(Q3-E)   (5 pins)
    Q3       TIP29A             pin   3  E
    Q4       2N6594             pin   3  C
    R14      2.7k               pin   2  
    R15      750                pin   1  
    R16      0.33               pin   1  

Net-(Q4-E)   (5 pins)
    C10      10000uF 16V        pin   1  
    Q4       2N6594             pin   2  E
    R13      68                 pin   1  
    S1       ~                  pin   6  
    S1       ~                  pin   7  

Net-(Q5-B)   (2 pins)
    Q5       A1015              pin   3  B
    R20      100k               pin   1  

Net-(Q5-C)   (2 pins)
    Q5       A1015              pin   2  C
    R21      3.3k               pin   2  

Net-(Q5-E)   (3 pins)
    Q5       A1015              pin   1  E
    R17      1k                 pin   2  2
    Z1       LM723C             pin   5  +

Net-(Q6-B)   (3 pins)
    Q6       MJE34              pin   1  B
    R28      1.2k               pin   2  
    Z2       LM723C             pin  11  VC

Net-(Q6-C)   (4 pins)
    Q6       MJE34              pin   2  C
    R29      2k                 pin   1  
    R30      5.6                pin   2  
    Z2       LM723C             pin  10  Vout

Net-(Q6-E)   (5 pins)
    C9       2200uF 35V         pin   1  
    Q6       MJE34              pin   3  E
    R28      1.2k               pin   1  
    S1       ~                  pin   3  
    Z2       LM723C             pin  12  V+

Net-(R101-Pad2)   (3 pins)
    R101     330                pin   2  
    R69      4.7k               pin   2  
    Z59      74LS367            pin  13  

Net-(R109-Pad2)   (3 pins)
    R109     330                pin   2  
    R76      4.7k               pin   2  
    Z66      74LS367            pin  11  

Net-(R17-Pad1)   (2 pins)
    R17      1k                 pin   1  1
    R18      1.2k               pin   1  

Net-(R17-Pad3)   (2 pins)
    R17      1k                 pin   3  3
    R24      3.3k               pin   1  

Net-(R23-Pad1)   (2 pins)
    R23      1k                 pin   1  1
    R25      3.3k               pin   1  

Net-(R23-Pad3)   (2 pins)
    R23      1k                 pin   3  3
    R26      2.2k               pin   2  

Net-(R32-Pad2)   (2 pins)
    R32      100                pin   2  
    S2       Reset              pin   4  

Net-(R54-Pad2)   (2 pins)
    R54      4.7k               pin   2  
    Z46      74LS04             pin   9  

Net-(R56-Pad1)   (3 pins)
    R56      910                pin   1  
    Y1       10.6445 MHz        pin   2  2
    Z50      7404               pin   5  

Net-(R57-Pad2)   (3 pins)
    R57      910                pin   2  
    Y1       10.6445 MHz        pin   1  1
    Z50      7404               pin   4  

Net-(Z1--)   (3 pins)
    C11      1nF                pin   1  
    R19      1.2k               pin   2  
    Z1       LM723C             pin   4  -

Net-(Z1-FC)   (2 pins)
    C11      1nF                pin   2  
    Z1       LM723C             pin  13  FC

Net-(Z1-ILIM)   (3 pins)
    R15      750                pin   2  
    R21      3.3k               pin   1  
    Z1       LM723C             pin   2  ILIM

Net-(Z1-VREF)   (2 pins)
    R18      1.2k               pin   2  
    Z1       LM723C             pin   6  VREF

Net-(Z12-A->B)   (2 pins)
    Z12      74LS245            pin   1  A->B
    Z40      74LS32             pin  11  

Net-(Z12-CE)   (2 pins)
    Z12      74LS245            pin  19  CE
    Z51      74LS08             pin   3  

Net-(Z13-Za)   (2 pins)
    R105     330                pin   2  
    Z13      74LS157            pin   4  Za

Net-(Z13-Zb)   (2 pins)
    R106     330                pin   2  
    Z13      74LS157            pin   7  Zb

Net-(Z13-Zc)   (2 pins)
    R102     330                pin   2  
    Z13      74LS157            pin   9  Zc

Net-(Z14-Za)   (2 pins)
    R104     330                pin   2  
    Z14      74LS157            pin   4  Za

Net-(Z14-Zb)   (2 pins)
    R107     330                pin   2  
    Z14      74LS157            pin   7  Zb

Net-(Z14-Zc)   (2 pins)
    R108     330                pin   2  
    Z14      74LS157            pin   9  Zc

Net-(Z14-Zd)   (2 pins)
    R103     330                pin   2  
    Z14      74LS157            pin  12  Zd

Net-(Z15-A0)   (9 pins)
    R104     330                pin   1  
    Z15      DRAM_4116          pin   5  A0
    Z16      DRAM_4116          pin   5  A0
    Z17      DRAM_4116          pin   5  A0
    Z18      DRAM_4116          pin   5  A0
    Z19      DRAM_4116          pin   5  A0
    Z20      DRAM_4116          pin   5  A0
    Z21      DRAM_4116          pin   5  A0
    Z22      DRAM_4116          pin   5  A0

Net-(Z15-A1)   (9 pins)
    R107     330                pin   1  
    Z15      DRAM_4116          pin   7  A1
    Z16      DRAM_4116          pin   7  A1
    Z17      DRAM_4116          pin   7  A1
    Z18      DRAM_4116          pin   7  A1
    Z19      DRAM_4116          pin   7  A1
    Z20      DRAM_4116          pin   7  A1
    Z21      DRAM_4116          pin   7  A1
    Z22      DRAM_4116          pin   7  A1

Net-(Z15-A2)   (9 pins)
    R108     330                pin   1  
    Z15      DRAM_4116          pin   6  A2
    Z16      DRAM_4116          pin   6  A2
    Z17      DRAM_4116          pin   6  A2
    Z18      DRAM_4116          pin   6  A2
    Z19      DRAM_4116          pin   6  A2
    Z20      DRAM_4116          pin   6  A2
    Z21      DRAM_4116          pin   6  A2
    Z22      DRAM_4116          pin   6  A2

Net-(Z15-A3)   (9 pins)
    R103     330                pin   1  
    Z15      DRAM_4116          pin  12  A3
    Z16      DRAM_4116          pin  12  A3
    Z17      DRAM_4116          pin  12  A3
    Z18      DRAM_4116          pin  12  A3
    Z19      DRAM_4116          pin  12  A3
    Z20      DRAM_4116          pin  12  A3
    Z21      DRAM_4116          pin  12  A3
    Z22      DRAM_4116          pin  12  A3

Net-(Z15-A4)   (9 pins)
    R105     330                pin   1  
    Z15      DRAM_4116          pin  11  A4
    Z16      DRAM_4116          pin  11  A4
    Z17      DRAM_4116          pin  11  A4
    Z18      DRAM_4116          pin  11  A4
    Z19      DRAM_4116          pin  11  A4
    Z20      DRAM_4116          pin  11  A4
    Z21      DRAM_4116          pin  11  A4
    Z22      DRAM_4116          pin  11  A4

Net-(Z15-A5)   (9 pins)
    R106     330                pin   1  
    Z15      DRAM_4116          pin  10  A5
    Z16      DRAM_4116          pin  10  A5
    Z17      DRAM_4116          pin  10  A5
    Z18      DRAM_4116          pin  10  A5
    Z19      DRAM_4116          pin  10  A5
    Z20      DRAM_4116          pin  10  A5
    Z21      DRAM_4116          pin  10  A5
    Z22      DRAM_4116          pin  10  A5

Net-(Z15-A6)   (9 pins)
    R102     330                pin   1  
    Z15      DRAM_4116          pin  13  A6
    Z16      DRAM_4116          pin  13  A6
    Z17      DRAM_4116          pin  13  A6
    Z18      DRAM_4116          pin  13  A6
    Z19      DRAM_4116          pin  13  A6
    Z20      DRAM_4116          pin  13  A6
    Z21      DRAM_4116          pin  13  A6
    Z22      DRAM_4116          pin  13  A6

Net-(Z15-~{CAS})   (9 pins)
    R101     330                pin   1  
    Z15      DRAM_4116          pin  15  ~{CAS}
    Z16      DRAM_4116          pin  15  ~{CAS}
    Z17      DRAM_4116          pin  15  ~{CAS}
    Z18      DRAM_4116          pin  15  ~{CAS}
    Z19      DRAM_4116          pin  15  ~{CAS}
    Z20      DRAM_4116          pin  15  ~{CAS}
    Z21      DRAM_4116          pin  15  ~{CAS}
    Z22      DRAM_4116          pin  15  ~{CAS}

Net-(Z15-~{RAS})   (9 pins)
    R109     330                pin   1  
    Z15      DRAM_4116          pin   4  ~{RAS}
    Z16      DRAM_4116          pin   4  ~{RAS}
    Z17      DRAM_4116          pin   4  ~{RAS}
    Z18      DRAM_4116          pin   4  ~{RAS}
    Z19      DRAM_4116          pin   4  ~{RAS}
    Z20      DRAM_4116          pin   4  ~{RAS}
    Z21      DRAM_4116          pin   4  ~{RAS}
    Z22      DRAM_4116          pin   4  ~{RAS}

Net-(Z15-~{WR})   (9 pins)
    R110     330                pin   1  
    Z15      DRAM_4116          pin   3  ~{WR}
    Z16      DRAM_4116          pin   3  ~{WR}
    Z17      DRAM_4116          pin   3  ~{WR}
    Z18      DRAM_4116          pin   3  ~{WR}
    Z19      DRAM_4116          pin   3  ~{WR}
    Z20      DRAM_4116          pin   3  ~{WR}
    Z21      DRAM_4116          pin   3  ~{WR}
    Z22      DRAM_4116          pin   3  ~{WR}

Net-(Z2-+)   (2 pins)
    R22      1.5k               pin   2  
    Z2       LM723C             pin   5  +

Net-(Z2--)   (3 pins)
    C16      1nF                pin   2  
    R23      1k                 pin   2  2
    Z2       LM723C             pin   4  -

Net-(Z2-FC)   (2 pins)
    C16      1nF                pin   1  
    Z2       LM723C             pin  13  FC

Net-(Z2-ILIM)   (3 pins)
    R27      12k                pin   1  
    R29      2k                 pin   2  
    Z2       LM723C             pin   2  ILIM

Net-(Z2-VREF)   (2 pins)
    R22      1.5k               pin   1  
    Z2       LM723C             pin   6  VREF

Net-(Z25A-+)   (2 pins)
    R35      680k               pin   2  
    Z25      LM3900             pin   1  +

Net-(Z25A--)   (3 pins)
    R44      470k               pin   2  
    R45      470k               pin   1  
    Z25      LM3900             pin   6  -

Net-(Z25B-+)   (3 pins)
    R36      1.8M               pin   1  
    R38      360k               pin   2  
    Z25      LM3900             pin   2  +

Net-(Z25B--)   (2 pins)
    R43      560k               pin   2  
    Z25      LM3900             pin   3  -

Net-(Z25C-+)   (2 pins)
    R46      470k               pin   2  
    Z25      LM3900             pin  13  +

Net-(Z25C--)   (2 pins)
    R47      470k               pin   2  
    Z25      LM3900             pin   8  -

Net-(Z25D-+)   (2 pins)
    R33      1M                 pin   2  
    Z25      LM3900             pin  12  +

Net-(Z25D--)   (3 pins)
    R50      470k               pin   2  
    R51      1M                 pin   1  
    Z25      LM3900             pin  11  -

Net-(Z25E-V+)   (3 pins)
    C19      100uF 16V          pin   2  
    R39      10                 pin   1  
    Z25      LM3900             pin  14  V+

Net-(Z26-Pad1)   (2 pins)
    Z26      74LS14             pin   1  
    Z5       74LS10             pin   6  

Net-(Z26-Pad11)   (2 pins)
    Z26      74LS14             pin  11  
    Z5       74LS10             pin  12  

Net-(Z26-Pad13)   (2 pins)
    Z26      74LS14             pin  13  
    Z5       74LS10             pin   8  

Net-(Z27-I0c)   (3 pins)
    Z27      74LS157            pin  11  I0c
    Z31      74LS132            pin  12  
    Z6       74LS92             pin   9  Q2

Net-(Z27-I1b)   (3 pins)
    Z27      74LS157            pin   6  I1b
    Z27      74LS157            pin  10  I1c
    Z6       74LS92             pin   8  Q3

Net-(Z28-R0(1))   (3 pins)
    Z26      74LS14             pin  12  
    Z28      74LS93             pin   2  R0(1)
    Z28      74LS93             pin   3  R0(2)

Net-(Z29-I1b)   (3 pins)
    R48      4.7k               pin   2  
    Z29      74LS157            pin   6  I1b
    Z29      74LS157            pin  13  I1d

Net-(Z31-Pad4)   (3 pins)
    Z31      74LS132            pin   4  
    Z31      74LS132            pin   8  
    Z59      74LS367            pin   4  

Net-(Z31-Pad6)   (2 pins)
    Z31      74LS132            pin   6  
    Z31      74LS132            pin   9  

Net-(Z32-Pad1)   (2 pins)
    Z32      74C00              pin   1  
    Z32      74C00              pin   6  

Net-(Z32-Pad10)   (3 pins)
    Z32      74C00              pin   4  
    Z32      74C00              pin  10  
    Z32      74C00              pin  11  

Net-(Z32-Pad12)   (3 pins)
    Z32      74C00              pin   9  
    Z32      74C00              pin  12  
    Z52      74LS08             pin   8  

Net-(Z32-Pad2)   (2 pins)
    Z32      74C00              pin   2  
    Z32      74C00              pin   8  

Net-(Z33-Pad12)   (2 pins)
    Z33      74LS04             pin  12  
    Z52      74LS08             pin  13  

Net-(Z35-R0(1))   (3 pins)
    Z26      74LS14             pin   2  
    Z35      74LS93             pin   2  R0(1)
    Z35      74LS93             pin   3  R0(2)

Net-(Z37-D0)   (3 pins)
    Z37      MCM6670            pin  12  D0
    Z38      MCM6670            pin  12  D0
    Z57      74LS166            pin   4  C

Net-(Z37-D1)   (3 pins)
    Z37      MCM6670            pin  13  D1
    Z38      MCM6670            pin  13  D1
    Z57      74LS166            pin   5  D

Net-(Z37-D2)   (3 pins)
    Z37      MCM6670            pin  14  D2
    Z38      MCM6670            pin  14  D2
    Z57      74LS166            pin  10  E

Net-(Z37-D3)   (3 pins)
    Z37      MCM6670            pin  15  D3
    Z38      MCM6670            pin  15  D3
    Z57      74LS166            pin  11  F

Net-(Z37-D4)   (3 pins)
    Z37      MCM6670            pin  16  D4
    Z38      MCM6670            pin  16  D4
    Z57      74LS166            pin  12  G

Net-(Z39-Za)   (4 pins)
    Z39      74LS153            pin   7  Za
    Z58      74LS166            pin  11  F
    Z58      74LS166            pin  12  G
    Z58      74LS166            pin  14  H

Net-(Z39-Zb)   (4 pins)
    Z39      74LS153            pin   9  Zb
    Z58      74LS166            pin   4  C
    Z58      74LS166            pin   5  D
    Z58      74LS166            pin  10  E

Net-(Z3A-1Y)   (2 pins)
    R9       120                pin   2  
    Z3       75452              pin   3  1Y

Net-(Z3B-2A)   (3 pins)
    Z3       75452              pin   6  2A
    Z3       75452              pin   7  2B
    Z4       74LS175            pin   2  Q0

Net-(Z4-Q3)   (2 pins)
    R3       7.5k               pin   1  
    Z4       74LS175            pin  15  Q3

Net-(Z4-~{Mr})   (2 pins)
    R40      4.7k               pin   2  
    Z4       74LS175            pin   1  ~{Mr}

Net-(Z4-~{Q2})   (3 pins)
    R4       7.5k               pin   2  
    R5       220k               pin   1  
    Z4       74LS175            pin  11  ~{Q2}

Net-(Z40-Pad2)   (3 pins)
    Z40      74LS32             pin   2  
    Z40      74LS32             pin   4  
    Z41      74LS30             pin   8  

Net-(Z40-Pad9)   (2 pins)
    Z40      74LS32             pin   9  
    Z60      74LS11             pin  12  

Net-(Z44-Pad11)   (2 pins)
    Z44      74LS00             pin  11  
    Z64      74LS32             pin  12  

Net-(Z44-Pad3)   (2 pins)
    Z44      74LS00             pin   3  
    Z45      74LS02             pin   3  

Net-(Z45-Pad1)   (2 pins)
    Z45      74LS02             pin   1  
    Z46      74LS04             pin   3  

Net-(Z45-Pad12)   (3 pins)
    Z45      74LS02             pin  12  
    Z46      74LS04             pin  13  
    Z47      74LS132            pin   3  

Net-(Z46-Pad2)   (2 pins)
    Z46      74LS04             pin   2  
    Z51      74LS08             pin  12  

Net-(Z47-Pad12)   (3 pins)
    Z47      74LS132            pin   8  
    Z47      74LS132            pin  12  
    Z47      74LS132            pin  13  

Net-(Z48-~{HALT})   (2 pins)
    Z47      74LS132            pin   5  
    Z48      Z80CPU             pin  18  ~{HALT}

Net-(Z48-~{IORQ})   (4 pins)
    Z48      Z80CPU             pin  20  ~{IORQ}
    Z64      74LS32             pin   9  
    Z67      74LS32             pin   5  
    Z67      74LS32             pin   9  

Net-(Z48-~{M1})   (2 pins)
    Z48      Z80CPU             pin  27  ~{M1}
    Z64      74LS32             pin  10  

Net-(Z48-~{NMI})   (2 pins)
    Z45      74LS02             pin  10  
    Z48      Z80CPU             pin  17  ~{NMI}

Net-(Z48-~{RD})   (5 pins)
    Z44      74LS00             pin  10  
    Z47      74LS132            pin   9  
    Z48      Z80CPU             pin  21  ~{RD}
    Z67      74LS32             pin  10  
    Z67      74LS32             pin  12  

Net-(Z48-~{RESET})   (2 pins)
    Z46      74LS04             pin  12  
    Z48      Z80CPU             pin  26  ~{RESET}

Net-(Z48-~{WR})   (4 pins)
    Z44      74LS00             pin   9  
    Z48      Z80CPU             pin  22  ~{WR}
    Z67      74LS32             pin   1  
    Z67      74LS32             pin   4  

Net-(Z49-OEa)   (7 pins)
    Z30      74LS367            pin   1  
    Z46      74LS04             pin  10  
    Z49      74LS244            pin   1  OEa
    Z49      74LS244            pin  19  OEb
    Z66      74LS367            pin   1  
    Z68      74LS244            pin   1  OEa
    Z68      74LS244            pin  19  OEb

Net-(Z50-Pad10)   (3 pins)
    Z50      7404               pin  10  
    Z55      74LS20             pin   4  
    Z55      74LS20             pin  12  

Net-(Z52-Pad11)   (2 pins)
    Z52      74LS08             pin   5  
    Z52      74LS08             pin  11  

Net-(Z52-Pad3)   (2 pins)
    Z52      74LS08             pin   3  
    Z52      74LS08             pin   4  

Net-(Z52-Pad6)   (2 pins)
    Z52      74LS08             pin   6  
    Z52      74LS08             pin   9  

Net-(Z53B-~{R})   (2 pins)
    R66      4.7k               pin   1  
    Z53      74LS74             pin  13  ~{R}

Net-(Z56-D1)   (2 pins)
    Z54      74LS02             pin   1  
    Z56      74LS175            pin   5  D1

Net-(Z57-Clk)   (3 pins)
    Z50      7404               pin  12  
    Z57      74LS166            pin   7  Clk
    Z58      74LS166            pin   7  Clk

Net-(Z57-Clr)   (3 pins)
    R68      4.7k               pin   1  
    Z57      74LS166            pin   9  Clr
    Z58      74LS166            pin   9  Clr

Net-(Z57-PE)   (2 pins)
    Z55      74LS20             pin   6  
    Z57      74LS166            pin  15  PE

Net-(Z57-Qh)   (2 pins)
    Z54      74LS02             pin  11  
    Z57      74LS166            pin  13  Qh

Net-(Z58-PE)   (2 pins)
    Z55      74LS20             pin   8  
    Z58      74LS166            pin  15  PE

Net-(Z58-Qh)   (2 pins)
    Z54      74LS02             pin  12  
    Z58      74LS166            pin  13  Qh

Net-(Z6-CP1..3)   (3 pins)
    Z31      74LS132            pin  13  
    Z6       74LS92             pin   1  CP1..3
    Z6       74LS92             pin  12  Q0

Net-(Z60-Pad1)   (2 pins)
    Z60      74LS11             pin   1  
    Z60      74LS11             pin   6  

Net-(Z61A-E)   (2 pins)
    Z61      74LS139            pin   1  E
    Z64      74LS32             pin   3  

Net-(Z61A-O3)   (2 pins)
    Z61      74LS139            pin   7  O3
    Z61      74LS139            pin  15  E

Net-(Z62A-D)   (2 pins)
    Z51      74LS08             pin  11  
    Z62      74LS74             pin   2  D

Net-(Z62A-Q)   (3 pins)
    Z32      74C00              pin   5  
    Z32      74C00              pin  13  
    Z62      74LS74             pin   5  Q

Net-(Z63A-Q)   (2 pins)
    Z63      74LS74             pin   5  Q
    Z63      74LS74             pin  12  D

Net-(Z64-Pad13)   (3 pins)
    Z64      74LS32             pin   2  
    Z64      74LS32             pin   6  
    Z64      74LS32             pin  13  

Net-(Z7-R0(1))   (3 pins)
    Z26      74LS14             pin  10  
    Z7       74LS93             pin   2  R0(1)
    Z7       74LS93             pin   3  R0(2)

unconnected-(J1-Pad5)   (1 pins)
    J1       Front View         pin   5  

unconnected-(J2-Pad2)   (1 pins)
    J2       Front View         pin   2  

unconnected-(J2-Pad3)   (1 pins)
    J2       Front View         pin   3  

unconnected-(K1-Pad5)   (1 pins)
    K1       Relay_SPDT         pin   5  

unconnected-(S2-Pad1)   (1 pins)
    S2       Reset              pin   1  

unconnected-(S2-Pad2)   (1 pins)
    S2       Reset              pin   2  

unconnected-(S2-Pad3)   (1 pins)
    S2       Reset              pin   3  

unconnected-(Z1-NC-Pad1)   (1 pins)
    Z1       LM723C             pin   1  NC

unconnected-(Z1-NC-Pad14)   (1 pins)
    Z1       LM723C             pin  14  NC

unconnected-(Z1-NC-Pad8)   (1 pins)
    Z1       LM723C             pin   8  NC

unconnected-(Z1-VZ-Pad9)   (1 pins)
    Z1       LM723C             pin   9  VZ

unconnected-(Z13-I0d-Pad14)   (1 pins)
    Z13      74LS157            pin  14  I0d

unconnected-(Z13-I1d-Pad13)   (1 pins)
    Z13      74LS157            pin  13  I1d

unconnected-(Z13-Zd-Pad12)   (1 pins)
    Z13      74LS157            pin  12  Zd

unconnected-(Z2-NC-Pad1)   (1 pins)
    Z2       LM723C             pin   1  NC

unconnected-(Z2-NC-Pad14)   (1 pins)
    Z2       LM723C             pin  14  NC

unconnected-(Z2-NC-Pad8)   (1 pins)
    Z2       LM723C             pin   8  NC

unconnected-(Z2-VZ-Pad9)   (1 pins)
    Z2       LM723C             pin   9  VZ

unconnected-(Z26-Pad3)   (1 pins)
    Z26      74LS14             pin   3  

unconnected-(Z26-Pad4)   (1 pins)
    Z26      74LS14             pin   4  

unconnected-(Z26-Pad5)   (1 pins)
    Z26      74LS14             pin   5  

unconnected-(Z26-Pad6)   (1 pins)
    Z26      74LS14             pin   6  

unconnected-(Z26-Pad8)   (1 pins)
    Z26      74LS14             pin   8  

unconnected-(Z26-Pad9)   (1 pins)
    Z26      74LS14             pin   9  

unconnected-(Z31-Pad1)   (1 pins)
    Z31      74LS132            pin   1  

unconnected-(Z31-Pad2)   (1 pins)
    Z31      74LS132            pin   2  

unconnected-(Z31-Pad3)   (1 pins)
    Z31      74LS132            pin   3  

unconnected-(Z33-Pad1)   (1 pins)
    Z33      74LS04             pin   1  

unconnected-(Z33-Pad2)   (1 pins)
    Z33      74LS04             pin   2  

unconnected-(Z33-Pad3)   (1 pins)
    Z33      74LS04             pin   3  

unconnected-(Z33-Pad4)   (1 pins)
    Z33      74LS04             pin   4  

unconnected-(Z33-Pad5)   (1 pins)
    Z33      74LS04             pin   5  

unconnected-(Z33-Pad6)   (1 pins)
    Z33      74LS04             pin   6  

unconnected-(Z33-Pad8)   (1 pins)
    Z33      74LS04             pin   8  

unconnected-(Z33-Pad9)   (1 pins)
    Z33      74LS04             pin   9  

unconnected-(Z34-Q3-Pad11)   (1 pins)
    Z34      74LS93             pin  11  Q3

unconnected-(Z39-I3a-Pad3)   (1 pins)
    Z39      74LS153            pin   3  I3a

unconnected-(Z39-I3b-Pad13)   (1 pins)
    Z39      74LS153            pin  13  I3b

unconnected-(Z4-Q1-Pad7)   (1 pins)
    Z4       74LS175            pin   7  Q1

unconnected-(Z4-Q2-Pad10)   (1 pins)
    Z4       74LS175            pin  10  Q2

unconnected-(Z4-~{Q0}-Pad3)   (1 pins)
    Z4       74LS175            pin   3  ~{Q0}

unconnected-(Z4-~{Q3}-Pad14)   (1 pins)
    Z4       74LS175            pin  14  ~{Q3}

unconnected-(Z44-Pad4)   (1 pins)
    Z44      74LS00             pin   4  

unconnected-(Z44-Pad5)   (1 pins)
    Z44      74LS00             pin   5  

unconnected-(Z44-Pad6)   (1 pins)
    Z44      74LS00             pin   6  

unconnected-(Z45-Pad4)   (1 pins)
    Z45      74LS02             pin   4  

unconnected-(Z45-Pad5)   (1 pins)
    Z45      74LS02             pin   5  

unconnected-(Z45-Pad6)   (1 pins)
    Z45      74LS02             pin   6  

unconnected-(Z46-Pad5)   (1 pins)
    Z46      74LS04             pin   5  

unconnected-(Z46-Pad6)   (1 pins)
    Z46      74LS04             pin   6  

unconnected-(Z48-~{BUSACK}-Pad23)   (1 pins)
    Z48      Z80CPU             pin  23  ~{BUSACK}

unconnected-(Z48-~{RFSH}-Pad28)   (1 pins)
    Z48      Z80CPU             pin  28  ~{RFSH}

unconnected-(Z50-Pad1)   (1 pins)
    Z50      7404               pin   1  

unconnected-(Z50-Pad2)   (1 pins)
    Z50      7404               pin   2  

unconnected-(Z51-Pad10)   (1 pins)
    Z51      74LS08             pin  10  

unconnected-(Z51-Pad4)   (1 pins)
    Z51      74LS08             pin   4  

unconnected-(Z51-Pad5)   (1 pins)
    Z51      74LS08             pin   5  

unconnected-(Z51-Pad6)   (1 pins)
    Z51      74LS08             pin   6  

unconnected-(Z51-Pad8)   (1 pins)
    Z51      74LS08             pin   8  

unconnected-(Z51-Pad9)   (1 pins)
    Z51      74LS08             pin   9  

unconnected-(Z53B-Q-Pad9)   (1 pins)
    Z53      74LS74             pin   9  Q

unconnected-(Z54-Pad10)   (1 pins)
    Z54      74LS02             pin  10  

unconnected-(Z54-Pad4)   (1 pins)
    Z54      74LS02             pin   4  

unconnected-(Z54-Pad5)   (1 pins)
    Z54      74LS02             pin   5  

unconnected-(Z54-Pad6)   (1 pins)
    Z54      74LS02             pin   6  

unconnected-(Z54-Pad8)   (1 pins)
    Z54      74LS02             pin   8  

unconnected-(Z54-Pad9)   (1 pins)
    Z54      74LS02             pin   9  

unconnected-(Z56-Q2-Pad10)   (1 pins)
    Z56      74LS175            pin  10  Q2

unconnected-(Z56-~{Q1}-Pad6)   (1 pins)
    Z56      74LS175            pin   6  ~{Q1}

unconnected-(Z56-~{Q3}-Pad14)   (1 pins)
    Z56      74LS175            pin  14  ~{Q3}

unconnected-(Z59-Pad10)   (1 pins)
    Z59      74LS367            pin  10  

unconnected-(Z59-Pad11)   (1 pins)
    Z59      74LS367            pin  11  

unconnected-(Z59-Pad12)   (1 pins)
    Z59      74LS367            pin  12  

unconnected-(Z59-Pad6)   (1 pins)
    Z59      74LS367            pin   6  

unconnected-(Z59-Pad7)   (1 pins)
    Z59      74LS367            pin   7  

unconnected-(Z59-Pad9)   (1 pins)
    Z59      74LS367            pin   9  

unconnected-(Z6-Q1-Pad11)   (1 pins)
    Z6       74LS92             pin  11  Q1

unconnected-(Z61B-O1-Pad11)   (1 pins)
    Z61      74LS139            pin  11  O1

unconnected-(Z62A-~{Q}-Pad6)   (1 pins)
    Z62      74LS74             pin   6  ~{Q}

unconnected-(Z62B-Q-Pad9)   (1 pins)
    Z62      74LS74             pin   9  Q

unconnected-(Z63A-~{Q}-Pad6)   (1 pins)
    Z63      74LS74             pin   6  ~{Q}

unconnected-(Z63B-~{Q}-Pad8)   (1 pins)
    Z63      74LS74             pin   8  ~{Q}

unconnected-(Z65-Q1-Pad11)   (1 pins)
    Z65      74LS92             pin  11  Q1

unconnected-(Z65-Q2-Pad9)   (1 pins)
    Z65      74LS92             pin   9  Q2

unconnected-(Z66-Pad10)   (1 pins)
    Z66      74LS367            pin  10  

unconnected-(Z66-Pad9)   (1 pins)
    Z66      74LS367            pin   9  

```
