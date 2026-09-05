# Keyboard adapter (Tandy <-> TEC) — complete netlist

Generated from `TRS-80-Model-I-Keyboard-Adapter-main` by `verify/emit.py`, which exports the schematic with `kicad-cli` and parses it with the same code the claims in `verify/claims.py` use.

**2 components · 20 nets · 39 pin connections.**

Three views of the same information: components, a connection view answering "what is this pin wired to", and a net index answering "what is on this net". The redundancy is deliberate — it is what lets the file be checked against itself.

No integrity problems: every node names a known component, every pin number is valid for that component's symbol, and the two views agree on the connection count.

## Components

| ref | value | sheet |
|---|---|---|
| `J1` | Tandy Model 1 |  |
| `J2` | TEC (Japanese) Model 1 |  |

## Connections

For each pin: its name, its net, and what else is on that net. Nets with more than 12 pins (power, ground, buses) are named rather than expanded.

```
J1  (Tandy Model 1, )
   pin   1 Pin_1          +5V                          J2.1(Pin_1)
   pin   2 Pin_2          A4                           J2.2(Pin_2)
   pin   3 Pin_3          A5                           J2.3(Pin_3)
   pin   4 Pin_4          A1                           J2.4(Pin_4)
   pin   5 Pin_5          A0                           J2.5(Pin_5)
   pin   6 Pin_6          A2                           J2.6(Pin_6)
   pin   7 Pin_7          A6                           J2.7(Pin_7)
   pin   8 Pin_8          A7                           J2.8(Pin_8)
   pin   9 Pin_9          A3                           J2.9(Pin_9)
   pin  10 Pin_10         D2                           J2.13(Pin_13)
   pin  11 Pin_11         D0                           J2.11(Pin_11)
   pin  12 Pin_12         D5                           J2.16(Pin_16)
   pin  13 Pin_13         D3                           J2.14(Pin_14)
   pin  14 Pin_14         ~{KYBD}                      J2.10(Pin_10)
   pin  15 Pin_15         D6                           J2.17(Pin_17)
   pin  16 Pin_16         D1                           J2.12(Pin_12)
   pin  17 Pin_17         D7                           J2.18(Pin_18)
   pin  18 Pin_18         D4                           J2.15(Pin_15)
   pin  19 Pin_19         GND                          J2.19(Pin_19)
   pin  20 Pin_20         unconnected-(J1-Pin_20-Pad20) (no other connection)

J2  (TEC (Japanese) Model 1, )
   pin   1 Pin_1          +5V                          J1.1(Pin_1)
   pin   2 Pin_2          A4                           J1.2(Pin_2)
   pin   3 Pin_3          A5                           J1.3(Pin_3)
   pin   4 Pin_4          A1                           J1.4(Pin_4)
   pin   5 Pin_5          A0                           J1.5(Pin_5)
   pin   6 Pin_6          A2                           J1.6(Pin_6)
   pin   7 Pin_7          A6                           J1.7(Pin_7)
   pin   8 Pin_8          A7                           J1.8(Pin_8)
   pin   9 Pin_9          A3                           J1.9(Pin_9)
   pin  10 Pin_10         ~{KYBD}                      J1.14(Pin_14)
   pin  11 Pin_11         D0                           J1.11(Pin_11)
   pin  12 Pin_12         D1                           J1.16(Pin_16)
   pin  13 Pin_13         D2                           J1.10(Pin_10)
   pin  14 Pin_14         D3                           J1.13(Pin_13)
   pin  15 Pin_15         D4                           J1.18(Pin_18)
   pin  16 Pin_16         D5                           J1.12(Pin_12)
   pin  17 Pin_17         D6                           J1.15(Pin_15)
   pin  18 Pin_18         D7                           J1.17(Pin_17)
   pin  19 Pin_19         GND                          J1.19(Pin_19)

```
## Nets

```
+5V   (2 pins)
    J1       Tandy Model 1      pin   1  Pin_1
    J2       TEC (Japanese) Model 1 pin   1  Pin_1

/A0   (2 pins)
    J1       Tandy Model 1      pin   5  Pin_5
    J2       TEC (Japanese) Model 1 pin   5  Pin_5

/A1   (2 pins)
    J1       Tandy Model 1      pin   4  Pin_4
    J2       TEC (Japanese) Model 1 pin   4  Pin_4

/A2   (2 pins)
    J1       Tandy Model 1      pin   6  Pin_6
    J2       TEC (Japanese) Model 1 pin   6  Pin_6

/A3   (2 pins)
    J1       Tandy Model 1      pin   9  Pin_9
    J2       TEC (Japanese) Model 1 pin   9  Pin_9

/A4   (2 pins)
    J1       Tandy Model 1      pin   2  Pin_2
    J2       TEC (Japanese) Model 1 pin   2  Pin_2

/A5   (2 pins)
    J1       Tandy Model 1      pin   3  Pin_3
    J2       TEC (Japanese) Model 1 pin   3  Pin_3

/A6   (2 pins)
    J1       Tandy Model 1      pin   7  Pin_7
    J2       TEC (Japanese) Model 1 pin   7  Pin_7

/A7   (2 pins)
    J1       Tandy Model 1      pin   8  Pin_8
    J2       TEC (Japanese) Model 1 pin   8  Pin_8

/D0   (2 pins)
    J1       Tandy Model 1      pin  11  Pin_11
    J2       TEC (Japanese) Model 1 pin  11  Pin_11

/D1   (2 pins)
    J1       Tandy Model 1      pin  16  Pin_16
    J2       TEC (Japanese) Model 1 pin  12  Pin_12

/D2   (2 pins)
    J1       Tandy Model 1      pin  10  Pin_10
    J2       TEC (Japanese) Model 1 pin  13  Pin_13

/D3   (2 pins)
    J1       Tandy Model 1      pin  13  Pin_13
    J2       TEC (Japanese) Model 1 pin  14  Pin_14

/D4   (2 pins)
    J1       Tandy Model 1      pin  18  Pin_18
    J2       TEC (Japanese) Model 1 pin  15  Pin_15

/D5   (2 pins)
    J1       Tandy Model 1      pin  12  Pin_12
    J2       TEC (Japanese) Model 1 pin  16  Pin_16

/D6   (2 pins)
    J1       Tandy Model 1      pin  15  Pin_15
    J2       TEC (Japanese) Model 1 pin  17  Pin_17

/D7   (2 pins)
    J1       Tandy Model 1      pin  17  Pin_17
    J2       TEC (Japanese) Model 1 pin  18  Pin_18

/~{KYBD}   (2 pins)
    J1       Tandy Model 1      pin  14  Pin_14
    J2       TEC (Japanese) Model 1 pin  10  Pin_10

GND   (2 pins)
    J1       Tandy Model 1      pin  19  Pin_19
    J2       TEC (Japanese) Model 1 pin  19  Pin_19

unconnected-(J1-Pin_20-Pad20)   (1 pins)
    J1       Tandy Model 1      pin  20  Pin_20

```
