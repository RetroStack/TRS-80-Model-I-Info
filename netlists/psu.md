# Power supply — complete netlist

Generated from `TRS-80-Model-I-Power-Supply-main` by `verify/emit.py`, which exports the schematic with `kicad-cli` and parses it with the same code the claims in `verify/claims.py` use.

**10 components · 11 nets · 32 pin connections.**

Three views of the same information: components, a connection view answering "what is this pin wired to", and a net index answering "what is on this net". The redundancy is deliberate — it is what lets the file be checked against itself.

No integrity problems: every node names a known component, every pin number is valid for that component's symbol, and the two views agree on the connection count.

## Components

| ref | value | sheet |
|---|---|---|
| `D1` | 1N4001 |  |
| `D2` | 1N4001 |  |
| `F1` | ~ |  |
| `J1` | Conn_01x02 |  |
| `J2` | Conn_01x04 |  |
| `J3` | Conn_01x06 |  |
| `LA1` | Lamp |  |
| `SW1` | SW_SPST |  |
| `SW2` | SW_SPST |  |
| `T1` | Transformer_1P_2SCT |  |

## Connections

For each pin: its name, its net, and what else is on that net. Nets with more than 12 pins (power, ground, buses) are named rather than expanded.

```
D1  (1N4001, )
   pin   1 K              Net-(D1-K)                   D2.1(K) J2.1(Pin_1)
   pin   2 A              A1                           J3.1(Pin_1) T1.3(SA1)

D2  (1N4001, )
   pin   1 K              Net-(D1-K)                   D1.1(K) J2.1(Pin_1)
   pin   2 A              B3                           J3.6(Pin_6) T1.8(SB3)

F1  (~, )
   pin   1 A              Net-(F1-A)                   J1.2(Pin_2)
   pin   2 B              Net-(F1-B)                   SW1.1(A)

J1  (Conn_01x02, )
   pin   1 Pin_1          Net-(J1-Pin_1)               SW2.1(A)
   pin   2 Pin_2          Net-(F1-A)                   F1.1(A)

J2  (Conn_01x04, )
   pin   1 Pin_1          Net-(D1-K)                   D1.1(K) D2.1(K)
   pin   2 Pin_2          A3                           J3.3(Pin_3) J3.4(Pin_4) T1.5(SA3) T1.6(SB1)
   pin   3 Pin_3          A2                           J3.2(Pin_2) T1.4(SA2)
   pin   4 Pin_4          B2                           J3.5(Pin_5) T1.7(SB2)

J3  (Conn_01x06, )
   pin   1 Pin_1          A1                           D1.2(A) T1.3(SA1)
   pin   2 Pin_2          A2                           J2.3(Pin_3) T1.4(SA2)
   pin   3 Pin_3          A3                           J2.2(Pin_2) J3.4(Pin_4) T1.5(SA3) T1.6(SB1)
   pin   4 Pin_4          A3                           J2.2(Pin_2) J3.3(Pin_3) T1.5(SA3) T1.6(SB1)
   pin   5 Pin_5          B2                           J2.4(Pin_4) T1.7(SB2)
   pin   6 Pin_6          B3                           D2.2(A) T1.8(SB3)

LA1  (Lamp, )
   pin   1 -              Net-(LA1--)                  SW2.2(B) T1.2(PB)
   pin   2 +              Net-(LA1-+)                  SW1.2(B) T1.1(PA)

SW1  (SW_SPST, )
   pin   1 A              Net-(F1-B)                   F1.2(B)
   pin   2 B              Net-(LA1-+)                  LA1.2(+) T1.1(PA)

SW2  (SW_SPST, )
   pin   1 A              Net-(J1-Pin_1)               J1.1(Pin_1)
   pin   2 B              Net-(LA1--)                  LA1.1(-) T1.2(PB)

T1  (Transformer_1P_2SCT, )
   pin   1 PA             Net-(LA1-+)                  LA1.2(+) SW1.2(B)
   pin   2 PB             Net-(LA1--)                  LA1.1(-) SW2.2(B)
   pin   3 SA1            A1                           D1.2(A) J3.1(Pin_1)
   pin   4 SA2            A2                           J2.3(Pin_3) J3.2(Pin_2)
   pin   5 SA3            A3                           J2.2(Pin_2) J3.3(Pin_3) J3.4(Pin_4) T1.6(SB1)
   pin   6 SB1            A3                           J2.2(Pin_2) J3.3(Pin_3) J3.4(Pin_4) T1.5(SA3)
   pin   7 SB2            B2                           J2.4(Pin_4) J3.5(Pin_5)
   pin   8 SB3            B3                           D2.2(A) J3.6(Pin_6)

```
## Nets

```
/A1   (3 pins)
    D1       1N4001             pin   2  A
    J3       Conn_01x06         pin   1  Pin_1
    T1       Transformer_1P_2SCT pin   3  SA1

/A2   (3 pins)
    J2       Conn_01x04         pin   3  Pin_3
    J3       Conn_01x06         pin   2  Pin_2
    T1       Transformer_1P_2SCT pin   4  SA2

/A3   (5 pins)
    J2       Conn_01x04         pin   2  Pin_2
    J3       Conn_01x06         pin   3  Pin_3
    J3       Conn_01x06         pin   4  Pin_4
    T1       Transformer_1P_2SCT pin   5  SA3
    T1       Transformer_1P_2SCT pin   6  SB1

/B2   (3 pins)
    J2       Conn_01x04         pin   4  Pin_4
    J3       Conn_01x06         pin   5  Pin_5
    T1       Transformer_1P_2SCT pin   7  SB2

/B3   (3 pins)
    D2       1N4001             pin   2  A
    J3       Conn_01x06         pin   6  Pin_6
    T1       Transformer_1P_2SCT pin   8  SB3

Net-(D1-K)   (3 pins)
    D1       1N4001             pin   1  K
    D2       1N4001             pin   1  K
    J2       Conn_01x04         pin   1  Pin_1

Net-(F1-A)   (2 pins)
    F1       ~                  pin   1  A
    J1       Conn_01x02         pin   2  Pin_2

Net-(F1-B)   (2 pins)
    F1       ~                  pin   2  B
    SW1      SW_SPST            pin   1  A

Net-(J1-Pin_1)   (2 pins)
    J1       Conn_01x02         pin   1  Pin_1
    SW2      SW_SPST            pin   1  A

Net-(LA1-+)   (3 pins)
    LA1      Lamp               pin   2  +
    SW1      SW_SPST            pin   2  B
    T1       Transformer_1P_2SCT pin   1  PA

Net-(LA1--)   (3 pins)
    LA1      Lamp               pin   1  -
    SW2      SW_SPST            pin   2  B
    T1       Transformer_1P_2SCT pin   2  PB

```
