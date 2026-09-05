# XRX III — complete netlist

Generated from `TRS-80-Model-I-XRX-III-main` by `verify/emit.py`, which exports the schematic with `kicad-cli` and parses it with the same code the claims in `verify/claims.py` use.

**11 components · 22 nets · 42 pin connections.**

Three views of the same information: components, a connection view answering "what is this pin wired to", and a net index answering "what is on this net". The redundancy is deliberate — it is what lets the file be checked against itself.

No integrity problems: every node names a known component, every pin number is valid for that component's symbol, and the two views agree on the connection count.

## Components

| ref | value | sheet |
|---|---|---|
| `CR1` | 1N4148 |  |
| `CR2` | 1N4148 |  |
| `J1` | YEL |  |
| `J2` | RED |  |
| `J3` | GRN |  |
| `J4` | VIO |  |
| `J5` | BLU |  |
| `J6` | BLK |  |
| `R1` | 10k |  |
| `Z1` | 4001 |  |
| `Z2` | 4040 |  |

## Connections

For each pin: its name, its net, and what else is on that net. Nets with more than 12 pins (power, ground, buses) are named rather than expanded.

```
CR1  (1N4148, )
   pin   1 K              Net-(CR1-K)                  Z2.14(Q9)
   pin   2 A              Net-(CR1-A)                  CR2.2(A) R1.2 Z1.13

CR2  (1N4148, )
   pin   1 K              Net-(CR2-K)                  Z2.13(Q7)
   pin   2 A              Net-(CR1-A)                  CR1.2(A) R1.2 Z1.13

J1  (YEL, )
   pin   1 Pin_1          Net-(J1-Pin_1)               Z2.10(CLK)

J2  (RED, )
   pin   1 Pin_1          +5V                          R1.1 Z1.14(VDD) Z2.16(VDD)

J3  (GRN, )
   pin   1 Pin_1          Net-(J3-Pin_1)               Z1.1

J4  (VIO, )
   pin   1 Pin_1          Net-(J4-Pin_1)               Z1.4

J5  (BLU, )
   pin   1 Pin_1          Net-(J5-Pin_1)               Z1.8

J6  (BLK, )
   pin   1 Pin_1          GND                          Z1.7(VSS) Z2.8(VSS)

R1  (10k, )
   pin   1                +5V                          J2.1(Pin_1) Z1.14(VDD) Z2.16(VDD)
   pin   2                Net-(CR1-A)                  CR1.2(A) CR2.2(A) Z1.13

Z1  (4001, )
   pin   1                Net-(J3-Pin_1)               J3.1(Pin_1)
   pin   2                Net-(Z1-Pad11)               Z1.11 Z1.9
   pin   3                Net-(Z1-Pad3)                Z1.5 Z1.6
   pin   4                Net-(J4-Pin_1)               J4.1(Pin_1)
   pin   5                Net-(Z1-Pad3)                Z1.3 Z1.6
   pin   6                Net-(Z1-Pad3)                Z1.3 Z1.5
   pin   7 VSS            GND                          J6.1(Pin_1) Z2.8(VSS)
   pin   8                Net-(J5-Pin_1)               J5.1(Pin_1)
   pin   9                Net-(Z1-Pad11)               Z1.11 Z1.2
   pin  10                Net-(Z2-Reset)               Z1.12 Z2.11(Reset)
   pin  11                Net-(Z1-Pad11)               Z1.2 Z1.9
   pin  12                Net-(Z2-Reset)               Z1.10 Z2.11(Reset)
   pin  13                Net-(CR1-A)                  CR1.2(A) CR2.2(A) R1.2
   pin  14 VDD            +5V                          J2.1(Pin_1) R1.1 Z2.16(VDD)

Z2  (4040, )
   pin   1 Q11            unconnected-(Z2-Q11-Pad1)    (no other connection)
   pin   2 Q5             unconnected-(Z2-Q5-Pad2)     (no other connection)
   pin   3 Q4             unconnected-(Z2-Q4-Pad3)     (no other connection)
   pin   4 Q6             unconnected-(Z2-Q6-Pad4)     (no other connection)
   pin   5 Q3             unconnected-(Z2-Q3-Pad5)     (no other connection)
   pin   6 Q2             unconnected-(Z2-Q2-Pad6)     (no other connection)
   pin   7 Q1             unconnected-(Z2-Q1-Pad7)     (no other connection)
   pin   8 VSS            GND                          J6.1(Pin_1) Z1.7(VSS)
   pin   9 Q0             unconnected-(Z2-Q0-Pad9)     (no other connection)
   pin  10 CLK            Net-(J1-Pin_1)               J1.1(Pin_1)
   pin  11 Reset          Net-(Z2-Reset)               Z1.10 Z1.12
   pin  12 Q8             unconnected-(Z2-Q8-Pad12)    (no other connection)
   pin  13 Q7             Net-(CR2-K)                  CR2.1(K)
   pin  14 Q9             Net-(CR1-K)                  CR1.1(K)
   pin  15 Q10            unconnected-(Z2-Q10-Pad15)   (no other connection)
   pin  16 VDD            +5V                          J2.1(Pin_1) R1.1 Z1.14(VDD)

```
## Nets

```
+5V   (4 pins)
    J2       RED                pin   1  Pin_1
    R1       10k                pin   1  
    Z1       4001               pin  14  VDD
    Z2       4040               pin  16  VDD

GND   (3 pins)
    J6       BLK                pin   1  Pin_1
    Z1       4001               pin   7  VSS
    Z2       4040               pin   8  VSS

Net-(CR1-A)   (4 pins)
    CR1      1N4148             pin   2  A
    CR2      1N4148             pin   2  A
    R1       10k                pin   2  
    Z1       4001               pin  13  

Net-(CR1-K)   (2 pins)
    CR1      1N4148             pin   1  K
    Z2       4040               pin  14  Q9

Net-(CR2-K)   (2 pins)
    CR2      1N4148             pin   1  K
    Z2       4040               pin  13  Q7

Net-(J1-Pin_1)   (2 pins)
    J1       YEL                pin   1  Pin_1
    Z2       4040               pin  10  CLK

Net-(J3-Pin_1)   (2 pins)
    J3       GRN                pin   1  Pin_1
    Z1       4001               pin   1  

Net-(J4-Pin_1)   (2 pins)
    J4       VIO                pin   1  Pin_1
    Z1       4001               pin   4  

Net-(J5-Pin_1)   (2 pins)
    J5       BLU                pin   1  Pin_1
    Z1       4001               pin   8  

Net-(Z1-Pad11)   (3 pins)
    Z1       4001               pin   2  
    Z1       4001               pin   9  
    Z1       4001               pin  11  

Net-(Z1-Pad3)   (3 pins)
    Z1       4001               pin   3  
    Z1       4001               pin   5  
    Z1       4001               pin   6  

Net-(Z2-Reset)   (3 pins)
    Z1       4001               pin  10  
    Z1       4001               pin  12  
    Z2       4040               pin  11  Reset

unconnected-(Z2-Q0-Pad9)   (1 pins)
    Z2       4040               pin   9  Q0

unconnected-(Z2-Q1-Pad7)   (1 pins)
    Z2       4040               pin   7  Q1

unconnected-(Z2-Q10-Pad15)   (1 pins)
    Z2       4040               pin  15  Q10

unconnected-(Z2-Q11-Pad1)   (1 pins)
    Z2       4040               pin   1  Q11

unconnected-(Z2-Q2-Pad6)   (1 pins)
    Z2       4040               pin   6  Q2

unconnected-(Z2-Q3-Pad5)   (1 pins)
    Z2       4040               pin   5  Q3

unconnected-(Z2-Q4-Pad3)   (1 pins)
    Z2       4040               pin   3  Q4

unconnected-(Z2-Q5-Pad2)   (1 pins)
    Z2       4040               pin   2  Q5

unconnected-(Z2-Q6-Pad4)   (1 pins)
    Z2       4040               pin   4  Q6

unconnected-(Z2-Q8-Pad12)   (1 pins)
    Z2       4040               pin  12  Q8

```
