# ALPS keyboard — complete netlist

Generated from `TRS-80-Model-I-Keyboard-ALPS-main` by `verify/emit.py`, which exports the schematic with `kicad-cli` and parses it with the same code the claims in `verify/claims.py` use.

**75 components · 55 nets · 227 pin connections.**

Three views of the same information: components, a connection view answering "what is this pin wired to", and a net index answering "what is on this net". The redundancy is deliberate — it is what lets the file be checked against itself.

No integrity problems: every node names a known component, every pin number is valid for that component's symbol, and the two views agree on the connection count.

## Components

| ref | value | sheet |
|---|---|---|
| `C1` | 0.1uF |  |
| `C2` | 0.1uF |  |
| `CR1` | RED 5mm |  |
| `J1` | Connection Keyboad Side |  |
| `R1` | 4.7k |  |
| `R2` | 330 |  |
| `SW1` | @ |  |
| `SW2` | H |  |
| `SW3` | P |  |
| `SW4` | X |  |
| `SW5` | 0 |  |
| `SW6` | 8 |  |
| `SW7` | ENTER |  |
| `SW8` | LSHIFT |  |
| `SW9` | RSHIFT |  |
| `SW10` | A |  |
| `SW11` | I |  |
| `SW12` | Q |  |
| `SW13` | Y |  |
| `SW14` | 1 |  |
| `SW15` | 9 |  |
| `SW16` | CLEAR |  |
| `SW17` | B |  |
| `SW18` | J |  |
| `SW19` | R |  |
| `SW20` | Z |  |
| `SW21` | 2 |  |
| `SW22` | : |  |
| `SW23` | BREAK |  |
| `SW24` | C |  |
| `SW25` | K |  |
| `SW26` | S |  |
| `SW27` | 3 |  |
| `SW28` | ; |  |
| `SW29` | UP |  |
| `SW30` | D |  |
| `SW31` | L |  |
| `SW32` | T |  |
| `SW33` | 4 |  |
| `SW34` | , |  |
| `SW35` | DOWN |  |
| `SW36` | E |  |
| `SW37` | M |  |
| `SW38` | U |  |
| `SW39` | 5 |  |
| `SW40` | - |  |
| `SW41` | LEFT |  |
| `SW42` | F |  |
| `SW43` | N |  |
| `SW44` | V |  |
| `SW45` | 6 |  |
| `SW46` | . |  |
| `SW47` | RIGHT |  |
| `SW48` | G |  |
| `SW49` | O |  |
| `SW50` | W |  |
| `SW51` | 7 |  |
| `SW52` | / |  |
| `SW53` | SPACE |  |
| `SW54` | 0 |  |
| `SW55` | 8 |  |
| `SW56` | ENTER |  |
| `SW57` | 1 |  |
| `SW58` | 9 |  |
| `SW59` | 2 |  |
| `SW60` | 3 |  |
| `SW61` | 4 |  |
| `SW62` | 5 |  |
| `SW63` | 6 |  |
| `SW64` | . |  |
| `SW65` | 7 |  |
| `Z1` | 74LS05 |  |
| `Z2` | 74LS05 |  |
| `Z3` | 74LS368 |  |
| `Z4` | 74LS368 |  |

## Connections

For each pin: its name, its net, and what else is on that net. Nets with more than 12 pins (power, ground, buses) are named rather than expanded.

```
C1  (0.1uF, )
   pin   1                +5V                          C2.1 CR1.2(A) J1.1(Pin_1) R1.1(R1) Z1.14(VCC) Z2.14(VCC) Z3.16(VCC) Z4.16(VCC)
   pin   2                GND                          C2.2 J1.19(Pin_19) R2.2 Z1.7(GND) Z2.7(GND) Z3.8(GND) Z4.8(GND)

C2  (0.1uF, )
   pin   1                +5V                          C1.1 CR1.2(A) J1.1(Pin_1) R1.1(R1) Z1.14(VCC) Z2.14(VCC) Z3.16(VCC) Z4.16(VCC)
   pin   2                GND                          C1.2 J1.19(Pin_19) R2.2 Z1.7(GND) Z2.7(GND) Z3.8(GND) Z4.8(GND)

CR1  (RED 5mm, )
   pin   1 K              Net-(CR1-K)                  R2.1
   pin   2 A              +5V                          C1.1 C2.1 J1.1(Pin_1) R1.1(R1) Z1.14(VCC) Z2.14(VCC) Z3.16(VCC) Z4.16(VCC)

J1  (Connection Keyboad Side, )
   pin   1 Pin_1          +5V                          C1.1 C2.1 CR1.2(A) R1.1(R1) Z1.14(VCC) Z2.14(VCC) Z3.16(VCC) Z4.16(VCC)
   pin   2 Pin_2          A4                           Z1.5
   pin   3 Pin_3          A5                           Z1.3
   pin   4 Pin_4          A1                           Z1.11
   pin   5 Pin_5          A0                           Z1.9
   pin   6 Pin_6          A2                           Z2.5
   pin   7 Pin_7          A6                           Z2.3
   pin   8 Pin_8          A7                           Z2.11
   pin   9 Pin_9          A3                           Z2.9
   pin  10 Pin_10         D2                           Z3.3
   pin  11 Pin_11         D0                           Z3.5
   pin  12 Pin_12         D5                           Z3.7
   pin  13 Pin_13         D3                           Z3.9
   pin  14 Pin_14         ~{KYBD}                      Z3.1 Z4.1
   pin  15 Pin_15         D6                           Z4.3
   pin  16 Pin_16         D1                           Z4.5
   pin  17 Pin_17         D7                           Z4.7
   pin  18 Pin_18         D4                           Z4.9
   pin  19 Pin_19         GND                          C1.2 C2.2 R2.2 Z1.7(GND) Z2.7(GND) Z3.8(GND) Z4.8(GND)
   pin  20 Pin_20         unconnected-(J1-Pin_20-Pad20) (no other connection)

R1  (4.7k, )
   pin   1 R1             +5V                          C1.1 C2.1 CR1.2(A) J1.1(Pin_1) Z1.14(VCC) Z2.14(VCC) Z3.16(VCC) Z4.16(VCC)
   pin   2 R1.2           Net-(R1A-R1.2)               SW30.2(2) SW31.1(1) SW32.2(2) SW33.1(1) SW34.2(2) SW35.1(1) SW61.1(1) Z4.10
   pin   3 R2.2           Net-(R1B-R2.2)               SW48.1(1) SW49.2(2) SW50.1(1) SW51.1(1) SW52.1(1) SW53.1(1) SW65.2(2) Z4.6
   pin   4 R3.2           Net-(R1C-R3.2)               SW10.2(2) SW11.1(1) SW12.1(1) SW13.1(1) SW14.1(1) SW15.1(1) SW16.2(2) SW57.1(1) SW58.1(1) Z4.4
   pin   5 R4.2           Net-(R1D-R4.2)               SW42.2(2) SW43.2(2) SW44.2(2) SW45.1(1) SW46.2(2) SW47.1(1) SW63.1(1) SW64.2(2) Z4.2
   pin   6 R5.2           Net-(R1E-R5.2)               SW24.1(1) SW25.2(2) SW26.2(2) SW27.1(1) SW28.2(2) SW29.2(2) SW60.1(1) Z3.10
   pin   7 R6.2           Net-(R1F-R6.2)               SW36.2(2) SW37.2(2) SW38.2(2) SW39.1(1) SW40.1(1) SW41.2(2) SW62.1(1) Z3.6
   pin   8 R7.2           Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]
   pin   9 R8.2           Net-(R1H-R8.2)               SW17.1(1) SW18.1(1) SW19.2(2) SW20.1(1) SW21.2(2) SW22.2(2) SW23.2(2) SW59.2(2) Z3.2

R2  (330, )
   pin   1                Net-(CR1-K)                  CR1.1(K)
   pin   2                GND                          C1.2 C2.2 J1.19(Pin_19) Z1.7(GND) Z2.7(GND) Z3.8(GND) Z4.8(GND)

SW1  (@, )
   pin   1 1              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]
   pin   2 2              Net-(SW1-Pad2)               SW10.1(1) SW17.2(2) SW24.2(2) SW30.1(1) SW36.1(1) SW42.1(1) SW48.2(2) Z1.8

SW2  (H, )
   pin   1 1              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]
   pin   2 2              Net-(SW11-Pad2)              SW11.2(2) SW18.2(2) SW25.1(1) SW31.2(2) SW37.1(1) SW43.1(1) SW49.1(1) Z1.10

SW3  (P, )
   pin   1 1              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]
   pin   2 2              Net-(SW12-Pad2)              SW12.2(2) SW19.1(1) SW26.1(1) SW32.1(1) SW38.1(1) SW44.1(1) SW50.2(2) Z2.6

SW4  (X, )
   pin   1 1              Net-(SW13-Pad2)              SW13.2(2) SW20.2(2) Z2.8
   pin   2 2              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]

SW5  (0, )
   pin   1 1              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]
   pin   2 2              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]

SW6  (8, )
   pin   1 1              Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW28.1(1) SW34.1(1) SW40.2(2) SW46.1(1) SW52.2(2) SW55.2(2) SW58.2(2) SW64.1(1) Z1.4
   pin   2 2              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]

SW7  (ENTER, )
   pin   1 1              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]
   pin   2 2              Net-(SW16-Pad1)              SW16.1(1) SW23.1(1) SW29.1(1) SW35.2(2) SW41.1(1) SW47.2(2) SW53.2(2) SW56.1(1) Z2.4

SW8  (LSHIFT, )
   pin   1 1              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]
   pin   2 2              Net-(SW8-Pad2)               SW9.1(1) Z2.10

SW9  (RSHIFT, )
   pin   1 1              Net-(SW8-Pad2)               SW8.2(2) Z2.10
   pin   2 2              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]

SW10  (A, )
   pin   1 1              Net-(SW1-Pad2)               SW1.2(2) SW17.2(2) SW24.2(2) SW30.1(1) SW36.1(1) SW42.1(1) SW48.2(2) Z1.8
   pin   2 2              Net-(R1C-R3.2)               R1.4(R3.2) SW11.1(1) SW12.1(1) SW13.1(1) SW14.1(1) SW15.1(1) SW16.2(2) SW57.1(1) SW58.1(1) Z4.4

SW11  (I, )
   pin   1 1              Net-(R1C-R3.2)               R1.4(R3.2) SW10.2(2) SW12.1(1) SW13.1(1) SW14.1(1) SW15.1(1) SW16.2(2) SW57.1(1) SW58.1(1) Z4.4
   pin   2 2              Net-(SW11-Pad2)              SW18.2(2) SW2.2(2) SW25.1(1) SW31.2(2) SW37.1(1) SW43.1(1) SW49.1(1) Z1.10

SW12  (Q, )
   pin   1 1              Net-(R1C-R3.2)               R1.4(R3.2) SW10.2(2) SW11.1(1) SW13.1(1) SW14.1(1) SW15.1(1) SW16.2(2) SW57.1(1) SW58.1(1) Z4.4
   pin   2 2              Net-(SW12-Pad2)              SW19.1(1) SW26.1(1) SW3.2(2) SW32.1(1) SW38.1(1) SW44.1(1) SW50.2(2) Z2.6

SW13  (Y, )
   pin   1 1              Net-(R1C-R3.2)               R1.4(R3.2) SW10.2(2) SW11.1(1) SW12.1(1) SW14.1(1) SW15.1(1) SW16.2(2) SW57.1(1) SW58.1(1) Z4.4
   pin   2 2              Net-(SW13-Pad2)              SW20.2(2) SW4.1(1) Z2.8

SW14  (1, )
   pin   1 1              Net-(R1C-R3.2)               R1.4(R3.2) SW10.2(2) SW11.1(1) SW12.1(1) SW13.1(1) SW15.1(1) SW16.2(2) SW57.1(1) SW58.1(1) Z4.4
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW15  (9, )
   pin   1 1              Net-(R1C-R3.2)               R1.4(R3.2) SW10.2(2) SW11.1(1) SW12.1(1) SW13.1(1) SW14.1(1) SW16.2(2) SW57.1(1) SW58.1(1) Z4.4
   pin   2 2              Net-(SW15-Pad2)              SW22.1(1) SW28.1(1) SW34.1(1) SW40.2(2) SW46.1(1) SW52.2(2) SW55.2(2) SW58.2(2) SW6.1(1) SW64.1(1) Z1.4

SW16  (CLEAR, )
   pin   1 1              Net-(SW16-Pad1)              SW23.1(1) SW29.1(1) SW35.2(2) SW41.1(1) SW47.2(2) SW53.2(2) SW56.1(1) SW7.2(2) Z2.4
   pin   2 2              Net-(R1C-R3.2)               R1.4(R3.2) SW10.2(2) SW11.1(1) SW12.1(1) SW13.1(1) SW14.1(1) SW15.1(1) SW57.1(1) SW58.1(1) Z4.4

SW17  (B, )
   pin   1 1              Net-(R1H-R8.2)               R1.9(R8.2) SW18.1(1) SW19.2(2) SW20.1(1) SW21.2(2) SW22.2(2) SW23.2(2) SW59.2(2) Z3.2
   pin   2 2              Net-(SW1-Pad2)               SW1.2(2) SW10.1(1) SW24.2(2) SW30.1(1) SW36.1(1) SW42.1(1) SW48.2(2) Z1.8

SW18  (J, )
   pin   1 1              Net-(R1H-R8.2)               R1.9(R8.2) SW17.1(1) SW19.2(2) SW20.1(1) SW21.2(2) SW22.2(2) SW23.2(2) SW59.2(2) Z3.2
   pin   2 2              Net-(SW11-Pad2)              SW11.2(2) SW2.2(2) SW25.1(1) SW31.2(2) SW37.1(1) SW43.1(1) SW49.1(1) Z1.10

SW19  (R, )
   pin   1 1              Net-(SW12-Pad2)              SW12.2(2) SW26.1(1) SW3.2(2) SW32.1(1) SW38.1(1) SW44.1(1) SW50.2(2) Z2.6
   pin   2 2              Net-(R1H-R8.2)               R1.9(R8.2) SW17.1(1) SW18.1(1) SW20.1(1) SW21.2(2) SW22.2(2) SW23.2(2) SW59.2(2) Z3.2

SW20  (Z, )
   pin   1 1              Net-(R1H-R8.2)               R1.9(R8.2) SW17.1(1) SW18.1(1) SW19.2(2) SW21.2(2) SW22.2(2) SW23.2(2) SW59.2(2) Z3.2
   pin   2 2              Net-(SW13-Pad2)              SW13.2(2) SW4.1(1) Z2.8

SW21  (2, )
   pin   1 1              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]
   pin   2 2              Net-(R1H-R8.2)               R1.9(R8.2) SW17.1(1) SW18.1(1) SW19.2(2) SW20.1(1) SW22.2(2) SW23.2(2) SW59.2(2) Z3.2

SW22  (:, )
   pin   1 1              Net-(SW15-Pad2)              SW15.2(2) SW28.1(1) SW34.1(1) SW40.2(2) SW46.1(1) SW52.2(2) SW55.2(2) SW58.2(2) SW6.1(1) SW64.1(1) Z1.4
   pin   2 2              Net-(R1H-R8.2)               R1.9(R8.2) SW17.1(1) SW18.1(1) SW19.2(2) SW20.1(1) SW21.2(2) SW23.2(2) SW59.2(2) Z3.2

SW23  (BREAK, )
   pin   1 1              Net-(SW16-Pad1)              SW16.1(1) SW29.1(1) SW35.2(2) SW41.1(1) SW47.2(2) SW53.2(2) SW56.1(1) SW7.2(2) Z2.4
   pin   2 2              Net-(R1H-R8.2)               R1.9(R8.2) SW17.1(1) SW18.1(1) SW19.2(2) SW20.1(1) SW21.2(2) SW22.2(2) SW59.2(2) Z3.2

SW24  (C, )
   pin   1 1              Net-(R1E-R5.2)               R1.6(R5.2) SW25.2(2) SW26.2(2) SW27.1(1) SW28.2(2) SW29.2(2) SW60.1(1) Z3.10
   pin   2 2              Net-(SW1-Pad2)               SW1.2(2) SW10.1(1) SW17.2(2) SW30.1(1) SW36.1(1) SW42.1(1) SW48.2(2) Z1.8

SW25  (K, )
   pin   1 1              Net-(SW11-Pad2)              SW11.2(2) SW18.2(2) SW2.2(2) SW31.2(2) SW37.1(1) SW43.1(1) SW49.1(1) Z1.10
   pin   2 2              Net-(R1E-R5.2)               R1.6(R5.2) SW24.1(1) SW26.2(2) SW27.1(1) SW28.2(2) SW29.2(2) SW60.1(1) Z3.10

SW26  (S, )
   pin   1 1              Net-(SW12-Pad2)              SW12.2(2) SW19.1(1) SW3.2(2) SW32.1(1) SW38.1(1) SW44.1(1) SW50.2(2) Z2.6
   pin   2 2              Net-(R1E-R5.2)               R1.6(R5.2) SW24.1(1) SW25.2(2) SW27.1(1) SW28.2(2) SW29.2(2) SW60.1(1) Z3.10

SW27  (3, )
   pin   1 1              Net-(R1E-R5.2)               R1.6(R5.2) SW24.1(1) SW25.2(2) SW26.2(2) SW28.2(2) SW29.2(2) SW60.1(1) Z3.10
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW28  (;, )
   pin   1 1              Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW34.1(1) SW40.2(2) SW46.1(1) SW52.2(2) SW55.2(2) SW58.2(2) SW6.1(1) SW64.1(1) Z1.4
   pin   2 2              Net-(R1E-R5.2)               R1.6(R5.2) SW24.1(1) SW25.2(2) SW26.2(2) SW27.1(1) SW29.2(2) SW60.1(1) Z3.10

SW29  (UP, )
   pin   1 1              Net-(SW16-Pad1)              SW16.1(1) SW23.1(1) SW35.2(2) SW41.1(1) SW47.2(2) SW53.2(2) SW56.1(1) SW7.2(2) Z2.4
   pin   2 2              Net-(R1E-R5.2)               R1.6(R5.2) SW24.1(1) SW25.2(2) SW26.2(2) SW27.1(1) SW28.2(2) SW60.1(1) Z3.10

SW30  (D, )
   pin   1 1              Net-(SW1-Pad2)               SW1.2(2) SW10.1(1) SW17.2(2) SW24.2(2) SW36.1(1) SW42.1(1) SW48.2(2) Z1.8
   pin   2 2              Net-(R1A-R1.2)               R1.2(R1.2) SW31.1(1) SW32.2(2) SW33.1(1) SW34.2(2) SW35.1(1) SW61.1(1) Z4.10

SW31  (L, )
   pin   1 1              Net-(R1A-R1.2)               R1.2(R1.2) SW30.2(2) SW32.2(2) SW33.1(1) SW34.2(2) SW35.1(1) SW61.1(1) Z4.10
   pin   2 2              Net-(SW11-Pad2)              SW11.2(2) SW18.2(2) SW2.2(2) SW25.1(1) SW37.1(1) SW43.1(1) SW49.1(1) Z1.10

SW32  (T, )
   pin   1 1              Net-(SW12-Pad2)              SW12.2(2) SW19.1(1) SW26.1(1) SW3.2(2) SW38.1(1) SW44.1(1) SW50.2(2) Z2.6
   pin   2 2              Net-(R1A-R1.2)               R1.2(R1.2) SW30.2(2) SW31.1(1) SW33.1(1) SW34.2(2) SW35.1(1) SW61.1(1) Z4.10

SW33  (4, )
   pin   1 1              Net-(R1A-R1.2)               R1.2(R1.2) SW30.2(2) SW31.1(1) SW32.2(2) SW34.2(2) SW35.1(1) SW61.1(1) Z4.10
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW34  (,, )
   pin   1 1              Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW28.1(1) SW40.2(2) SW46.1(1) SW52.2(2) SW55.2(2) SW58.2(2) SW6.1(1) SW64.1(1) Z1.4
   pin   2 2              Net-(R1A-R1.2)               R1.2(R1.2) SW30.2(2) SW31.1(1) SW32.2(2) SW33.1(1) SW35.1(1) SW61.1(1) Z4.10

SW35  (DOWN, )
   pin   1 1              Net-(R1A-R1.2)               R1.2(R1.2) SW30.2(2) SW31.1(1) SW32.2(2) SW33.1(1) SW34.2(2) SW61.1(1) Z4.10
   pin   2 2              Net-(SW16-Pad1)              SW16.1(1) SW23.1(1) SW29.1(1) SW41.1(1) SW47.2(2) SW53.2(2) SW56.1(1) SW7.2(2) Z2.4

SW36  (E, )
   pin   1 1              Net-(SW1-Pad2)               SW1.2(2) SW10.1(1) SW17.2(2) SW24.2(2) SW30.1(1) SW42.1(1) SW48.2(2) Z1.8
   pin   2 2              Net-(R1F-R6.2)               R1.7(R6.2) SW37.2(2) SW38.2(2) SW39.1(1) SW40.1(1) SW41.2(2) SW62.1(1) Z3.6

SW37  (M, )
   pin   1 1              Net-(SW11-Pad2)              SW11.2(2) SW18.2(2) SW2.2(2) SW25.1(1) SW31.2(2) SW43.1(1) SW49.1(1) Z1.10
   pin   2 2              Net-(R1F-R6.2)               R1.7(R6.2) SW36.2(2) SW38.2(2) SW39.1(1) SW40.1(1) SW41.2(2) SW62.1(1) Z3.6

SW38  (U, )
   pin   1 1              Net-(SW12-Pad2)              SW12.2(2) SW19.1(1) SW26.1(1) SW3.2(2) SW32.1(1) SW44.1(1) SW50.2(2) Z2.6
   pin   2 2              Net-(R1F-R6.2)               R1.7(R6.2) SW36.2(2) SW37.2(2) SW39.1(1) SW40.1(1) SW41.2(2) SW62.1(1) Z3.6

SW39  (5, )
   pin   1 1              Net-(R1F-R6.2)               R1.7(R6.2) SW36.2(2) SW37.2(2) SW38.2(2) SW40.1(1) SW41.2(2) SW62.1(1) Z3.6
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW40  (-, )
   pin   1 1              Net-(R1F-R6.2)               R1.7(R6.2) SW36.2(2) SW37.2(2) SW38.2(2) SW39.1(1) SW41.2(2) SW62.1(1) Z3.6
   pin   2 2              Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW28.1(1) SW34.1(1) SW46.1(1) SW52.2(2) SW55.2(2) SW58.2(2) SW6.1(1) SW64.1(1) Z1.4

SW41  (LEFT, )
   pin   1 1              Net-(SW16-Pad1)              SW16.1(1) SW23.1(1) SW29.1(1) SW35.2(2) SW47.2(2) SW53.2(2) SW56.1(1) SW7.2(2) Z2.4
   pin   2 2              Net-(R1F-R6.2)               R1.7(R6.2) SW36.2(2) SW37.2(2) SW38.2(2) SW39.1(1) SW40.1(1) SW62.1(1) Z3.6

SW42  (F, )
   pin   1 1              Net-(SW1-Pad2)               SW1.2(2) SW10.1(1) SW17.2(2) SW24.2(2) SW30.1(1) SW36.1(1) SW48.2(2) Z1.8
   pin   2 2              Net-(R1D-R4.2)               R1.5(R4.2) SW43.2(2) SW44.2(2) SW45.1(1) SW46.2(2) SW47.1(1) SW63.1(1) SW64.2(2) Z4.2

SW43  (N, )
   pin   1 1              Net-(SW11-Pad2)              SW11.2(2) SW18.2(2) SW2.2(2) SW25.1(1) SW31.2(2) SW37.1(1) SW49.1(1) Z1.10
   pin   2 2              Net-(R1D-R4.2)               R1.5(R4.2) SW42.2(2) SW44.2(2) SW45.1(1) SW46.2(2) SW47.1(1) SW63.1(1) SW64.2(2) Z4.2

SW44  (V, )
   pin   1 1              Net-(SW12-Pad2)              SW12.2(2) SW19.1(1) SW26.1(1) SW3.2(2) SW32.1(1) SW38.1(1) SW50.2(2) Z2.6
   pin   2 2              Net-(R1D-R4.2)               R1.5(R4.2) SW42.2(2) SW43.2(2) SW45.1(1) SW46.2(2) SW47.1(1) SW63.1(1) SW64.2(2) Z4.2

SW45  (6, )
   pin   1 1              Net-(R1D-R4.2)               R1.5(R4.2) SW42.2(2) SW43.2(2) SW44.2(2) SW46.2(2) SW47.1(1) SW63.1(1) SW64.2(2) Z4.2
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW46  (., )
   pin   1 1              Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW28.1(1) SW34.1(1) SW40.2(2) SW52.2(2) SW55.2(2) SW58.2(2) SW6.1(1) SW64.1(1) Z1.4
   pin   2 2              Net-(R1D-R4.2)               R1.5(R4.2) SW42.2(2) SW43.2(2) SW44.2(2) SW45.1(1) SW47.1(1) SW63.1(1) SW64.2(2) Z4.2

SW47  (RIGHT, )
   pin   1 1              Net-(R1D-R4.2)               R1.5(R4.2) SW42.2(2) SW43.2(2) SW44.2(2) SW45.1(1) SW46.2(2) SW63.1(1) SW64.2(2) Z4.2
   pin   2 2              Net-(SW16-Pad1)              SW16.1(1) SW23.1(1) SW29.1(1) SW35.2(2) SW41.1(1) SW53.2(2) SW56.1(1) SW7.2(2) Z2.4

SW48  (G, )
   pin   1 1              Net-(R1B-R2.2)               R1.3(R2.2) SW49.2(2) SW50.1(1) SW51.1(1) SW52.1(1) SW53.1(1) SW65.2(2) Z4.6
   pin   2 2              Net-(SW1-Pad2)               SW1.2(2) SW10.1(1) SW17.2(2) SW24.2(2) SW30.1(1) SW36.1(1) SW42.1(1) Z1.8

SW49  (O, )
   pin   1 1              Net-(SW11-Pad2)              SW11.2(2) SW18.2(2) SW2.2(2) SW25.1(1) SW31.2(2) SW37.1(1) SW43.1(1) Z1.10
   pin   2 2              Net-(R1B-R2.2)               R1.3(R2.2) SW48.1(1) SW50.1(1) SW51.1(1) SW52.1(1) SW53.1(1) SW65.2(2) Z4.6

SW50  (W, )
   pin   1 1              Net-(R1B-R2.2)               R1.3(R2.2) SW48.1(1) SW49.2(2) SW51.1(1) SW52.1(1) SW53.1(1) SW65.2(2) Z4.6
   pin   2 2              Net-(SW12-Pad2)              SW12.2(2) SW19.1(1) SW26.1(1) SW3.2(2) SW32.1(1) SW38.1(1) SW44.1(1) Z2.6

SW51  (7, )
   pin   1 1              Net-(R1B-R2.2)               R1.3(R2.2) SW48.1(1) SW49.2(2) SW50.1(1) SW52.1(1) SW53.1(1) SW65.2(2) Z4.6
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW52  (/, )
   pin   1 1              Net-(R1B-R2.2)               R1.3(R2.2) SW48.1(1) SW49.2(2) SW50.1(1) SW51.1(1) SW53.1(1) SW65.2(2) Z4.6
   pin   2 2              Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW28.1(1) SW34.1(1) SW40.2(2) SW46.1(1) SW55.2(2) SW58.2(2) SW6.1(1) SW64.1(1) Z1.4

SW53  (SPACE, )
   pin   1 1              Net-(R1B-R2.2)               R1.3(R2.2) SW48.1(1) SW49.2(2) SW50.1(1) SW51.1(1) SW52.1(1) SW65.2(2) Z4.6
   pin   2 2              Net-(SW16-Pad1)              SW16.1(1) SW23.1(1) SW29.1(1) SW35.2(2) SW41.1(1) SW47.2(2) SW56.1(1) SW7.2(2) Z2.4

SW54  (0, )
   pin   1 1              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW55  (8, )
   pin   1 1              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]
   pin   2 2              Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW28.1(1) SW34.1(1) SW40.2(2) SW46.1(1) SW52.2(2) SW58.2(2) SW6.1(1) SW64.1(1) Z1.4

SW56  (ENTER, )
   pin   1 1              Net-(SW16-Pad1)              SW16.1(1) SW23.1(1) SW29.1(1) SW35.2(2) SW41.1(1) SW47.2(2) SW53.2(2) SW7.2(2) Z2.4
   pin   2 2              Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]

SW57  (1, )
   pin   1 1              Net-(R1C-R3.2)               R1.4(R3.2) SW10.2(2) SW11.1(1) SW12.1(1) SW13.1(1) SW14.1(1) SW15.1(1) SW16.2(2) SW58.1(1) Z4.4
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW58  (9, )
   pin   1 1              Net-(R1C-R3.2)               R1.4(R3.2) SW10.2(2) SW11.1(1) SW12.1(1) SW13.1(1) SW14.1(1) SW15.1(1) SW16.2(2) SW57.1(1) Z4.4
   pin   2 2              Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW28.1(1) SW34.1(1) SW40.2(2) SW46.1(1) SW52.2(2) SW55.2(2) SW6.1(1) SW64.1(1) Z1.4

SW59  (2, )
   pin   1 1              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]
   pin   2 2              Net-(R1H-R8.2)               R1.9(R8.2) SW17.1(1) SW18.1(1) SW19.2(2) SW20.1(1) SW21.2(2) SW22.2(2) SW23.2(2) Z3.2

SW60  (3, )
   pin   1 1              Net-(R1E-R5.2)               R1.6(R5.2) SW24.1(1) SW25.2(2) SW26.2(2) SW27.1(1) SW28.2(2) SW29.2(2) Z3.10
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW61  (4, )
   pin   1 1              Net-(R1A-R1.2)               R1.2(R1.2) SW30.2(2) SW31.1(1) SW32.2(2) SW33.1(1) SW34.2(2) SW35.1(1) Z4.10
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW62  (5, )
   pin   1 1              Net-(R1F-R6.2)               R1.7(R6.2) SW36.2(2) SW37.2(2) SW38.2(2) SW39.1(1) SW40.1(1) SW41.2(2) Z3.6
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW63  (6, )
   pin   1 1              Net-(R1D-R4.2)               R1.5(R4.2) SW42.2(2) SW43.2(2) SW44.2(2) SW45.1(1) SW46.2(2) SW47.1(1) SW64.2(2) Z4.2
   pin   2 2              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]

SW64  (., )
   pin   1 1              Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW28.1(1) SW34.1(1) SW40.2(2) SW46.1(1) SW52.2(2) SW55.2(2) SW58.2(2) SW6.1(1) Z1.4
   pin   2 2              Net-(R1D-R4.2)               R1.5(R4.2) SW42.2(2) SW43.2(2) SW44.2(2) SW45.1(1) SW46.2(2) SW47.1(1) SW63.1(1) Z4.2

SW65  (7, )
   pin   1 1              Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]
   pin   2 2              Net-(R1B-R2.2)               R1.3(R2.2) SW48.1(1) SW49.2(2) SW50.1(1) SW51.1(1) SW52.1(1) SW53.1(1) Z4.6

Z1  (74LS05, )
   pin   1                unconnected-(Z1-Pad1)        (no other connection)
   pin   2                unconnected-(Z1-Pad2)        (no other connection)
   pin   3                A5                           J1.3(Pin_3)
   pin   4                Net-(SW15-Pad2)              SW15.2(2) SW22.1(1) SW28.1(1) SW34.1(1) SW40.2(2) SW46.1(1) SW52.2(2) SW55.2(2) SW58.2(2) SW6.1(1) SW64.1(1)
   pin   5                A4                           J1.2(Pin_2)
   pin   6                Net-(SW14-Pad2)              [net Net-(SW14-Pad2), 17 pins]
   pin   7 GND            GND                          C1.2 C2.2 J1.19(Pin_19) R2.2 Z2.7(GND) Z3.8(GND) Z4.8(GND)
   pin   8                Net-(SW1-Pad2)               SW1.2(2) SW10.1(1) SW17.2(2) SW24.2(2) SW30.1(1) SW36.1(1) SW42.1(1) SW48.2(2)
   pin   9                A0                           J1.5(Pin_5)
   pin  10                Net-(SW11-Pad2)              SW11.2(2) SW18.2(2) SW2.2(2) SW25.1(1) SW31.2(2) SW37.1(1) SW43.1(1) SW49.1(1)
   pin  11                A1                           J1.4(Pin_4)
   pin  12                unconnected-(Z1-Pad12)       (no other connection)
   pin  13                unconnected-(Z1-Pad13)       (no other connection)
   pin  14 VCC            +5V                          C1.1 C2.1 CR1.2(A) J1.1(Pin_1) R1.1(R1) Z2.14(VCC) Z3.16(VCC) Z4.16(VCC)

Z2  (74LS05, )
   pin   1                unconnected-(Z2-Pad1)        (no other connection)
   pin   2                unconnected-(Z2-Pad2)        (no other connection)
   pin   3                A6                           J1.7(Pin_7)
   pin   4                Net-(SW16-Pad1)              SW16.1(1) SW23.1(1) SW29.1(1) SW35.2(2) SW41.1(1) SW47.2(2) SW53.2(2) SW56.1(1) SW7.2(2)
   pin   5                A2                           J1.6(Pin_6)
   pin   6                Net-(SW12-Pad2)              SW12.2(2) SW19.1(1) SW26.1(1) SW3.2(2) SW32.1(1) SW38.1(1) SW44.1(1) SW50.2(2)
   pin   7 GND            GND                          C1.2 C2.2 J1.19(Pin_19) R2.2 Z1.7(GND) Z3.8(GND) Z4.8(GND)
   pin   8                Net-(SW13-Pad2)              SW13.2(2) SW20.2(2) SW4.1(1)
   pin   9                A3                           J1.9(Pin_9)
   pin  10                Net-(SW8-Pad2)               SW8.2(2) SW9.1(1)
   pin  11                A7                           J1.8(Pin_8)
   pin  12                unconnected-(Z2-Pad12)       (no other connection)
   pin  13                unconnected-(Z2-Pad13)       (no other connection)
   pin  14 VCC            +5V                          C1.1 C2.1 CR1.2(A) J1.1(Pin_1) R1.1(R1) Z1.14(VCC) Z3.16(VCC) Z4.16(VCC)

Z3  (74LS368, )
   pin   1                ~{KYBD}                      J1.14(Pin_14) Z4.1
   pin   2                Net-(R1H-R8.2)               R1.9(R8.2) SW17.1(1) SW18.1(1) SW19.2(2) SW20.1(1) SW21.2(2) SW22.2(2) SW23.2(2) SW59.2(2)
   pin   3                D2                           J1.10(Pin_10)
   pin   4                Net-(R1G-R7.2)               [net Net-(R1G-R7.2), 14 pins]
   pin   5                D0                           J1.11(Pin_11)
   pin   6                Net-(R1F-R6.2)               R1.7(R6.2) SW36.2(2) SW37.2(2) SW38.2(2) SW39.1(1) SW40.1(1) SW41.2(2) SW62.1(1)
   pin   7                D5                           J1.12(Pin_12)
   pin   8 GND            GND                          C1.2 C2.2 J1.19(Pin_19) R2.2 Z1.7(GND) Z2.7(GND) Z4.8(GND)
   pin   9                D3                           J1.13(Pin_13)
   pin  10                Net-(R1E-R5.2)               R1.6(R5.2) SW24.1(1) SW25.2(2) SW26.2(2) SW27.1(1) SW28.2(2) SW29.2(2) SW60.1(1)
   pin  11                unconnected-(Z3-Pad11)       (no other connection)
   pin  12                unconnected-(Z3-Pad12)       (no other connection)
   pin  13                unconnected-(Z3-Pad13)       (no other connection)
   pin  14                unconnected-(Z3-Pad14)       (no other connection)
   pin  15                unconnected-(Z3-Pad15)       (no other connection)
   pin  16 VCC            +5V                          C1.1 C2.1 CR1.2(A) J1.1(Pin_1) R1.1(R1) Z1.14(VCC) Z2.14(VCC) Z4.16(VCC)

Z4  (74LS368, )
   pin   1                ~{KYBD}                      J1.14(Pin_14) Z3.1
   pin   2                Net-(R1D-R4.2)               R1.5(R4.2) SW42.2(2) SW43.2(2) SW44.2(2) SW45.1(1) SW46.2(2) SW47.1(1) SW63.1(1) SW64.2(2)
   pin   3                D6                           J1.15(Pin_15)
   pin   4                Net-(R1C-R3.2)               R1.4(R3.2) SW10.2(2) SW11.1(1) SW12.1(1) SW13.1(1) SW14.1(1) SW15.1(1) SW16.2(2) SW57.1(1) SW58.1(1)
   pin   5                D1                           J1.16(Pin_16)
   pin   6                Net-(R1B-R2.2)               R1.3(R2.2) SW48.1(1) SW49.2(2) SW50.1(1) SW51.1(1) SW52.1(1) SW53.1(1) SW65.2(2)
   pin   7                D7                           J1.17(Pin_17)
   pin   8 GND            GND                          C1.2 C2.2 J1.19(Pin_19) R2.2 Z1.7(GND) Z2.7(GND) Z3.8(GND)
   pin   9                D4                           J1.18(Pin_18)
   pin  10                Net-(R1A-R1.2)               R1.2(R1.2) SW30.2(2) SW31.1(1) SW32.2(2) SW33.1(1) SW34.2(2) SW35.1(1) SW61.1(1)
   pin  11                unconnected-(Z4-Pad11)       (no other connection)
   pin  12                unconnected-(Z4-Pad12)       (no other connection)
   pin  13                unconnected-(Z4-Pad13)       (no other connection)
   pin  14                unconnected-(Z4-Pad14)       (no other connection)
   pin  15                unconnected-(Z4-Pad15)       (no other connection)
   pin  16 VCC            +5V                          C1.1 C2.1 CR1.2(A) J1.1(Pin_1) R1.1(R1) Z1.14(VCC) Z2.14(VCC) Z3.16(VCC)

```
## Nets

```
+5V   (9 pins)
    C1       0.1uF              pin   1  
    C2       0.1uF              pin   1  
    CR1      RED 5mm            pin   2  A
    J1       Connection Keyboad Side pin   1  Pin_1
    R1       4.7k               pin   1  R1
    Z1       74LS05             pin  14  VCC
    Z2       74LS05             pin  14  VCC
    Z3       74LS368            pin  16  VCC
    Z4       74LS368            pin  16  VCC

/A0   (2 pins)
    J1       Connection Keyboad Side pin   5  Pin_5
    Z1       74LS05             pin   9  

/A1   (2 pins)
    J1       Connection Keyboad Side pin   4  Pin_4
    Z1       74LS05             pin  11  

/A2   (2 pins)
    J1       Connection Keyboad Side pin   6  Pin_6
    Z2       74LS05             pin   5  

/A3   (2 pins)
    J1       Connection Keyboad Side pin   9  Pin_9
    Z2       74LS05             pin   9  

/A4   (2 pins)
    J1       Connection Keyboad Side pin   2  Pin_2
    Z1       74LS05             pin   5  

/A5   (2 pins)
    J1       Connection Keyboad Side pin   3  Pin_3
    Z1       74LS05             pin   3  

/A6   (2 pins)
    J1       Connection Keyboad Side pin   7  Pin_7
    Z2       74LS05             pin   3  

/A7   (2 pins)
    J1       Connection Keyboad Side pin   8  Pin_8
    Z2       74LS05             pin  11  

/D0   (2 pins)
    J1       Connection Keyboad Side pin  11  Pin_11
    Z3       74LS368            pin   5  

/D1   (2 pins)
    J1       Connection Keyboad Side pin  16  Pin_16
    Z4       74LS368            pin   5  

/D2   (2 pins)
    J1       Connection Keyboad Side pin  10  Pin_10
    Z3       74LS368            pin   3  

/D3   (2 pins)
    J1       Connection Keyboad Side pin  13  Pin_13
    Z3       74LS368            pin   9  

/D4   (2 pins)
    J1       Connection Keyboad Side pin  18  Pin_18
    Z4       74LS368            pin   9  

/D5   (2 pins)
    J1       Connection Keyboad Side pin  12  Pin_12
    Z3       74LS368            pin   7  

/D6   (2 pins)
    J1       Connection Keyboad Side pin  15  Pin_15
    Z4       74LS368            pin   3  

/D7   (2 pins)
    J1       Connection Keyboad Side pin  17  Pin_17
    Z4       74LS368            pin   7  

/~{KYBD}   (3 pins)
    J1       Connection Keyboad Side pin  14  Pin_14
    Z3       74LS368            pin   1  
    Z4       74LS368            pin   1  

GND   (8 pins)
    C1       0.1uF              pin   2  
    C2       0.1uF              pin   2  
    J1       Connection Keyboad Side pin  19  Pin_19
    R2       330                pin   2  
    Z1       74LS05             pin   7  GND
    Z2       74LS05             pin   7  GND
    Z3       74LS368            pin   8  GND
    Z4       74LS368            pin   8  GND

Net-(CR1-K)   (2 pins)
    CR1      RED 5mm            pin   1  K
    R2       330                pin   1  

Net-(R1A-R1.2)   (9 pins)
    R1       4.7k               pin   2  R1.2
    SW30     D                  pin   2  2
    SW31     L                  pin   1  1
    SW32     T                  pin   2  2
    SW33     4                  pin   1  1
    SW34     ,                  pin   2  2
    SW35     DOWN               pin   1  1
    SW61     4                  pin   1  1
    Z4       74LS368            pin  10  

Net-(R1B-R2.2)   (9 pins)
    R1       4.7k               pin   3  R2.2
    SW48     G                  pin   1  1
    SW49     O                  pin   2  2
    SW50     W                  pin   1  1
    SW51     7                  pin   1  1
    SW52     /                  pin   1  1
    SW53     SPACE              pin   1  1
    SW65     7                  pin   2  2
    Z4       74LS368            pin   6  

Net-(R1C-R3.2)   (11 pins)
    R1       4.7k               pin   4  R3.2
    SW10     A                  pin   2  2
    SW11     I                  pin   1  1
    SW12     Q                  pin   1  1
    SW13     Y                  pin   1  1
    SW14     1                  pin   1  1
    SW15     9                  pin   1  1
    SW16     CLEAR              pin   2  2
    SW57     1                  pin   1  1
    SW58     9                  pin   1  1
    Z4       74LS368            pin   4  

Net-(R1D-R4.2)   (10 pins)
    R1       4.7k               pin   5  R4.2
    SW42     F                  pin   2  2
    SW43     N                  pin   2  2
    SW44     V                  pin   2  2
    SW45     6                  pin   1  1
    SW46     .                  pin   2  2
    SW47     RIGHT              pin   1  1
    SW63     6                  pin   1  1
    SW64     .                  pin   2  2
    Z4       74LS368            pin   2  

Net-(R1E-R5.2)   (9 pins)
    R1       4.7k               pin   6  R5.2
    SW24     C                  pin   1  1
    SW25     K                  pin   2  2
    SW26     S                  pin   2  2
    SW27     3                  pin   1  1
    SW28     ;                  pin   2  2
    SW29     UP                 pin   2  2
    SW60     3                  pin   1  1
    Z3       74LS368            pin  10  

Net-(R1F-R6.2)   (9 pins)
    R1       4.7k               pin   7  R6.2
    SW36     E                  pin   2  2
    SW37     M                  pin   2  2
    SW38     U                  pin   2  2
    SW39     5                  pin   1  1
    SW40     -                  pin   1  1
    SW41     LEFT               pin   2  2
    SW62     5                  pin   1  1
    Z3       74LS368            pin   6  

Net-(R1G-R7.2)   (14 pins)
    R1       4.7k               pin   8  R7.2
    SW1      @                  pin   1  1
    SW2      H                  pin   1  1
    SW3      P                  pin   1  1
    SW4      X                  pin   2  2
    SW5      0                  pin   2  2
    SW54     0                  pin   1  1
    SW55     8                  pin   1  1
    SW56     ENTER              pin   2  2
    SW6      8                  pin   2  2
    SW7      ENTER              pin   1  1
    SW8      LSHIFT             pin   1  1
    SW9      RSHIFT             pin   2  2
    Z3       74LS368            pin   4  

Net-(R1H-R8.2)   (10 pins)
    R1       4.7k               pin   9  R8.2
    SW17     B                  pin   1  1
    SW18     J                  pin   1  1
    SW19     R                  pin   2  2
    SW20     Z                  pin   1  1
    SW21     2                  pin   2  2
    SW22     :                  pin   2  2
    SW23     BREAK              pin   2  2
    SW59     2                  pin   2  2
    Z3       74LS368            pin   2  

Net-(SW1-Pad2)   (9 pins)
    SW1      @                  pin   2  2
    SW10     A                  pin   1  1
    SW17     B                  pin   2  2
    SW24     C                  pin   2  2
    SW30     D                  pin   1  1
    SW36     E                  pin   1  1
    SW42     F                  pin   1  1
    SW48     G                  pin   2  2
    Z1       74LS05             pin   8  

Net-(SW11-Pad2)   (9 pins)
    SW11     I                  pin   2  2
    SW18     J                  pin   2  2
    SW2      H                  pin   2  2
    SW25     K                  pin   1  1
    SW31     L                  pin   2  2
    SW37     M                  pin   1  1
    SW43     N                  pin   1  1
    SW49     O                  pin   1  1
    Z1       74LS05             pin  10  

Net-(SW12-Pad2)   (9 pins)
    SW12     Q                  pin   2  2
    SW19     R                  pin   1  1
    SW26     S                  pin   1  1
    SW3      P                  pin   2  2
    SW32     T                  pin   1  1
    SW38     U                  pin   1  1
    SW44     V                  pin   1  1
    SW50     W                  pin   2  2
    Z2       74LS05             pin   6  

Net-(SW13-Pad2)   (4 pins)
    SW13     Y                  pin   2  2
    SW20     Z                  pin   2  2
    SW4      X                  pin   1  1
    Z2       74LS05             pin   8  

Net-(SW14-Pad2)   (17 pins)
    SW14     1                  pin   2  2
    SW21     2                  pin   1  1
    SW27     3                  pin   2  2
    SW33     4                  pin   2  2
    SW39     5                  pin   2  2
    SW45     6                  pin   2  2
    SW5      0                  pin   1  1
    SW51     7                  pin   2  2
    SW54     0                  pin   2  2
    SW57     1                  pin   2  2
    SW59     2                  pin   1  1
    SW60     3                  pin   2  2
    SW61     4                  pin   2  2
    SW62     5                  pin   2  2
    SW63     6                  pin   2  2
    SW65     7                  pin   1  1
    Z1       74LS05             pin   6  

Net-(SW15-Pad2)   (12 pins)
    SW15     9                  pin   2  2
    SW22     :                  pin   1  1
    SW28     ;                  pin   1  1
    SW34     ,                  pin   1  1
    SW40     -                  pin   2  2
    SW46     .                  pin   1  1
    SW52     /                  pin   2  2
    SW55     8                  pin   2  2
    SW58     9                  pin   2  2
    SW6      8                  pin   1  1
    SW64     .                  pin   1  1
    Z1       74LS05             pin   4  

Net-(SW16-Pad1)   (10 pins)
    SW16     CLEAR              pin   1  1
    SW23     BREAK              pin   1  1
    SW29     UP                 pin   1  1
    SW35     DOWN               pin   2  2
    SW41     LEFT               pin   1  1
    SW47     RIGHT              pin   2  2
    SW53     SPACE              pin   2  2
    SW56     ENTER              pin   1  1
    SW7      ENTER              pin   2  2
    Z2       74LS05             pin   4  

Net-(SW8-Pad2)   (3 pins)
    SW8      LSHIFT             pin   2  2
    SW9      RSHIFT             pin   1  1
    Z2       74LS05             pin  10  

unconnected-(J1-Pin_20-Pad20)   (1 pins)
    J1       Connection Keyboad Side pin  20  Pin_20

unconnected-(Z1-Pad1)   (1 pins)
    Z1       74LS05             pin   1  

unconnected-(Z1-Pad12)   (1 pins)
    Z1       74LS05             pin  12  

unconnected-(Z1-Pad13)   (1 pins)
    Z1       74LS05             pin  13  

unconnected-(Z1-Pad2)   (1 pins)
    Z1       74LS05             pin   2  

unconnected-(Z2-Pad1)   (1 pins)
    Z2       74LS05             pin   1  

unconnected-(Z2-Pad12)   (1 pins)
    Z2       74LS05             pin  12  

unconnected-(Z2-Pad13)   (1 pins)
    Z2       74LS05             pin  13  

unconnected-(Z2-Pad2)   (1 pins)
    Z2       74LS05             pin   2  

unconnected-(Z3-Pad11)   (1 pins)
    Z3       74LS368            pin  11  

unconnected-(Z3-Pad12)   (1 pins)
    Z3       74LS368            pin  12  

unconnected-(Z3-Pad13)   (1 pins)
    Z3       74LS368            pin  13  

unconnected-(Z3-Pad14)   (1 pins)
    Z3       74LS368            pin  14  

unconnected-(Z3-Pad15)   (1 pins)
    Z3       74LS368            pin  15  

unconnected-(Z4-Pad11)   (1 pins)
    Z4       74LS368            pin  11  

unconnected-(Z4-Pad12)   (1 pins)
    Z4       74LS368            pin  12  

unconnected-(Z4-Pad13)   (1 pins)
    Z4       74LS368            pin  13  

unconnected-(Z4-Pad14)   (1 pins)
    Z4       74LS368            pin  14  

unconnected-(Z4-Pad15)   (1 pins)
    Z4       74LS368            pin  15  

```
