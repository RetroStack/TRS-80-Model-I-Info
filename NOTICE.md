# Third-party material

The documents and the verification harness in this repository are original work, MIT licensed
in [LICENSE](LICENSE). What they are *about* is not, and none of it is redistributed here.

## Not included, and needed to run the checks

**RetroStack's KiCad board reconstructions.** Eleven boards, redrawn from physical hardware.
`TRS80_SCHEMATICS` points the harness at a directory holding them. They are published as their
own repositories and carry their own terms; this repository ships none of their files, only
generated netlists in [`netlists/`](netlists/README.md) and readings of the drawings.

**ROM images.** `TRS80_ROMS` points at a directory of them. The Level I and Level II system
ROMs are Radio Shack / Tandy firmware and are **not** in this repository. The six character
generator images are likewise not included. Eight claims read them; without the directory those
claims skip and the run still passes.

## Quoted, not reproduced

**Radio Shack manuals.** The *TRS-80 Technical Manual* (1978) and the *Expansion Interface
Service Manual* are quoted in short passages with page citations, for identification and
commentary. Neither is reproduced here in whole or in substantial part.

**Hand-drawn Percom Doubler schematics.** Described and cited; the scans themselves are not
included. The two boards are credited to F. J. Kraan (1986) and A. Colson (1982) as their
drawings state.

**The Model I RS-232 rebuild** is Roger Murley / BYTESHiFT's design, read and described here,
not reproduced.

## Trademarks

TRS-80, Radio Shack and Tandy are trademarks of their respective owners. This is an independent
reference work with no affiliation to, or endorsement by, any of them.
