# Model I main board, Rev G — complete netlist

Generated from `TRS-80-Model-I-G-E1-main` by `verify/emit.py`, which exports the schematic with `kicad-cli` and parses it with the same code the claims in `verify/claims.py` use.

**230 components · 375 nets · 1562 pin connections.**

Three views of the same information: components, a connection view answering "what is this pin wired to", and a net index answering "what is on this net". The redundancy is deliberate — it is what lets the file be checked against itself.

No integrity problems: every node names a known component, every pin number is valid for that component's symbol, and the two views agree on the connection count.

## Components

| ref | value | sheet |
|---|---|---|
| `C1` | 220uF 16V | Power |
| `C2` | 10uF 16V | Video Mixer |
| `C3` | 0.01uF 24V | Power |
| `C4` | 10uF 16V | Power |
| `C5` | 10uF 16V | Cassette Interface |
| `C6` | 100uF 16V | Cassette Interface |
| `C7` | 0.01uF 24V | Video Mixer |
| `C8` | 2200uF 35V | Power |
| `C9` | 10000uF 16V | Power |
| `C10` | 10uF 16V | Power |
| `C11` | 10uF 16V | Power |
| `C12` | 470pF | Power |
| `C13` | 470pF | Power |
| `C14` | 0.01uF 24V | Power |
| `C15` | 0.01uF 24V | Power |
| `C16` | 0.1uF 12V | Capacitors |
| `C17` | 0.1uF 12V | Capacitors |
| `C18` | 0.1uF 12V | Capacitors |
| `C19` | 0.1uF 12V | Capacitors |
| `C20` | 330pF | Video Sync |
| `C21` | 750pF | Video Sync |
| `C22` | 0.1uF 12V | Capacitors |
| `C23` | 0.1uF 12V | Capacitors |
| `C24` | 220pF | Cassette Interface |
| `C25` | 220pF | Cassette Interface |
| `C26` | 0.047uF | Video Sync |
| `C27` | 0.022uF | Video Sync |
| `C28` | 0.1uF 25V | Capacitors |
| `C29` | 0.1uF 12V | Capacitors |
| `C30` | 0.1uF 25V | Capacitors |
| `C31` | 0.1uF 12V | Capacitors |
| `C32` | 0.1uF 25V | Capacitors |
| `C33` | 0.1uF 12V | Capacitors |
| `C34` | 0.1uF 25V | Capacitors |
| `C35` | 0.1uF 12V | Capacitors |
| `C36` | 0.1uF 12V | Capacitors |
| `C37` | 0.1uF 12V | Capacitors |
| `C38` | 0.1uF 12V | Capacitors |
| `C39` | 0.1uF 12V | Cassette Interface |
| `C40` | 0.1uF 12V | Capacitors |
| `C41` | 0.1uF 12V | Capacitors |
| `C42` | 22uF 16V | CPU |
| `C43` | 47pF | Clock |
| `C44` | 0.1uF 12V | Capacitors |
| `C45` | 0.1uF 12V | Capacitors |
| `C46` | 0.1uF 12V | Capacitors |
| `C47` | 0.1uF 12V | Capacitors |
| `C48` | 0.1uF 12V | Capacitors |
| `C49` | 0.1uF 12V | Capacitors |
| `C50` | 0.1uF 12V | Capacitors |
| `C51` | 0.1uF 12V | Capacitors |
| `C52` | 0.1uF 12V | Capacitors |
| `C53` | 0.1uF 12V | Capacitors |
| `C54` | 0.1uF 12V | Capacitors |
| `C55` | 0.1uF 12V | Capacitors |
| `C56` | 0.1uF 12V | Capacitors |
| `C57` | 10uF 16V | CPU |
| `C58` | 0.1uF 12V | Capacitors |
| `C_C58` | 0.1uF 12V | Cassette Interface |
| `CR1` | 1N4735 | Power |
| `CR2` | 1N5231 | Power |
| `CR3` | 1N4148 | Cassette Interface |
| `CR4` | 1N4148 | Cassette Interface |
| `CR5` | 1N4148 | Cassette Interface |
| `CR6` | 1N4148 | Cassette Interface |
| `CR7` | 1N4148 | Cassette Interface |
| `CR8` | MDA202 | Power |
| `CR9` | 1N982 | Cassette Interface |
| `CR10` | 1N982 | Cassette Interface |
| `C_R67` | 220 | Cassette Interface |
| `J1` | Front View | Power |
| `J2` | Front View | Video Mixer |
| `J3` | Front View | Cassette Interface |
| `J4` | Edge Connector | Card-Edge Interface |
| `J100` | Connection Mainboard Side | Keyboard |
| `K1` | Relay_SPST-NO | Cassette Interface |
| `Q1` | 2N3904 | Video Mixer |
| `Q2` | 2N3906 | Video Mixer |
| `Q3` | TIP29A | Power |
| `Q4` | 2N6594 | Power |
| `Q5` | 2N3906 | Power |
| `Q6` | MJE34 | Power |
| `R1` | 68 | Power |
| `R2` | 2.7k | Power |
| `R3` | 750 | Power |
| `R4` | 0.33 | Power |
| `R5` | 1k | Power |
| `R6` | 1.2k | Power |
| `R7` | 1.2k | Power |
| `R8` | 100k | Power |
| `R9` | 3.3k | Power |
| `R10` | 1k | Power |
| `R11` | 3.3k | Power |
| `R12` | 3.3k | Power |
| `R13` | 2.2k | Power |
| `R14` | 12k | Power |
| `R15` | 1.5k | Power |
| `R16` | 1.2k | Power |
| `R17` | 2k | Power |
| `R18` | 5.6 | Power |
| `R19` | 220 | Power |
| `R20` | 100k | Video Sync |
| `R21` | 100k | Video Sync |
| `R22` | 75 | Video Mixer |
| `R23` | 120 | Video Mixer |
| `R24` | 680k | Cassette Interface |
| `R25` | 1.6M | Cassette Interface |
| `R26` | 1M | Cassette Interface |
| `R27` | 330 | Video Mixer |
| `R28` | 270 | Video Mixer |
| `R29` | 1.8k | Video Mixer |
| `R30` | 47 | Video Mixer |
| `R31` | 10 | Cassette Interface |
| `R32` | 10k | Cassette Interface |
| `R33` | 360k | Cassette Interface |
| `R34` | 470k | Cassette Interface |
| `R35` | 470k | Cassette Interface |
| `R36` | 360k | Cassette Interface |
| `R37` | 560k | Cassette Interface |
| `R38` | 470k | Cassette Interface |
| `R39` | 4.7k | Video Latch |
| `R40` | 4.7k | Video Generator |
| `R41` | 470k | Cassette Interface |
| `R42` | 1M | Cassette Interface |
| `R43` | 10k | Video Sync |
| `R44` | 10k | Video Sync |
| `R45` | 470k | Cassette Interface |
| `R46` | 910 | Clock |
| `R47` | 10k | CPU |
| `R48` | 4.7k | Address Decoder |
| `R49` | 4.7k | Video Access Multiplexer |
| `R50` | 4.7k | Card-Edge Interface |
| `R51` | 4.7k | Card-Edge Interface |
| `R52` | 910 | Clock |
| `R53` | 1.2k | Cassette Interface |
| `R54` | 7.5k | Cassette Interface |
| `R55` | 7.5k | Cassette Interface |
| `R56` | 220k | Cassette Interface |
| `R57` | 4.7k | RAM |
| `R58` | 4.7k | Card-Edge Interface |
| `R59` | 4.7k | Cassette Interface |
| `R60` | 4.7k | RAM |
| `R61` | 4.7k | Address Decoder |
| `R62` | 4.7k | Address Decoder |
| `R63` | 4.7k | Video Counter |
| `R64` | 330 | CPU |
| `R65` | 10k | CPU |
| `R66` | 4.7k | RAM |
| `R67` | 4.7k |  |
| `R68` | 4.7k | Address Decoder |
| `R69` | 4.7k |  |
| `S1` | ~ | Power |
| `S2` | Reset | CPU |
| `Y1` | 10.6445 MHz | Clock |
| `Z1` | LM723C | Power |
| `Z2` | LM723C | Power |
| `Z3` | ~ | Address Decoder |
| `Z4` | LM3900 | Cassette Interface |
| `Z5` | 74C00 | Video Sync |
| `Z6` | 74C04 | Video Sync |
| `Z7` | 74LS74 | Video Latch |
| `Z8` | 74LS153 | Video Generator |
| `Z9` | 74LS04 | Video Generator |
| `Z10` | 74LS166 | Video Generator |
| `Z11` | 74LS166 | Video Generator |
| `Z12` | 74LS93 | Video Counter |
| `Z13` | 4116 | RAM |
| `Z14` | 4116 | RAM |
| `Z15` | 4116 | RAM |
| `Z16` | 4116 | RAM |
| `Z17` | 4116 | RAM |
| `Z18` | 4116 | RAM |
| `Z19` | 4116 | RAM |
| `Z20` | 4116 | RAM |
| `Z21` | 74LS156 | Address Decoder |
| `Z22` | 74LS367 | CPU Gating |
| `Z23` | 74LS32 | CPU |
| `Z24` | 74LS132 | Cassette Interface |
| `Z25` | 74LS32 | Cassette Interface |
| `Z26` | 74LS20 | Video Generator |
| `Z27` | 74LS175 | Video Latch |
| `Z28` | 74LS174 | Video Latch |
| `Z29` | MCM6670 | Video Generator |
| `Z30` | 74LS02 | Video RAM |
| `Z31` | 74LS157 | Video Access Multiplexer |
| `Z32` | 74LS93 | Video Counter |
| `Z33` | 2364_20L | ROM |
| `Z34` | 2332_20L_21L | ROM |
| `Z35` | 74LS157 | RAM |
| `Z36` | 74LS32 | Address Decoder |
| `Z37` | 74LS02 | CPU |
| `Z38` | 74LS367 | CPU Gating |
| `Z39` | 74LS367 | CPU Gating |
| `Z40` | Z80CPU | CPU |
| `Z41` | 75452 | Cassette Interface |
| `Z42` | 74LS04 |  |
| `Z43` | 74LS157 | Video Counter |
| `Z44` | 74LS367 | Cassette Interface |
| `Z45` | 2102 | Video RAM |
| `Z46` | 2102 | Video RAM |
| `Z47` | 2102 | Video RAM |
| `Z48` | 2102 | Video RAM |
| `Z49` | 74LS157 | Video Access Multiplexer |
| `Z50` | 74LS93 | Video Counter |
| `Z51` | 74LS157 | RAM |
| `Z52` | 74LS04 | CPU |
| `Z53` | 74LS132 | CPU |
| `Z54` | 74LS30 | Cassette Interface |
| `Z55` | 74LS367 | CPU Gating |
| `Z56` | 74LS92 | CPU |
| `Z57` | 74C04 | Video Sync |
| `Z58` | 74LS92 | Video Counter |
| `Z59` | 74LS175 | Cassette Interface |
| `Z60` | 74LS367 | Video RAM |
| `Z61` | 2102 | Video RAM |
| `Z62` | 2102 | Video RAM |
| `Z63` | 2102 | Video RAM |
| `Z64` | 74LS157 | Video Access Multiplexer |
| `Z65` | 74LS93 | Video Counter |
| `Z66` | 74LS11 | Video Counter |
| `Z67` | 74LS367 | RAM |
| `Z68` | 74LS367 | RAM |
| `Z69` | 74LS74 | CPU |
| `Z70` | 74LS74 | CPU |
| `Z71` | ~ | RAM |
| `Z72` | 74LS367 | CPU |
| `Z73` | 74LS32 | CPU |
| `Z74` | 74LS00 | CPU |
| `Z75` | 74LS367 | CPU Gating |
| `Z76` | 74LS367 | CPU Gating |

## Connections

For each pin: its name, its net, and what else is on that net. Nets with more than 12 pins (power, ground, buses) are named rather than expanded.

```
C1  (220uF 16V, Power)
   pin   1                GND                          [net GND, 204 pins]
   pin   2                Net-(C1-Pad2)                R19.2 S1.10

C2  (10uF 16V, Video Mixer)
   pin   1                Net-(Q1-C)                   C7.1 Q1.3(C) R30.2
   pin   2                GND                          [net GND, 204 pins]

C3  (0.01uF 24V, Power)
   pin   1                -5V                          [net -5V, 16 pins]
   pin   2                GND                          [net GND, 204 pins]

C4  (10uF 16V, Power)
   pin   1                GND                          [net GND, 204 pins]
   pin   2                -5V                          [net -5V, 16 pins]

C5  (10uF 16V, Cassette Interface)
   pin   1                Net-(C5-Pad1)                R24.1 R25.2 R26.1 R32.1
   pin   2                GND                          [net GND, 204 pins]

C6  (100uF 16V, Cassette Interface)
   pin   1                GND                          [net GND, 204 pins]
   pin   2                Net-(Z4E-V+)                 R31.1 Z4.14(V+)

C7  (0.01uF 24V, Video Mixer)
   pin   1                Net-(Q1-C)                   C2.1 Q1.3(C) R30.2
   pin   2                GND                          [net GND, 204 pins]

C8  (2200uF 35V, Power)
   pin   1                Net-(Q6-E)                   Q6.3(E) R16.1 S1.3 Z2.12(V+)
   pin   2                GND                          [net GND, 204 pins]

C9  (10000uF 16V, Power)
   pin   1                Net-(Q4-E)                   Q4.2(E) R1.1 S1.6 S1.7
   pin   2                GND                          [net GND, 204 pins]

C10  (10uF 16V, Power)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C11  (10uF 16V, Power)
   pin   1                +12V                         [net +12V, 19 pins]
   pin   2                GND                          [net GND, 204 pins]

C12  (470pF, Power)
   pin   1                Net-(Z1--)                   R7.2 Z1.4(-)
   pin   2                Net-(Z1-FC)                  Z1.13(FC)

C13  (470pF, Power)
   pin   1                Net-(Z2-FC)                  Z2.13(FC)
   pin   2                Net-(Z2--)                   R10.2(2) Z2.4(-)

C14  (0.01uF 24V, Power)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C15  (0.01uF 24V, Power)
   pin   1                +12V                         [net +12V, 19 pins]
   pin   2                GND                          [net GND, 204 pins]

C16  (0.1uF 12V, Capacitors)
   pin   1                -5V                          [net -5V, 16 pins]
   pin   2                GND                          [net GND, 204 pins]

C17  (0.1uF 12V, Capacitors)
   pin   1                -5V                          [net -5V, 16 pins]
   pin   2                GND                          [net GND, 204 pins]

C18  (0.1uF 12V, Capacitors)
   pin   1                -5V                          [net -5V, 16 pins]
   pin   2                GND                          [net GND, 204 pins]

C19  (0.1uF 12V, Capacitors)
   pin   1                -5V                          [net -5V, 16 pins]
   pin   2                GND                          [net GND, 204 pins]

C20  (330pF, Video Sync)
   pin   1                Net-(C20-Pad1)               R20.2(2) Z6.3
   pin   2                Net-(C20-Pad2)               C21.1 Z6.6

C21  (750pF, Video Sync)
   pin   1                Net-(C20-Pad2)               C20.2 Z6.6
   pin   2                Net-(C21-Pad2)               R43.1 Z6.11

C22  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C23  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C24  (220pF, Cassette Interface)
   pin   1                CASSIN                       C_R67.2 J3.4
   pin   2                Net-(C24-Pad2)               C25.1 R36.1

C25  (220pF, Cassette Interface)
   pin   1                Net-(C24-Pad2)               C24.2 R36.1
   pin   2                Net-(C25-Pad2)               R33.1

C26  (0.047uF, Video Sync)
   pin   1                Net-(C26-Pad1)               R21.2(2) Z57.13
   pin   2                Net-(C26-Pad2)               C27.1 Z57.10

C27  (0.022uF, Video Sync)
   pin   1                Net-(C26-Pad2)               C26.2 Z57.10
   pin   2                Net-(C27-Pad2)               R44.2 Z57.5

C28  (0.1uF 25V, Capacitors)
   pin   1                +12V                         [net +12V, 19 pins]
   pin   2                GND                          [net GND, 204 pins]

C29  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C30  (0.1uF 25V, Capacitors)
   pin   1                +12V                         [net +12V, 19 pins]
   pin   2                GND                          [net GND, 204 pins]

C31  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C32  (0.1uF 25V, Capacitors)
   pin   1                +12V                         [net +12V, 19 pins]
   pin   2                GND                          [net GND, 204 pins]

C33  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C34  (0.1uF 25V, Capacitors)
   pin   1                +12V                         [net +12V, 19 pins]
   pin   2                GND                          [net GND, 204 pins]

C35  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C36  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C37  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C38  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C39  (0.1uF 12V, Cassette Interface)
   pin   1                GND                          [net GND, 204 pins]
   pin   2                Net-(CR7-K)                  CR7.1(K) R45.1

C40  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C41  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C42  (22uF 16V, CPU)
   pin   1                Net-(C42-Pad1)               R47.2 Z53.12 Z53.13
   pin   2                GND                          [net GND, 204 pins]

C43  (47pF, Clock)
   pin   1                Net-(C43-Pad1)               R46.1 Z42.1
   pin   2                Net-(C43-Pad2)               R52.2 Z42.4 Z42.5

C44  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C45  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C46  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C47  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C48  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C49  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C50  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C51  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C52  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C53  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C54  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C55  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C56  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C57  (10uF 16V, CPU)
   pin   1                Net-(C57-Pad1)               R65.2 S2.4 Z53.1
   pin   2                GND                          [net GND, 204 pins]

C58  (0.1uF 12V, Capacitors)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                GND                          [net GND, 204 pins]

C_C58  (0.1uF 12V, Cassette Interface)
   pin   1                Net-(CR10-A)                 CR10.2(A) J3.3 K1.3
   pin   2                Net-(CR9-A)                  CR9.2(A) J3.1 K1.4

CR1  (1N4735, Power)
   pin   1 K              +5V                          [net +5V, 134 pins]
   pin   2 A              GND                          [net GND, 204 pins]

CR2  (1N5231, Power)
   pin   1 K              GND                          [net GND, 204 pins]
   pin   2 A              -5V                          [net -5V, 16 pins]

CR3  (1N4148, Cassette Interface)
   pin   1 K              +5V                          [net +5V, 134 pins]
   pin   2 A              Net-(CR3-A)                  K1.2 Z41.3(1Y)

CR4  (1N4148, Cassette Interface)
   pin   1 K              Net-(CR4-K)                  CR5.1(K) R41.1
   pin   2 A              Net-(CR4-A)                  R34.2 Z4.4

CR5  (1N4148, Cassette Interface)
   pin   1 K              Net-(CR4-K)                  CR4.1(K) R41.1
   pin   2 A              Net-(CR5-A)                  R35.1 R36.2 R37.1 Z4.5

CR6  (1N4148, Cassette Interface)
   pin   1 K              Net-(CR6-K)                  CR7.2(A)
   pin   2 A              Net-(CR6-A)                  R38.1 R42.2 Z4.9

CR7  (1N4148, Cassette Interface)
   pin   1 K              Net-(CR7-K)                  C39.2 R45.1
   pin   2 A              Net-(CR6-K)                  CR6.1(K)

CR8  (MDA202, Power)
   pin   1 +              Net-(CR8-+)                  S1.4 S1.5 S1.8 S1.9
   pin   2                Net-(CR8-Pad2)               J1.1
   pin   3                Net-(CR8-Pad3)               J1.3
   pin   4 -              Net-(CR8--)                  S1.11 S1.12

CR9  (1N982, Cassette Interface)
   pin   1 K              Net-(CR10-K)                 CR10.1(K)
   pin   2 A              Net-(CR9-A)                  C_C58.2 J3.1 K1.4

CR10  (1N982, Cassette Interface)
   pin   1 K              Net-(CR10-K)                 CR9.1(K)
   pin   2 A              Net-(CR10-A)                 C_C58.1 J3.3 K1.3

C_R67  (220, Cassette Interface)
   pin   1                GND                          [net GND, 204 pins]
   pin   2                CASSIN                       C24.1 J3.4

J1  (Front View, Power)
   pin   1                Net-(CR8-Pad2)               CR8.2
   pin   2                Net-(J1-Pad2)                S1.1 S1.2
   pin   3                Net-(CR8-Pad3)               CR8.3
   pin   4                GND                          [net GND, 204 pins]
   pin   5                unconnected-(J1-Pad5)        (no other connection)

J2  (Front View, Video Mixer)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                unconnected-(J2-Pad2)        (no other connection)
   pin   3                unconnected-(J2-Pad3)        (no other connection)
   pin   4                Net-(Q1-E)                   Q1.1(E) R22.1
   pin   5                GND                          [net GND, 204 pins]

J3  (Front View, Cassette Interface)
   pin   1                Net-(CR9-A)                  CR9.2(A) C_C58.2 K1.4
   pin   2                GND                          [net GND, 204 pins]
   pin   3                Net-(CR10-A)                 CR10.2(A) C_C58.1 K1.3
   pin   4                CASSIN                       C24.1 C_R67.2
   pin   5                CASSOUT                      R53.2 R54.2 R55.1

J4  (Edge Connector, Card-Edge Interface)
   pin   1 Pin_1          ~{RAS}                       Z68.14 Z72.5 Z73.5
   pin   2 Pin_2          ~{SYSRES}                    Z37.1
   pin   3 Pin_3          ~{CAS}                       Z67.14 Z72.9
   pin   4 Pin_4          A10                          Z33.19(A10) Z34.19(A10) Z36.13 Z38.3 Z51.3(I1a) Z52.1
   pin   5 Pin_5          A12                          Z21.13(A0) Z33.21(A12) Z34.21(~{CE2}) Z38.5 Z51.10(I1c)
   pin   6 Pin_6          A13                          Z21.3(A1) Z38.7 Z71.16
   pin   7 Pin_7          A15                          Z38.9 Z73.4
   pin   8 Pin_8          GND                          [net GND, 204 pins]
   pin   9 Pin_9          A11                          Z33.18(A11) Z34.18(A11) Z37.5 Z37.6 Z38.13 Z51.6(I1b)
   pin  10 Pin_10         A14                          Z21.1(Ea1) Z21.15(Eb2) Z38.11
   pin  11 Pin_11         A8                           Z31.2(I0a) Z33.23(A8) Z34.23(A8) Z35.10(I1c) Z39.3
   pin  12 Pin_12         ~{OUT}                       Z22.3 Z25.9
   pin  13 Pin_13         ~{WR}                        Z13.3(~{WR}) Z14.3(~{WR}) Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z22.5 Z49.14(I0d)
   pin  14 Pin_14         ~{INTAK}                     Z73.3
   pin  15 Pin_15         ~{RD}                        Z22.7 Z49.5(I0b) Z52.13
   pin  16 Pin_16         MUX                          Z35.1(S) Z51.1(S) Z72.3
   pin  17 Pin_17         A9                           Z31.5(I0b) Z33.22(A9) Z34.22(A9) Z35.13(I1d) Z39.13
   pin  18 Pin_18         D4                           J100.18(Pin_18) Z15.2(IN) Z55.2 Z60.9 Z61.11(IN) Z67.9 Z75.7
   pin  19 Pin_19         ~{IN}                        Z22.9 Z25.4
   pin  20 Pin_20         D7                           J100.17(Pin_17) Z13.2(IN) Z44.11 Z60.3 Z63.11(IN) Z67.7 Z75.11 Z76.6
   pin  21 Pin_21         ~{INT}                       R50.2 Z40.16(~{INT})
   pin  22 Pin_22         D1                           J100.16(Pin_16) Z16.2(IN) Z44.5 Z47.11(IN) Z59.5(D1) Z68.3 Z76.13 Z76.2
   pin  23 Pin_23         ~{TEST}                      R58.2 Z40.25(~{BUSRQ}) Z52.3 Z53.4
   pin  24 Pin_24         D6                           J100.15(Pin_15) Z14.2(IN) Z44.13 Z55.10 Z60.5 Z67.5 Z75.9
   pin  25 Pin_25         A0                           J100.5(Pin_5) Z33.8(A0) Z34.8(A0) Z35.2(I0a) Z52.5 Z55.11 Z64.11(I0c)
   pin  26 Pin_26         D3                           J100.13(Pin_13) Z19.2(IN) Z44.9 Z45.11(IN) Z55.4 Z59.13(D3) Z68.7 Z75.5
   pin  27 Pin_27         A1                           J100.4(Pin_4) Z33.7(A1) Z34.7(A1) Z35.5(I0b) Z54.11 Z55.13 Z64.2(I0a)
   pin  28 Pin_28         D5                           J100.12(Pin_12) Z20.2(IN) Z55.6 Z60.7 Z62.11(IN) Z67.3 Z75.3
   pin  29 Pin_29         GND                          [net GND, 204 pins]
   pin  30 Pin_30         D0                           J100.11(Pin_11) Z17.2(IN) Z44.7 Z48.11(IN) Z59.4(D0) Z68.9 Z76.10 Z76.11
   pin  31 Pin_31         A4                           J100.2(Pin_2) Z33.4(A4) Z34.4(A4) Z39.7 Z49.11(I0c) Z51.2(I0a) Z54.4
   pin  32 Pin_32         D2                           J100.10(Pin_10) Z18.2(IN) Z44.3 Z46.11(IN) Z59.12(D2) Z68.5 Z75.13 Z76.4
   pin  33 Pin_33         ~{WAIT}                      R51.2 Z40.24(~{WAIT})
   pin  34 Pin_34         A3                           J100.9(Pin_9) Z22.13 Z33.5(A3) Z34.5(A3) Z35.14(I0d) Z54.1 Z64.5(I0b)
   pin  35 Pin_35         A5                           J100.3(Pin_3) Z33.3(A5) Z34.3(A5) Z39.9 Z49.2(I0a) Z51.5(I0b) Z54.12
   pin  36 Pin_36         A7                           J100.8(Pin_8) Z31.14(I0d) Z33.1(A7) Z34.1(A7) Z35.6(I1b) Z39.11 Z54.5 Z54.6
   pin  37 Pin_37         GND                          [net GND, 204 pins]
   pin  38 Pin_38         A6                           J100.7(Pin_7) Z31.11(I0c) Z33.2(A6) Z34.2(A6) Z39.5 Z51.11(I0c) Z54.3 Z71.15
   pin  39 Pin_39         GND                          [net GND, 204 pins]
   pin  40 Pin_40         A2                           J100.6(Pin_6) Z22.11 Z33.6(A2) Z34.6(A2) Z35.11(I0c) Z54.2 Z64.14(I0d)

J100  (Connection Mainboard Side, Keyboard)
   pin   1 Pin_1          +5V                          [net +5V, 134 pins]
   pin   2 Pin_2          A4                           J4.31(Pin_31) Z33.4(A4) Z34.4(A4) Z39.7 Z49.11(I0c) Z51.2(I0a) Z54.4
   pin   3 Pin_3          A5                           J4.35(Pin_35) Z33.3(A5) Z34.3(A5) Z39.9 Z49.2(I0a) Z51.5(I0b) Z54.12
   pin   4 Pin_4          A1                           J4.27(Pin_27) Z33.7(A1) Z34.7(A1) Z35.5(I0b) Z54.11 Z55.13 Z64.2(I0a)
   pin   5 Pin_5          A0                           J4.25(Pin_25) Z33.8(A0) Z34.8(A0) Z35.2(I0a) Z52.5 Z55.11 Z64.11(I0c)
   pin   6 Pin_6          A2                           J4.40(Pin_40) Z22.11 Z33.6(A2) Z34.6(A2) Z35.11(I0c) Z54.2 Z64.14(I0d)
   pin   7 Pin_7          A6                           J4.38(Pin_38) Z31.11(I0c) Z33.2(A6) Z34.2(A6) Z39.5 Z51.11(I0c) Z54.3 Z71.15
   pin   8 Pin_8          A7                           J4.36(Pin_36) Z31.14(I0d) Z33.1(A7) Z34.1(A7) Z35.6(I1b) Z39.11 Z54.5 Z54.6
   pin   9 Pin_9          A3                           J4.34(Pin_34) Z22.13 Z33.5(A3) Z34.5(A3) Z35.14(I0d) Z54.1 Z64.5(I0b)
   pin  10 Pin_10         D2                           J4.32(Pin_32) Z18.2(IN) Z44.3 Z46.11(IN) Z59.12(D2) Z68.5 Z75.13 Z76.4
   pin  11 Pin_11         D0                           J4.30(Pin_30) Z17.2(IN) Z44.7 Z48.11(IN) Z59.4(D0) Z68.9 Z76.10 Z76.11
   pin  12 Pin_12         D5                           J4.28(Pin_28) Z20.2(IN) Z55.6 Z60.7 Z62.11(IN) Z67.3 Z75.3
   pin  13 Pin_13         D3                           J4.26(Pin_26) Z19.2(IN) Z44.9 Z45.11(IN) Z55.4 Z59.13(D3) Z68.7 Z75.5
   pin  14 Pin_14         ~{KYBD}                      Z36.11
   pin  15 Pin_15         D6                           J4.24(Pin_24) Z14.2(IN) Z44.13 Z55.10 Z60.5 Z67.5 Z75.9
   pin  16 Pin_16         D1                           J4.22(Pin_22) Z16.2(IN) Z44.5 Z47.11(IN) Z59.5(D1) Z68.3 Z76.13 Z76.2
   pin  17 Pin_17         D7                           J4.20(Pin_20) Z13.2(IN) Z44.11 Z60.3 Z63.11(IN) Z67.7 Z75.11 Z76.6
   pin  18 Pin_18         D4                           J4.18(Pin_18) Z15.2(IN) Z55.2 Z60.9 Z61.11(IN) Z67.9 Z75.7
   pin  19 Pin_19         GND                          [net GND, 204 pins]
   pin  20 Pin_20         unconnected-(J100-Pin_20-Pad20) (no other connection)

K1  (Relay_SPST-NO, Cassette Interface)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(CR3-A)                  CR3.2(A) Z41.3(1Y)
   pin   3                Net-(CR10-A)                 CR10.2(A) C_C58.1 J3.3
   pin   4                Net-(CR9-A)                  CR9.2(A) C_C58.2 J3.1

Q1  (2N3904, Video Mixer)
   pin   1 E              Net-(Q1-E)                   J2.4 R22.1
   pin   2 B              Net-(Q1-B)                   R23.1 R27.1 R28.2
   pin   3 C              Net-(Q1-C)                   C2.1 C7.1 R30.2

Q2  (2N3906, Video Mixer)
   pin   1 E              +5V                          [net +5V, 134 pins]
   pin   2 B              Net-(Q2-B)                   R29.2
   pin   3 C              Net-(Q2-C)                   R28.1

Q3  (TIP29A, Power)
   pin   1 B              Net-(Q3-B)                   R2.1 Z1.10(Vout)
   pin   2 C              Net-(Q3-C)                   Q4.1(B) R1.2
   pin   3 E              Net-(Q3-E)                   Q4.3(C) R2.2 R3.1 R4.1

Q4  (2N6594, Power)
   pin   1 B              Net-(Q3-C)                   Q3.2(C) R1.2
   pin   2 E              Net-(Q4-E)                   C9.1 R1.1 S1.6 S1.7
   pin   3 C              Net-(Q3-E)                   Q3.3(E) R2.2 R3.1 R4.1

Q5  (2N3906, Power)
   pin   1 E              Net-(Q5-E)                   R5.2(2) Z1.5(+)
   pin   2 B              Net-(Q5-B)                   R8.1
   pin   3 C              Net-(Q5-C)                   R9.2

Q6  (MJE34, Power)
   pin   1 B              Net-(Q6-B)                   R16.2 Z2.11(VC)
   pin   2 C              Net-(Q6-C)                   R17.1 R18.2 Z2.10(Vout)
   pin   3 E              Net-(Q6-E)                   C8.1 R16.1 S1.3 Z2.12(V+)

R1  (68, Power)
   pin   1                Net-(Q4-E)                   C9.1 Q4.2(E) S1.6 S1.7
   pin   2                Net-(Q3-C)                   Q3.2(C) Q4.1(B)

R2  (2.7k, Power)
   pin   1                Net-(Q3-B)                   Q3.1(B) Z1.10(Vout)
   pin   2                Net-(Q3-E)                   Q3.3(E) Q4.3(C) R3.1 R4.1

R3  (750, Power)
   pin   1                Net-(Q3-E)                   Q3.3(E) Q4.3(C) R2.2 R4.1
   pin   2                Net-(Z1-ILIM)                R9.1 Z1.2(ILIM)

R4  (0.33, Power)
   pin   1                Net-(Q3-E)                   Q3.3(E) Q4.3(C) R2.2 R3.1
   pin   2                +5V                          [net +5V, 134 pins]

R5  (1k, Power)
   pin   1 1              Net-(R5-Pad1)                R6.1
   pin   2 2              Net-(Q5-E)                   Q5.1(E) Z1.5(+)
   pin   3 3              Net-(R11-Pad1)               R11.1

R6  (1.2k, Power)
   pin   1                Net-(R5-Pad1)                R5.1(1)
   pin   2                Net-(Z1-VREF)                Z1.6(VREF)

R7  (1.2k, Power)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(Z1--)                   C12.1 Z1.4(-)

R8  (100k, Power)
   pin   1                Net-(Q5-B)                   Q5.2(B)
   pin   2                +5V                          [net +5V, 134 pins]

R9  (3.3k, Power)
   pin   1                Net-(Z1-ILIM)                R3.2 Z1.2(ILIM)
   pin   2                Net-(Q5-C)                   Q5.3(C)

R10  (1k, Power)
   pin   1 1              Net-(R10-Pad1)               R12.1
   pin   2 2              Net-(Z2--)                   C13.2 Z2.4(-)
   pin   3 3              Net-(R10-Pad3)               R13.2

R11  (3.3k, Power)
   pin   1                Net-(R11-Pad1)               R5.3(3)
   pin   2                GND                          [net GND, 204 pins]

R12  (3.3k, Power)
   pin   1                Net-(R10-Pad1)               R10.1(1)
   pin   2                GND                          [net GND, 204 pins]

R13  (2.2k, Power)
   pin   1                +12V                         [net +12V, 19 pins]
   pin   2                Net-(R10-Pad3)               R10.3(3)

R14  (12k, Power)
   pin   1                Net-(Z2-ILIM)                R17.2 Z2.2(ILIM)
   pin   2                GND                          [net GND, 204 pins]

R15  (1.5k, Power)
   pin   1                Net-(Z2-VREF)                Z2.6(VREF)
   pin   2                Net-(Z2-+)                   Z2.5(+)

R16  (1.2k, Power)
   pin   1                Net-(Q6-E)                   C8.1 Q6.3(E) S1.3 Z2.12(V+)
   pin   2                Net-(Q6-B)                   Q6.1(B) Z2.11(VC)

R17  (2k, Power)
   pin   1                Net-(Q6-C)                   Q6.2(C) R18.2 Z2.10(Vout)
   pin   2                Net-(Z2-ILIM)                R14.1 Z2.2(ILIM)

R18  (5.6, Power)
   pin   1                +12V                         [net +12V, 19 pins]
   pin   2                Net-(Q6-C)                   Q6.2(C) R17.1 Z2.10(Vout)

R19  (220, Power)
   pin   1                -5V                          [net -5V, 16 pins]
   pin   2                Net-(C1-Pad2)                C1.2 S1.10

R20  (100k, Video Sync)
   pin   1 1              Net-(R20-Pad1)               Z6.2
   pin   2 2              Net-(C20-Pad1)               C20.1 Z6.3
   pin   3 3              unconnected-(R20-Pad3)       (no other connection)

R21  (100k, Video Sync)
   pin   1 1              Net-(R21-Pad1)               Z57.4
   pin   2 2              Net-(C26-Pad1)               C26.1 Z57.13
   pin   3 3              unconnected-(R21-Pad3)       (no other connection)

R22  (75, Video Mixer)
   pin   1                Net-(Q1-E)                   J2.4 Q1.1(E)
   pin   2                GND                          [net GND, 204 pins]

R23  (120, Video Mixer)
   pin   1                Net-(Q1-B)                   Q1.2(B) R27.1 R28.2
   pin   2                Net-(Z41B-2Y)                Z41.5(2Y)

R24  (680k, Cassette Interface)
   pin   1                Net-(C5-Pad1)                C5.1 R25.2 R26.1 R32.1
   pin   2                Net-(Z4B-+)                  Z4.2(+)

R25  (1.6M, Cassette Interface)
   pin   1                Net-(Z4A-+)                  R33.2 Z4.1(+)
   pin   2                Net-(C5-Pad1)                C5.1 R24.1 R26.1 R32.1

R26  (1M, Cassette Interface)
   pin   1                Net-(C5-Pad1)                C5.1 R24.1 R25.2 R32.1
   pin   2                Net-(Z4C-+)                  Z4.13(+)

R27  (330, Video Mixer)
   pin   1                Net-(Q1-B)                   Q1.2(B) R23.1 R28.2
   pin   2                GND                          [net GND, 204 pins]

R28  (270, Video Mixer)
   pin   1                Net-(Q2-C)                   Q2.3(C)
   pin   2                Net-(Q1-B)                   Q1.2(B) R23.1 R27.1

R29  (1.8k, Video Mixer)
   pin   1                SYNC                         Z5.8
   pin   2                Net-(Q2-B)                   Q2.2(B)

R30  (47, Video Mixer)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(Q1-C)                   C2.1 C7.1 Q1.3(C)

R31  (10, Cassette Interface)
   pin   1                Net-(Z4E-V+)                 C6.2 Z4.14(V+)
   pin   2                +5V                          [net +5V, 134 pins]

R32  (10k, Cassette Interface)
   pin   1                Net-(C5-Pad1)                C5.1 R24.1 R25.2 R26.1
   pin   2                +5V                          [net +5V, 134 pins]

R33  (360k, Cassette Interface)
   pin   1                Net-(C25-Pad2)               C25.2
   pin   2                Net-(Z4A-+)                  R25.1 Z4.1(+)

R34  (470k, Cassette Interface)
   pin   1                Net-(Z4B--)                  R35.2 Z4.3(-)
   pin   2                Net-(CR4-A)                  CR4.2(A) Z4.4

R35  (470k, Cassette Interface)
   pin   1                Net-(CR5-A)                  CR5.2(A) R36.2 R37.1 Z4.5
   pin   2                Net-(Z4B--)                  R34.1 Z4.3(-)

R36  (360k, Cassette Interface)
   pin   1                Net-(C24-Pad2)               C24.2 C25.1
   pin   2                Net-(CR5-A)                  CR5.2(A) R35.1 R37.1 Z4.5

R37  (560k, Cassette Interface)
   pin   1                Net-(CR5-A)                  CR5.2(A) R35.1 R36.2 Z4.5
   pin   2                Net-(Z4A--)                  Z4.6(-)

R38  (470k, Cassette Interface)
   pin   1                Net-(CR6-A)                  CR6.2(A) R42.2 Z4.9
   pin   2                Net-(Z4D-+)                  Z4.12(+)

R39  (4.7k, Video Latch)
   pin   1                Net-(Z7A-~{R})               Z7.1(~{R})
   pin   2                +5V                          [net +5V, 134 pins]

R40  (4.7k, Video Generator)
   pin   1                Net-(Z10-Clr)                Z10.9(Clr) Z11.9(Clr)
   pin   2                +5V                          [net +5V, 134 pins]

R41  (470k, Cassette Interface)
   pin   1                Net-(CR4-K)                  CR4.1(K) CR5.1(K)
   pin   2                Net-(Z4C--)                  R42.1 Z4.8(-)

R42  (1M, Cassette Interface)
   pin   1                Net-(Z4C--)                  R41.2 Z4.8(-)
   pin   2                Net-(CR6-A)                  CR6.2(A) R38.1 Z4.9

R43  (10k, Video Sync)
   pin   1                Net-(C21-Pad2)               C21.2 Z6.11
   pin   2                GND                          [net GND, 204 pins]

R44  (10k, Video Sync)
   pin   1                GND                          [net GND, 204 pins]
   pin   2                Net-(C27-Pad2)               C27.2 Z57.5

R45  (470k, Cassette Interface)
   pin   1                Net-(CR7-K)                  C39.2 CR7.1(K)
   pin   2                Net-(Z4D--)                  Z4.11(-)

R46  (910, Clock)
   pin   1                Net-(C43-Pad1)               C43.1 Z42.1
   pin   2                Net-(R46-Pad2)               Y1.1(1) Z42.2

R47  (10k, CPU)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(C42-Pad1)               C42.1 Z53.12 Z53.13

R48  (4.7k, Address Decoder)
   pin   1                Net-(Z21-Q3b)                Z21.12(Q3b) Z36.4
   pin   2                +5V                          [net +5V, 134 pins]

R49  (4.7k, Video Access Multiplexer)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(Z49-I1b)                Z49.13(I1d) Z49.6(I1b)

R50  (4.7k, Card-Edge Interface)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                ~{INT}                       J4.21(Pin_21) Z40.16(~{INT})

R51  (4.7k, Card-Edge Interface)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                ~{WAIT}                      J4.33(Pin_33) Z40.24(~{WAIT})

R52  (910, Clock)
   pin   1                Net-(R52-Pad1)               Y1.2(2) Z42.3
   pin   2                Net-(C43-Pad2)               C43.2 Z42.4 Z42.5

R53  (1.2k, Cassette Interface)
   pin   1                GND                          [net GND, 204 pins]
   pin   2                CASSOUT                      J3.5 R54.2 R55.1

R54  (7.5k, Cassette Interface)
   pin   1                Net-(Z59-Q0)                 Z59.2(Q0)
   pin   2                CASSOUT                      J3.5 R53.2 R55.1

R55  (7.5k, Cassette Interface)
   pin   1                CASSOUT                      J3.5 R53.2 R54.2
   pin   2                Net-(Z59-~{Q1})              R56.1 Z59.6(~{Q1})

R56  (220k, Cassette Interface)
   pin   1                Net-(Z59-~{Q1})              R55.2 Z59.6(~{Q1})
   pin   2                +5V                          [net +5V, 134 pins]

R57  (4.7k, RAM)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(Z13-~{CAS})             Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z67.13

R58  (4.7k, Card-Edge Interface)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                ~{TEST}                      J4.23(Pin_23) Z40.25(~{BUSRQ}) Z52.3 Z53.4

R59  (4.7k, Cassette Interface)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(Z59-~{Mr})              Z59.1(~{Mr})

R60  (4.7k, RAM)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(Z13-~{RAS})             Z13.4(~{RAS}) Z14.4(~{RAS}) Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z68.13

R61  (4.7k, Address Decoder)
   pin   1                ~{ROMA}                      Z3.7 Z3.8 Z33.20(~{OE}) Z74.9
   pin   2                +5V                          [net +5V, 134 pins]

R62  (4.7k, Address Decoder)
   pin   1                ~{RAM}                       Z3.12 Z3.13 Z3.14 Z3.15 Z71.12 Z71.4 Z74.10
   pin   2                +5V                          [net +5V, 134 pins]

R63  (4.7k, Video Counter)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(Z70B-~{R})              Z70.13(~{R})

R64  (330, CPU)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                ZCLK                         Z40.6(~{CLK}) Z72.11

R65  (10k, CPU)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(C57-Pad1)               C57.1 S2.4 Z53.1

R66  (4.7k, RAM)
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(R66-Pad2)               Z71.10

R67  (4.7k, )
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                Net-(R67-Pad2)               Z42.9

R68  (4.7k, Address Decoder)
   pin   1                ~{ROMB}                      Z3.1 Z3.6 Z34.20(~{CE1}) Z74.12 Z74.13
   pin   2                +5V                          [net +5V, 134 pins]

R69  (4.7k, )
   pin   1                +5V                          [net +5V, 134 pins]
   pin   2                HI                           Z69.10(~{S}) Z69.4(~{S}) Z70.10(~{S}) Z70.4(~{S})

S1  (~, Power)
   pin   1                Net-(J1-Pad2)                J1.2 S1.2
   pin   2                Net-(J1-Pad2)                J1.2 S1.1
   pin   3                Net-(Q6-E)                   C8.1 Q6.3(E) R16.1 Z2.12(V+)
   pin   4                Net-(CR8-+)                  CR8.1(+) S1.5 S1.8 S1.9
   pin   5                Net-(CR8-+)                  CR8.1(+) S1.4 S1.8 S1.9
   pin   6                Net-(Q4-E)                   C9.1 Q4.2(E) R1.1 S1.7
   pin   7                Net-(Q4-E)                   C9.1 Q4.2(E) R1.1 S1.6
   pin   8                Net-(CR8-+)                  CR8.1(+) S1.4 S1.5 S1.9
   pin   9                Net-(CR8-+)                  CR8.1(+) S1.4 S1.5 S1.8
   pin  10                Net-(C1-Pad2)                C1.2 R19.2
   pin  11                Net-(CR8--)                  CR8.4(-) S1.12
   pin  12                Net-(CR8--)                  CR8.4(-) S1.11

S2  (Reset, CPU)
   pin   1                unconnected-(S2-Pad1)        (no other connection)
   pin   2                unconnected-(S2-Pad2)        (no other connection)
   pin   3                unconnected-(S2-Pad3)        (no other connection)
   pin   4                Net-(C57-Pad1)               C57.1 R65.2 Z53.1
   pin   5                GND                          [net GND, 204 pins]
   pin   6                GND                          [net GND, 204 pins]

Y1  (10.6445 MHz, Clock)
   pin   1 1              Net-(R46-Pad2)               R46.2 Z42.2
   pin   2 2              Net-(R52-Pad1)               R52.1 Z42.3

Z1  (LM723C, Power)
   pin   1 NC             unconnected-(Z1-NC-Pad1)     (no other connection)
   pin   2 ILIM           Net-(Z1-ILIM)                R3.2 R9.1
   pin   3 CSEN           +5V                          [net +5V, 134 pins]
   pin   4 -              Net-(Z1--)                   C12.1 R7.2
   pin   5 +              Net-(Q5-E)                   Q5.1(E) R5.2(2)
   pin   6 VREF           Net-(Z1-VREF)                R6.2
   pin   7 V-             GND                          [net GND, 204 pins]
   pin   8 NC             unconnected-(Z1-NC-Pad8)     (no other connection)
   pin   9 VZ             unconnected-(Z1-VZ-Pad9)     (no other connection)
   pin  10 Vout           Net-(Q3-B)                   Q3.1(B) R2.1
   pin  11 VC             +12V                         [net +12V, 19 pins]
   pin  12 V+             +12V                         [net +12V, 19 pins]
   pin  13 FC             Net-(Z1-FC)                  C12.2
   pin  14 NC             unconnected-(Z1-NC-Pad14)    (no other connection)

Z2  (LM723C, Power)
   pin   1 NC             unconnected-(Z2-NC-Pad1)     (no other connection)
   pin   2 ILIM           Net-(Z2-ILIM)                R14.1 R17.2
   pin   3 CSEN           +12V                         [net +12V, 19 pins]
   pin   4 -              Net-(Z2--)                   C13.2 R10.2(2)
   pin   5 +              Net-(Z2-+)                   R15.2
   pin   6 VREF           Net-(Z2-VREF)                R15.1
   pin   7 V-             GND                          [net GND, 204 pins]
   pin   8 NC             unconnected-(Z2-NC-Pad8)     (no other connection)
   pin   9 VZ             unconnected-(Z2-VZ-Pad9)     (no other connection)
   pin  10 Vout           Net-(Q6-C)                   Q6.2(C) R17.1 R18.2
   pin  11 VC             Net-(Q6-B)                   Q6.1(B) R16.2
   pin  12 V+             Net-(Q6-E)                   C8.1 Q6.3(E) R16.1 S1.3
   pin  13 FC             Net-(Z2-FC)                  C13.1
   pin  14 NC             unconnected-(Z2-NC-Pad14)    (no other connection)

Z3  (~, Address Decoder)
   pin   1                ~{ROMB}                      R68.1 Z3.6 Z34.20(~{CE1}) Z74.12 Z74.13
   pin   2                Net-(Z21-Q0a)                Z21.7(Q0a)
   pin   3                Net-(Z21-Q1a)                Z21.6(Q1a)
   pin   4                Net-(Z21-Q2a)                Z21.5(Q2a)
   pin   5                Net-(Z21-Q3a)                Z21.4(Q3a)
   pin   6                ~{ROMB}                      R68.1 Z3.1 Z34.20(~{CE1}) Z74.12 Z74.13
   pin   7                ~{ROMA}                      R61.1 Z3.8 Z33.20(~{OE}) Z74.9
   pin   8                ~{ROMA}                      R61.1 Z3.7 Z33.20(~{OE}) Z74.9
   pin   9                Net-(Z21-Q1b)                Z21.10(Q1b)
   pin  10                Net-(Z21-Q0b)                Z21.9(Q0b) Z3.16
   pin  11                Net-(Z21-Q2b)                Z21.11(Q2b)
   pin  12                ~{RAM}                       R62.1 Z3.13 Z3.14 Z3.15 Z71.12 Z71.4 Z74.10
   pin  13                ~{RAM}                       R62.1 Z3.12 Z3.14 Z3.15 Z71.12 Z71.4 Z74.10
   pin  14                ~{RAM}                       R62.1 Z3.12 Z3.13 Z3.15 Z71.12 Z71.4 Z74.10
   pin  15                ~{RAM}                       R62.1 Z3.12 Z3.13 Z3.14 Z71.12 Z71.4 Z74.10
   pin  16                Net-(Z21-Q0b)                Z21.9(Q0b) Z3.10

Z4  (LM3900, Cassette Interface)
   pin   1 +              Net-(Z4A-+)                  R25.1 R33.2
   pin   2 +              Net-(Z4B-+)                  R24.2
   pin   3 -              Net-(Z4B--)                  R34.1 R35.2
   pin   4                Net-(CR4-A)                  CR4.2(A) R34.2
   pin   5                Net-(CR5-A)                  CR5.2(A) R35.1 R36.2 R37.1
   pin   6 -              Net-(Z4A--)                  R37.2
   pin   7 V-             GND                          [net GND, 204 pins]
   pin   8 -              Net-(Z4C--)                  R41.2 R42.1
   pin   9                Net-(CR6-A)                  CR6.2(A) R38.1 R42.2
   pin  10                Net-(Z24-Pad9)               Z24.9
   pin  11 -              Net-(Z4D--)                  R45.2
   pin  12 +              Net-(Z4D-+)                  R38.2
   pin  13 +              Net-(Z4C-+)                  R26.2
   pin  14 V+             Net-(Z4E-V+)                 C6.2 R31.1

Z5  (74C00, Video Sync)
   pin   1                Net-(Z5-Pad1)                Z5.5 Z57.8
   pin   2                Net-(Z5-Pad13)               Z5.13 Z6.8
   pin   3                Net-(Z5-Pad12)               Z5.12 Z5.4
   pin   4                Net-(Z5-Pad12)               Z5.12 Z5.3
   pin   5                Net-(Z5-Pad1)                Z5.1 Z57.8
   pin   6                Net-(Z5-Pad6)                Z5.9
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                SYNC                         R29.1
   pin   9                Net-(Z5-Pad6)                Z5.6
   pin  10                Net-(Z5-Pad10)               Z5.11
   pin  11                Net-(Z5-Pad10)               Z5.10
   pin  12                Net-(Z5-Pad12)               Z5.3 Z5.4
   pin  13                Net-(Z5-Pad13)               Z5.2 Z6.8
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z6  (74C04, Video Sync)
   pin   1                Net-(Z6-Pad1)                Z6.12
   pin   2                Net-(R20-Pad1)               R20.1(1)
   pin   3                Net-(C20-Pad1)               C20.1 R20.2(2)
   pin   4                Net-(Z6-Pad4)                Z6.5
   pin   5                Net-(Z6-Pad4)                Z6.4
   pin   6                Net-(C20-Pad2)               C20.2 C21.1
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                Net-(Z5-Pad13)               Z5.13 Z5.2
   pin   9                Net-(Z6-Pad10)               Z6.10
   pin  10                Net-(Z6-Pad10)               Z6.9
   pin  11                Net-(C21-Pad2)               C21.2 R43.1
   pin  12                Net-(Z6-Pad1)                Z6.1
   pin  13                HDRV                         Z12.14(CP0) Z30.8 Z50.11(Q3) Z66.4
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z7  (74LS74, Video Latch)
   pin   1 ~{R}           Net-(Z7A-~{R})               R39.1
   pin   2 D              GND                          [net GND, 204 pins]
   pin   3 C              ~{LATCH}                     Z24.3 Z27.9(Cp) Z28.9(Cp) Z9.3
   pin   4 ~{S}           ~{VID}                       Z31.1(S) Z36.8 Z49.1(S) Z64.1(S)
   pin   5 Q              unconnected-(Z7A-Q-Pad5)     (no other connection)
   pin   6 ~{Q}           ~{VCLR}                      Z27.1(~{Mr}) Z28.1(~{Mr})
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8 ~{Q}           unconnected-(Z7B-~{Q}-Pad8)  (no other connection)
   pin   9 Q              unconnected-(Z7B-Q-Pad9)     (no other connection)
   pin  10 ~{S}           GND                          [net GND, 204 pins]
   pin  11 C              GND                          [net GND, 204 pins]
   pin  12 D              GND                          [net GND, 204 pins]
   pin  13 ~{R}           GND                          [net GND, 204 pins]
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z8  (74LS153, Video Generator)
   pin   1 Ea             GND                          [net GND, 204 pins]
   pin   2 S1             L3                           Z12.11(Q3) Z27.12(D2) Z65.14(CP0) Z66.11
   pin   3 I3a            unconnected-(Z8-I3a-Pad3)    (no other connection)
   pin   4 I2a            LB4                          Z28.5(Q1) Z29.3(A4)
   pin   5 I1a            LB2                          Z28.2(Q0) Z29.5(A2)
   pin   6 I0a            LB0                          Z28.15(Q5) Z29.7(A0)
   pin   7 Za             Net-(Z11-F)                  Z11.11(F) Z11.12(G) Z11.14(H)
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Zb             Net-(Z11-C)                  Z11.10(E) Z11.4(C) Z11.5(D)
   pin  10 I0b            LB1                          Z28.12(Q4) Z29.6(A1)
   pin  11 I1b            LB3                          Z28.7(Q2) Z29.4(A3)
   pin  12 I2b            LB5                          Z28.10(Q3) Z29.2(A5)
   pin  13 I3b            unconnected-(Z8-I3b-Pad13)   (no other connection)
   pin  14 S0             L2                           Z12.8(Q2) Z29.8(R2) Z66.10 Z66.9
   pin  15 Eb             GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z9  (74LS04, Video Generator)
   pin   1                GND                          [net GND, 204 pins]
   pin   2                unconnected-(Z9-Pad2)        (no other connection)
   pin   3                ~{LATCH}                     Z24.3 Z27.9(Cp) Z28.9(Cp) Z7.3(C)
   pin   4                Net-(Z26-Pad13)              Z26.13 Z26.5
   pin   5                GND                          [net GND, 204 pins]
   pin   6                unconnected-(Z9-Pad6)        (no other connection)
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                Net-(Z10-Clk)                Z10.7(Clk) Z11.7(Clk)
   pin   9                SHIFT                        Z43.4(Za) Z58.14(CP0)
   pin  10                unconnected-(Z9-Pad10)       (no other connection)
   pin  11                GND                          [net GND, 204 pins]
   pin  12                unconnected-(Z9-Pad12)       (no other connection)
   pin  13                GND                          [net GND, 204 pins]
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z10  (74LS166, Video Generator)
   pin   1 Ds             GND                          [net GND, 204 pins]
   pin   2 A              GND                          [net GND, 204 pins]
   pin   3 B              GND                          [net GND, 204 pins]
   pin   4 C              Net-(Z10-C)                  Z29.12(D0)
   pin   5 D              Net-(Z10-D)                  Z29.13(D1)
   pin   6 CE             GND                          [net GND, 204 pins]
   pin   7 Clk            Net-(Z10-Clk)                Z11.7(Clk) Z9.8
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Clr            Net-(Z10-Clr)                R40.1 Z11.9(Clr)
   pin  10 E              Net-(Z10-E)                  Z29.14(D2)
   pin  11 F              Net-(Z10-F)                  Z29.15(D3)
   pin  12 G              Net-(Z10-G)                  Z29.16(D4)
   pin  13 Qh             Net-(Z10-Qh)                 Z30.3
   pin  14 H              GND                          [net GND, 204 pins]
   pin  15 PE             Net-(Z10-PE)                 Z26.8
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z11  (74LS166, Video Generator)
   pin   1 Ds             GND                          [net GND, 204 pins]
   pin   2 A              GND                          [net GND, 204 pins]
   pin   3 B              GND                          [net GND, 204 pins]
   pin   4 C              Net-(Z11-C)                  Z11.10(E) Z11.5(D) Z8.9(Zb)
   pin   5 D              Net-(Z11-C)                  Z11.10(E) Z11.4(C) Z8.9(Zb)
   pin   6 CE             GND                          [net GND, 204 pins]
   pin   7 Clk            Net-(Z10-Clk)                Z10.7(Clk) Z9.8
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Clr            Net-(Z10-Clr)                R40.1 Z10.9(Clr)
   pin  10 E              Net-(Z11-C)                  Z11.4(C) Z11.5(D) Z8.9(Zb)
   pin  11 F              Net-(Z11-F)                  Z11.12(G) Z11.14(H) Z8.7(Za)
   pin  12 G              Net-(Z11-F)                  Z11.11(F) Z11.14(H) Z8.7(Za)
   pin  13 Qh             Net-(Z11-Qh)                 Z30.2
   pin  14 H              Net-(Z11-F)                  Z11.11(F) Z11.12(G) Z8.7(Za)
   pin  15 PE             Net-(Z11-PE)                 Z26.6
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z12  (74LS93, Video Counter)
   pin   1 CP1..3         L0                           Z12.12(Q0) Z29.11(R0)
   pin   2 R0(1)          Net-(Z12-R0(1))              Z12.3(R0(2)) Z66.8
   pin   3 R0(2)          Net-(Z12-R0(1))              Z12.2(R0(1)) Z66.8
   pin   5 VCC            +5V                          [net +5V, 134 pins]
   pin   8 Q2             L2                           Z29.8(R2) Z66.10 Z66.9 Z8.14(S0)
   pin   9 Q1             L1                           Z29.10(R1)
   pin  10 GND            GND                          [net GND, 204 pins]
   pin  11 Q3             L3                           Z27.12(D2) Z65.14(CP0) Z66.11 Z8.2(S1)
   pin  12 Q0             L0                           Z12.1(CP1..3) Z29.11(R0)
   pin  14 CP0            HDRV                         Z30.8 Z50.11(Q3) Z6.13 Z66.4

Z13  (4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 16 pins]
   pin   2 IN             D7                           J100.17(Pin_17) J4.20(Pin_20) Z44.11 Z60.3 Z63.11(IN) Z67.7 Z75.11 Z76.6
   pin   3 ~{WR}          ~{WR}                        J4.13(Pin_13) Z14.3(~{WR}) Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z22.5 Z49.14(I0d)
   pin   4 ~{RAS}         Net-(Z13-~{RAS})             R60.2 Z14.4(~{RAS}) Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z68.13
   pin   5 A0             Net-(Z13-A0)                 Z14.5(A0) Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z35.4(Za)
   pin   6 A2             Net-(Z13-A2)                 Z14.6(A2) Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z35.9(Zc)
   pin   7 A1             Net-(Z13-A1)                 Z14.7(A1) Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z35.7(Zb)
   pin   8 VDD            +12V                         [net +12V, 19 pins]
   pin   9 VCC            +5V                          [net +5V, 134 pins]
   pin  10 A5             Net-(Z13-A5)                 Z14.10(A5) Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z51.7(Zb)
   pin  11 A4             Net-(Z13-A4)                 Z14.11(A4) Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z51.4(Za)
   pin  12 A3             Net-(Z13-A3)                 Z14.12(A3) Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z35.12(Zd)
   pin  13 A6             Net-(Z13-A6)                 Z14.13(A6) Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z71.13 Z71.14
   pin  14 OUT            ROMD7                        Z33.17(D7) Z34.17(D7) Z67.6
   pin  15 ~{CAS}         Net-(Z13-~{CAS})             R57.2 Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z67.13
   pin  16 VSS            GND                          [net GND, 204 pins]

Z14  (4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 16 pins]
   pin   2 IN             D6                           J100.15(Pin_15) J4.24(Pin_24) Z44.13 Z55.10 Z60.5 Z67.5 Z75.9
   pin   3 ~{WR}          ~{WR}                        J4.13(Pin_13) Z13.3(~{WR}) Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z22.5 Z49.14(I0d)
   pin   4 ~{RAS}         Net-(Z13-~{RAS})             R60.2 Z13.4(~{RAS}) Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z68.13
   pin   5 A0             Net-(Z13-A0)                 Z13.5(A0) Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z35.4(Za)
   pin   6 A2             Net-(Z13-A2)                 Z13.6(A2) Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z35.9(Zc)
   pin   7 A1             Net-(Z13-A1)                 Z13.7(A1) Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z35.7(Zb)
   pin   8 VDD            +12V                         [net +12V, 19 pins]
   pin   9 VCC            +5V                          [net +5V, 134 pins]
   pin  10 A5             Net-(Z13-A5)                 Z13.10(A5) Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z51.7(Zb)
   pin  11 A4             Net-(Z13-A4)                 Z13.11(A4) Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z51.4(Za)
   pin  12 A3             Net-(Z13-A3)                 Z13.12(A3) Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z35.12(Zd)
   pin  13 A6             Net-(Z13-A6)                 Z13.13(A6) Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z71.13 Z71.14
   pin  14 OUT            ROMD6                        Z33.16(D6) Z34.16(D6) Z67.4
   pin  15 ~{CAS}         Net-(Z13-~{CAS})             R57.2 Z13.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z67.13
   pin  16 VSS            GND                          [net GND, 204 pins]

Z15  (4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 16 pins]
   pin   2 IN             D4                           J100.18(Pin_18) J4.18(Pin_18) Z55.2 Z60.9 Z61.11(IN) Z67.9 Z75.7
   pin   3 ~{WR}          ~{WR}                        J4.13(Pin_13) Z13.3(~{WR}) Z14.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z22.5 Z49.14(I0d)
   pin   4 ~{RAS}         Net-(Z13-~{RAS})             R60.2 Z13.4(~{RAS}) Z14.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z68.13
   pin   5 A0             Net-(Z13-A0)                 Z13.5(A0) Z14.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z35.4(Za)
   pin   6 A2             Net-(Z13-A2)                 Z13.6(A2) Z14.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z35.9(Zc)
   pin   7 A1             Net-(Z13-A1)                 Z13.7(A1) Z14.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z35.7(Zb)
   pin   8 VDD            +12V                         [net +12V, 19 pins]
   pin   9 VCC            +5V                          [net +5V, 134 pins]
   pin  10 A5             Net-(Z13-A5)                 Z13.10(A5) Z14.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z51.7(Zb)
   pin  11 A4             Net-(Z13-A4)                 Z13.11(A4) Z14.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z51.4(Za)
   pin  12 A3             Net-(Z13-A3)                 Z13.12(A3) Z14.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z35.12(Zd)
   pin  13 A6             Net-(Z13-A6)                 Z13.13(A6) Z14.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z71.13 Z71.14
   pin  14 OUT            ROMD4                        Z33.14(D4) Z34.14(D4) Z67.10
   pin  15 ~{CAS}         Net-(Z13-~{CAS})             R57.2 Z13.15(~{CAS}) Z14.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z67.13
   pin  16 VSS            GND                          [net GND, 204 pins]

Z16  (4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 16 pins]
   pin   2 IN             D1                           J100.16(Pin_16) J4.22(Pin_22) Z44.5 Z47.11(IN) Z59.5(D1) Z68.3 Z76.13 Z76.2
   pin   3 ~{WR}          ~{WR}                        J4.13(Pin_13) Z13.3(~{WR}) Z14.3(~{WR}) Z15.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z22.5 Z49.14(I0d)
   pin   4 ~{RAS}         Net-(Z13-~{RAS})             R60.2 Z13.4(~{RAS}) Z14.4(~{RAS}) Z15.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z68.13
   pin   5 A0             Net-(Z13-A0)                 Z13.5(A0) Z14.5(A0) Z15.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z35.4(Za)
   pin   6 A2             Net-(Z13-A2)                 Z13.6(A2) Z14.6(A2) Z15.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z35.9(Zc)
   pin   7 A1             Net-(Z13-A1)                 Z13.7(A1) Z14.7(A1) Z15.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z35.7(Zb)
   pin   8 VDD            +12V                         [net +12V, 19 pins]
   pin   9 VCC            +5V                          [net +5V, 134 pins]
   pin  10 A5             Net-(Z13-A5)                 Z13.10(A5) Z14.10(A5) Z15.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z51.7(Zb)
   pin  11 A4             Net-(Z13-A4)                 Z13.11(A4) Z14.11(A4) Z15.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z51.4(Za)
   pin  12 A3             Net-(Z13-A3)                 Z13.12(A3) Z14.12(A3) Z15.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z35.12(Zd)
   pin  13 A6             Net-(Z13-A6)                 Z13.13(A6) Z14.13(A6) Z15.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z71.13 Z71.14
   pin  14 OUT            ROMD1                        Z33.10(D1) Z34.10(D1) Z68.2
   pin  15 ~{CAS}         Net-(Z13-~{CAS})             R57.2 Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z67.13
   pin  16 VSS            GND                          [net GND, 204 pins]

Z17  (4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 16 pins]
   pin   2 IN             D0                           J100.11(Pin_11) J4.30(Pin_30) Z44.7 Z48.11(IN) Z59.4(D0) Z68.9 Z76.10 Z76.11
   pin   3 ~{WR}          ~{WR}                        J4.13(Pin_13) Z13.3(~{WR}) Z14.3(~{WR}) Z15.3(~{WR}) Z16.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z22.5 Z49.14(I0d)
   pin   4 ~{RAS}         Net-(Z13-~{RAS})             R60.2 Z13.4(~{RAS}) Z14.4(~{RAS}) Z15.4(~{RAS}) Z16.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z68.13
   pin   5 A0             Net-(Z13-A0)                 Z13.5(A0) Z14.5(A0) Z15.5(A0) Z16.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0) Z35.4(Za)
   pin   6 A2             Net-(Z13-A2)                 Z13.6(A2) Z14.6(A2) Z15.6(A2) Z16.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2) Z35.9(Zc)
   pin   7 A1             Net-(Z13-A1)                 Z13.7(A1) Z14.7(A1) Z15.7(A1) Z16.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1) Z35.7(Zb)
   pin   8 VDD            +12V                         [net +12V, 19 pins]
   pin   9 VCC            +5V                          [net +5V, 134 pins]
   pin  10 A5             Net-(Z13-A5)                 Z13.10(A5) Z14.10(A5) Z15.10(A5) Z16.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5) Z51.7(Zb)
   pin  11 A4             Net-(Z13-A4)                 Z13.11(A4) Z14.11(A4) Z15.11(A4) Z16.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4) Z51.4(Za)
   pin  12 A3             Net-(Z13-A3)                 Z13.12(A3) Z14.12(A3) Z15.12(A3) Z16.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3) Z35.12(Zd)
   pin  13 A6             Net-(Z13-A6)                 Z13.13(A6) Z14.13(A6) Z15.13(A6) Z16.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z71.13 Z71.14
   pin  14 OUT            ROMD0                        Z33.9(D0) Z34.9(D0) Z68.10
   pin  15 ~{CAS}         Net-(Z13-~{CAS})             R57.2 Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z67.13
   pin  16 VSS            GND                          [net GND, 204 pins]

Z18  (4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 16 pins]
   pin   2 IN             D2                           J100.10(Pin_10) J4.32(Pin_32) Z44.3 Z46.11(IN) Z59.12(D2) Z68.5 Z75.13 Z76.4
   pin   3 ~{WR}          ~{WR}                        J4.13(Pin_13) Z13.3(~{WR}) Z14.3(~{WR}) Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z22.5 Z49.14(I0d)
   pin   4 ~{RAS}         Net-(Z13-~{RAS})             R60.2 Z13.4(~{RAS}) Z14.4(~{RAS}) Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS}) Z68.13
   pin   5 A0             Net-(Z13-A0)                 Z13.5(A0) Z14.5(A0) Z15.5(A0) Z16.5(A0) Z17.5(A0) Z19.5(A0) Z20.5(A0) Z35.4(Za)
   pin   6 A2             Net-(Z13-A2)                 Z13.6(A2) Z14.6(A2) Z15.6(A2) Z16.6(A2) Z17.6(A2) Z19.6(A2) Z20.6(A2) Z35.9(Zc)
   pin   7 A1             Net-(Z13-A1)                 Z13.7(A1) Z14.7(A1) Z15.7(A1) Z16.7(A1) Z17.7(A1) Z19.7(A1) Z20.7(A1) Z35.7(Zb)
   pin   8 VDD            +12V                         [net +12V, 19 pins]
   pin   9 VCC            +5V                          [net +5V, 134 pins]
   pin  10 A5             Net-(Z13-A5)                 Z13.10(A5) Z14.10(A5) Z15.10(A5) Z16.10(A5) Z17.10(A5) Z19.10(A5) Z20.10(A5) Z51.7(Zb)
   pin  11 A4             Net-(Z13-A4)                 Z13.11(A4) Z14.11(A4) Z15.11(A4) Z16.11(A4) Z17.11(A4) Z19.11(A4) Z20.11(A4) Z51.4(Za)
   pin  12 A3             Net-(Z13-A3)                 Z13.12(A3) Z14.12(A3) Z15.12(A3) Z16.12(A3) Z17.12(A3) Z19.12(A3) Z20.12(A3) Z35.12(Zd)
   pin  13 A6             Net-(Z13-A6)                 Z13.13(A6) Z14.13(A6) Z15.13(A6) Z16.13(A6) Z17.13(A6) Z19.13(A6) Z20.13(A6) Z71.13 Z71.14
   pin  14 OUT            ROMD2                        Z33.11(D2) Z34.11(D2) Z68.4
   pin  15 ~{CAS}         Net-(Z13-~{CAS})             R57.2 Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS}) Z67.13
   pin  16 VSS            GND                          [net GND, 204 pins]

Z19  (4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 16 pins]
   pin   2 IN             D3                           J100.13(Pin_13) J4.26(Pin_26) Z44.9 Z45.11(IN) Z55.4 Z59.13(D3) Z68.7 Z75.5
   pin   3 ~{WR}          ~{WR}                        J4.13(Pin_13) Z13.3(~{WR}) Z14.3(~{WR}) Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z20.3(~{WR}) Z22.5 Z49.14(I0d)
   pin   4 ~{RAS}         Net-(Z13-~{RAS})             R60.2 Z13.4(~{RAS}) Z14.4(~{RAS}) Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z20.4(~{RAS}) Z68.13
   pin   5 A0             Net-(Z13-A0)                 Z13.5(A0) Z14.5(A0) Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z20.5(A0) Z35.4(Za)
   pin   6 A2             Net-(Z13-A2)                 Z13.6(A2) Z14.6(A2) Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z20.6(A2) Z35.9(Zc)
   pin   7 A1             Net-(Z13-A1)                 Z13.7(A1) Z14.7(A1) Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z20.7(A1) Z35.7(Zb)
   pin   8 VDD            +12V                         [net +12V, 19 pins]
   pin   9 VCC            +5V                          [net +5V, 134 pins]
   pin  10 A5             Net-(Z13-A5)                 Z13.10(A5) Z14.10(A5) Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z20.10(A5) Z51.7(Zb)
   pin  11 A4             Net-(Z13-A4)                 Z13.11(A4) Z14.11(A4) Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z20.11(A4) Z51.4(Za)
   pin  12 A3             Net-(Z13-A3)                 Z13.12(A3) Z14.12(A3) Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z20.12(A3) Z35.12(Zd)
   pin  13 A6             Net-(Z13-A6)                 Z13.13(A6) Z14.13(A6) Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z20.13(A6) Z71.13 Z71.14
   pin  14 OUT            ROMD3                        Z33.13(D3) Z34.13(D3) Z68.6
   pin  15 ~{CAS}         Net-(Z13-~{CAS})             R57.2 Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z20.15(~{CAS}) Z67.13
   pin  16 VSS            GND                          [net GND, 204 pins]

Z20  (4116, RAM)
   pin   1 VBB            -5V                          [net -5V, 16 pins]
   pin   2 IN             D5                           J100.12(Pin_12) J4.28(Pin_28) Z55.6 Z60.7 Z62.11(IN) Z67.3 Z75.3
   pin   3 ~{WR}          ~{WR}                        J4.13(Pin_13) Z13.3(~{WR}) Z14.3(~{WR}) Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z22.5 Z49.14(I0d)
   pin   4 ~{RAS}         Net-(Z13-~{RAS})             R60.2 Z13.4(~{RAS}) Z14.4(~{RAS}) Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z68.13
   pin   5 A0             Net-(Z13-A0)                 Z13.5(A0) Z14.5(A0) Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z35.4(Za)
   pin   6 A2             Net-(Z13-A2)                 Z13.6(A2) Z14.6(A2) Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z35.9(Zc)
   pin   7 A1             Net-(Z13-A1)                 Z13.7(A1) Z14.7(A1) Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z35.7(Zb)
   pin   8 VDD            +12V                         [net +12V, 19 pins]
   pin   9 VCC            +5V                          [net +5V, 134 pins]
   pin  10 A5             Net-(Z13-A5)                 Z13.10(A5) Z14.10(A5) Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z51.7(Zb)
   pin  11 A4             Net-(Z13-A4)                 Z13.11(A4) Z14.11(A4) Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z51.4(Za)
   pin  12 A3             Net-(Z13-A3)                 Z13.12(A3) Z14.12(A3) Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z35.12(Zd)
   pin  13 A6             Net-(Z13-A6)                 Z13.13(A6) Z14.13(A6) Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z71.13 Z71.14
   pin  14 OUT            ROMD5                        Z33.15(D5) Z34.15(D5) Z67.2
   pin  15 ~{CAS}         Net-(Z13-~{CAS})             R57.2 Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z67.13
   pin  16 VSS            GND                          [net GND, 204 pins]

Z21  (74LS156, Address Decoder)
   pin   1 Ea1            A14                          J4.10(Pin_10) Z21.15(Eb2) Z38.11
   pin   2 Ea2            Net-(Z21-Ea2)                Z21.14(Eb1) Z73.6
   pin   3 A1             A13                          J4.6(Pin_6) Z38.7 Z71.16
   pin   4 Q3a            Net-(Z21-Q3a)                Z3.5
   pin   5 Q2a            Net-(Z21-Q2a)                Z3.4
   pin   6 Q1a            Net-(Z21-Q1a)                Z3.3
   pin   7 Q0a            Net-(Z21-Q0a)                Z3.2
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Q0b            Net-(Z21-Q0b)                Z3.10 Z3.16
   pin  10 Q1b            Net-(Z21-Q1b)                Z3.9
   pin  11 Q2b            Net-(Z21-Q2b)                Z3.11
   pin  12 Q3b            Net-(Z21-Q3b)                R48.1 Z36.4
   pin  13 A0             A12                          J4.5(Pin_5) Z33.21(A12) Z34.21(~{CE2}) Z38.5 Z51.10(I1c)
   pin  14 Eb1            Net-(Z21-Ea2)                Z21.2(Ea2) Z73.6
   pin  15 Eb2            A14                          J4.10(Pin_10) Z21.1(Ea1) Z38.11
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z22  (74LS367, CPU Gating)
   pin   1                Net-(Z22-Pad1)               Z22.15 Z38.1 Z38.15 Z39.1 Z39.15 Z52.4 Z55.15 Z72.1
   pin   2                ~{ZOUT}                      Z23.3
   pin   3                ~{OUT}                       J4.12(Pin_12) Z25.9
   pin   4                ~{ZWR}                       Z23.11
   pin   5                ~{WR}                        J4.13(Pin_13) Z13.3(~{WR}) Z14.3(~{WR}) Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z49.14(I0d)
   pin   6                ~{ZRD}                       Z23.6
   pin   7                ~{RD}                        J4.15(Pin_15) Z49.5(I0b) Z52.13
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                ~{IN}                        J4.19(Pin_19) Z25.4
   pin  10                ~{ZIN}                       Z23.8
   pin  11                A2                           J100.6(Pin_6) J4.40(Pin_40) Z33.6(A2) Z34.6(A2) Z35.11(I0c) Z54.2 Z64.14(I0d)
   pin  12                ZA2                          Z40.32(A2)
   pin  13                A3                           J100.9(Pin_9) J4.34(Pin_34) Z33.5(A3) Z34.5(A3) Z35.14(I0d) Z54.1 Z64.5(I0b)
   pin  14                ZA3                          Z40.33(A3)
   pin  15                Net-(Z22-Pad1)               Z22.1 Z38.1 Z38.15 Z39.1 Z39.15 Z52.4 Z55.15 Z72.1
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z23  (74LS32, CPU)
   pin   1                Net-(Z40-~{WR})              Z23.13 Z40.22(~{WR}) Z74.2
   pin   2                Net-(Z40-~{IORQ})            Z23.10 Z40.20(~{IORQ}) Z73.1
   pin   3                ~{ZOUT}                      Z22.2
   pin   4                ~{ZRAS}                      Z23.12 Z40.19(~{MREQ}) Z72.4
   pin   5                Net-(Z40-~{RD})              Z23.9 Z40.21(~{RD}) Z53.5 Z74.1
   pin   6                ~{ZRD}                       Z22.6
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                ~{ZIN}                       Z22.10
   pin   9                Net-(Z40-~{RD})              Z23.5 Z40.21(~{RD}) Z53.5 Z74.1
   pin  10                Net-(Z40-~{IORQ})            Z23.2 Z40.20(~{IORQ}) Z73.1
   pin  11                ~{ZWR}                       Z22.4
   pin  12                ~{ZRAS}                      Z23.4 Z40.19(~{MREQ}) Z72.4
   pin  13                Net-(Z40-~{WR})              Z23.1 Z40.22(~{WR}) Z74.2
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z24  (74LS132, Cassette Interface)
   pin   1                Net-(Z58-CP1..3)             Z58.1(CP1..3) Z58.12(Q0)
   pin   2                Net-(Z43-I0c)                Z43.11(I0c) Z58.9(Q2)
   pin   3                ~{LATCH}                     Z27.9(Cp) Z28.9(Cp) Z7.3(C) Z9.3
   pin   4                GND                          [net GND, 204 pins]
   pin   5                GND                          [net GND, 204 pins]
   pin   6                unconnected-(Z24-Pad6)       (no other connection)
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                Net-(Z24-Pad12)              Z24.12 Z44.12
   pin   9                Net-(Z24-Pad9)               Z4.10
   pin  10                Net-(Z24-Pad10)              Z24.11
   pin  11                Net-(Z24-Pad10)              Z24.10
   pin  12                Net-(Z24-Pad12)              Z24.8 Z44.12
   pin  13                ~{OUTSIG}                    Z25.8 Z59.9(Cp)
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z25  (74LS32, Cassette Interface)
   pin   1                GND                          [net GND, 204 pins]
   pin   2                GND                          [net GND, 204 pins]
   pin   3                unconnected-(Z25-Pad3)       (no other connection)
   pin   4                ~{IN}                        J4.19(Pin_19) Z22.9
   pin   5                Net-(Z25-Pad10)              Z25.10 Z36.3
   pin   6                ~{INSIG}                     Z44.15
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                ~{OUTSIG}                    Z24.13 Z59.9(Cp)
   pin   9                ~{OUT}                       J4.12(Pin_12) Z22.3
   pin  10                Net-(Z25-Pad10)              Z25.5 Z36.3
   pin  11                unconnected-(Z25-Pad11)      (no other connection)
   pin  12                GND                          [net GND, 204 pins]
   pin  13                GND                          [net GND, 204 pins]
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z26  (74LS20, Video Generator)
   pin   1                ~{BLANK}                     Z26.2 Z26.9 Z27.7(Q1)
   pin   2                ~{BLANK}                     Z26.1 Z26.9 Z27.7(Q1)
   pin   4                GRAPHICS                     Z27.3(~{Q0})
   pin   5                Net-(Z26-Pad13)              Z26.13 Z9.4
   pin   6                Net-(Z11-PE)                 Z11.15(PE)
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                Net-(Z10-PE)                 Z10.15(PE)
   pin   9                ~{BLANK}                     Z26.1 Z26.2 Z27.7(Q1)
   pin  10                ~{GRAPHICS}                  Z27.2(Q0)
   pin  12                ~{CHARGAP}                   Z27.11(~{Q2})
   pin  13                Net-(Z26-Pad13)              Z26.5 Z9.4
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z27  (74LS175, Video Latch)
   pin   1 ~{Mr}          ~{VCLR}                      Z28.1(~{Mr}) Z7.6(~{Q})
   pin   2 Q0             ~{GRAPHICS}                  Z26.10
   pin   3 ~{Q0}          GRAPHICS                     Z26.4
   pin   4 D0             Net-(Z27-D0)                 Z42.12
   pin   5 D1             Net-(Z27-D1)                 Z30.10
   pin   6 ~{Q1}          unconnected-(Z27-~{Q1}-Pad6) (no other connection)
   pin   7 Q1             ~{BLANK}                     Z26.1 Z26.2 Z26.9
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Cp             ~{LATCH}                     Z24.3 Z28.9(Cp) Z7.3(C) Z9.3
   pin  10 Q2             unconnected-(Z27-Q2-Pad10)   (no other connection)
   pin  11 ~{Q2}          ~{CHARGAP}                   Z26.12
   pin  12 D2             L3                           Z12.11(Q3) Z65.14(CP0) Z66.11 Z8.2(S1)
   pin  13 D3             VD6                          Z30.13 Z60.4
   pin  14 ~{Q3}          unconnected-(Z27-~{Q3}-Pad14) (no other connection)
   pin  15 Q3             LB6                          Z29.1(A6)
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z28  (74LS174, Video Latch)
   pin   1 ~{Mr}          ~{VCLR}                      Z27.1(~{Mr}) Z7.6(~{Q})
   pin   2 Q0             LB2                          Z29.5(A2) Z8.5(I1a)
   pin   3 D0             VD2                          Z44.2 Z46.12(OUT)
   pin   4 D1             VD4                          Z60.10 Z61.12(OUT)
   pin   5 Q1             LB4                          Z29.3(A4) Z8.4(I2a)
   pin   6 D2             VD3                          Z44.10 Z45.12(OUT)
   pin   7 Q2             LB3                          Z29.4(A3) Z8.11(I1b)
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Cp             ~{LATCH}                     Z24.3 Z27.9(Cp) Z7.3(C) Z9.3
   pin  10 Q3             LB5                          Z29.2(A5) Z8.12(I2b)
   pin  11 D3             VD5                          Z30.12 Z60.6 Z62.12(OUT)
   pin  12 Q4             LB1                          Z29.6(A1) Z8.10(I0b)
   pin  13 D4             VD1                          Z44.4 Z47.12(OUT)
   pin  14 D5             VD0                          Z44.6 Z48.12(OUT)
   pin  15 Q5             LB0                          Z29.7(A0) Z8.6(I0a)
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z29  (MCM6670, Video Generator)
   pin   1 A6             LB6                          Z27.15(Q3)
   pin   2 A5             LB5                          Z28.10(Q3) Z8.12(I2b)
   pin   3 A4             LB4                          Z28.5(Q1) Z8.4(I2a)
   pin   4 A3             LB3                          Z28.7(Q2) Z8.11(I1b)
   pin   5 A2             LB2                          Z28.2(Q0) Z8.5(I1a)
   pin   6 A1             LB1                          Z28.12(Q4) Z8.10(I0b)
   pin   7 A0             LB0                          Z28.15(Q5) Z8.6(I0a)
   pin   8 R2             L2                           Z12.8(Q2) Z66.10 Z66.9 Z8.14(S0)
   pin   9 GND            GND                          [net GND, 204 pins]
   pin  10 R1             L1                           Z12.9(Q1)
   pin  11 R0             L0                           Z12.1(CP1..3) Z12.12(Q0)
   pin  12 D0             Net-(Z10-C)                  Z10.4(C)
   pin  13 D1             Net-(Z10-D)                  Z10.5(D)
   pin  14 D2             Net-(Z10-E)                  Z10.10(E)
   pin  15 D3             Net-(Z10-F)                  Z10.11(F)
   pin  16 D4             Net-(Z10-G)                  Z10.12(G)
   pin  17 ~{CS}          GND                          [net GND, 204 pins]
   pin  18 VCC            +5V                          [net +5V, 134 pins]

Z30  (74LS02, Video RAM)
   pin   1                PIXEL                        Z41.6(2A) Z41.7(2B)
   pin   2                Net-(Z11-Qh)                 Z11.13(Qh)
   pin   3                Net-(Z10-Qh)                 Z10.13(Qh)
   pin   4                unconnected-(Z30-Pad4)       (no other connection)
   pin   5                GND                          [net GND, 204 pins]
   pin   6                GND                          [net GND, 204 pins]
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                HDRV                         Z12.14(CP0) Z50.11(Q3) Z6.13 Z66.4
   pin   9                VDRV                         Z32.11(Q3) Z57.1 Z66.1
   pin  10                Net-(Z27-D1)                 Z27.5(D1)
   pin  11                VD7                          Z42.13 Z60.2 Z63.12(OUT)
   pin  12                VD5                          Z28.11(D3) Z60.6 Z62.12(OUT)
   pin  13                VD6                          Z27.13(D3) Z60.4
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z31  (74LS157, Video Access Multiplexer)
   pin   1 S              ~{VID}                       Z36.8 Z49.1(S) Z64.1(S) Z7.4(~{S})
   pin   2 I0a            A8                           J4.11(Pin_11) Z33.23(A8) Z34.23(A8) Z35.10(I1c) Z39.3
   pin   3 I1a            R2                           Z32.9(Q1) Z66.2
   pin   4 Za             VA8                          Z45.15(A8) Z46.15(A8) Z47.15(A8) Z48.15(A8) Z61.15(A8) Z62.15(A8) Z63.15(A8)
   pin   5 I0b            A9                           J4.17(Pin_17) Z33.22(A9) Z34.22(A9) Z35.13(I1d) Z39.13
   pin   6 I1b            R3                           Z32.8(Q2)
   pin   7 Zb             VA9                          Z45.14(A9) Z46.14(A9) Z47.14(A9) Z48.14(A9) Z61.14(A9) Z62.14(A9) Z63.14(A9)
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Zc             VA6                          Z45.1(A6) Z46.1(A6) Z47.1(A6) Z48.1(A6) Z61.1(A6) Z62.1(A6) Z63.1(A6)
   pin  10 I1c            R0                           Z32.14(CP0) Z65.12(Q0)
   pin  11 I0c            A6                           J100.7(Pin_7) J4.38(Pin_38) Z33.2(A6) Z34.2(A6) Z39.5 Z51.11(I0c) Z54.3 Z71.15
   pin  12 Zd             VA7                          Z45.16(A7) Z46.16(A7) Z47.16(A7) Z48.16(A7) Z61.16(A7) Z62.16(A7) Z63.16(A7)
   pin  13 I1d            R1                           Z32.1(CP1..3) Z32.12(Q0) Z66.13
   pin  14 I0d            A7                           J100.8(Pin_8) J4.36(Pin_36) Z33.1(A7) Z34.1(A7) Z35.6(I1b) Z39.11 Z54.5 Z54.6
   pin  15 E              GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z32  (74LS93, Video Counter)
   pin   1 CP1..3         R1                           Z31.13(I1d) Z32.12(Q0) Z66.13
   pin   2 R0(1)          Net-(Z32-R0(1))              Z32.3(R0(2)) Z66.12
   pin   3 R0(2)          Net-(Z32-R0(1))              Z32.2(R0(1)) Z66.12
   pin   5 VCC            +5V                          [net +5V, 134 pins]
   pin   8 Q2             R3                           Z31.6(I1b)
   pin   9 Q1             R2                           Z31.3(I1a) Z66.2
   pin  10 GND            GND                          [net GND, 204 pins]
   pin  11 Q3             VDRV                         Z30.9 Z57.1 Z66.1
   pin  12 Q0             R1                           Z31.13(I1d) Z32.1(CP1..3) Z66.13
   pin  14 CP0            R0                           Z31.10(I1c) Z65.12(Q0)

Z33  (2364_20L, ROM)
   pin   1 A7             A7                           J100.8(Pin_8) J4.36(Pin_36) Z31.14(I0d) Z34.1(A7) Z35.6(I1b) Z39.11 Z54.5 Z54.6
   pin   2 A6             A6                           J100.7(Pin_7) J4.38(Pin_38) Z31.11(I0c) Z34.2(A6) Z39.5 Z51.11(I0c) Z54.3 Z71.15
   pin   3 A5             A5                           J100.3(Pin_3) J4.35(Pin_35) Z34.3(A5) Z39.9 Z49.2(I0a) Z51.5(I0b) Z54.12
   pin   4 A4             A4                           J100.2(Pin_2) J4.31(Pin_31) Z34.4(A4) Z39.7 Z49.11(I0c) Z51.2(I0a) Z54.4
   pin   5 A3             A3                           J100.9(Pin_9) J4.34(Pin_34) Z22.13 Z34.5(A3) Z35.14(I0d) Z54.1 Z64.5(I0b)
   pin   6 A2             A2                           J100.6(Pin_6) J4.40(Pin_40) Z22.11 Z34.6(A2) Z35.11(I0c) Z54.2 Z64.14(I0d)
   pin   7 A1             A1                           J100.4(Pin_4) J4.27(Pin_27) Z34.7(A1) Z35.5(I0b) Z54.11 Z55.13 Z64.2(I0a)
   pin   8 A0             A0                           J100.5(Pin_5) J4.25(Pin_25) Z34.8(A0) Z35.2(I0a) Z52.5 Z55.11 Z64.11(I0c)
   pin   9 D0             ROMD0                        Z17.14(OUT) Z34.9(D0) Z68.10
   pin  10 D1             ROMD1                        Z16.14(OUT) Z34.10(D1) Z68.2
   pin  11 D2             ROMD2                        Z18.14(OUT) Z34.11(D2) Z68.4
   pin  12 GND            GND                          [net GND, 204 pins]
   pin  13 D3             ROMD3                        Z19.14(OUT) Z34.13(D3) Z68.6
   pin  14 D4             ROMD4                        Z15.14(OUT) Z34.14(D4) Z67.10
   pin  15 D5             ROMD5                        Z20.14(OUT) Z34.15(D5) Z67.2
   pin  16 D6             ROMD6                        Z14.14(OUT) Z34.16(D6) Z67.4
   pin  17 D7             ROMD7                        Z13.14(OUT) Z34.17(D7) Z67.6
   pin  18 A11            A11                          J4.9(Pin_9) Z34.18(A11) Z37.5 Z37.6 Z38.13 Z51.6(I1b)
   pin  19 A10            A10                          J4.4(Pin_4) Z34.19(A10) Z36.13 Z38.3 Z51.3(I1a) Z52.1
   pin  20 ~{OE}          ~{ROMA}                      R61.1 Z3.7 Z3.8 Z74.9
   pin  21 A12            A12                          J4.5(Pin_5) Z21.13(A0) Z34.21(~{CE2}) Z38.5 Z51.10(I1c)
   pin  22 A9             A9                           J4.17(Pin_17) Z31.5(I0b) Z34.22(A9) Z35.13(I1d) Z39.13
   pin  23 A8             A8                           J4.11(Pin_11) Z31.2(I0a) Z34.23(A8) Z35.10(I1c) Z39.3
   pin  24 VCC            +5V                          [net +5V, 134 pins]

Z34  (2332_20L_21L, ROM)
   pin   1 A7             A7                           J100.8(Pin_8) J4.36(Pin_36) Z31.14(I0d) Z33.1(A7) Z35.6(I1b) Z39.11 Z54.5 Z54.6
   pin   2 A6             A6                           J100.7(Pin_7) J4.38(Pin_38) Z31.11(I0c) Z33.2(A6) Z39.5 Z51.11(I0c) Z54.3 Z71.15
   pin   3 A5             A5                           J100.3(Pin_3) J4.35(Pin_35) Z33.3(A5) Z39.9 Z49.2(I0a) Z51.5(I0b) Z54.12
   pin   4 A4             A4                           J100.2(Pin_2) J4.31(Pin_31) Z33.4(A4) Z39.7 Z49.11(I0c) Z51.2(I0a) Z54.4
   pin   5 A3             A3                           J100.9(Pin_9) J4.34(Pin_34) Z22.13 Z33.5(A3) Z35.14(I0d) Z54.1 Z64.5(I0b)
   pin   6 A2             A2                           J100.6(Pin_6) J4.40(Pin_40) Z22.11 Z33.6(A2) Z35.11(I0c) Z54.2 Z64.14(I0d)
   pin   7 A1             A1                           J100.4(Pin_4) J4.27(Pin_27) Z33.7(A1) Z35.5(I0b) Z54.11 Z55.13 Z64.2(I0a)
   pin   8 A0             A0                           J100.5(Pin_5) J4.25(Pin_25) Z33.8(A0) Z35.2(I0a) Z52.5 Z55.11 Z64.11(I0c)
   pin   9 D0             ROMD0                        Z17.14(OUT) Z33.9(D0) Z68.10
   pin  10 D1             ROMD1                        Z16.14(OUT) Z33.10(D1) Z68.2
   pin  11 D2             ROMD2                        Z18.14(OUT) Z33.11(D2) Z68.4
   pin  12 GND            GND                          [net GND, 204 pins]
   pin  13 D3             ROMD3                        Z19.14(OUT) Z33.13(D3) Z68.6
   pin  14 D4             ROMD4                        Z15.14(OUT) Z33.14(D4) Z67.10
   pin  15 D5             ROMD5                        Z20.14(OUT) Z33.15(D5) Z67.2
   pin  16 D6             ROMD6                        Z14.14(OUT) Z33.16(D6) Z67.4
   pin  17 D7             ROMD7                        Z13.14(OUT) Z33.17(D7) Z67.6
   pin  18 A11            A11                          J4.9(Pin_9) Z33.18(A11) Z37.5 Z37.6 Z38.13 Z51.6(I1b)
   pin  19 A10            A10                          J4.4(Pin_4) Z33.19(A10) Z36.13 Z38.3 Z51.3(I1a) Z52.1
   pin  20 ~{CE1}         ~{ROMB}                      R68.1 Z3.1 Z3.6 Z74.12 Z74.13
   pin  21 ~{CE2}         A12                          J4.5(Pin_5) Z21.13(A0) Z33.21(A12) Z38.5 Z51.10(I1c)
   pin  22 A9             A9                           J4.17(Pin_17) Z31.5(I0b) Z33.22(A9) Z35.13(I1d) Z39.13
   pin  23 A8             A8                           J4.11(Pin_11) Z31.2(I0a) Z33.23(A8) Z35.10(I1c) Z39.3
   pin  24 VCC            +5V                          [net +5V, 134 pins]

Z35  (74LS157, RAM)
   pin   1 S              MUX                          J4.16(Pin_16) Z51.1(S) Z72.3
   pin   2 I0a            A0                           J100.5(Pin_5) J4.25(Pin_25) Z33.8(A0) Z34.8(A0) Z52.5 Z55.11 Z64.11(I0c)
   pin   3 I1a            Net-(Z35-I1a)                Z71.1 Z71.2 Z71.7 Z71.8
   pin   4 Za             Net-(Z13-A0)                 Z13.5(A0) Z14.5(A0) Z15.5(A0) Z16.5(A0) Z17.5(A0) Z18.5(A0) Z19.5(A0) Z20.5(A0)
   pin   5 I0b            A1                           J100.4(Pin_4) J4.27(Pin_27) Z33.7(A1) Z34.7(A1) Z54.11 Z55.13 Z64.2(I0a)
   pin   6 I1b            A7                           J100.8(Pin_8) J4.36(Pin_36) Z31.14(I0d) Z33.1(A7) Z34.1(A7) Z39.11 Z54.5 Z54.6
   pin   7 Zb             Net-(Z13-A1)                 Z13.7(A1) Z14.7(A1) Z15.7(A1) Z16.7(A1) Z17.7(A1) Z18.7(A1) Z19.7(A1) Z20.7(A1)
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Zc             Net-(Z13-A2)                 Z13.6(A2) Z14.6(A2) Z15.6(A2) Z16.6(A2) Z17.6(A2) Z18.6(A2) Z19.6(A2) Z20.6(A2)
   pin  10 I1c            A8                           J4.11(Pin_11) Z31.2(I0a) Z33.23(A8) Z34.23(A8) Z39.3
   pin  11 I0c            A2                           J100.6(Pin_6) J4.40(Pin_40) Z22.11 Z33.6(A2) Z34.6(A2) Z54.2 Z64.14(I0d)
   pin  12 Zd             Net-(Z13-A3)                 Z13.12(A3) Z14.12(A3) Z15.12(A3) Z16.12(A3) Z17.12(A3) Z18.12(A3) Z19.12(A3) Z20.12(A3)
   pin  13 I1d            A9                           J4.17(Pin_17) Z31.5(I0b) Z33.22(A9) Z34.22(A9) Z39.13
   pin  14 I0d            A3                           J100.9(Pin_9) J4.34(Pin_34) Z22.13 Z33.5(A3) Z34.5(A3) Z54.1 Z64.5(I0b)
   pin  15 E              GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z36  (74LS32, Address Decoder)
   pin   1                Net-(Z36-Pad1)               Z52.6
   pin   2                Net-(Z36-Pad2)               Z54.8
   pin   3                Net-(Z25-Pad10)              Z25.10 Z25.5
   pin   4                Net-(Z21-Q3b)                R48.1 Z21.12(Q3b)
   pin   5                Net-(Z36-Pad5)               Z37.4
   pin   6                Net-(Z36-Pad10)              Z36.10 Z36.12
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                ~{VID}                       Z31.1(S) Z49.1(S) Z64.1(S) Z7.4(~{S})
   pin   9                Net-(Z36-Pad9)               Z52.2
   pin  10                Net-(Z36-Pad10)              Z36.12 Z36.6
   pin  11                ~{KYBD}                      J100.14(Pin_14)
   pin  12                Net-(Z36-Pad10)              Z36.10 Z36.6
   pin  13                A10                          J4.4(Pin_4) Z33.19(A10) Z34.19(A10) Z38.3 Z51.3(I1a) Z52.1
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z37  (74LS02, CPU)
   pin   1                ~{SYSRES}                    J4.2(Pin_2)
   pin   2                Net-(Z37-Pad2)               Z52.11 Z53.11
   pin   3                Net-(Z37-Pad11)              Z37.11 Z37.12 Z53.3
   pin   4                Net-(Z36-Pad5)               Z36.5
   pin   5                A11                          J4.9(Pin_9) Z33.18(A11) Z34.18(A11) Z37.6 Z38.13 Z51.6(I1b)
   pin   6                A11                          J4.9(Pin_9) Z33.18(A11) Z34.18(A11) Z37.5 Z38.13 Z51.6(I1b)
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                GND                          [net GND, 204 pins]
   pin   9                GND                          [net GND, 204 pins]
   pin  10                unconnected-(Z37-Pad10)      (no other connection)
   pin  11                Net-(Z37-Pad11)              Z37.12 Z37.3 Z53.3
   pin  12                Net-(Z37-Pad11)              Z37.11 Z37.3 Z53.3
   pin  13                Net-(Z40-~{NMI})             Z40.17(~{NMI})
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z38  (74LS367, CPU Gating)
   pin   1                Net-(Z22-Pad1)               Z22.1 Z22.15 Z38.15 Z39.1 Z39.15 Z52.4 Z55.15 Z72.1
   pin   2                ZA10                         Z40.40(A10)
   pin   3                A10                          J4.4(Pin_4) Z33.19(A10) Z34.19(A10) Z36.13 Z51.3(I1a) Z52.1
   pin   4                ZA12                         Z40.2(A12)
   pin   5                A12                          J4.5(Pin_5) Z21.13(A0) Z33.21(A12) Z34.21(~{CE2}) Z51.10(I1c)
   pin   6                ZA13                         Z40.3(A13)
   pin   7                A13                          J4.6(Pin_6) Z21.3(A1) Z71.16
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                A15                          J4.7(Pin_7) Z73.4
   pin  10                ZA15                         Z40.5(A15)
   pin  11                A14                          J4.10(Pin_10) Z21.1(Ea1) Z21.15(Eb2)
   pin  12                ZA14                         Z40.4(A14)
   pin  13                A11                          J4.9(Pin_9) Z33.18(A11) Z34.18(A11) Z37.5 Z37.6 Z51.6(I1b)
   pin  14                ZA11                         Z40.1(A11)
   pin  15                Net-(Z22-Pad1)               Z22.1 Z22.15 Z38.1 Z39.1 Z39.15 Z52.4 Z55.15 Z72.1
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z39  (74LS367, CPU Gating)
   pin   1                Net-(Z22-Pad1)               Z22.1 Z22.15 Z38.1 Z38.15 Z39.15 Z52.4 Z55.15 Z72.1
   pin   2                ZA8                          Z40.38(A8)
   pin   3                A8                           J4.11(Pin_11) Z31.2(I0a) Z33.23(A8) Z34.23(A8) Z35.10(I1c)
   pin   4                ZA6                          Z40.36(A6)
   pin   5                A6                           J100.7(Pin_7) J4.38(Pin_38) Z31.11(I0c) Z33.2(A6) Z34.2(A6) Z51.11(I0c) Z54.3 Z71.15
   pin   6                ZA4                          Z40.34(A4)
   pin   7                A4                           J100.2(Pin_2) J4.31(Pin_31) Z33.4(A4) Z34.4(A4) Z49.11(I0c) Z51.2(I0a) Z54.4
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                A5                           J100.3(Pin_3) J4.35(Pin_35) Z33.3(A5) Z34.3(A5) Z49.2(I0a) Z51.5(I0b) Z54.12
   pin  10                ZA5                          Z40.35(A5)
   pin  11                A7                           J100.8(Pin_8) J4.36(Pin_36) Z31.14(I0d) Z33.1(A7) Z34.1(A7) Z35.6(I1b) Z54.5 Z54.6
   pin  12                ZA7                          Z40.37(A7)
   pin  13                A9                           J4.17(Pin_17) Z31.5(I0b) Z33.22(A9) Z34.22(A9) Z35.13(I1d)
   pin  14                ZA9                          Z40.39(A9)
   pin  15                Net-(Z22-Pad1)               Z22.1 Z22.15 Z38.1 Z38.15 Z39.1 Z52.4 Z55.15 Z72.1
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z40  (Z80CPU, CPU)
   pin   1 A11            ZA11                         Z38.14
   pin   2 A12            ZA12                         Z38.4
   pin   3 A13            ZA13                         Z38.6
   pin   4 A14            ZA14                         Z38.12
   pin   5 A15            ZA15                         Z38.10
   pin   6 ~{CLK}         ZCLK                         R64.2 Z72.11
   pin   7 D4             ZD4                          Z55.3 Z75.6
   pin   8 D3             ZD3                          Z55.5 Z75.4
   pin   9 D5             ZD5                          Z55.7 Z75.2
   pin  10 D6             ZD6                          Z55.9 Z75.10
   pin  11 VCC            +5V                          [net +5V, 134 pins]
   pin  12 D2             ZD2                          Z75.14 Z76.5
   pin  13 D7             ZD7                          Z75.12 Z76.7
   pin  14 D0             ZD0                          Z76.12 Z76.9
   pin  15 D1             ZD1                          Z76.14 Z76.3
   pin  16 ~{INT}         ~{INT}                       J4.21(Pin_21) R50.2
   pin  17 ~{NMI}         Net-(Z40-~{NMI})             Z37.13
   pin  18 ~{HALT}        Net-(Z40-~{HALT})            Z53.2
   pin  19 ~{MREQ}        ~{ZRAS}                      Z23.12 Z23.4 Z72.4
   pin  20 ~{IORQ}        Net-(Z40-~{IORQ})            Z23.10 Z23.2 Z73.1
   pin  21 ~{RD}          Net-(Z40-~{RD})              Z23.5 Z23.9 Z53.5 Z74.1
   pin  22 ~{WR}          Net-(Z40-~{WR})              Z23.1 Z23.13 Z74.2
   pin  23 ~{BUSACK}      unconnected-(Z40-~{BUSACK}-Pad23) (no other connection)
   pin  24 ~{WAIT}        ~{WAIT}                      J4.33(Pin_33) R51.2
   pin  25 ~{BUSRQ}       ~{TEST}                      J4.23(Pin_23) R58.2 Z52.3 Z53.4
   pin  26 ~{RESET}       Net-(Z40-~{RESET})           Z52.10
   pin  27 ~{M1}          Net-(Z40-~{M1})              Z73.2
   pin  28 ~{RFSH}        unconnected-(Z40-~{RFSH}-Pad28) (no other connection)
   pin  29 GND            GND                          [net GND, 204 pins]
   pin  30 A0             ZA0                          Z55.12
   pin  31 A1             ZA1                          Z55.14
   pin  32 A2             ZA2                          Z22.12
   pin  33 A3             ZA3                          Z22.14
   pin  34 A4             ZA4                          Z39.6
   pin  35 A5             ZA5                          Z39.10
   pin  36 A6             ZA6                          Z39.4
   pin  37 A7             ZA7                          Z39.12
   pin  38 A8             ZA8                          Z39.2
   pin  39 A9             ZA9                          Z39.14
   pin  40 A10            ZA10                         Z38.2

Z41  (75452, Cassette Interface)
   pin   1 1A             Net-(Z41A-1A)                Z41.2(1B) Z59.10(Q2)
   pin   2 1B             Net-(Z41A-1A)                Z41.1(1A) Z59.10(Q2)
   pin   3 1Y             Net-(CR3-A)                  CR3.2(A) K1.2
   pin   4 GND            GND                          [net GND, 204 pins]
   pin   5 2Y             Net-(Z41B-2Y)                R23.2
   pin   6 2A             PIXEL                        Z30.1 Z41.7(2B)
   pin   7 2B             PIXEL                        Z30.1 Z41.6(2A)
   pin   8 VCC            +5V                          [net +5V, 134 pins]

Z42  (74LS04, )
   pin   1                Net-(C43-Pad1)               C43.1 R46.1
   pin   2                Net-(R46-Pad2)               R46.2 Y1.1(1)
   pin   3                Net-(R52-Pad1)               R52.1 Y1.2(2)
   pin   4                Net-(C43-Pad2)               C43.2 R52.2 Z42.5
   pin   5                Net-(C43-Pad2)               C43.2 R52.2 Z42.4
   pin   6                CLK                          Z43.3(I1a) Z56.1(CP1..3) Z69.11(C) Z69.3(C) Z70.11(C) Z70.3(C)
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                ~{CLK_EN}                    Z56.6(R0(1)) Z56.7(R0(2)) Z58.6(R0(1)) Z58.7(R0(2))
   pin   9                Net-(R67-Pad2)               R67.2
   pin  10                unconnected-(Z42-Pad10)      (no other connection)
   pin  11                GND                          [net GND, 204 pins]
   pin  12                Net-(Z27-D0)                 Z27.4(D0)
   pin  13                VD7                          Z30.11 Z60.2 Z63.12(OUT)
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z43  (74LS157, Video Counter)
   pin   1 S              MODESEL                      Z44.14 Z59.14(~{Q3})
   pin   2 I0a            Net-(Z43-I0a)                Z70.9(Q)
   pin   3 I1a            CLK                          Z42.6 Z56.1(CP1..3) Z69.11(C) Z69.3(C) Z70.11(C) Z70.3(C)
   pin   4 Za             SHIFT                        Z58.14(CP0) Z9.9
   pin   5 I0b            GND                          [net GND, 204 pins]
   pin   6 I1b            Net-(Z43-I1b)                Z43.10(I1c) Z58.8(Q3)
   pin   7 Zb             C0                           Z64.10(I1c)
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Zc             Net-(Z43-Zc)                 Z65.1(CP1..3)
   pin  10 I1c            Net-(Z43-I1b)                Z43.6(I1b) Z58.8(Q3)
   pin  11 I0c            Net-(Z43-I0c)                Z24.2 Z58.9(Q2)
   pin  12 Zd             unconnected-(Z43-Zd-Pad12)   (no other connection)
   pin  13 I1d            unconnected-(Z43-I1d-Pad13)  (no other connection)
   pin  14 I0d            unconnected-(Z43-I0d-Pad14)  (no other connection)
   pin  15 E              GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z44  (74LS367, Cassette Interface)
   pin   1                ~{VRD}                       Z49.7(Zb) Z60.1
   pin   2                VD2                          Z28.3(D0) Z46.12(OUT)
   pin   3                D2                           J100.10(Pin_10) J4.32(Pin_32) Z18.2(IN) Z46.11(IN) Z59.12(D2) Z68.5 Z75.13 Z76.4
   pin   4                VD1                          Z28.13(D4) Z47.12(OUT)
   pin   5                D1                           J100.16(Pin_16) J4.22(Pin_22) Z16.2(IN) Z47.11(IN) Z59.5(D1) Z68.3 Z76.13 Z76.2
   pin   6                VD0                          Z28.14(D5) Z48.12(OUT)
   pin   7                D0                           J100.11(Pin_11) J4.30(Pin_30) Z17.2(IN) Z48.11(IN) Z59.4(D0) Z68.9 Z76.10 Z76.11
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                D3                           J100.13(Pin_13) J4.26(Pin_26) Z19.2(IN) Z45.11(IN) Z55.4 Z59.13(D3) Z68.7 Z75.5
   pin  10                VD3                          Z28.6(D2) Z45.12(OUT)
   pin  11                D7                           J100.17(Pin_17) J4.20(Pin_20) Z13.2(IN) Z60.3 Z63.11(IN) Z67.7 Z75.11 Z76.6
   pin  12                Net-(Z24-Pad12)              Z24.12 Z24.8
   pin  13                D6                           J100.15(Pin_15) J4.24(Pin_24) Z14.2(IN) Z55.10 Z60.5 Z67.5 Z75.9
   pin  14                MODESEL                      Z43.1(S) Z59.14(~{Q3})
   pin  15                ~{INSIG}                     Z25.6
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z45  (2102, Video RAM)
   pin   1 A6             VA6                          Z31.9(Zc) Z46.1(A6) Z47.1(A6) Z48.1(A6) Z61.1(A6) Z62.1(A6) Z63.1(A6)
   pin   2 A5             VA5                          Z46.2(A5) Z47.2(A5) Z48.2(A5) Z49.4(Za) Z61.2(A5) Z62.2(A5) Z63.2(A5)
   pin   3 R/~{W}         ~{VWR}                       Z46.3(R/~{W}) Z47.3(R/~{W}) Z48.3(R/~{W}) Z49.12(Zd) Z61.3(R/~{W}) Z62.3(R/~{W}) Z63.3(R/~{W})
   pin   4 A1             VA1                          Z46.4(A1) Z47.4(A1) Z48.4(A1) Z61.4(A1) Z62.4(A1) Z63.4(A1) Z64.4(Za)
   pin   5 A2             VA2                          Z46.5(A2) Z47.5(A2) Z48.5(A2) Z61.5(A2) Z62.5(A2) Z63.5(A2) Z64.12(Zd)
   pin   6 A3             VA3                          Z46.6(A3) Z47.6(A3) Z48.6(A3) Z61.6(A3) Z62.6(A3) Z63.6(A3) Z64.7(Zb)
   pin   7 A4             VA4                          Z46.7(A4) Z47.7(A4) Z48.7(A4) Z49.9(Zc) Z61.7(A4) Z62.7(A4) Z63.7(A4)
   pin   8 A0             VA0                          Z46.8(A0) Z47.8(A0) Z48.8(A0) Z61.8(A0) Z62.8(A0) Z63.8(A0) Z64.9(Zc)
   pin   9 GND            GND                          [net GND, 204 pins]
   pin  10 VCC            +5V                          [net +5V, 134 pins]
   pin  11 IN             D3                           J100.13(Pin_13) J4.26(Pin_26) Z19.2(IN) Z44.9 Z55.4 Z59.13(D3) Z68.7 Z75.5
   pin  12 OUT            VD3                          Z28.6(D2) Z44.10
   pin  13 ~{CE}          GND                          [net GND, 204 pins]
   pin  14 A9             VA9                          Z31.7(Zb) Z46.14(A9) Z47.14(A9) Z48.14(A9) Z61.14(A9) Z62.14(A9) Z63.14(A9)
   pin  15 A8             VA8                          Z31.4(Za) Z46.15(A8) Z47.15(A8) Z48.15(A8) Z61.15(A8) Z62.15(A8) Z63.15(A8)
   pin  16 A7             VA7                          Z31.12(Zd) Z46.16(A7) Z47.16(A7) Z48.16(A7) Z61.16(A7) Z62.16(A7) Z63.16(A7)

Z46  (2102, Video RAM)
   pin   1 A6             VA6                          Z31.9(Zc) Z45.1(A6) Z47.1(A6) Z48.1(A6) Z61.1(A6) Z62.1(A6) Z63.1(A6)
   pin   2 A5             VA5                          Z45.2(A5) Z47.2(A5) Z48.2(A5) Z49.4(Za) Z61.2(A5) Z62.2(A5) Z63.2(A5)
   pin   3 R/~{W}         ~{VWR}                       Z45.3(R/~{W}) Z47.3(R/~{W}) Z48.3(R/~{W}) Z49.12(Zd) Z61.3(R/~{W}) Z62.3(R/~{W}) Z63.3(R/~{W})
   pin   4 A1             VA1                          Z45.4(A1) Z47.4(A1) Z48.4(A1) Z61.4(A1) Z62.4(A1) Z63.4(A1) Z64.4(Za)
   pin   5 A2             VA2                          Z45.5(A2) Z47.5(A2) Z48.5(A2) Z61.5(A2) Z62.5(A2) Z63.5(A2) Z64.12(Zd)
   pin   6 A3             VA3                          Z45.6(A3) Z47.6(A3) Z48.6(A3) Z61.6(A3) Z62.6(A3) Z63.6(A3) Z64.7(Zb)
   pin   7 A4             VA4                          Z45.7(A4) Z47.7(A4) Z48.7(A4) Z49.9(Zc) Z61.7(A4) Z62.7(A4) Z63.7(A4)
   pin   8 A0             VA0                          Z45.8(A0) Z47.8(A0) Z48.8(A0) Z61.8(A0) Z62.8(A0) Z63.8(A0) Z64.9(Zc)
   pin   9 GND            GND                          [net GND, 204 pins]
   pin  10 VCC            +5V                          [net +5V, 134 pins]
   pin  11 IN             D2                           J100.10(Pin_10) J4.32(Pin_32) Z18.2(IN) Z44.3 Z59.12(D2) Z68.5 Z75.13 Z76.4
   pin  12 OUT            VD2                          Z28.3(D0) Z44.2
   pin  13 ~{CE}          GND                          [net GND, 204 pins]
   pin  14 A9             VA9                          Z31.7(Zb) Z45.14(A9) Z47.14(A9) Z48.14(A9) Z61.14(A9) Z62.14(A9) Z63.14(A9)
   pin  15 A8             VA8                          Z31.4(Za) Z45.15(A8) Z47.15(A8) Z48.15(A8) Z61.15(A8) Z62.15(A8) Z63.15(A8)
   pin  16 A7             VA7                          Z31.12(Zd) Z45.16(A7) Z47.16(A7) Z48.16(A7) Z61.16(A7) Z62.16(A7) Z63.16(A7)

Z47  (2102, Video RAM)
   pin   1 A6             VA6                          Z31.9(Zc) Z45.1(A6) Z46.1(A6) Z48.1(A6) Z61.1(A6) Z62.1(A6) Z63.1(A6)
   pin   2 A5             VA5                          Z45.2(A5) Z46.2(A5) Z48.2(A5) Z49.4(Za) Z61.2(A5) Z62.2(A5) Z63.2(A5)
   pin   3 R/~{W}         ~{VWR}                       Z45.3(R/~{W}) Z46.3(R/~{W}) Z48.3(R/~{W}) Z49.12(Zd) Z61.3(R/~{W}) Z62.3(R/~{W}) Z63.3(R/~{W})
   pin   4 A1             VA1                          Z45.4(A1) Z46.4(A1) Z48.4(A1) Z61.4(A1) Z62.4(A1) Z63.4(A1) Z64.4(Za)
   pin   5 A2             VA2                          Z45.5(A2) Z46.5(A2) Z48.5(A2) Z61.5(A2) Z62.5(A2) Z63.5(A2) Z64.12(Zd)
   pin   6 A3             VA3                          Z45.6(A3) Z46.6(A3) Z48.6(A3) Z61.6(A3) Z62.6(A3) Z63.6(A3) Z64.7(Zb)
   pin   7 A4             VA4                          Z45.7(A4) Z46.7(A4) Z48.7(A4) Z49.9(Zc) Z61.7(A4) Z62.7(A4) Z63.7(A4)
   pin   8 A0             VA0                          Z45.8(A0) Z46.8(A0) Z48.8(A0) Z61.8(A0) Z62.8(A0) Z63.8(A0) Z64.9(Zc)
   pin   9 GND            GND                          [net GND, 204 pins]
   pin  10 VCC            +5V                          [net +5V, 134 pins]
   pin  11 IN             D1                           J100.16(Pin_16) J4.22(Pin_22) Z16.2(IN) Z44.5 Z59.5(D1) Z68.3 Z76.13 Z76.2
   pin  12 OUT            VD1                          Z28.13(D4) Z44.4
   pin  13 ~{CE}          GND                          [net GND, 204 pins]
   pin  14 A9             VA9                          Z31.7(Zb) Z45.14(A9) Z46.14(A9) Z48.14(A9) Z61.14(A9) Z62.14(A9) Z63.14(A9)
   pin  15 A8             VA8                          Z31.4(Za) Z45.15(A8) Z46.15(A8) Z48.15(A8) Z61.15(A8) Z62.15(A8) Z63.15(A8)
   pin  16 A7             VA7                          Z31.12(Zd) Z45.16(A7) Z46.16(A7) Z48.16(A7) Z61.16(A7) Z62.16(A7) Z63.16(A7)

Z48  (2102, Video RAM)
   pin   1 A6             VA6                          Z31.9(Zc) Z45.1(A6) Z46.1(A6) Z47.1(A6) Z61.1(A6) Z62.1(A6) Z63.1(A6)
   pin   2 A5             VA5                          Z45.2(A5) Z46.2(A5) Z47.2(A5) Z49.4(Za) Z61.2(A5) Z62.2(A5) Z63.2(A5)
   pin   3 R/~{W}         ~{VWR}                       Z45.3(R/~{W}) Z46.3(R/~{W}) Z47.3(R/~{W}) Z49.12(Zd) Z61.3(R/~{W}) Z62.3(R/~{W}) Z63.3(R/~{W})
   pin   4 A1             VA1                          Z45.4(A1) Z46.4(A1) Z47.4(A1) Z61.4(A1) Z62.4(A1) Z63.4(A1) Z64.4(Za)
   pin   5 A2             VA2                          Z45.5(A2) Z46.5(A2) Z47.5(A2) Z61.5(A2) Z62.5(A2) Z63.5(A2) Z64.12(Zd)
   pin   6 A3             VA3                          Z45.6(A3) Z46.6(A3) Z47.6(A3) Z61.6(A3) Z62.6(A3) Z63.6(A3) Z64.7(Zb)
   pin   7 A4             VA4                          Z45.7(A4) Z46.7(A4) Z47.7(A4) Z49.9(Zc) Z61.7(A4) Z62.7(A4) Z63.7(A4)
   pin   8 A0             VA0                          Z45.8(A0) Z46.8(A0) Z47.8(A0) Z61.8(A0) Z62.8(A0) Z63.8(A0) Z64.9(Zc)
   pin   9 GND            GND                          [net GND, 204 pins]
   pin  10 VCC            +5V                          [net +5V, 134 pins]
   pin  11 IN             D0                           J100.11(Pin_11) J4.30(Pin_30) Z17.2(IN) Z44.7 Z59.4(D0) Z68.9 Z76.10 Z76.11
   pin  12 OUT            VD0                          Z28.14(D5) Z44.6
   pin  13 ~{CE}          GND                          [net GND, 204 pins]
   pin  14 A9             VA9                          Z31.7(Zb) Z45.14(A9) Z46.14(A9) Z47.14(A9) Z61.14(A9) Z62.14(A9) Z63.14(A9)
   pin  15 A8             VA8                          Z31.4(Za) Z45.15(A8) Z46.15(A8) Z47.15(A8) Z61.15(A8) Z62.15(A8) Z63.15(A8)
   pin  16 A7             VA7                          Z31.12(Zd) Z45.16(A7) Z46.16(A7) Z47.16(A7) Z61.16(A7) Z62.16(A7) Z63.16(A7)

Z49  (74LS157, Video Access Multiplexer)
   pin   1 S              ~{VID}                       Z31.1(S) Z36.8 Z64.1(S) Z7.4(~{S})
   pin   2 I0a            A5                           J100.3(Pin_3) J4.35(Pin_35) Z33.3(A5) Z34.3(A5) Z39.9 Z51.5(I0b) Z54.12
   pin   3 I1a            C5                           Z50.8(Q2) Z66.5
   pin   4 Za             VA5                          Z45.2(A5) Z46.2(A5) Z47.2(A5) Z48.2(A5) Z61.2(A5) Z62.2(A5) Z63.2(A5)
   pin   5 I0b            ~{RD}                        J4.15(Pin_15) Z22.7 Z52.13
   pin   6 I1b            Net-(Z49-I1b)                R49.2 Z49.13(I1d)
   pin   7 Zb             ~{VRD}                       Z44.1 Z60.1
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Zc             VA4                          Z45.7(A4) Z46.7(A4) Z47.7(A4) Z48.7(A4) Z61.7(A4) Z62.7(A4) Z63.7(A4)
   pin  10 I1c            C4                           Z50.9(Q1) Z66.3
   pin  11 I0c            A4                           J100.2(Pin_2) J4.31(Pin_31) Z33.4(A4) Z34.4(A4) Z39.7 Z51.2(I0a) Z54.4
   pin  12 Zd             ~{VWR}                       Z45.3(R/~{W}) Z46.3(R/~{W}) Z47.3(R/~{W}) Z48.3(R/~{W}) Z61.3(R/~{W}) Z62.3(R/~{W}) Z63.3(R/~{W})
   pin  13 I1d            Net-(Z49-I1b)                R49.2 Z49.6(I1b)
   pin  14 I0d            ~{WR}                        J4.13(Pin_13) Z13.3(~{WR}) Z14.3(~{WR}) Z15.3(~{WR}) Z16.3(~{WR}) Z17.3(~{WR}) Z18.3(~{WR}) Z19.3(~{WR}) Z20.3(~{WR}) Z22.5
   pin  15 E              GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z50  (74LS93, Video Counter)
   pin   1 CP1..3         C3                           Z50.12(Q0) Z64.6(I1b)
   pin   2 R0(1)          Net-(Z50-R0(1))              Z50.3(R0(2)) Z66.6
   pin   3 R0(2)          Net-(Z50-R0(1))              Z50.2(R0(1)) Z66.6
   pin   5 VCC            +5V                          [net +5V, 134 pins]
   pin   8 Q2             C5                           Z49.3(I1a) Z66.5
   pin   9 Q1             C4                           Z49.10(I1c) Z66.3
   pin  10 GND            GND                          [net GND, 204 pins]
   pin  11 Q3             HDRV                         Z12.14(CP0) Z30.8 Z6.13 Z66.4
   pin  12 Q0             C3                           Z50.1(CP1..3) Z64.6(I1b)
   pin  14 CP0            C2                           Z64.13(I1d) Z65.8(Q2)

Z51  (74LS157, RAM)
   pin   1 S              MUX                          J4.16(Pin_16) Z35.1(S) Z72.3
   pin   2 I0a            A4                           J100.2(Pin_2) J4.31(Pin_31) Z33.4(A4) Z34.4(A4) Z39.7 Z49.11(I0c) Z54.4
   pin   3 I1a            A10                          J4.4(Pin_4) Z33.19(A10) Z34.19(A10) Z36.13 Z38.3 Z52.1
   pin   4 Za             Net-(Z13-A4)                 Z13.11(A4) Z14.11(A4) Z15.11(A4) Z16.11(A4) Z17.11(A4) Z18.11(A4) Z19.11(A4) Z20.11(A4)
   pin   5 I0b            A5                           J100.3(Pin_3) J4.35(Pin_35) Z33.3(A5) Z34.3(A5) Z39.9 Z49.2(I0a) Z54.12
   pin   6 I1b            A11                          J4.9(Pin_9) Z33.18(A11) Z34.18(A11) Z37.5 Z37.6 Z38.13
   pin   7 Zb             Net-(Z13-A5)                 Z13.10(A5) Z14.10(A5) Z15.10(A5) Z16.10(A5) Z17.10(A5) Z18.10(A5) Z19.10(A5) Z20.10(A5)
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Zc             Net-(Z51-Zc)                 Z71.3
   pin  10 I1c            A12                          J4.5(Pin_5) Z21.13(A0) Z33.21(A12) Z34.21(~{CE2}) Z38.5
   pin  11 I0c            A6                           J100.7(Pin_7) J4.38(Pin_38) Z31.11(I0c) Z33.2(A6) Z34.2(A6) Z39.5 Z54.3 Z71.15
   pin  12 Zd             unconnected-(Z51-Zd-Pad12)   (no other connection)
   pin  13 I1d            unconnected-(Z51-I1d-Pad13)  (no other connection)
   pin  14 I0d            unconnected-(Z51-I0d-Pad14)  (no other connection)
   pin  15 E              GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z52  (74LS04, CPU)
   pin   1                A10                          J4.4(Pin_4) Z33.19(A10) Z34.19(A10) Z36.13 Z38.3 Z51.3(I1a)
   pin   2                Net-(Z36-Pad9)               Z36.9
   pin   3                ~{TEST}                      J4.23(Pin_23) R58.2 Z40.25(~{BUSRQ}) Z53.4
   pin   4                Net-(Z22-Pad1)               Z22.1 Z22.15 Z38.1 Z38.15 Z39.1 Z39.15 Z55.15 Z72.1
   pin   5                A0                           J100.5(Pin_5) J4.25(Pin_25) Z33.8(A0) Z34.8(A0) Z35.2(I0a) Z55.11 Z64.11(I0c)
   pin   6                Net-(Z36-Pad1)               Z36.1
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                unconnected-(Z52-Pad8)       (no other connection)
   pin   9                GND                          [net GND, 204 pins]
   pin  10                Net-(Z40-~{RESET})           Z40.26(~{RESET})
   pin  11                Net-(Z37-Pad2)               Z37.2 Z53.11
   pin  12                Net-(Z52-Pad12)              Z74.4
   pin  13                ~{RD}                        J4.15(Pin_15) Z22.7 Z49.5(I0b)
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z53  (74LS132, CPU)
   pin   1                Net-(C57-Pad1)               C57.1 R65.2 S2.4
   pin   2                Net-(Z40-~{HALT})            Z40.18(~{HALT})
   pin   3                Net-(Z37-Pad11)              Z37.11 Z37.12 Z37.3
   pin   4                ~{TEST}                      J4.23(Pin_23) R58.2 Z40.25(~{BUSRQ}) Z52.3
   pin   5                Net-(Z40-~{RD})              Z23.5 Z23.9 Z40.21(~{RD}) Z74.1
   pin   6                ~{DBOUT}                     Z53.10 Z53.9 Z75.1 Z75.15 Z76.15
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                ~{DBIN}                      Z55.1 Z76.1
   pin   9                ~{DBOUT}                     Z53.10 Z53.6 Z75.1 Z75.15 Z76.15
   pin  10                ~{DBOUT}                     Z53.6 Z53.9 Z75.1 Z75.15 Z76.15
   pin  11                Net-(Z37-Pad2)               Z37.2 Z52.11
   pin  12                Net-(C42-Pad1)               C42.1 R47.2 Z53.13
   pin  13                Net-(C42-Pad1)               C42.1 R47.2 Z53.12
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z54  (74LS30, Cassette Interface)
   pin   1                A3                           J100.9(Pin_9) J4.34(Pin_34) Z22.13 Z33.5(A3) Z34.5(A3) Z35.14(I0d) Z64.5(I0b)
   pin   2                A2                           J100.6(Pin_6) J4.40(Pin_40) Z22.11 Z33.6(A2) Z34.6(A2) Z35.11(I0c) Z64.14(I0d)
   pin   3                A6                           J100.7(Pin_7) J4.38(Pin_38) Z31.11(I0c) Z33.2(A6) Z34.2(A6) Z39.5 Z51.11(I0c) Z71.15
   pin   4                A4                           J100.2(Pin_2) J4.31(Pin_31) Z33.4(A4) Z34.4(A4) Z39.7 Z49.11(I0c) Z51.2(I0a)
   pin   5                A7                           J100.8(Pin_8) J4.36(Pin_36) Z31.14(I0d) Z33.1(A7) Z34.1(A7) Z35.6(I1b) Z39.11 Z54.6
   pin   6                A7                           J100.8(Pin_8) J4.36(Pin_36) Z31.14(I0d) Z33.1(A7) Z34.1(A7) Z35.6(I1b) Z39.11 Z54.5
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                Net-(Z36-Pad2)               Z36.2
   pin  11                A1                           J100.4(Pin_4) J4.27(Pin_27) Z33.7(A1) Z34.7(A1) Z35.5(I0b) Z55.13 Z64.2(I0a)
   pin  12                A5                           J100.3(Pin_3) J4.35(Pin_35) Z33.3(A5) Z34.3(A5) Z39.9 Z49.2(I0a) Z51.5(I0b)
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z55  (74LS367, CPU Gating)
   pin   1                ~{DBIN}                      Z53.8 Z76.1
   pin   2                D4                           J100.18(Pin_18) J4.18(Pin_18) Z15.2(IN) Z60.9 Z61.11(IN) Z67.9 Z75.7
   pin   3                ZD4                          Z40.7(D4) Z75.6
   pin   4                D3                           J100.13(Pin_13) J4.26(Pin_26) Z19.2(IN) Z44.9 Z45.11(IN) Z59.13(D3) Z68.7 Z75.5
   pin   5                ZD3                          Z40.8(D3) Z75.4
   pin   6                D5                           J100.12(Pin_12) J4.28(Pin_28) Z20.2(IN) Z60.7 Z62.11(IN) Z67.3 Z75.3
   pin   7                ZD5                          Z40.9(D5) Z75.2
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                ZD6                          Z40.10(D6) Z75.10
   pin  10                D6                           J100.15(Pin_15) J4.24(Pin_24) Z14.2(IN) Z44.13 Z60.5 Z67.5 Z75.9
   pin  11                A0                           J100.5(Pin_5) J4.25(Pin_25) Z33.8(A0) Z34.8(A0) Z35.2(I0a) Z52.5 Z64.11(I0c)
   pin  12                ZA0                          Z40.30(A0)
   pin  13                A1                           J100.4(Pin_4) J4.27(Pin_27) Z33.7(A1) Z34.7(A1) Z35.5(I0b) Z54.11 Z64.2(I0a)
   pin  14                ZA1                          Z40.31(A1)
   pin  15                Net-(Z22-Pad1)               Z22.1 Z22.15 Z38.1 Z38.15 Z39.1 Z39.15 Z52.4 Z72.1
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z56  (74LS92, CPU)
   pin   1 CP1..3         CLK                          Z42.6 Z43.3(I1a) Z69.11(C) Z69.3(C) Z70.11(C) Z70.3(C)
   pin   5 VCC            +5V                          [net +5V, 134 pins]
   pin   6 R0(1)          ~{CLK_EN}                    Z42.8 Z56.7(R0(2)) Z58.6(R0(1)) Z58.7(R0(2))
   pin   7 R0(2)          ~{CLK_EN}                    Z42.8 Z56.6(R0(1)) Z58.6(R0(1)) Z58.7(R0(2))
   pin   8 Q3             Net-(Z56-Q3)                 Z72.12
   pin   9 Q2             unconnected-(Z56-Q2-Pad9)    (no other connection)
   pin  10 GND            GND                          [net GND, 204 pins]
   pin  11 Q1             unconnected-(Z56-Q1-Pad11)   (no other connection)
   pin  12 Q0             unconnected-(Z56-Q0-Pad12)   (no other connection)
   pin  14 CP0            unconnected-(Z56-CP0-Pad14)  (no other connection)

Z57  (74C04, Video Sync)
   pin   1                VDRV                         Z30.9 Z32.11(Q3) Z66.1
   pin   2                Net-(Z57-Pad2)               Z57.3
   pin   3                Net-(Z57-Pad2)               Z57.2
   pin   4                Net-(R21-Pad1)               R21.1(1)
   pin   5                Net-(C27-Pad2)               C27.2 R44.2
   pin   6                Net-(Z57-Pad6)               Z57.9
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                Net-(Z5-Pad1)                Z5.1 Z5.5
   pin   9                Net-(Z57-Pad6)               Z57.6
   pin  10                Net-(C26-Pad2)               C26.2 C27.1
   pin  11                Net-(Z57-Pad11)              Z57.12
   pin  12                Net-(Z57-Pad11)              Z57.11
   pin  13                Net-(C26-Pad1)               C26.1 R21.2(2)
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z58  (74LS92, Video Counter)
   pin   1 CP1..3         Net-(Z58-CP1..3)             Z24.1 Z58.12(Q0)
   pin   5 VCC            +5V                          [net +5V, 134 pins]
   pin   6 R0(1)          ~{CLK_EN}                    Z42.8 Z56.6(R0(1)) Z56.7(R0(2)) Z58.7(R0(2))
   pin   7 R0(2)          ~{CLK_EN}                    Z42.8 Z56.6(R0(1)) Z56.7(R0(2)) Z58.6(R0(1))
   pin   8 Q3             Net-(Z43-I1b)                Z43.10(I1c) Z43.6(I1b)
   pin   9 Q2             Net-(Z43-I0c)                Z24.2 Z43.11(I0c)
   pin  10 GND            GND                          [net GND, 204 pins]
   pin  11 Q1             unconnected-(Z58-Q1-Pad11)   (no other connection)
   pin  12 Q0             Net-(Z58-CP1..3)             Z24.1 Z58.1(CP1..3)
   pin  14 CP0            SHIFT                        Z43.4(Za) Z9.9

Z59  (74LS175, Cassette Interface)
   pin   1 ~{Mr}          Net-(Z59-~{Mr})              R59.2
   pin   2 Q0             Net-(Z59-Q0)                 R54.1
   pin   3 ~{Q0}          unconnected-(Z59-~{Q0}-Pad3) (no other connection)
   pin   4 D0             D0                           J100.11(Pin_11) J4.30(Pin_30) Z17.2(IN) Z44.7 Z48.11(IN) Z68.9 Z76.10 Z76.11
   pin   5 D1             D1                           J100.16(Pin_16) J4.22(Pin_22) Z16.2(IN) Z44.5 Z47.11(IN) Z68.3 Z76.13 Z76.2
   pin   6 ~{Q1}          Net-(Z59-~{Q1})              R55.2 R56.1
   pin   7 Q1             unconnected-(Z59-Q1-Pad7)    (no other connection)
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Cp             ~{OUTSIG}                    Z24.13 Z25.8
   pin  10 Q2             Net-(Z41A-1A)                Z41.1(1A) Z41.2(1B)
   pin  11 ~{Q2}          unconnected-(Z59-~{Q2}-Pad11) (no other connection)
   pin  12 D2             D2                           J100.10(Pin_10) J4.32(Pin_32) Z18.2(IN) Z44.3 Z46.11(IN) Z68.5 Z75.13 Z76.4
   pin  13 D3             D3                           J100.13(Pin_13) J4.26(Pin_26) Z19.2(IN) Z44.9 Z45.11(IN) Z55.4 Z68.7 Z75.5
   pin  14 ~{Q3}          MODESEL                      Z43.1(S) Z44.14
   pin  15 Q3             unconnected-(Z59-Q3-Pad15)   (no other connection)
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z60  (74LS367, Video RAM)
   pin   1                ~{VRD}                       Z44.1 Z49.7(Zb)
   pin   2                VD7                          Z30.11 Z42.13 Z63.12(OUT)
   pin   3                D7                           J100.17(Pin_17) J4.20(Pin_20) Z13.2(IN) Z44.11 Z63.11(IN) Z67.7 Z75.11 Z76.6
   pin   4                VD6                          Z27.13(D3) Z30.13
   pin   5                D6                           J100.15(Pin_15) J4.24(Pin_24) Z14.2(IN) Z44.13 Z55.10 Z67.5 Z75.9
   pin   6                VD5                          Z28.11(D3) Z30.12 Z62.12(OUT)
   pin   7                D5                           J100.12(Pin_12) J4.28(Pin_28) Z20.2(IN) Z55.6 Z62.11(IN) Z67.3 Z75.3
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                D4                           J100.18(Pin_18) J4.18(Pin_18) Z15.2(IN) Z55.2 Z61.11(IN) Z67.9 Z75.7
   pin  10                VD4                          Z28.4(D1) Z61.12(OUT)
   pin  11                unconnected-(Z60-Pad11)      (no other connection)
   pin  12                GND                          [net GND, 204 pins]
   pin  13                unconnected-(Z60-Pad13)      (no other connection)
   pin  14                GND                          [net GND, 204 pins]
   pin  15                GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z61  (2102, Video RAM)
   pin   1 A6             VA6                          Z31.9(Zc) Z45.1(A6) Z46.1(A6) Z47.1(A6) Z48.1(A6) Z62.1(A6) Z63.1(A6)
   pin   2 A5             VA5                          Z45.2(A5) Z46.2(A5) Z47.2(A5) Z48.2(A5) Z49.4(Za) Z62.2(A5) Z63.2(A5)
   pin   3 R/~{W}         ~{VWR}                       Z45.3(R/~{W}) Z46.3(R/~{W}) Z47.3(R/~{W}) Z48.3(R/~{W}) Z49.12(Zd) Z62.3(R/~{W}) Z63.3(R/~{W})
   pin   4 A1             VA1                          Z45.4(A1) Z46.4(A1) Z47.4(A1) Z48.4(A1) Z62.4(A1) Z63.4(A1) Z64.4(Za)
   pin   5 A2             VA2                          Z45.5(A2) Z46.5(A2) Z47.5(A2) Z48.5(A2) Z62.5(A2) Z63.5(A2) Z64.12(Zd)
   pin   6 A3             VA3                          Z45.6(A3) Z46.6(A3) Z47.6(A3) Z48.6(A3) Z62.6(A3) Z63.6(A3) Z64.7(Zb)
   pin   7 A4             VA4                          Z45.7(A4) Z46.7(A4) Z47.7(A4) Z48.7(A4) Z49.9(Zc) Z62.7(A4) Z63.7(A4)
   pin   8 A0             VA0                          Z45.8(A0) Z46.8(A0) Z47.8(A0) Z48.8(A0) Z62.8(A0) Z63.8(A0) Z64.9(Zc)
   pin   9 GND            GND                          [net GND, 204 pins]
   pin  10 VCC            +5V                          [net +5V, 134 pins]
   pin  11 IN             D4                           J100.18(Pin_18) J4.18(Pin_18) Z15.2(IN) Z55.2 Z60.9 Z67.9 Z75.7
   pin  12 OUT            VD4                          Z28.4(D1) Z60.10
   pin  13 ~{CE}          GND                          [net GND, 204 pins]
   pin  14 A9             VA9                          Z31.7(Zb) Z45.14(A9) Z46.14(A9) Z47.14(A9) Z48.14(A9) Z62.14(A9) Z63.14(A9)
   pin  15 A8             VA8                          Z31.4(Za) Z45.15(A8) Z46.15(A8) Z47.15(A8) Z48.15(A8) Z62.15(A8) Z63.15(A8)
   pin  16 A7             VA7                          Z31.12(Zd) Z45.16(A7) Z46.16(A7) Z47.16(A7) Z48.16(A7) Z62.16(A7) Z63.16(A7)

Z62  (2102, Video RAM)
   pin   1 A6             VA6                          Z31.9(Zc) Z45.1(A6) Z46.1(A6) Z47.1(A6) Z48.1(A6) Z61.1(A6) Z63.1(A6)
   pin   2 A5             VA5                          Z45.2(A5) Z46.2(A5) Z47.2(A5) Z48.2(A5) Z49.4(Za) Z61.2(A5) Z63.2(A5)
   pin   3 R/~{W}         ~{VWR}                       Z45.3(R/~{W}) Z46.3(R/~{W}) Z47.3(R/~{W}) Z48.3(R/~{W}) Z49.12(Zd) Z61.3(R/~{W}) Z63.3(R/~{W})
   pin   4 A1             VA1                          Z45.4(A1) Z46.4(A1) Z47.4(A1) Z48.4(A1) Z61.4(A1) Z63.4(A1) Z64.4(Za)
   pin   5 A2             VA2                          Z45.5(A2) Z46.5(A2) Z47.5(A2) Z48.5(A2) Z61.5(A2) Z63.5(A2) Z64.12(Zd)
   pin   6 A3             VA3                          Z45.6(A3) Z46.6(A3) Z47.6(A3) Z48.6(A3) Z61.6(A3) Z63.6(A3) Z64.7(Zb)
   pin   7 A4             VA4                          Z45.7(A4) Z46.7(A4) Z47.7(A4) Z48.7(A4) Z49.9(Zc) Z61.7(A4) Z63.7(A4)
   pin   8 A0             VA0                          Z45.8(A0) Z46.8(A0) Z47.8(A0) Z48.8(A0) Z61.8(A0) Z63.8(A0) Z64.9(Zc)
   pin   9 GND            GND                          [net GND, 204 pins]
   pin  10 VCC            +5V                          [net +5V, 134 pins]
   pin  11 IN             D5                           J100.12(Pin_12) J4.28(Pin_28) Z20.2(IN) Z55.6 Z60.7 Z67.3 Z75.3
   pin  12 OUT            VD5                          Z28.11(D3) Z30.12 Z60.6
   pin  13 ~{CE}          GND                          [net GND, 204 pins]
   pin  14 A9             VA9                          Z31.7(Zb) Z45.14(A9) Z46.14(A9) Z47.14(A9) Z48.14(A9) Z61.14(A9) Z63.14(A9)
   pin  15 A8             VA8                          Z31.4(Za) Z45.15(A8) Z46.15(A8) Z47.15(A8) Z48.15(A8) Z61.15(A8) Z63.15(A8)
   pin  16 A7             VA7                          Z31.12(Zd) Z45.16(A7) Z46.16(A7) Z47.16(A7) Z48.16(A7) Z61.16(A7) Z63.16(A7)

Z63  (2102, Video RAM)
   pin   1 A6             VA6                          Z31.9(Zc) Z45.1(A6) Z46.1(A6) Z47.1(A6) Z48.1(A6) Z61.1(A6) Z62.1(A6)
   pin   2 A5             VA5                          Z45.2(A5) Z46.2(A5) Z47.2(A5) Z48.2(A5) Z49.4(Za) Z61.2(A5) Z62.2(A5)
   pin   3 R/~{W}         ~{VWR}                       Z45.3(R/~{W}) Z46.3(R/~{W}) Z47.3(R/~{W}) Z48.3(R/~{W}) Z49.12(Zd) Z61.3(R/~{W}) Z62.3(R/~{W})
   pin   4 A1             VA1                          Z45.4(A1) Z46.4(A1) Z47.4(A1) Z48.4(A1) Z61.4(A1) Z62.4(A1) Z64.4(Za)
   pin   5 A2             VA2                          Z45.5(A2) Z46.5(A2) Z47.5(A2) Z48.5(A2) Z61.5(A2) Z62.5(A2) Z64.12(Zd)
   pin   6 A3             VA3                          Z45.6(A3) Z46.6(A3) Z47.6(A3) Z48.6(A3) Z61.6(A3) Z62.6(A3) Z64.7(Zb)
   pin   7 A4             VA4                          Z45.7(A4) Z46.7(A4) Z47.7(A4) Z48.7(A4) Z49.9(Zc) Z61.7(A4) Z62.7(A4)
   pin   8 A0             VA0                          Z45.8(A0) Z46.8(A0) Z47.8(A0) Z48.8(A0) Z61.8(A0) Z62.8(A0) Z64.9(Zc)
   pin   9 GND            GND                          [net GND, 204 pins]
   pin  10 VCC            +5V                          [net +5V, 134 pins]
   pin  11 IN             D7                           J100.17(Pin_17) J4.20(Pin_20) Z13.2(IN) Z44.11 Z60.3 Z67.7 Z75.11 Z76.6
   pin  12 OUT            VD7                          Z30.11 Z42.13 Z60.2
   pin  13 ~{CE}          GND                          [net GND, 204 pins]
   pin  14 A9             VA9                          Z31.7(Zb) Z45.14(A9) Z46.14(A9) Z47.14(A9) Z48.14(A9) Z61.14(A9) Z62.14(A9)
   pin  15 A8             VA8                          Z31.4(Za) Z45.15(A8) Z46.15(A8) Z47.15(A8) Z48.15(A8) Z61.15(A8) Z62.15(A8)
   pin  16 A7             VA7                          Z31.12(Zd) Z45.16(A7) Z46.16(A7) Z47.16(A7) Z48.16(A7) Z61.16(A7) Z62.16(A7)

Z64  (74LS157, Video Access Multiplexer)
   pin   1 S              ~{VID}                       Z31.1(S) Z36.8 Z49.1(S) Z7.4(~{S})
   pin   2 I0a            A1                           J100.4(Pin_4) J4.27(Pin_27) Z33.7(A1) Z34.7(A1) Z35.5(I0b) Z54.11 Z55.13
   pin   3 I1a            C1                           Z65.9(Q1)
   pin   4 Za             VA1                          Z45.4(A1) Z46.4(A1) Z47.4(A1) Z48.4(A1) Z61.4(A1) Z62.4(A1) Z63.4(A1)
   pin   5 I0b            A3                           J100.9(Pin_9) J4.34(Pin_34) Z22.13 Z33.5(A3) Z34.5(A3) Z35.14(I0d) Z54.1
   pin   6 I1b            C3                           Z50.1(CP1..3) Z50.12(Q0)
   pin   7 Zb             VA3                          Z45.6(A3) Z46.6(A3) Z47.6(A3) Z48.6(A3) Z61.6(A3) Z62.6(A3) Z63.6(A3)
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9 Zc             VA0                          Z45.8(A0) Z46.8(A0) Z47.8(A0) Z48.8(A0) Z61.8(A0) Z62.8(A0) Z63.8(A0)
   pin  10 I1c            C0                           Z43.7(Zb)
   pin  11 I0c            A0                           J100.5(Pin_5) J4.25(Pin_25) Z33.8(A0) Z34.8(A0) Z35.2(I0a) Z52.5 Z55.11
   pin  12 Zd             VA2                          Z45.5(A2) Z46.5(A2) Z47.5(A2) Z48.5(A2) Z61.5(A2) Z62.5(A2) Z63.5(A2)
   pin  13 I1d            C2                           Z50.14(CP0) Z65.8(Q2)
   pin  14 I0d            A2                           J100.6(Pin_6) J4.40(Pin_40) Z22.11 Z33.6(A2) Z34.6(A2) Z35.11(I0c) Z54.2
   pin  15 E              GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z65  (74LS93, Video Counter)
   pin   1 CP1..3         Net-(Z43-Zc)                 Z43.9(Zc)
   pin   2 R0(1)          GND                          [net GND, 204 pins]
   pin   3 R0(2)          GND                          [net GND, 204 pins]
   pin   5 VCC            +5V                          [net +5V, 134 pins]
   pin   8 Q2             C2                           Z50.14(CP0) Z64.13(I1d)
   pin   9 Q1             C1                           Z64.3(I1a)
   pin  10 GND            GND                          [net GND, 204 pins]
   pin  11 Q3             unconnected-(Z65-Q3-Pad11)   (no other connection)
   pin  12 Q0             R0                           Z31.10(I1c) Z32.14(CP0)
   pin  14 CP0            L3                           Z12.11(Q3) Z27.12(D2) Z66.11 Z8.2(S1)

Z66  (74LS11, Video Counter)
   pin   1                VDRV                         Z30.9 Z32.11(Q3) Z57.1
   pin   2                R2                           Z31.3(I1a) Z32.9(Q1)
   pin   3                C4                           Z49.10(I1c) Z50.9(Q1)
   pin   4                HDRV                         Z12.14(CP0) Z30.8 Z50.11(Q3) Z6.13
   pin   5                C5                           Z49.3(I1a) Z50.8(Q2)
   pin   6                Net-(Z50-R0(1))              Z50.2(R0(1)) Z50.3(R0(2))
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                Net-(Z12-R0(1))              Z12.2(R0(1)) Z12.3(R0(2))
   pin   9                L2                           Z12.8(Q2) Z29.8(R2) Z66.10 Z8.14(S0)
   pin  10                L2                           Z12.8(Q2) Z29.8(R2) Z66.9 Z8.14(S0)
   pin  11                L3                           Z12.11(Q3) Z27.12(D2) Z65.14(CP0) Z8.2(S1)
   pin  12                Net-(Z32-R0(1))              Z32.2(R0(1)) Z32.3(R0(2))
   pin  13                R1                           Z31.13(I1d) Z32.1(CP1..3) Z32.12(Q0)
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z67  (74LS367, RAM)
   pin   1                ~{MEM}                       Z68.1 Z74.6
   pin   2                ROMD5                        Z20.14(OUT) Z33.15(D5) Z34.15(D5)
   pin   3                D5                           J100.12(Pin_12) J4.28(Pin_28) Z20.2(IN) Z55.6 Z60.7 Z62.11(IN) Z75.3
   pin   4                ROMD6                        Z14.14(OUT) Z33.16(D6) Z34.16(D6)
   pin   5                D6                           J100.15(Pin_15) J4.24(Pin_24) Z14.2(IN) Z44.13 Z55.10 Z60.5 Z75.9
   pin   6                ROMD7                        Z13.14(OUT) Z33.17(D7) Z34.17(D7)
   pin   7                D7                           J100.17(Pin_17) J4.20(Pin_20) Z13.2(IN) Z44.11 Z60.3 Z63.11(IN) Z75.11 Z76.6
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                D4                           J100.18(Pin_18) J4.18(Pin_18) Z15.2(IN) Z55.2 Z60.9 Z61.11(IN) Z75.7
   pin  10                ROMD4                        Z15.14(OUT) Z33.14(D4) Z34.14(D4)
   pin  11                unconnected-(Z67-Pad11)      (no other connection)
   pin  12                GND                          [net GND, 204 pins]
   pin  13                Net-(Z13-~{CAS})             R57.2 Z13.15(~{CAS}) Z14.15(~{CAS}) Z15.15(~{CAS}) Z16.15(~{CAS}) Z17.15(~{CAS}) Z18.15(~{CAS}) Z19.15(~{CAS}) Z20.15(~{CAS})
   pin  14                ~{CAS}                       J4.3(Pin_3) Z72.9
   pin  15                Net-(Z67-Pad15)              Z71.5 Z71.6
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z68  (74LS367, RAM)
   pin   1                ~{MEM}                       Z67.1 Z74.6
   pin   2                ROMD1                        Z16.14(OUT) Z33.10(D1) Z34.10(D1)
   pin   3                D1                           J100.16(Pin_16) J4.22(Pin_22) Z16.2(IN) Z44.5 Z47.11(IN) Z59.5(D1) Z76.13 Z76.2
   pin   4                ROMD2                        Z18.14(OUT) Z33.11(D2) Z34.11(D2)
   pin   5                D2                           J100.10(Pin_10) J4.32(Pin_32) Z18.2(IN) Z44.3 Z46.11(IN) Z59.12(D2) Z75.13 Z76.4
   pin   6                ROMD3                        Z19.14(OUT) Z33.13(D3) Z34.13(D3)
   pin   7                D3                           J100.13(Pin_13) J4.26(Pin_26) Z19.2(IN) Z44.9 Z45.11(IN) Z55.4 Z59.13(D3) Z75.5
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                D0                           J100.11(Pin_11) J4.30(Pin_30) Z17.2(IN) Z44.7 Z48.11(IN) Z59.4(D0) Z76.10 Z76.11
   pin  10                ROMD0                        Z17.14(OUT) Z33.9(D0) Z34.9(D0)
   pin  11                unconnected-(Z68-Pad11)      (no other connection)
   pin  12                GND                          [net GND, 204 pins]
   pin  13                Net-(Z13-~{RAS})             R60.2 Z13.4(~{RAS}) Z14.4(~{RAS}) Z15.4(~{RAS}) Z16.4(~{RAS}) Z17.4(~{RAS}) Z18.4(~{RAS}) Z19.4(~{RAS}) Z20.4(~{RAS})
   pin  14                ~{RAS}                       J4.1(Pin_1) Z72.5 Z73.5
   pin  15                GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z69  (74LS74, CPU)
   pin   1 ~{R}           MREQ                         Z69.13(~{R}) Z69.2(D) Z70.1(~{R}) Z74.3
   pin   2 D              MREQ                         Z69.1(~{R}) Z69.13(~{R}) Z70.1(~{R}) Z74.3
   pin   3 C              CLK                          Z42.6 Z43.3(I1a) Z56.1(CP1..3) Z69.11(C) Z70.11(C) Z70.3(C)
   pin   4 ~{S}           HI                           R69.2 Z69.10(~{S}) Z70.10(~{S}) Z70.4(~{S})
   pin   5 Q              Net-(Z69A-Q)                 Z69.12(D)
   pin   6 ~{Q}           unconnected-(Z69A-~{Q}-Pad6) (no other connection)
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8 ~{Q}           unconnected-(Z69B-~{Q}-Pad8) (no other connection)
   pin   9 Q              ZMUX                         Z70.2(D) Z72.2
   pin  10 ~{S}           HI                           R69.2 Z69.4(~{S}) Z70.10(~{S}) Z70.4(~{S})
   pin  11 C              CLK                          Z42.6 Z43.3(I1a) Z56.1(CP1..3) Z69.3(C) Z70.11(C) Z70.3(C)
   pin  12 D              Net-(Z69A-Q)                 Z69.5(Q)
   pin  13 ~{R}           MREQ                         Z69.1(~{R}) Z69.2(D) Z70.1(~{R}) Z74.3
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z70  (74LS74, CPU)
   pin   1 ~{R}           MREQ                         Z69.1(~{R}) Z69.13(~{R}) Z69.2(D) Z74.3
   pin   2 D              ZMUX                         Z69.9(Q) Z72.2
   pin   3 C              CLK                          Z42.6 Z43.3(I1a) Z56.1(CP1..3) Z69.11(C) Z69.3(C) Z70.11(C)
   pin   4 ~{S}           HI                           R69.2 Z69.10(~{S}) Z69.4(~{S}) Z70.10(~{S})
   pin   5 Q              unconnected-(Z70A-Q-Pad5)    (no other connection)
   pin   6 ~{Q}           ~{ZCAS}                      Z72.10
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8 ~{Q}           Net-(Z70B-D)                 Z70.12(D)
   pin   9 Q              Net-(Z43-I0a)                Z43.2(I0a)
   pin  10 ~{S}           HI                           R69.2 Z69.10(~{S}) Z69.4(~{S}) Z70.4(~{S})
   pin  11 C              CLK                          Z42.6 Z43.3(I1a) Z56.1(CP1..3) Z69.11(C) Z69.3(C) Z70.3(C)
   pin  12 D              Net-(Z70B-D)                 Z70.8(~{Q})
   pin  13 ~{R}           Net-(Z70B-~{R})              R63.2
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z71  (~, RAM)
   pin   1                Net-(Z35-I1a)                Z35.3(I1a) Z71.2 Z71.7 Z71.8
   pin   2                Net-(Z35-I1a)                Z35.3(I1a) Z71.1 Z71.7 Z71.8
   pin   3                Net-(Z51-Zc)                 Z51.9(Zc)
   pin   4                ~{RAM}                       R62.1 Z3.12 Z3.13 Z3.14 Z3.15 Z71.12 Z74.10
   pin   5                Net-(Z67-Pad15)              Z67.15 Z71.6
   pin   6                Net-(Z67-Pad15)              Z67.15 Z71.5
   pin   7                Net-(Z35-I1a)                Z35.3(I1a) Z71.1 Z71.2 Z71.8
   pin   8                Net-(Z35-I1a)                Z35.3(I1a) Z71.1 Z71.2 Z71.7
   pin   9                GND                          [net GND, 204 pins]
   pin  10                Net-(R66-Pad2)               R66.2
   pin  11                GND                          [net GND, 204 pins]
   pin  12                ~{RAM}                       R62.1 Z3.12 Z3.13 Z3.14 Z3.15 Z71.4 Z74.10
   pin  13                Net-(Z13-A6)                 Z13.13(A6) Z14.13(A6) Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z71.14
   pin  14                Net-(Z13-A6)                 Z13.13(A6) Z14.13(A6) Z15.13(A6) Z16.13(A6) Z17.13(A6) Z18.13(A6) Z19.13(A6) Z20.13(A6) Z71.13
   pin  15                A6                           J100.7(Pin_7) J4.38(Pin_38) Z31.11(I0c) Z33.2(A6) Z34.2(A6) Z39.5 Z51.11(I0c) Z54.3
   pin  16                A13                          J4.6(Pin_6) Z21.3(A1) Z38.7

Z72  (74LS367, CPU)
   pin   1                Net-(Z22-Pad1)               Z22.1 Z22.15 Z38.1 Z38.15 Z39.1 Z39.15 Z52.4 Z55.15
   pin   2                ZMUX                         Z69.9(Q) Z70.2(D)
   pin   3                MUX                          J4.16(Pin_16) Z35.1(S) Z51.1(S)
   pin   4                ~{ZRAS}                      Z23.12 Z23.4 Z40.19(~{MREQ})
   pin   5                ~{RAS}                       J4.1(Pin_1) Z68.14 Z73.5
   pin   6                GND                          [net GND, 204 pins]
   pin   7                unconnected-(Z72-Pad7)       (no other connection)
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                ~{CAS}                       J4.3(Pin_3) Z67.14
   pin  10                ~{ZCAS}                      Z70.6(~{Q})
   pin  11                ZCLK                         R64.2 Z40.6(~{CLK})
   pin  12                Net-(Z56-Q3)                 Z56.8(Q3)
   pin  13                unconnected-(Z72-Pad13)      (no other connection)
   pin  14                GND                          [net GND, 204 pins]
   pin  15                GND                          [net GND, 204 pins]
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z73  (74LS32, CPU)
   pin   1                Net-(Z40-~{IORQ})            Z23.10 Z23.2 Z40.20(~{IORQ})
   pin   2                Net-(Z40-~{M1})              Z40.27(~{M1})
   pin   3                ~{INTAK}                     J4.14(Pin_14)
   pin   4                A15                          J4.7(Pin_7) Z38.9
   pin   5                ~{RAS}                       J4.1(Pin_1) Z68.14 Z72.5
   pin   6                Net-(Z21-Ea2)                Z21.14(Eb1) Z21.2(Ea2)
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                Net-(Z73-Pad8)               Z74.5
   pin   9                Net-(Z73-Pad9)               Z74.8
   pin  10                Net-(Z73-Pad10)              Z74.11
   pin  11                unconnected-(Z73-Pad11)      (no other connection)
   pin  12                +5V                          [net +5V, 134 pins]
   pin  13                +5V                          [net +5V, 134 pins]
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z74  (74LS00, CPU)
   pin   1                Net-(Z40-~{RD})              Z23.5 Z23.9 Z40.21(~{RD}) Z53.5
   pin   2                Net-(Z40-~{WR})              Z23.1 Z23.13 Z40.22(~{WR})
   pin   3                MREQ                         Z69.1(~{R}) Z69.13(~{R}) Z69.2(D) Z70.1(~{R})
   pin   4                Net-(Z52-Pad12)              Z52.12
   pin   5                Net-(Z73-Pad8)               Z73.8
   pin   6                ~{MEM}                       Z67.1 Z68.1
   pin   7 GND            GND                          [net GND, 204 pins]
   pin   8                Net-(Z73-Pad9)               Z73.9
   pin   9                ~{ROMA}                      R61.1 Z3.7 Z3.8 Z33.20(~{OE})
   pin  10                ~{RAM}                       R62.1 Z3.12 Z3.13 Z3.14 Z3.15 Z71.12 Z71.4
   pin  11                Net-(Z73-Pad10)              Z73.10
   pin  12                ~{ROMB}                      R68.1 Z3.1 Z3.6 Z34.20(~{CE1}) Z74.13
   pin  13                ~{ROMB}                      R68.1 Z3.1 Z3.6 Z34.20(~{CE1}) Z74.12
   pin  14 VCC            +5V                          [net +5V, 134 pins]

Z75  (74LS367, CPU Gating)
   pin   1                ~{DBOUT}                     Z53.10 Z53.6 Z53.9 Z75.15 Z76.15
   pin   2                ZD5                          Z40.9(D5) Z55.7
   pin   3                D5                           J100.12(Pin_12) J4.28(Pin_28) Z20.2(IN) Z55.6 Z60.7 Z62.11(IN) Z67.3
   pin   4                ZD3                          Z40.8(D3) Z55.5
   pin   5                D3                           J100.13(Pin_13) J4.26(Pin_26) Z19.2(IN) Z44.9 Z45.11(IN) Z55.4 Z59.13(D3) Z68.7
   pin   6                ZD4                          Z40.7(D4) Z55.3
   pin   7                D4                           J100.18(Pin_18) J4.18(Pin_18) Z15.2(IN) Z55.2 Z60.9 Z61.11(IN) Z67.9
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                D6                           J100.15(Pin_15) J4.24(Pin_24) Z14.2(IN) Z44.13 Z55.10 Z60.5 Z67.5
   pin  10                ZD6                          Z40.10(D6) Z55.9
   pin  11                D7                           J100.17(Pin_17) J4.20(Pin_20) Z13.2(IN) Z44.11 Z60.3 Z63.11(IN) Z67.7 Z76.6
   pin  12                ZD7                          Z40.13(D7) Z76.7
   pin  13                D2                           J100.10(Pin_10) J4.32(Pin_32) Z18.2(IN) Z44.3 Z46.11(IN) Z59.12(D2) Z68.5 Z76.4
   pin  14                ZD2                          Z40.12(D2) Z76.5
   pin  15                ~{DBOUT}                     Z53.10 Z53.6 Z53.9 Z75.1 Z76.15
   pin  16 VCC            +5V                          [net +5V, 134 pins]

Z76  (74LS367, CPU Gating)
   pin   1                ~{DBIN}                      Z53.8 Z55.1
   pin   2                D1                           J100.16(Pin_16) J4.22(Pin_22) Z16.2(IN) Z44.5 Z47.11(IN) Z59.5(D1) Z68.3 Z76.13
   pin   3                ZD1                          Z40.15(D1) Z76.14
   pin   4                D2                           J100.10(Pin_10) J4.32(Pin_32) Z18.2(IN) Z44.3 Z46.11(IN) Z59.12(D2) Z68.5 Z75.13
   pin   5                ZD2                          Z40.12(D2) Z75.14
   pin   6                D7                           J100.17(Pin_17) J4.20(Pin_20) Z13.2(IN) Z44.11 Z60.3 Z63.11(IN) Z67.7 Z75.11
   pin   7                ZD7                          Z40.13(D7) Z75.12
   pin   8 GND            GND                          [net GND, 204 pins]
   pin   9                ZD0                          Z40.14(D0) Z76.12
   pin  10                D0                           J100.11(Pin_11) J4.30(Pin_30) Z17.2(IN) Z44.7 Z48.11(IN) Z59.4(D0) Z68.9 Z76.11
   pin  11                D0                           J100.11(Pin_11) J4.30(Pin_30) Z17.2(IN) Z44.7 Z48.11(IN) Z59.4(D0) Z68.9 Z76.10
   pin  12                ZD0                          Z40.14(D0) Z76.9
   pin  13                D1                           J100.16(Pin_16) J4.22(Pin_22) Z16.2(IN) Z44.5 Z47.11(IN) Z59.5(D1) Z68.3 Z76.2
   pin  14                ZD1                          Z40.15(D1) Z76.3
   pin  15                ~{DBOUT}                     Z53.10 Z53.6 Z53.9 Z75.1 Z75.15
   pin  16 VCC            +5V                          [net +5V, 134 pins]

```
## Nets

```
+12V   (19 pins)
    C11      10uF 16V           pin   1  
    C15      0.01uF 24V         pin   1  
    C28      0.1uF 25V          pin   1  
    C30      0.1uF 25V          pin   1  
    C32      0.1uF 25V          pin   1  
    C34      0.1uF 25V          pin   1  
    R13      2.2k               pin   1  
    R18      5.6                pin   1  
    Z1       LM723C             pin  11  VC
    Z1       LM723C             pin  12  V+
    Z13      4116               pin   8  VDD
    Z14      4116               pin   8  VDD
    Z15      4116               pin   8  VDD
    Z16      4116               pin   8  VDD
    Z17      4116               pin   8  VDD
    Z18      4116               pin   8  VDD
    Z19      4116               pin   8  VDD
    Z2       LM723C             pin   3  CSEN
    Z20      4116               pin   8  VDD

+5V   (134 pins)
    C10      10uF 16V           pin   1  
    C14      0.01uF 24V         pin   1  
    C22      0.1uF 12V          pin   1  
    C23      0.1uF 12V          pin   1  
    C29      0.1uF 12V          pin   1  
    C31      0.1uF 12V          pin   1  
    C33      0.1uF 12V          pin   1  
    C35      0.1uF 12V          pin   1  
    C36      0.1uF 12V          pin   1  
    C37      0.1uF 12V          pin   1  
    C38      0.1uF 12V          pin   1  
    C40      0.1uF 12V          pin   1  
    C41      0.1uF 12V          pin   1  
    C44      0.1uF 12V          pin   1  
    C45      0.1uF 12V          pin   1  
    C46      0.1uF 12V          pin   1  
    C47      0.1uF 12V          pin   1  
    C48      0.1uF 12V          pin   1  
    C49      0.1uF 12V          pin   1  
    C50      0.1uF 12V          pin   1  
    C51      0.1uF 12V          pin   1  
    C52      0.1uF 12V          pin   1  
    C53      0.1uF 12V          pin   1  
    C54      0.1uF 12V          pin   1  
    C55      0.1uF 12V          pin   1  
    C56      0.1uF 12V          pin   1  
    C58      0.1uF 12V          pin   1  
    CR1      1N4735             pin   1  K
    CR3      1N4148             pin   1  K
    J100     Connection Mainboard Side pin   1  Pin_1
    J2       Front View         pin   1  
    K1       Relay_SPST-NO      pin   1  
    Q2       2N3906             pin   1  E
    R30      47                 pin   1  
    R31      10                 pin   2  
    R32      10k                pin   2  
    R39      4.7k               pin   2  
    R4       0.33               pin   2  
    R40      4.7k               pin   2  
    R47      10k                pin   1  
    R48      4.7k               pin   2  
    R49      4.7k               pin   1  
    R50      4.7k               pin   1  
    R51      4.7k               pin   1  
    R56      220k               pin   2  
    R57      4.7k               pin   1  
    R58      4.7k               pin   1  
    R59      4.7k               pin   1  
    R60      4.7k               pin   1  
    R61      4.7k               pin   2  
    R62      4.7k               pin   2  
    R63      4.7k               pin   1  
    R64      330                pin   1  
    R65      10k                pin   1  
    R66      4.7k               pin   1  
    R67      4.7k               pin   1  
    R68      4.7k               pin   2  
    R69      4.7k               pin   1  
    R7       1.2k               pin   1  
    R8       100k               pin   2  
    Z1       LM723C             pin   3  CSEN
    Z10      74LS166            pin  16  VCC
    Z11      74LS166            pin  16  VCC
    Z12      74LS93             pin   5  VCC
    Z13      4116               pin   9  VCC
    Z14      4116               pin   9  VCC
    Z15      4116               pin   9  VCC
    Z16      4116               pin   9  VCC
    Z17      4116               pin   9  VCC
    Z18      4116               pin   9  VCC
    Z19      4116               pin   9  VCC
    Z20      4116               pin   9  VCC
    Z21      74LS156            pin  16  VCC
    Z22      74LS367            pin  16  VCC
    Z23      74LS32             pin  14  VCC
    Z24      74LS132            pin  14  VCC
    Z25      74LS32             pin  14  VCC
    Z26      74LS20             pin  14  VCC
    Z27      74LS175            pin  16  VCC
    Z28      74LS174            pin  16  VCC
    Z29      MCM6670            pin  18  VCC
    Z30      74LS02             pin  14  VCC
    Z31      74LS157            pin  16  VCC
    Z32      74LS93             pin   5  VCC
    Z33      2364_20L           pin  24  VCC
    Z34      2332_20L_21L       pin  24  VCC
    Z35      74LS157            pin  16  VCC
    Z36      74LS32             pin  14  VCC
    Z37      74LS02             pin  14  VCC
    Z38      74LS367            pin  16  VCC
    Z39      74LS367            pin  16  VCC
    Z40      Z80CPU             pin  11  VCC
    Z41      75452              pin   8  VCC
    Z42      74LS04             pin  14  VCC
    Z43      74LS157            pin  16  VCC
    Z44      74LS367            pin  16  VCC
    Z45      2102               pin  10  VCC
    Z46      2102               pin  10  VCC
    Z47      2102               pin  10  VCC
    Z48      2102               pin  10  VCC
    Z49      74LS157            pin  16  VCC
    Z5       74C00              pin  14  VCC
    Z50      74LS93             pin   5  VCC
    Z51      74LS157            pin  16  VCC
    Z52      74LS04             pin  14  VCC
    Z53      74LS132            pin  14  VCC
    Z54      74LS30             pin  14  VCC
    Z55      74LS367            pin  16  VCC
    Z56      74LS92             pin   5  VCC
    Z57      74C04              pin  14  VCC
    Z58      74LS92             pin   5  VCC
    Z59      74LS175            pin  16  VCC
    Z6       74C04              pin  14  VCC
    Z60      74LS367            pin  16  VCC
    Z61      2102               pin  10  VCC
    Z62      2102               pin  10  VCC
    Z63      2102               pin  10  VCC
    Z64      74LS157            pin  16  VCC
    Z65      74LS93             pin   5  VCC
    Z66      74LS11             pin  14  VCC
    Z67      74LS367            pin  16  VCC
    Z68      74LS367            pin  16  VCC
    Z69      74LS74             pin  14  VCC
    Z7       74LS74             pin  14  VCC
    Z70      74LS74             pin  14  VCC
    Z72      74LS367            pin  16  VCC
    Z73      74LS32             pin  12  
    Z73      74LS32             pin  13  
    Z73      74LS32             pin  14  VCC
    Z74      74LS00             pin  14  VCC
    Z75      74LS367            pin  16  VCC
    Z76      74LS367            pin  16  VCC
    Z8       74LS153            pin  16  VCC
    Z9       74LS04             pin  14  VCC

-5V   (16 pins)
    C16      0.1uF 12V          pin   1  
    C17      0.1uF 12V          pin   1  
    C18      0.1uF 12V          pin   1  
    C19      0.1uF 12V          pin   1  
    C3       0.01uF 24V         pin   1  
    C4       10uF 16V           pin   2  
    CR2      1N5231             pin   2  A
    R19      220                pin   1  
    Z13      4116               pin   1  VBB
    Z14      4116               pin   1  VBB
    Z15      4116               pin   1  VBB
    Z16      4116               pin   1  VBB
    Z17      4116               pin   1  VBB
    Z18      4116               pin   1  VBB
    Z19      4116               pin   1  VBB
    Z20      4116               pin   1  VBB

/A0   (8 pins)
    J100     Connection Mainboard Side pin   5  Pin_5
    J4       Edge Connector     pin  25  Pin_25
    Z33      2364_20L           pin   8  A0
    Z34      2332_20L_21L       pin   8  A0
    Z35      74LS157            pin   2  I0a
    Z52      74LS04             pin   5  
    Z55      74LS367            pin  11  
    Z64      74LS157            pin  11  I0c

/A1   (8 pins)
    J100     Connection Mainboard Side pin   4  Pin_4
    J4       Edge Connector     pin  27  Pin_27
    Z33      2364_20L           pin   7  A1
    Z34      2332_20L_21L       pin   7  A1
    Z35      74LS157            pin   5  I0b
    Z54      74LS30             pin  11  
    Z55      74LS367            pin  13  
    Z64      74LS157            pin   2  I0a

/A10   (7 pins)
    J4       Edge Connector     pin   4  Pin_4
    Z33      2364_20L           pin  19  A10
    Z34      2332_20L_21L       pin  19  A10
    Z36      74LS32             pin  13  
    Z38      74LS367            pin   3  
    Z51      74LS157            pin   3  I1a
    Z52      74LS04             pin   1  

/A11   (7 pins)
    J4       Edge Connector     pin   9  Pin_9
    Z33      2364_20L           pin  18  A11
    Z34      2332_20L_21L       pin  18  A11
    Z37      74LS02             pin   5  
    Z37      74LS02             pin   6  
    Z38      74LS367            pin  13  
    Z51      74LS157            pin   6  I1b

/A12   (6 pins)
    J4       Edge Connector     pin   5  Pin_5
    Z21      74LS156            pin  13  A0
    Z33      2364_20L           pin  21  A12
    Z34      2332_20L_21L       pin  21  ~{CE2}
    Z38      74LS367            pin   5  
    Z51      74LS157            pin  10  I1c

/A13   (4 pins)
    J4       Edge Connector     pin   6  Pin_6
    Z21      74LS156            pin   3  A1
    Z38      74LS367            pin   7  
    Z71      ~                  pin  16  

/A14   (4 pins)
    J4       Edge Connector     pin  10  Pin_10
    Z21      74LS156            pin   1  Ea1
    Z21      74LS156            pin  15  Eb2
    Z38      74LS367            pin  11  

/A15   (3 pins)
    J4       Edge Connector     pin   7  Pin_7
    Z38      74LS367            pin   9  
    Z73      74LS32             pin   4  

/A2   (8 pins)
    J100     Connection Mainboard Side pin   6  Pin_6
    J4       Edge Connector     pin  40  Pin_40
    Z22      74LS367            pin  11  
    Z33      2364_20L           pin   6  A2
    Z34      2332_20L_21L       pin   6  A2
    Z35      74LS157            pin  11  I0c
    Z54      74LS30             pin   2  
    Z64      74LS157            pin  14  I0d

/A3   (8 pins)
    J100     Connection Mainboard Side pin   9  Pin_9
    J4       Edge Connector     pin  34  Pin_34
    Z22      74LS367            pin  13  
    Z33      2364_20L           pin   5  A3
    Z34      2332_20L_21L       pin   5  A3
    Z35      74LS157            pin  14  I0d
    Z54      74LS30             pin   1  
    Z64      74LS157            pin   5  I0b

/A4   (8 pins)
    J100     Connection Mainboard Side pin   2  Pin_2
    J4       Edge Connector     pin  31  Pin_31
    Z33      2364_20L           pin   4  A4
    Z34      2332_20L_21L       pin   4  A4
    Z39      74LS367            pin   7  
    Z49      74LS157            pin  11  I0c
    Z51      74LS157            pin   2  I0a
    Z54      74LS30             pin   4  

/A5   (8 pins)
    J100     Connection Mainboard Side pin   3  Pin_3
    J4       Edge Connector     pin  35  Pin_35
    Z33      2364_20L           pin   3  A5
    Z34      2332_20L_21L       pin   3  A5
    Z39      74LS367            pin   9  
    Z49      74LS157            pin   2  I0a
    Z51      74LS157            pin   5  I0b
    Z54      74LS30             pin  12  

/A6   (9 pins)
    J100     Connection Mainboard Side pin   7  Pin_7
    J4       Edge Connector     pin  38  Pin_38
    Z31      74LS157            pin  11  I0c
    Z33      2364_20L           pin   2  A6
    Z34      2332_20L_21L       pin   2  A6
    Z39      74LS367            pin   5  
    Z51      74LS157            pin  11  I0c
    Z54      74LS30             pin   3  
    Z71      ~                  pin  15  

/A7   (9 pins)
    J100     Connection Mainboard Side pin   8  Pin_8
    J4       Edge Connector     pin  36  Pin_36
    Z31      74LS157            pin  14  I0d
    Z33      2364_20L           pin   1  A7
    Z34      2332_20L_21L       pin   1  A7
    Z35      74LS157            pin   6  I1b
    Z39      74LS367            pin  11  
    Z54      74LS30             pin   5  
    Z54      74LS30             pin   6  

/A8   (6 pins)
    J4       Edge Connector     pin  11  Pin_11
    Z31      74LS157            pin   2  I0a
    Z33      2364_20L           pin  23  A8
    Z34      2332_20L_21L       pin  23  A8
    Z35      74LS157            pin  10  I1c
    Z39      74LS367            pin   3  

/A9   (6 pins)
    J4       Edge Connector     pin  17  Pin_17
    Z31      74LS157            pin   5  I0b
    Z33      2364_20L           pin  22  A9
    Z34      2332_20L_21L       pin  22  A9
    Z35      74LS157            pin  13  I1d
    Z39      74LS367            pin  13  

/Address Decoder/~{KYBD}   (2 pins)
    J100     Connection Mainboard Side pin  14  Pin_14
    Z36      74LS32             pin  11  

/Address Decoder/~{MEM}   (3 pins)
    Z67      74LS367            pin   1  
    Z68      74LS367            pin   1  
    Z74      74LS00             pin   6  

/Address Decoder/~{RAM}   (8 pins)
    R62      4.7k               pin   1  
    Z3       ~                  pin  12  
    Z3       ~                  pin  13  
    Z3       ~                  pin  14  
    Z3       ~                  pin  15  
    Z71      ~                  pin   4  
    Z71      ~                  pin  12  
    Z74      74LS00             pin  10  

/Address Decoder/~{RAS}   (4 pins)
    J4       Edge Connector     pin   1  Pin_1
    Z68      74LS367            pin  14  
    Z72      74LS367            pin   5  
    Z73      74LS32             pin   5  

/Address Decoder/~{RD}   (4 pins)
    J4       Edge Connector     pin  15  Pin_15
    Z22      74LS367            pin   7  
    Z49      74LS157            pin   5  I0b
    Z52      74LS04             pin  13  

/Address Decoder/~{ROMA}   (5 pins)
    R61      4.7k               pin   1  
    Z3       ~                  pin   7  
    Z3       ~                  pin   8  
    Z33      2364_20L           pin  20  ~{OE}
    Z74      74LS00             pin   9  

/Address Decoder/~{ROMB}   (6 pins)
    R68      4.7k               pin   1  
    Z3       ~                  pin   1  
    Z3       ~                  pin   6  
    Z34      2332_20L_21L       pin  20  ~{CE1}
    Z74      74LS00             pin  12  
    Z74      74LS00             pin  13  

/Address Decoder/~{VID}   (5 pins)
    Z31      74LS157            pin   1  S
    Z36      74LS32             pin   8  
    Z49      74LS157            pin   1  S
    Z64      74LS157            pin   1  S
    Z7       74LS74             pin   4  ~{S}

/CPU Gating/MUX   (4 pins)
    J4       Edge Connector     pin  16  Pin_16
    Z35      74LS157            pin   1  S
    Z51      74LS157            pin   1  S
    Z72      74LS367            pin   3  

/CPU Gating/ZA0   (2 pins)
    Z40      Z80CPU             pin  30  A0
    Z55      74LS367            pin  12  

/CPU Gating/ZA1   (2 pins)
    Z40      Z80CPU             pin  31  A1
    Z55      74LS367            pin  14  

/CPU Gating/ZA10   (2 pins)
    Z38      74LS367            pin   2  
    Z40      Z80CPU             pin  40  A10

/CPU Gating/ZA11   (2 pins)
    Z38      74LS367            pin  14  
    Z40      Z80CPU             pin   1  A11

/CPU Gating/ZA12   (2 pins)
    Z38      74LS367            pin   4  
    Z40      Z80CPU             pin   2  A12

/CPU Gating/ZA13   (2 pins)
    Z38      74LS367            pin   6  
    Z40      Z80CPU             pin   3  A13

/CPU Gating/ZA14   (2 pins)
    Z38      74LS367            pin  12  
    Z40      Z80CPU             pin   4  A14

/CPU Gating/ZA15   (2 pins)
    Z38      74LS367            pin  10  
    Z40      Z80CPU             pin   5  A15

/CPU Gating/ZA2   (2 pins)
    Z22      74LS367            pin  12  
    Z40      Z80CPU             pin  32  A2

/CPU Gating/ZA3   (2 pins)
    Z22      74LS367            pin  14  
    Z40      Z80CPU             pin  33  A3

/CPU Gating/ZA4   (2 pins)
    Z39      74LS367            pin   6  
    Z40      Z80CPU             pin  34  A4

/CPU Gating/ZA5   (2 pins)
    Z39      74LS367            pin  10  
    Z40      Z80CPU             pin  35  A5

/CPU Gating/ZA6   (2 pins)
    Z39      74LS367            pin   4  
    Z40      Z80CPU             pin  36  A6

/CPU Gating/ZA7   (2 pins)
    Z39      74LS367            pin  12  
    Z40      Z80CPU             pin  37  A7

/CPU Gating/ZA8   (2 pins)
    Z39      74LS367            pin   2  
    Z40      Z80CPU             pin  38  A8

/CPU Gating/ZA9   (2 pins)
    Z39      74LS367            pin  14  
    Z40      Z80CPU             pin  39  A9

/CPU Gating/ZD0   (3 pins)
    Z40      Z80CPU             pin  14  D0
    Z76      74LS367            pin   9  
    Z76      74LS367            pin  12  

/CPU Gating/ZD1   (3 pins)
    Z40      Z80CPU             pin  15  D1
    Z76      74LS367            pin   3  
    Z76      74LS367            pin  14  

/CPU Gating/ZD2   (3 pins)
    Z40      Z80CPU             pin  12  D2
    Z75      74LS367            pin  14  
    Z76      74LS367            pin   5  

/CPU Gating/ZD3   (3 pins)
    Z40      Z80CPU             pin   8  D3
    Z55      74LS367            pin   5  
    Z75      74LS367            pin   4  

/CPU Gating/ZD4   (3 pins)
    Z40      Z80CPU             pin   7  D4
    Z55      74LS367            pin   3  
    Z75      74LS367            pin   6  

/CPU Gating/ZD5   (3 pins)
    Z40      Z80CPU             pin   9  D5
    Z55      74LS367            pin   7  
    Z75      74LS367            pin   2  

/CPU Gating/ZD6   (3 pins)
    Z40      Z80CPU             pin  10  D6
    Z55      74LS367            pin   9  
    Z75      74LS367            pin  10  

/CPU Gating/ZD7   (3 pins)
    Z40      Z80CPU             pin  13  D7
    Z75      74LS367            pin  12  
    Z76      74LS367            pin   7  

/CPU Gating/ZMUX   (3 pins)
    Z69      74LS74             pin   9  Q
    Z70      74LS74             pin   2  D
    Z72      74LS367            pin   2  

/CPU Gating/~{CAS}   (3 pins)
    J4       Edge Connector     pin   3  Pin_3
    Z67      74LS367            pin  14  
    Z72      74LS367            pin   9  

/CPU Gating/~{DBIN}   (3 pins)
    Z53      74LS132            pin   8  
    Z55      74LS367            pin   1  
    Z76      74LS367            pin   1  

/CPU Gating/~{DBOUT}   (6 pins)
    Z53      74LS132            pin   6  
    Z53      74LS132            pin   9  
    Z53      74LS132            pin  10  
    Z75      74LS367            pin   1  
    Z75      74LS367            pin  15  
    Z76      74LS367            pin  15  

/CPU Gating/~{IN}   (3 pins)
    J4       Edge Connector     pin  19  Pin_19
    Z22      74LS367            pin   9  
    Z25      74LS32             pin   4  

/CPU Gating/~{OUT}   (3 pins)
    J4       Edge Connector     pin  12  Pin_12
    Z22      74LS367            pin   3  
    Z25      74LS32             pin   9  

/CPU Gating/~{TEST}   (5 pins)
    J4       Edge Connector     pin  23  Pin_23
    R58      4.7k               pin   2  
    Z40      Z80CPU             pin  25  ~{BUSRQ}
    Z52      74LS04             pin   3  
    Z53      74LS132            pin   4  

/CPU Gating/~{WR}   (11 pins)
    J4       Edge Connector     pin  13  Pin_13
    Z13      4116               pin   3  ~{WR}
    Z14      4116               pin   3  ~{WR}
    Z15      4116               pin   3  ~{WR}
    Z16      4116               pin   3  ~{WR}
    Z17      4116               pin   3  ~{WR}
    Z18      4116               pin   3  ~{WR}
    Z19      4116               pin   3  ~{WR}
    Z20      4116               pin   3  ~{WR}
    Z22      74LS367            pin   5  
    Z49      74LS157            pin  14  I0d

/CPU Gating/~{ZCAS}   (2 pins)
    Z70      74LS74             pin   6  ~{Q}
    Z72      74LS367            pin  10  

/CPU Gating/~{ZIN}   (2 pins)
    Z22      74LS367            pin  10  
    Z23      74LS32             pin   8  

/CPU Gating/~{ZOUT}   (2 pins)
    Z22      74LS367            pin   2  
    Z23      74LS32             pin   3  

/CPU Gating/~{ZRAS}   (4 pins)
    Z23      74LS32             pin   4  
    Z23      74LS32             pin  12  
    Z40      Z80CPU             pin  19  ~{MREQ}
    Z72      74LS367            pin   4  

/CPU Gating/~{ZRD}   (2 pins)
    Z22      74LS367            pin   6  
    Z23      74LS32             pin   6  

/CPU Gating/~{ZWR}   (2 pins)
    Z22      74LS367            pin   4  
    Z23      74LS32             pin  11  

/CPU/CLK   (7 pins)
    Z42      74LS04             pin   6  
    Z43      74LS157            pin   3  I1a
    Z56      74LS92             pin   1  CP1..3
    Z69      74LS74             pin   3  C
    Z69      74LS74             pin  11  C
    Z70      74LS74             pin   3  C
    Z70      74LS74             pin  11  C

/CPU/HI   (5 pins)
    R69      4.7k               pin   2  
    Z69      74LS74             pin   4  ~{S}
    Z69      74LS74             pin  10  ~{S}
    Z70      74LS74             pin   4  ~{S}
    Z70      74LS74             pin  10  ~{S}

/CPU/MREQ   (5 pins)
    Z69      74LS74             pin   1  ~{R}
    Z69      74LS74             pin   2  D
    Z69      74LS74             pin  13  ~{R}
    Z70      74LS74             pin   1  ~{R}
    Z74      74LS00             pin   3  

/CPU/ZCLK   (3 pins)
    R64      330                pin   2  
    Z40      Z80CPU             pin   6  ~{CLK}
    Z72      74LS367            pin  11  

/CPU/~{CLK_EN}   (5 pins)
    Z42      74LS04             pin   8  
    Z56      74LS92             pin   6  R0(1)
    Z56      74LS92             pin   7  R0(2)
    Z58      74LS92             pin   6  R0(1)
    Z58      74LS92             pin   7  R0(2)

/CPU/~{INTAK}   (2 pins)
    J4       Edge Connector     pin  14  Pin_14
    Z73      74LS32             pin   3  

/CPU/~{INT}   (3 pins)
    J4       Edge Connector     pin  21  Pin_21
    R50      4.7k               pin   2  
    Z40      Z80CPU             pin  16  ~{INT}

/CPU/~{SYSRES}   (2 pins)
    J4       Edge Connector     pin   2  Pin_2
    Z37      74LS02             pin   1  

/CPU/~{WAIT}   (3 pins)
    J4       Edge Connector     pin  33  Pin_33
    R51      4.7k               pin   2  
    Z40      Z80CPU             pin  24  ~{WAIT}

/Cassette Interface/CASSIN   (3 pins)
    C24      220pF              pin   1  
    C_R67    220                pin   2  
    J3       Front View         pin   4  

/Cassette Interface/CASSOUT   (4 pins)
    J3       Front View         pin   5  
    R53      1.2k               pin   2  
    R54      7.5k               pin   2  
    R55      7.5k               pin   1  

/Cassette Interface/MODESEL   (3 pins)
    Z43      74LS157            pin   1  S
    Z44      74LS367            pin  14  
    Z59      74LS175            pin  14  ~{Q3}

/Cassette Interface/~{INSIG}   (2 pins)
    Z25      74LS32             pin   6  
    Z44      74LS367            pin  15  

/Cassette Interface/~{OUTSIG}   (3 pins)
    Z24      74LS132            pin  13  
    Z25      74LS32             pin   8  
    Z59      74LS175            pin   9  Cp

/D0   (9 pins)
    J100     Connection Mainboard Side pin  11  Pin_11
    J4       Edge Connector     pin  30  Pin_30
    Z17      4116               pin   2  IN
    Z44      74LS367            pin   7  
    Z48      2102               pin  11  IN
    Z59      74LS175            pin   4  D0
    Z68      74LS367            pin   9  
    Z76      74LS367            pin  10  
    Z76      74LS367            pin  11  

/D1   (9 pins)
    J100     Connection Mainboard Side pin  16  Pin_16
    J4       Edge Connector     pin  22  Pin_22
    Z16      4116               pin   2  IN
    Z44      74LS367            pin   5  
    Z47      2102               pin  11  IN
    Z59      74LS175            pin   5  D1
    Z68      74LS367            pin   3  
    Z76      74LS367            pin   2  
    Z76      74LS367            pin  13  

/D2   (9 pins)
    J100     Connection Mainboard Side pin  10  Pin_10
    J4       Edge Connector     pin  32  Pin_32
    Z18      4116               pin   2  IN
    Z44      74LS367            pin   3  
    Z46      2102               pin  11  IN
    Z59      74LS175            pin  12  D2
    Z68      74LS367            pin   5  
    Z75      74LS367            pin  13  
    Z76      74LS367            pin   4  

/D3   (9 pins)
    J100     Connection Mainboard Side pin  13  Pin_13
    J4       Edge Connector     pin  26  Pin_26
    Z19      4116               pin   2  IN
    Z44      74LS367            pin   9  
    Z45      2102               pin  11  IN
    Z55      74LS367            pin   4  
    Z59      74LS175            pin  13  D3
    Z68      74LS367            pin   7  
    Z75      74LS367            pin   5  

/D4   (8 pins)
    J100     Connection Mainboard Side pin  18  Pin_18
    J4       Edge Connector     pin  18  Pin_18
    Z15      4116               pin   2  IN
    Z55      74LS367            pin   2  
    Z60      74LS367            pin   9  
    Z61      2102               pin  11  IN
    Z67      74LS367            pin   9  
    Z75      74LS367            pin   7  

/D5   (8 pins)
    J100     Connection Mainboard Side pin  12  Pin_12
    J4       Edge Connector     pin  28  Pin_28
    Z20      4116               pin   2  IN
    Z55      74LS367            pin   6  
    Z60      74LS367            pin   7  
    Z62      2102               pin  11  IN
    Z67      74LS367            pin   3  
    Z75      74LS367            pin   3  

/D6   (8 pins)
    J100     Connection Mainboard Side pin  15  Pin_15
    J4       Edge Connector     pin  24  Pin_24
    Z14      4116               pin   2  IN
    Z44      74LS367            pin  13  
    Z55      74LS367            pin  10  
    Z60      74LS367            pin   5  
    Z67      74LS367            pin   5  
    Z75      74LS367            pin   9  

/D7   (9 pins)
    J100     Connection Mainboard Side pin  17  Pin_17
    J4       Edge Connector     pin  20  Pin_20
    Z13      4116               pin   2  IN
    Z44      74LS367            pin  11  
    Z60      74LS367            pin   3  
    Z63      2102               pin  11  IN
    Z67      74LS367            pin   7  
    Z75      74LS367            pin  11  
    Z76      74LS367            pin   6  

/RAM-ROM Interface/ROMD0   (4 pins)
    Z17      4116               pin  14  OUT
    Z33      2364_20L           pin   9  D0
    Z34      2332_20L_21L       pin   9  D0
    Z68      74LS367            pin  10  

/RAM-ROM Interface/ROMD1   (4 pins)
    Z16      4116               pin  14  OUT
    Z33      2364_20L           pin  10  D1
    Z34      2332_20L_21L       pin  10  D1
    Z68      74LS367            pin   2  

/RAM-ROM Interface/ROMD2   (4 pins)
    Z18      4116               pin  14  OUT
    Z33      2364_20L           pin  11  D2
    Z34      2332_20L_21L       pin  11  D2
    Z68      74LS367            pin   4  

/RAM-ROM Interface/ROMD3   (4 pins)
    Z19      4116               pin  14  OUT
    Z33      2364_20L           pin  13  D3
    Z34      2332_20L_21L       pin  13  D3
    Z68      74LS367            pin   6  

/RAM-ROM Interface/ROMD4   (4 pins)
    Z15      4116               pin  14  OUT
    Z33      2364_20L           pin  14  D4
    Z34      2332_20L_21L       pin  14  D4
    Z67      74LS367            pin  10  

/RAM-ROM Interface/ROMD5   (4 pins)
    Z20      4116               pin  14  OUT
    Z33      2364_20L           pin  15  D5
    Z34      2332_20L_21L       pin  15  D5
    Z67      74LS367            pin   2  

/RAM-ROM Interface/ROMD6   (4 pins)
    Z14      4116               pin  14  OUT
    Z33      2364_20L           pin  16  D6
    Z34      2332_20L_21L       pin  16  D6
    Z67      74LS367            pin   4  

/RAM-ROM Interface/ROMD7   (4 pins)
    Z13      4116               pin  14  OUT
    Z33      2364_20L           pin  17  D7
    Z34      2332_20L_21L       pin  17  D7
    Z67      74LS367            pin   6  

/Video/Video Access Multiplexer/C0   (2 pins)
    Z43      74LS157            pin   7  Zb
    Z64      74LS157            pin  10  I1c

/Video/Video Access Multiplexer/C1   (2 pins)
    Z64      74LS157            pin   3  I1a
    Z65      74LS93             pin   9  Q1

/Video/Video Access Multiplexer/C2   (3 pins)
    Z50      74LS93             pin  14  CP0
    Z64      74LS157            pin  13  I1d
    Z65      74LS93             pin   8  Q2

/Video/Video Access Multiplexer/C3   (3 pins)
    Z50      74LS93             pin   1  CP1..3
    Z50      74LS93             pin  12  Q0
    Z64      74LS157            pin   6  I1b

/Video/Video Access Multiplexer/C4   (3 pins)
    Z49      74LS157            pin  10  I1c
    Z50      74LS93             pin   9  Q1
    Z66      74LS11             pin   3  

/Video/Video Access Multiplexer/C5   (3 pins)
    Z49      74LS157            pin   3  I1a
    Z50      74LS93             pin   8  Q2
    Z66      74LS11             pin   5  

/Video/Video Access Multiplexer/R0   (3 pins)
    Z31      74LS157            pin  10  I1c
    Z32      74LS93             pin  14  CP0
    Z65      74LS93             pin  12  Q0

/Video/Video Access Multiplexer/R1   (4 pins)
    Z31      74LS157            pin  13  I1d
    Z32      74LS93             pin   1  CP1..3
    Z32      74LS93             pin  12  Q0
    Z66      74LS11             pin  13  

/Video/Video Access Multiplexer/R2   (3 pins)
    Z31      74LS157            pin   3  I1a
    Z32      74LS93             pin   9  Q1
    Z66      74LS11             pin   2  

/Video/Video Access Multiplexer/R3   (2 pins)
    Z31      74LS157            pin   6  I1b
    Z32      74LS93             pin   8  Q2

/Video/Video Access Multiplexer/VA0   (8 pins)
    Z45      2102               pin   8  A0
    Z46      2102               pin   8  A0
    Z47      2102               pin   8  A0
    Z48      2102               pin   8  A0
    Z61      2102               pin   8  A0
    Z62      2102               pin   8  A0
    Z63      2102               pin   8  A0
    Z64      74LS157            pin   9  Zc

/Video/Video Access Multiplexer/VA1   (8 pins)
    Z45      2102               pin   4  A1
    Z46      2102               pin   4  A1
    Z47      2102               pin   4  A1
    Z48      2102               pin   4  A1
    Z61      2102               pin   4  A1
    Z62      2102               pin   4  A1
    Z63      2102               pin   4  A1
    Z64      74LS157            pin   4  Za

/Video/Video Access Multiplexer/VA2   (8 pins)
    Z45      2102               pin   5  A2
    Z46      2102               pin   5  A2
    Z47      2102               pin   5  A2
    Z48      2102               pin   5  A2
    Z61      2102               pin   5  A2
    Z62      2102               pin   5  A2
    Z63      2102               pin   5  A2
    Z64      74LS157            pin  12  Zd

/Video/Video Access Multiplexer/VA3   (8 pins)
    Z45      2102               pin   6  A3
    Z46      2102               pin   6  A3
    Z47      2102               pin   6  A3
    Z48      2102               pin   6  A3
    Z61      2102               pin   6  A3
    Z62      2102               pin   6  A3
    Z63      2102               pin   6  A3
    Z64      74LS157            pin   7  Zb

/Video/Video Access Multiplexer/VA4   (8 pins)
    Z45      2102               pin   7  A4
    Z46      2102               pin   7  A4
    Z47      2102               pin   7  A4
    Z48      2102               pin   7  A4
    Z49      74LS157            pin   9  Zc
    Z61      2102               pin   7  A4
    Z62      2102               pin   7  A4
    Z63      2102               pin   7  A4

/Video/Video Access Multiplexer/VA5   (8 pins)
    Z45      2102               pin   2  A5
    Z46      2102               pin   2  A5
    Z47      2102               pin   2  A5
    Z48      2102               pin   2  A5
    Z49      74LS157            pin   4  Za
    Z61      2102               pin   2  A5
    Z62      2102               pin   2  A5
    Z63      2102               pin   2  A5

/Video/Video Access Multiplexer/VA6   (8 pins)
    Z31      74LS157            pin   9  Zc
    Z45      2102               pin   1  A6
    Z46      2102               pin   1  A6
    Z47      2102               pin   1  A6
    Z48      2102               pin   1  A6
    Z61      2102               pin   1  A6
    Z62      2102               pin   1  A6
    Z63      2102               pin   1  A6

/Video/Video Access Multiplexer/VA7   (8 pins)
    Z31      74LS157            pin  12  Zd
    Z45      2102               pin  16  A7
    Z46      2102               pin  16  A7
    Z47      2102               pin  16  A7
    Z48      2102               pin  16  A7
    Z61      2102               pin  16  A7
    Z62      2102               pin  16  A7
    Z63      2102               pin  16  A7

/Video/Video Access Multiplexer/VA8   (8 pins)
    Z31      74LS157            pin   4  Za
    Z45      2102               pin  15  A8
    Z46      2102               pin  15  A8
    Z47      2102               pin  15  A8
    Z48      2102               pin  15  A8
    Z61      2102               pin  15  A8
    Z62      2102               pin  15  A8
    Z63      2102               pin  15  A8

/Video/Video Access Multiplexer/VA9   (8 pins)
    Z31      74LS157            pin   7  Zb
    Z45      2102               pin  14  A9
    Z46      2102               pin  14  A9
    Z47      2102               pin  14  A9
    Z48      2102               pin  14  A9
    Z61      2102               pin  14  A9
    Z62      2102               pin  14  A9
    Z63      2102               pin  14  A9

/Video/Video Access Multiplexer/~{VRD}   (3 pins)
    Z44      74LS367            pin   1  
    Z49      74LS157            pin   7  Zb
    Z60      74LS367            pin   1  

/Video/Video Access Multiplexer/~{VWR}   (8 pins)
    Z45      2102               pin   3  R/~{W}
    Z46      2102               pin   3  R/~{W}
    Z47      2102               pin   3  R/~{W}
    Z48      2102               pin   3  R/~{W}
    Z49      74LS157            pin  12  Zd
    Z61      2102               pin   3  R/~{W}
    Z62      2102               pin   3  R/~{W}
    Z63      2102               pin   3  R/~{W}

/Video/Video Counter/HDRV   (5 pins)
    Z12      74LS93             pin  14  CP0
    Z30      74LS02             pin   8  
    Z50      74LS93             pin  11  Q3
    Z6       74C04              pin  13  
    Z66      74LS11             pin   4  

/Video/Video Counter/L0   (3 pins)
    Z12      74LS93             pin   1  CP1..3
    Z12      74LS93             pin  12  Q0
    Z29      MCM6670            pin  11  R0

/Video/Video Counter/L1   (2 pins)
    Z12      74LS93             pin   9  Q1
    Z29      MCM6670            pin  10  R1

/Video/Video Counter/L2   (5 pins)
    Z12      74LS93             pin   8  Q2
    Z29      MCM6670            pin   8  R2
    Z66      74LS11             pin   9  
    Z66      74LS11             pin  10  
    Z8       74LS153            pin  14  S0

/Video/Video Counter/L3   (5 pins)
    Z12      74LS93             pin  11  Q3
    Z27      74LS175            pin  12  D2
    Z65      74LS93             pin  14  CP0
    Z66      74LS11             pin  11  
    Z8       74LS153            pin   2  S1

/Video/Video Counter/SHIFT   (3 pins)
    Z43      74LS157            pin   4  Za
    Z58      74LS92             pin  14  CP0
    Z9       74LS04             pin   9  

/Video/Video Counter/VDRV   (4 pins)
    Z30      74LS02             pin   9  
    Z32      74LS93             pin  11  Q3
    Z57      74C04              pin   1  
    Z66      74LS11             pin   1  

/Video/Video Counter/~{LATCH}   (5 pins)
    Z24      74LS132            pin   3  
    Z27      74LS175            pin   9  Cp
    Z28      74LS174            pin   9  Cp
    Z7       74LS74             pin   3  C
    Z9       74LS04             pin   3  

/Video/Video Generator/GRAPHICS   (2 pins)
    Z26      74LS20             pin   4  
    Z27      74LS175            pin   3  ~{Q0}

/Video/Video Generator/LB0   (3 pins)
    Z28      74LS174            pin  15  Q5
    Z29      MCM6670            pin   7  A0
    Z8       74LS153            pin   6  I0a

/Video/Video Generator/LB1   (3 pins)
    Z28      74LS174            pin  12  Q4
    Z29      MCM6670            pin   6  A1
    Z8       74LS153            pin  10  I0b

/Video/Video Generator/LB2   (3 pins)
    Z28      74LS174            pin   2  Q0
    Z29      MCM6670            pin   5  A2
    Z8       74LS153            pin   5  I1a

/Video/Video Generator/LB3   (3 pins)
    Z28      74LS174            pin   7  Q2
    Z29      MCM6670            pin   4  A3
    Z8       74LS153            pin  11  I1b

/Video/Video Generator/LB4   (3 pins)
    Z28      74LS174            pin   5  Q1
    Z29      MCM6670            pin   3  A4
    Z8       74LS153            pin   4  I2a

/Video/Video Generator/LB5   (3 pins)
    Z28      74LS174            pin  10  Q3
    Z29      MCM6670            pin   2  A5
    Z8       74LS153            pin  12  I2b

/Video/Video Generator/LB6   (2 pins)
    Z27      74LS175            pin  15  Q3
    Z29      MCM6670            pin   1  A6

/Video/Video Generator/PIXEL   (3 pins)
    Z30      74LS02             pin   1  
    Z41      75452              pin   6  2A
    Z41      75452              pin   7  2B

/Video/Video Generator/~{BLANK}   (4 pins)
    Z26      74LS20             pin   1  
    Z26      74LS20             pin   2  
    Z26      74LS20             pin   9  
    Z27      74LS175            pin   7  Q1

/Video/Video Generator/~{CHARGAP}   (2 pins)
    Z26      74LS20             pin  12  
    Z27      74LS175            pin  11  ~{Q2}

/Video/Video Generator/~{GRAPHICS}   (2 pins)
    Z26      74LS20             pin  10  
    Z27      74LS175            pin   2  Q0

/Video/Video Latch/VD0   (3 pins)
    Z28      74LS174            pin  14  D5
    Z44      74LS367            pin   6  
    Z48      2102               pin  12  OUT

/Video/Video Latch/VD1   (3 pins)
    Z28      74LS174            pin  13  D4
    Z44      74LS367            pin   4  
    Z47      2102               pin  12  OUT

/Video/Video Latch/VD2   (3 pins)
    Z28      74LS174            pin   3  D0
    Z44      74LS367            pin   2  
    Z46      2102               pin  12  OUT

/Video/Video Latch/VD3   (3 pins)
    Z28      74LS174            pin   6  D2
    Z44      74LS367            pin  10  
    Z45      2102               pin  12  OUT

/Video/Video Latch/VD4   (3 pins)
    Z28      74LS174            pin   4  D1
    Z60      74LS367            pin  10  
    Z61      2102               pin  12  OUT

/Video/Video Latch/VD5   (4 pins)
    Z28      74LS174            pin  11  D3
    Z30      74LS02             pin  12  
    Z60      74LS367            pin   6  
    Z62      2102               pin  12  OUT

/Video/Video Latch/VD6   (3 pins)
    Z27      74LS175            pin  13  D3
    Z30      74LS02             pin  13  
    Z60      74LS367            pin   4  

/Video/Video Latch/VD7   (4 pins)
    Z30      74LS02             pin  11  
    Z42      74LS04             pin  13  
    Z60      74LS367            pin   2  
    Z63      2102               pin  12  OUT

/Video/Video Latch/~{VCLR}   (3 pins)
    Z27      74LS175            pin   1  ~{Mr}
    Z28      74LS174            pin   1  ~{Mr}
    Z7       74LS74             pin   6  ~{Q}

/Video/Video Mixer/SYNC   (2 pins)
    R29      1.8k               pin   1  
    Z5       74C00              pin   8  

GND   (204 pins)
    C1       220uF 16V          pin   1  
    C10      10uF 16V           pin   2  
    C11      10uF 16V           pin   2  
    C14      0.01uF 24V         pin   2  
    C15      0.01uF 24V         pin   2  
    C16      0.1uF 12V          pin   2  
    C17      0.1uF 12V          pin   2  
    C18      0.1uF 12V          pin   2  
    C19      0.1uF 12V          pin   2  
    C2       10uF 16V           pin   2  
    C22      0.1uF 12V          pin   2  
    C23      0.1uF 12V          pin   2  
    C28      0.1uF 25V          pin   2  
    C29      0.1uF 12V          pin   2  
    C3       0.01uF 24V         pin   2  
    C30      0.1uF 25V          pin   2  
    C31      0.1uF 12V          pin   2  
    C32      0.1uF 25V          pin   2  
    C33      0.1uF 12V          pin   2  
    C34      0.1uF 25V          pin   2  
    C35      0.1uF 12V          pin   2  
    C36      0.1uF 12V          pin   2  
    C37      0.1uF 12V          pin   2  
    C38      0.1uF 12V          pin   2  
    C39      0.1uF 12V          pin   1  
    C4       10uF 16V           pin   1  
    C40      0.1uF 12V          pin   2  
    C41      0.1uF 12V          pin   2  
    C42      22uF 16V           pin   2  
    C44      0.1uF 12V          pin   2  
    C45      0.1uF 12V          pin   2  
    C46      0.1uF 12V          pin   2  
    C47      0.1uF 12V          pin   2  
    C48      0.1uF 12V          pin   2  
    C49      0.1uF 12V          pin   2  
    C5       10uF 16V           pin   2  
    C50      0.1uF 12V          pin   2  
    C51      0.1uF 12V          pin   2  
    C52      0.1uF 12V          pin   2  
    C53      0.1uF 12V          pin   2  
    C54      0.1uF 12V          pin   2  
    C55      0.1uF 12V          pin   2  
    C56      0.1uF 12V          pin   2  
    C57      10uF 16V           pin   2  
    C58      0.1uF 12V          pin   2  
    C6       100uF 16V          pin   1  
    C7       0.01uF 24V         pin   2  
    C8       2200uF 35V         pin   2  
    C9       10000uF 16V        pin   2  
    CR1      1N4735             pin   2  A
    CR2      1N5231             pin   1  K
    C_R67    220                pin   1  
    J1       Front View         pin   4  
    J100     Connection Mainboard Side pin  19  Pin_19
    J2       Front View         pin   5  
    J3       Front View         pin   2  
    J4       Edge Connector     pin   8  Pin_8
    J4       Edge Connector     pin  29  Pin_29
    J4       Edge Connector     pin  37  Pin_37
    J4       Edge Connector     pin  39  Pin_39
    R11      3.3k               pin   2  
    R12      3.3k               pin   2  
    R14      12k                pin   2  
    R22      75                 pin   2  
    R27      330                pin   2  
    R43      10k                pin   2  
    R44      10k                pin   1  
    R53      1.2k               pin   1  
    S2       Reset              pin   5  
    S2       Reset              pin   6  
    Z1       LM723C             pin   7  V-
    Z10      74LS166            pin   1  Ds
    Z10      74LS166            pin   2  A
    Z10      74LS166            pin   3  B
    Z10      74LS166            pin   6  CE
    Z10      74LS166            pin   8  GND
    Z10      74LS166            pin  14  H
    Z11      74LS166            pin   1  Ds
    Z11      74LS166            pin   2  A
    Z11      74LS166            pin   3  B
    Z11      74LS166            pin   6  CE
    Z11      74LS166            pin   8  GND
    Z12      74LS93             pin  10  GND
    Z13      4116               pin  16  VSS
    Z14      4116               pin  16  VSS
    Z15      4116               pin  16  VSS
    Z16      4116               pin  16  VSS
    Z17      4116               pin  16  VSS
    Z18      4116               pin  16  VSS
    Z19      4116               pin  16  VSS
    Z2       LM723C             pin   7  V-
    Z20      4116               pin  16  VSS
    Z21      74LS156            pin   8  GND
    Z22      74LS367            pin   8  GND
    Z23      74LS32             pin   7  GND
    Z24      74LS132            pin   4  
    Z24      74LS132            pin   5  
    Z24      74LS132            pin   7  GND
    Z25      74LS32             pin   1  
    Z25      74LS32             pin   2  
    Z25      74LS32             pin   7  GND
    Z25      74LS32             pin  12  
    Z25      74LS32             pin  13  
    Z26      74LS20             pin   7  GND
    Z27      74LS175            pin   8  GND
    Z28      74LS174            pin   8  GND
    Z29      MCM6670            pin   9  GND
    Z29      MCM6670            pin  17  ~{CS}
    Z30      74LS02             pin   5  
    Z30      74LS02             pin   6  
    Z30      74LS02             pin   7  GND
    Z31      74LS157            pin   8  GND
    Z31      74LS157            pin  15  E
    Z32      74LS93             pin  10  GND
    Z33      2364_20L           pin  12  GND
    Z34      2332_20L_21L       pin  12  GND
    Z35      74LS157            pin   8  GND
    Z35      74LS157            pin  15  E
    Z36      74LS32             pin   7  GND
    Z37      74LS02             pin   7  GND
    Z37      74LS02             pin   8  
    Z37      74LS02             pin   9  
    Z38      74LS367            pin   8  GND
    Z39      74LS367            pin   8  GND
    Z4       LM3900             pin   7  V-
    Z40      Z80CPU             pin  29  GND
    Z41      75452              pin   4  GND
    Z42      74LS04             pin   7  GND
    Z42      74LS04             pin  11  
    Z43      74LS157            pin   5  I0b
    Z43      74LS157            pin   8  GND
    Z43      74LS157            pin  15  E
    Z44      74LS367            pin   8  GND
    Z45      2102               pin   9  GND
    Z45      2102               pin  13  ~{CE}
    Z46      2102               pin   9  GND
    Z46      2102               pin  13  ~{CE}
    Z47      2102               pin   9  GND
    Z47      2102               pin  13  ~{CE}
    Z48      2102               pin   9  GND
    Z48      2102               pin  13  ~{CE}
    Z49      74LS157            pin   8  GND
    Z49      74LS157            pin  15  E
    Z5       74C00              pin   7  GND
    Z50      74LS93             pin  10  GND
    Z51      74LS157            pin   8  GND
    Z51      74LS157            pin  15  E
    Z52      74LS04             pin   7  GND
    Z52      74LS04             pin   9  
    Z53      74LS132            pin   7  GND
    Z54      74LS30             pin   7  GND
    Z55      74LS367            pin   8  GND
    Z56      74LS92             pin  10  GND
    Z57      74C04              pin   7  GND
    Z58      74LS92             pin  10  GND
    Z59      74LS175            pin   8  GND
    Z6       74C04              pin   7  GND
    Z60      74LS367            pin   8  GND
    Z60      74LS367            pin  12  
    Z60      74LS367            pin  14  
    Z60      74LS367            pin  15  
    Z61      2102               pin   9  GND
    Z61      2102               pin  13  ~{CE}
    Z62      2102               pin   9  GND
    Z62      2102               pin  13  ~{CE}
    Z63      2102               pin   9  GND
    Z63      2102               pin  13  ~{CE}
    Z64      74LS157            pin   8  GND
    Z64      74LS157            pin  15  E
    Z65      74LS93             pin   2  R0(1)
    Z65      74LS93             pin   3  R0(2)
    Z65      74LS93             pin  10  GND
    Z66      74LS11             pin   7  GND
    Z67      74LS367            pin   8  GND
    Z67      74LS367            pin  12  
    Z68      74LS367            pin   8  GND
    Z68      74LS367            pin  12  
    Z68      74LS367            pin  15  
    Z69      74LS74             pin   7  GND
    Z7       74LS74             pin   2  D
    Z7       74LS74             pin   7  GND
    Z7       74LS74             pin  10  ~{S}
    Z7       74LS74             pin  11  C
    Z7       74LS74             pin  12  D
    Z7       74LS74             pin  13  ~{R}
    Z70      74LS74             pin   7  GND
    Z71      ~                  pin   9  
    Z71      ~                  pin  11  
    Z72      74LS367            pin   6  
    Z72      74LS367            pin   8  GND
    Z72      74LS367            pin  14  
    Z72      74LS367            pin  15  
    Z73      74LS32             pin   7  GND
    Z74      74LS00             pin   7  GND
    Z75      74LS367            pin   8  GND
    Z76      74LS367            pin   8  GND
    Z8       74LS153            pin   1  Ea
    Z8       74LS153            pin   8  GND
    Z8       74LS153            pin  15  Eb
    Z9       74LS04             pin   1  
    Z9       74LS04             pin   5  
    Z9       74LS04             pin   7  GND
    Z9       74LS04             pin  11  
    Z9       74LS04             pin  13  

Net-(C1-Pad2)   (3 pins)
    C1       220uF 16V          pin   2  
    R19      220                pin   2  
    S1       ~                  pin  10  

Net-(C20-Pad1)   (3 pins)
    C20      330pF              pin   1  
    R20      100k               pin   2  2
    Z6       74C04              pin   3  

Net-(C20-Pad2)   (3 pins)
    C20      330pF              pin   2  
    C21      750pF              pin   1  
    Z6       74C04              pin   6  

Net-(C21-Pad2)   (3 pins)
    C21      750pF              pin   2  
    R43      10k                pin   1  
    Z6       74C04              pin  11  

Net-(C24-Pad2)   (3 pins)
    C24      220pF              pin   2  
    C25      220pF              pin   1  
    R36      360k               pin   1  

Net-(C25-Pad2)   (2 pins)
    C25      220pF              pin   2  
    R33      360k               pin   1  

Net-(C26-Pad1)   (3 pins)
    C26      0.047uF            pin   1  
    R21      100k               pin   2  2
    Z57      74C04              pin  13  

Net-(C26-Pad2)   (3 pins)
    C26      0.047uF            pin   2  
    C27      0.022uF            pin   1  
    Z57      74C04              pin  10  

Net-(C27-Pad2)   (3 pins)
    C27      0.022uF            pin   2  
    R44      10k                pin   2  
    Z57      74C04              pin   5  

Net-(C42-Pad1)   (4 pins)
    C42      22uF 16V           pin   1  
    R47      10k                pin   2  
    Z53      74LS132            pin  12  
    Z53      74LS132            pin  13  

Net-(C43-Pad1)   (3 pins)
    C43      47pF               pin   1  
    R46      910                pin   1  
    Z42      74LS04             pin   1  

Net-(C43-Pad2)   (4 pins)
    C43      47pF               pin   2  
    R52      910                pin   2  
    Z42      74LS04             pin   4  
    Z42      74LS04             pin   5  

Net-(C5-Pad1)   (5 pins)
    C5       10uF 16V           pin   1  
    R24      680k               pin   1  
    R25      1.6M               pin   2  
    R26      1M                 pin   1  
    R32      10k                pin   1  

Net-(C57-Pad1)   (4 pins)
    C57      10uF 16V           pin   1  
    R65      10k                pin   2  
    S2       Reset              pin   4  
    Z53      74LS132            pin   1  

Net-(CR10-A)   (4 pins)
    CR10     1N982              pin   2  A
    C_C58    0.1uF 12V          pin   1  
    J3       Front View         pin   3  
    K1       Relay_SPST-NO      pin   3  

Net-(CR10-K)   (2 pins)
    CR10     1N982              pin   1  K
    CR9      1N982              pin   1  K

Net-(CR3-A)   (3 pins)
    CR3      1N4148             pin   2  A
    K1       Relay_SPST-NO      pin   2  
    Z41      75452              pin   3  1Y

Net-(CR4-A)   (3 pins)
    CR4      1N4148             pin   2  A
    R34      470k               pin   2  
    Z4       LM3900             pin   4  

Net-(CR4-K)   (3 pins)
    CR4      1N4148             pin   1  K
    CR5      1N4148             pin   1  K
    R41      470k               pin   1  

Net-(CR5-A)   (5 pins)
    CR5      1N4148             pin   2  A
    R35      470k               pin   1  
    R36      360k               pin   2  
    R37      560k               pin   1  
    Z4       LM3900             pin   5  

Net-(CR6-A)   (4 pins)
    CR6      1N4148             pin   2  A
    R38      470k               pin   1  
    R42      1M                 pin   2  
    Z4       LM3900             pin   9  

Net-(CR6-K)   (2 pins)
    CR6      1N4148             pin   1  K
    CR7      1N4148             pin   2  A

Net-(CR7-K)   (3 pins)
    C39      0.1uF 12V          pin   2  
    CR7      1N4148             pin   1  K
    R45      470k               pin   1  

Net-(CR8-+)   (5 pins)
    CR8      MDA202             pin   1  +
    S1       ~                  pin   4  
    S1       ~                  pin   5  
    S1       ~                  pin   8  
    S1       ~                  pin   9  

Net-(CR8--)   (3 pins)
    CR8      MDA202             pin   4  -
    S1       ~                  pin  11  
    S1       ~                  pin  12  

Net-(CR8-Pad2)   (2 pins)
    CR8      MDA202             pin   2  
    J1       Front View         pin   1  

Net-(CR8-Pad3)   (2 pins)
    CR8      MDA202             pin   3  
    J1       Front View         pin   3  

Net-(CR9-A)   (4 pins)
    CR9      1N982              pin   2  A
    C_C58    0.1uF 12V          pin   2  
    J3       Front View         pin   1  
    K1       Relay_SPST-NO      pin   4  

Net-(J1-Pad2)   (3 pins)
    J1       Front View         pin   2  
    S1       ~                  pin   1  
    S1       ~                  pin   2  

Net-(Q1-B)   (4 pins)
    Q1       2N3904             pin   2  B
    R23      120                pin   1  
    R27      330                pin   1  
    R28      270                pin   2  

Net-(Q1-C)   (4 pins)
    C2       10uF 16V           pin   1  
    C7       0.01uF 24V         pin   1  
    Q1       2N3904             pin   3  C
    R30      47                 pin   2  

Net-(Q1-E)   (3 pins)
    J2       Front View         pin   4  
    Q1       2N3904             pin   1  E
    R22      75                 pin   1  

Net-(Q2-B)   (2 pins)
    Q2       2N3906             pin   2  B
    R29      1.8k               pin   2  

Net-(Q2-C)   (2 pins)
    Q2       2N3906             pin   3  C
    R28      270                pin   1  

Net-(Q3-B)   (3 pins)
    Q3       TIP29A             pin   1  B
    R2       2.7k               pin   1  
    Z1       LM723C             pin  10  Vout

Net-(Q3-C)   (3 pins)
    Q3       TIP29A             pin   2  C
    Q4       2N6594             pin   1  B
    R1       68                 pin   2  

Net-(Q3-E)   (5 pins)
    Q3       TIP29A             pin   3  E
    Q4       2N6594             pin   3  C
    R2       2.7k               pin   2  
    R3       750                pin   1  
    R4       0.33               pin   1  

Net-(Q4-E)   (5 pins)
    C9       10000uF 16V        pin   1  
    Q4       2N6594             pin   2  E
    R1       68                 pin   1  
    S1       ~                  pin   6  
    S1       ~                  pin   7  

Net-(Q5-B)   (2 pins)
    Q5       2N3906             pin   2  B
    R8       100k               pin   1  

Net-(Q5-C)   (2 pins)
    Q5       2N3906             pin   3  C
    R9       3.3k               pin   2  

Net-(Q5-E)   (3 pins)
    Q5       2N3906             pin   1  E
    R5       1k                 pin   2  2
    Z1       LM723C             pin   5  +

Net-(Q6-B)   (3 pins)
    Q6       MJE34              pin   1  B
    R16      1.2k               pin   2  
    Z2       LM723C             pin  11  VC

Net-(Q6-C)   (4 pins)
    Q6       MJE34              pin   2  C
    R17      2k                 pin   1  
    R18      5.6                pin   2  
    Z2       LM723C             pin  10  Vout

Net-(Q6-E)   (5 pins)
    C8       2200uF 35V         pin   1  
    Q6       MJE34              pin   3  E
    R16      1.2k               pin   1  
    S1       ~                  pin   3  
    Z2       LM723C             pin  12  V+

Net-(R10-Pad1)   (2 pins)
    R10      1k                 pin   1  1
    R12      3.3k               pin   1  

Net-(R10-Pad3)   (2 pins)
    R10      1k                 pin   3  3
    R13      2.2k               pin   2  

Net-(R11-Pad1)   (2 pins)
    R11      3.3k               pin   1  
    R5       1k                 pin   3  3

Net-(R20-Pad1)   (2 pins)
    R20      100k               pin   1  1
    Z6       74C04              pin   2  

Net-(R21-Pad1)   (2 pins)
    R21      100k               pin   1  1
    Z57      74C04              pin   4  

Net-(R46-Pad2)   (3 pins)
    R46      910                pin   2  
    Y1       10.6445 MHz        pin   1  1
    Z42      74LS04             pin   2  

Net-(R5-Pad1)   (2 pins)
    R5       1k                 pin   1  1
    R6       1.2k               pin   1  

Net-(R52-Pad1)   (3 pins)
    R52      910                pin   1  
    Y1       10.6445 MHz        pin   2  2
    Z42      74LS04             pin   3  

Net-(R66-Pad2)   (2 pins)
    R66      4.7k               pin   2  
    Z71      ~                  pin  10  

Net-(R67-Pad2)   (2 pins)
    R67      4.7k               pin   2  
    Z42      74LS04             pin   9  

Net-(Z1--)   (3 pins)
    C12      470pF              pin   1  
    R7       1.2k               pin   2  
    Z1       LM723C             pin   4  -

Net-(Z1-FC)   (2 pins)
    C12      470pF              pin   2  
    Z1       LM723C             pin  13  FC

Net-(Z1-ILIM)   (3 pins)
    R3       750                pin   2  
    R9       3.3k               pin   1  
    Z1       LM723C             pin   2  ILIM

Net-(Z1-VREF)   (2 pins)
    R6       1.2k               pin   2  
    Z1       LM723C             pin   6  VREF

Net-(Z10-C)   (2 pins)
    Z10      74LS166            pin   4  C
    Z29      MCM6670            pin  12  D0

Net-(Z10-Clk)   (3 pins)
    Z10      74LS166            pin   7  Clk
    Z11      74LS166            pin   7  Clk
    Z9       74LS04             pin   8  

Net-(Z10-Clr)   (3 pins)
    R40      4.7k               pin   1  
    Z10      74LS166            pin   9  Clr
    Z11      74LS166            pin   9  Clr

Net-(Z10-D)   (2 pins)
    Z10      74LS166            pin   5  D
    Z29      MCM6670            pin  13  D1

Net-(Z10-E)   (2 pins)
    Z10      74LS166            pin  10  E
    Z29      MCM6670            pin  14  D2

Net-(Z10-F)   (2 pins)
    Z10      74LS166            pin  11  F
    Z29      MCM6670            pin  15  D3

Net-(Z10-G)   (2 pins)
    Z10      74LS166            pin  12  G
    Z29      MCM6670            pin  16  D4

Net-(Z10-PE)   (2 pins)
    Z10      74LS166            pin  15  PE
    Z26      74LS20             pin   8  

Net-(Z10-Qh)   (2 pins)
    Z10      74LS166            pin  13  Qh
    Z30      74LS02             pin   3  

Net-(Z11-C)   (4 pins)
    Z11      74LS166            pin   4  C
    Z11      74LS166            pin   5  D
    Z11      74LS166            pin  10  E
    Z8       74LS153            pin   9  Zb

Net-(Z11-F)   (4 pins)
    Z11      74LS166            pin  11  F
    Z11      74LS166            pin  12  G
    Z11      74LS166            pin  14  H
    Z8       74LS153            pin   7  Za

Net-(Z11-PE)   (2 pins)
    Z11      74LS166            pin  15  PE
    Z26      74LS20             pin   6  

Net-(Z11-Qh)   (2 pins)
    Z11      74LS166            pin  13  Qh
    Z30      74LS02             pin   2  

Net-(Z12-R0(1))   (3 pins)
    Z12      74LS93             pin   2  R0(1)
    Z12      74LS93             pin   3  R0(2)
    Z66      74LS11             pin   8  

Net-(Z13-A0)   (9 pins)
    Z13      4116               pin   5  A0
    Z14      4116               pin   5  A0
    Z15      4116               pin   5  A0
    Z16      4116               pin   5  A0
    Z17      4116               pin   5  A0
    Z18      4116               pin   5  A0
    Z19      4116               pin   5  A0
    Z20      4116               pin   5  A0
    Z35      74LS157            pin   4  Za

Net-(Z13-A1)   (9 pins)
    Z13      4116               pin   7  A1
    Z14      4116               pin   7  A1
    Z15      4116               pin   7  A1
    Z16      4116               pin   7  A1
    Z17      4116               pin   7  A1
    Z18      4116               pin   7  A1
    Z19      4116               pin   7  A1
    Z20      4116               pin   7  A1
    Z35      74LS157            pin   7  Zb

Net-(Z13-A2)   (9 pins)
    Z13      4116               pin   6  A2
    Z14      4116               pin   6  A2
    Z15      4116               pin   6  A2
    Z16      4116               pin   6  A2
    Z17      4116               pin   6  A2
    Z18      4116               pin   6  A2
    Z19      4116               pin   6  A2
    Z20      4116               pin   6  A2
    Z35      74LS157            pin   9  Zc

Net-(Z13-A3)   (9 pins)
    Z13      4116               pin  12  A3
    Z14      4116               pin  12  A3
    Z15      4116               pin  12  A3
    Z16      4116               pin  12  A3
    Z17      4116               pin  12  A3
    Z18      4116               pin  12  A3
    Z19      4116               pin  12  A3
    Z20      4116               pin  12  A3
    Z35      74LS157            pin  12  Zd

Net-(Z13-A4)   (9 pins)
    Z13      4116               pin  11  A4
    Z14      4116               pin  11  A4
    Z15      4116               pin  11  A4
    Z16      4116               pin  11  A4
    Z17      4116               pin  11  A4
    Z18      4116               pin  11  A4
    Z19      4116               pin  11  A4
    Z20      4116               pin  11  A4
    Z51      74LS157            pin   4  Za

Net-(Z13-A5)   (9 pins)
    Z13      4116               pin  10  A5
    Z14      4116               pin  10  A5
    Z15      4116               pin  10  A5
    Z16      4116               pin  10  A5
    Z17      4116               pin  10  A5
    Z18      4116               pin  10  A5
    Z19      4116               pin  10  A5
    Z20      4116               pin  10  A5
    Z51      74LS157            pin   7  Zb

Net-(Z13-A6)   (10 pins)
    Z13      4116               pin  13  A6
    Z14      4116               pin  13  A6
    Z15      4116               pin  13  A6
    Z16      4116               pin  13  A6
    Z17      4116               pin  13  A6
    Z18      4116               pin  13  A6
    Z19      4116               pin  13  A6
    Z20      4116               pin  13  A6
    Z71      ~                  pin  13  
    Z71      ~                  pin  14  

Net-(Z13-~{CAS})   (10 pins)
    R57      4.7k               pin   2  
    Z13      4116               pin  15  ~{CAS}
    Z14      4116               pin  15  ~{CAS}
    Z15      4116               pin  15  ~{CAS}
    Z16      4116               pin  15  ~{CAS}
    Z17      4116               pin  15  ~{CAS}
    Z18      4116               pin  15  ~{CAS}
    Z19      4116               pin  15  ~{CAS}
    Z20      4116               pin  15  ~{CAS}
    Z67      74LS367            pin  13  

Net-(Z13-~{RAS})   (10 pins)
    R60      4.7k               pin   2  
    Z13      4116               pin   4  ~{RAS}
    Z14      4116               pin   4  ~{RAS}
    Z15      4116               pin   4  ~{RAS}
    Z16      4116               pin   4  ~{RAS}
    Z17      4116               pin   4  ~{RAS}
    Z18      4116               pin   4  ~{RAS}
    Z19      4116               pin   4  ~{RAS}
    Z20      4116               pin   4  ~{RAS}
    Z68      74LS367            pin  13  

Net-(Z2-+)   (2 pins)
    R15      1.5k               pin   2  
    Z2       LM723C             pin   5  +

Net-(Z2--)   (3 pins)
    C13      470pF              pin   2  
    R10      1k                 pin   2  2
    Z2       LM723C             pin   4  -

Net-(Z2-FC)   (2 pins)
    C13      470pF              pin   1  
    Z2       LM723C             pin  13  FC

Net-(Z2-ILIM)   (3 pins)
    R14      12k                pin   1  
    R17      2k                 pin   2  
    Z2       LM723C             pin   2  ILIM

Net-(Z2-VREF)   (2 pins)
    R15      1.5k               pin   1  
    Z2       LM723C             pin   6  VREF

Net-(Z21-Ea2)   (3 pins)
    Z21      74LS156            pin   2  Ea2
    Z21      74LS156            pin  14  Eb1
    Z73      74LS32             pin   6  

Net-(Z21-Q0a)   (2 pins)
    Z21      74LS156            pin   7  Q0a
    Z3       ~                  pin   2  

Net-(Z21-Q0b)   (3 pins)
    Z21      74LS156            pin   9  Q0b
    Z3       ~                  pin  10  
    Z3       ~                  pin  16  

Net-(Z21-Q1a)   (2 pins)
    Z21      74LS156            pin   6  Q1a
    Z3       ~                  pin   3  

Net-(Z21-Q1b)   (2 pins)
    Z21      74LS156            pin  10  Q1b
    Z3       ~                  pin   9  

Net-(Z21-Q2a)   (2 pins)
    Z21      74LS156            pin   5  Q2a
    Z3       ~                  pin   4  

Net-(Z21-Q2b)   (2 pins)
    Z21      74LS156            pin  11  Q2b
    Z3       ~                  pin  11  

Net-(Z21-Q3a)   (2 pins)
    Z21      74LS156            pin   4  Q3a
    Z3       ~                  pin   5  

Net-(Z21-Q3b)   (3 pins)
    R48      4.7k               pin   1  
    Z21      74LS156            pin  12  Q3b
    Z36      74LS32             pin   4  

Net-(Z22-Pad1)   (9 pins)
    Z22      74LS367            pin   1  
    Z22      74LS367            pin  15  
    Z38      74LS367            pin   1  
    Z38      74LS367            pin  15  
    Z39      74LS367            pin   1  
    Z39      74LS367            pin  15  
    Z52      74LS04             pin   4  
    Z55      74LS367            pin  15  
    Z72      74LS367            pin   1  

Net-(Z24-Pad10)   (2 pins)
    Z24      74LS132            pin  10  
    Z24      74LS132            pin  11  

Net-(Z24-Pad12)   (3 pins)
    Z24      74LS132            pin   8  
    Z24      74LS132            pin  12  
    Z44      74LS367            pin  12  

Net-(Z24-Pad9)   (2 pins)
    Z24      74LS132            pin   9  
    Z4       LM3900             pin  10  

Net-(Z25-Pad10)   (3 pins)
    Z25      74LS32             pin   5  
    Z25      74LS32             pin  10  
    Z36      74LS32             pin   3  

Net-(Z26-Pad13)   (3 pins)
    Z26      74LS20             pin   5  
    Z26      74LS20             pin  13  
    Z9       74LS04             pin   4  

Net-(Z27-D0)   (2 pins)
    Z27      74LS175            pin   4  D0
    Z42      74LS04             pin  12  

Net-(Z27-D1)   (2 pins)
    Z27      74LS175            pin   5  D1
    Z30      74LS02             pin  10  

Net-(Z32-R0(1))   (3 pins)
    Z32      74LS93             pin   2  R0(1)
    Z32      74LS93             pin   3  R0(2)
    Z66      74LS11             pin  12  

Net-(Z35-I1a)   (5 pins)
    Z35      74LS157            pin   3  I1a
    Z71      ~                  pin   1  
    Z71      ~                  pin   2  
    Z71      ~                  pin   7  
    Z71      ~                  pin   8  

Net-(Z36-Pad1)   (2 pins)
    Z36      74LS32             pin   1  
    Z52      74LS04             pin   6  

Net-(Z36-Pad10)   (3 pins)
    Z36      74LS32             pin   6  
    Z36      74LS32             pin  10  
    Z36      74LS32             pin  12  

Net-(Z36-Pad2)   (2 pins)
    Z36      74LS32             pin   2  
    Z54      74LS30             pin   8  

Net-(Z36-Pad5)   (2 pins)
    Z36      74LS32             pin   5  
    Z37      74LS02             pin   4  

Net-(Z36-Pad9)   (2 pins)
    Z36      74LS32             pin   9  
    Z52      74LS04             pin   2  

Net-(Z37-Pad11)   (4 pins)
    Z37      74LS02             pin   3  
    Z37      74LS02             pin  11  
    Z37      74LS02             pin  12  
    Z53      74LS132            pin   3  

Net-(Z37-Pad2)   (3 pins)
    Z37      74LS02             pin   2  
    Z52      74LS04             pin  11  
    Z53      74LS132            pin  11  

Net-(Z40-~{HALT})   (2 pins)
    Z40      Z80CPU             pin  18  ~{HALT}
    Z53      74LS132            pin   2  

Net-(Z40-~{IORQ})   (4 pins)
    Z23      74LS32             pin   2  
    Z23      74LS32             pin  10  
    Z40      Z80CPU             pin  20  ~{IORQ}
    Z73      74LS32             pin   1  

Net-(Z40-~{M1})   (2 pins)
    Z40      Z80CPU             pin  27  ~{M1}
    Z73      74LS32             pin   2  

Net-(Z40-~{NMI})   (2 pins)
    Z37      74LS02             pin  13  
    Z40      Z80CPU             pin  17  ~{NMI}

Net-(Z40-~{RD})   (5 pins)
    Z23      74LS32             pin   5  
    Z23      74LS32             pin   9  
    Z40      Z80CPU             pin  21  ~{RD}
    Z53      74LS132            pin   5  
    Z74      74LS00             pin   1  

Net-(Z40-~{RESET})   (2 pins)
    Z40      Z80CPU             pin  26  ~{RESET}
    Z52      74LS04             pin  10  

Net-(Z40-~{WR})   (4 pins)
    Z23      74LS32             pin   1  
    Z23      74LS32             pin  13  
    Z40      Z80CPU             pin  22  ~{WR}
    Z74      74LS00             pin   2  

Net-(Z41A-1A)   (3 pins)
    Z41      75452              pin   1  1A
    Z41      75452              pin   2  1B
    Z59      74LS175            pin  10  Q2

Net-(Z41B-2Y)   (2 pins)
    R23      120                pin   2  
    Z41      75452              pin   5  2Y

Net-(Z43-I0a)   (2 pins)
    Z43      74LS157            pin   2  I0a
    Z70      74LS74             pin   9  Q

Net-(Z43-I0c)   (3 pins)
    Z24      74LS132            pin   2  
    Z43      74LS157            pin  11  I0c
    Z58      74LS92             pin   9  Q2

Net-(Z43-I1b)   (3 pins)
    Z43      74LS157            pin   6  I1b
    Z43      74LS157            pin  10  I1c
    Z58      74LS92             pin   8  Q3

Net-(Z43-Zc)   (2 pins)
    Z43      74LS157            pin   9  Zc
    Z65      74LS93             pin   1  CP1..3

Net-(Z49-I1b)   (3 pins)
    R49      4.7k               pin   2  
    Z49      74LS157            pin   6  I1b
    Z49      74LS157            pin  13  I1d

Net-(Z4A-+)   (3 pins)
    R25      1.6M               pin   1  
    R33      360k               pin   2  
    Z4       LM3900             pin   1  +

Net-(Z4A--)   (2 pins)
    R37      560k               pin   2  
    Z4       LM3900             pin   6  -

Net-(Z4B-+)   (2 pins)
    R24      680k               pin   2  
    Z4       LM3900             pin   2  +

Net-(Z4B--)   (3 pins)
    R34      470k               pin   1  
    R35      470k               pin   2  
    Z4       LM3900             pin   3  -

Net-(Z4C-+)   (2 pins)
    R26      1M                 pin   2  
    Z4       LM3900             pin  13  +

Net-(Z4C--)   (3 pins)
    R41      470k               pin   2  
    R42      1M                 pin   1  
    Z4       LM3900             pin   8  -

Net-(Z4D-+)   (2 pins)
    R38      470k               pin   2  
    Z4       LM3900             pin  12  +

Net-(Z4D--)   (2 pins)
    R45      470k               pin   2  
    Z4       LM3900             pin  11  -

Net-(Z4E-V+)   (3 pins)
    C6       100uF 16V          pin   2  
    R31      10                 pin   1  
    Z4       LM3900             pin  14  V+

Net-(Z5-Pad1)   (3 pins)
    Z5       74C00              pin   1  
    Z5       74C00              pin   5  
    Z57      74C04              pin   8  

Net-(Z5-Pad10)   (2 pins)
    Z5       74C00              pin  10  
    Z5       74C00              pin  11  

Net-(Z5-Pad12)   (3 pins)
    Z5       74C00              pin   3  
    Z5       74C00              pin   4  
    Z5       74C00              pin  12  

Net-(Z5-Pad13)   (3 pins)
    Z5       74C00              pin   2  
    Z5       74C00              pin  13  
    Z6       74C04              pin   8  

Net-(Z5-Pad6)   (2 pins)
    Z5       74C00              pin   6  
    Z5       74C00              pin   9  

Net-(Z50-R0(1))   (3 pins)
    Z50      74LS93             pin   2  R0(1)
    Z50      74LS93             pin   3  R0(2)
    Z66      74LS11             pin   6  

Net-(Z51-Zc)   (2 pins)
    Z51      74LS157            pin   9  Zc
    Z71      ~                  pin   3  

Net-(Z52-Pad12)   (2 pins)
    Z52      74LS04             pin  12  
    Z74      74LS00             pin   4  

Net-(Z56-Q3)   (2 pins)
    Z56      74LS92             pin   8  Q3
    Z72      74LS367            pin  12  

Net-(Z57-Pad11)   (2 pins)
    Z57      74C04              pin  11  
    Z57      74C04              pin  12  

Net-(Z57-Pad2)   (2 pins)
    Z57      74C04              pin   2  
    Z57      74C04              pin   3  

Net-(Z57-Pad6)   (2 pins)
    Z57      74C04              pin   6  
    Z57      74C04              pin   9  

Net-(Z58-CP1..3)   (3 pins)
    Z24      74LS132            pin   1  
    Z58      74LS92             pin   1  CP1..3
    Z58      74LS92             pin  12  Q0

Net-(Z59-Q0)   (2 pins)
    R54      7.5k               pin   1  
    Z59      74LS175            pin   2  Q0

Net-(Z59-~{Mr})   (2 pins)
    R59      4.7k               pin   2  
    Z59      74LS175            pin   1  ~{Mr}

Net-(Z59-~{Q1})   (3 pins)
    R55      7.5k               pin   2  
    R56      220k               pin   1  
    Z59      74LS175            pin   6  ~{Q1}

Net-(Z6-Pad1)   (2 pins)
    Z6       74C04              pin   1  
    Z6       74C04              pin  12  

Net-(Z6-Pad10)   (2 pins)
    Z6       74C04              pin   9  
    Z6       74C04              pin  10  

Net-(Z6-Pad4)   (2 pins)
    Z6       74C04              pin   4  
    Z6       74C04              pin   5  

Net-(Z67-Pad15)   (3 pins)
    Z67      74LS367            pin  15  
    Z71      ~                  pin   5  
    Z71      ~                  pin   6  

Net-(Z69A-Q)   (2 pins)
    Z69      74LS74             pin   5  Q
    Z69      74LS74             pin  12  D

Net-(Z70B-D)   (2 pins)
    Z70      74LS74             pin   8  ~{Q}
    Z70      74LS74             pin  12  D

Net-(Z70B-~{R})   (2 pins)
    R63      4.7k               pin   2  
    Z70      74LS74             pin  13  ~{R}

Net-(Z73-Pad10)   (2 pins)
    Z73      74LS32             pin  10  
    Z74      74LS00             pin  11  

Net-(Z73-Pad8)   (2 pins)
    Z73      74LS32             pin   8  
    Z74      74LS00             pin   5  

Net-(Z73-Pad9)   (2 pins)
    Z73      74LS32             pin   9  
    Z74      74LS00             pin   8  

Net-(Z7A-~{R})   (2 pins)
    R39      4.7k               pin   1  
    Z7       74LS74             pin   1  ~{R}

unconnected-(J1-Pad5)   (1 pins)
    J1       Front View         pin   5  

unconnected-(J100-Pin_20-Pad20)   (1 pins)
    J100     Connection Mainboard Side pin  20  Pin_20

unconnected-(J2-Pad2)   (1 pins)
    J2       Front View         pin   2  

unconnected-(J2-Pad3)   (1 pins)
    J2       Front View         pin   3  

unconnected-(R20-Pad3)   (1 pins)
    R20      100k               pin   3  3

unconnected-(R21-Pad3)   (1 pins)
    R21      100k               pin   3  3

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

unconnected-(Z2-NC-Pad1)   (1 pins)
    Z2       LM723C             pin   1  NC

unconnected-(Z2-NC-Pad14)   (1 pins)
    Z2       LM723C             pin  14  NC

unconnected-(Z2-NC-Pad8)   (1 pins)
    Z2       LM723C             pin   8  NC

unconnected-(Z2-VZ-Pad9)   (1 pins)
    Z2       LM723C             pin   9  VZ

unconnected-(Z24-Pad6)   (1 pins)
    Z24      74LS132            pin   6  

unconnected-(Z25-Pad11)   (1 pins)
    Z25      74LS32             pin  11  

unconnected-(Z25-Pad3)   (1 pins)
    Z25      74LS32             pin   3  

unconnected-(Z27-Q2-Pad10)   (1 pins)
    Z27      74LS175            pin  10  Q2

unconnected-(Z27-~{Q1}-Pad6)   (1 pins)
    Z27      74LS175            pin   6  ~{Q1}

unconnected-(Z27-~{Q3}-Pad14)   (1 pins)
    Z27      74LS175            pin  14  ~{Q3}

unconnected-(Z30-Pad4)   (1 pins)
    Z30      74LS02             pin   4  

unconnected-(Z37-Pad10)   (1 pins)
    Z37      74LS02             pin  10  

unconnected-(Z40-~{BUSACK}-Pad23)   (1 pins)
    Z40      Z80CPU             pin  23  ~{BUSACK}

unconnected-(Z40-~{RFSH}-Pad28)   (1 pins)
    Z40      Z80CPU             pin  28  ~{RFSH}

unconnected-(Z42-Pad10)   (1 pins)
    Z42      74LS04             pin  10  

unconnected-(Z43-I0d-Pad14)   (1 pins)
    Z43      74LS157            pin  14  I0d

unconnected-(Z43-I1d-Pad13)   (1 pins)
    Z43      74LS157            pin  13  I1d

unconnected-(Z43-Zd-Pad12)   (1 pins)
    Z43      74LS157            pin  12  Zd

unconnected-(Z51-I0d-Pad14)   (1 pins)
    Z51      74LS157            pin  14  I0d

unconnected-(Z51-I1d-Pad13)   (1 pins)
    Z51      74LS157            pin  13  I1d

unconnected-(Z51-Zd-Pad12)   (1 pins)
    Z51      74LS157            pin  12  Zd

unconnected-(Z52-Pad8)   (1 pins)
    Z52      74LS04             pin   8  

unconnected-(Z56-CP0-Pad14)   (1 pins)
    Z56      74LS92             pin  14  CP0

unconnected-(Z56-Q0-Pad12)   (1 pins)
    Z56      74LS92             pin  12  Q0

unconnected-(Z56-Q1-Pad11)   (1 pins)
    Z56      74LS92             pin  11  Q1

unconnected-(Z56-Q2-Pad9)   (1 pins)
    Z56      74LS92             pin   9  Q2

unconnected-(Z58-Q1-Pad11)   (1 pins)
    Z58      74LS92             pin  11  Q1

unconnected-(Z59-Q1-Pad7)   (1 pins)
    Z59      74LS175            pin   7  Q1

unconnected-(Z59-Q3-Pad15)   (1 pins)
    Z59      74LS175            pin  15  Q3

unconnected-(Z59-~{Q0}-Pad3)   (1 pins)
    Z59      74LS175            pin   3  ~{Q0}

unconnected-(Z59-~{Q2}-Pad11)   (1 pins)
    Z59      74LS175            pin  11  ~{Q2}

unconnected-(Z60-Pad11)   (1 pins)
    Z60      74LS367            pin  11  

unconnected-(Z60-Pad13)   (1 pins)
    Z60      74LS367            pin  13  

unconnected-(Z65-Q3-Pad11)   (1 pins)
    Z65      74LS93             pin  11  Q3

unconnected-(Z67-Pad11)   (1 pins)
    Z67      74LS367            pin  11  

unconnected-(Z68-Pad11)   (1 pins)
    Z68      74LS367            pin  11  

unconnected-(Z69A-~{Q}-Pad6)   (1 pins)
    Z69      74LS74             pin   6  ~{Q}

unconnected-(Z69B-~{Q}-Pad8)   (1 pins)
    Z69      74LS74             pin   8  ~{Q}

unconnected-(Z70A-Q-Pad5)   (1 pins)
    Z70      74LS74             pin   5  Q

unconnected-(Z72-Pad13)   (1 pins)
    Z72      74LS367            pin  13  

unconnected-(Z72-Pad7)   (1 pins)
    Z72      74LS367            pin   7  

unconnected-(Z73-Pad11)   (1 pins)
    Z73      74LS32             pin  11  

unconnected-(Z7A-Q-Pad5)   (1 pins)
    Z7       74LS74             pin   5  Q

unconnected-(Z7B-Q-Pad9)   (1 pins)
    Z7       74LS74             pin   9  Q

unconnected-(Z7B-~{Q}-Pad8)   (1 pins)
    Z7       74LS74             pin   8  ~{Q}

unconnected-(Z8-I3a-Pad3)   (1 pins)
    Z8       74LS153            pin   3  I3a

unconnected-(Z8-I3b-Pad13)   (1 pins)
    Z8       74LS153            pin  13  I3b

unconnected-(Z9-Pad10)   (1 pins)
    Z9       74LS04             pin  10  

unconnected-(Z9-Pad12)   (1 pins)
    Z9       74LS04             pin  12  

unconnected-(Z9-Pad2)   (1 pins)
    Z9       74LS04             pin   2  

unconnected-(Z9-Pad6)   (1 pins)
    Z9       74LS04             pin   6  

```
