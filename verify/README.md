# Checking the claims

Every factual claim in `docs/` that can be tested has an executable assertion here, and
the assertions run.

```sh
TRS80_SCHEMATICS=~/schematics TRS80_ROMS=~/roms python3 verify/run.py --self-test
```

Neither directory is in this repository, because neither is ours: the KiCad sources are
RetroStack's and the ROM images are Tandy's. Every claim needing one skips cleanly when its
variable is unset and the run still passes — it just checks less, and says so. The
netlist-backed claims are the exception that needs neither: `kicad-cli`'s own exports are
committed under `netlists/exports/`, so 63 of the 79 run on a fresh clone with nothing set.

## The rule this folder runs on

> **A claim of the form "X is the only Y" must enumerate every Y and assert the complement is
> empty. A comparison that cannot produce the complement cannot support the claim.**

A query whose output is read and believed is not verification, and the failure is usually
invisible: comparing each component's KiCad `Value` field looks like a complete comparison, but
it is structurally blind to `Z3` and `Z71`, which have no value at all.

The largest application of the rule is `us-revision-differences-are-complete`, which holds all
71 nets that differ between the US boards and requires the set to match exactly. That is what
turns "here are the differences we found" into "here are the differences": two of the nine
differences this folder lists are visible only once every net is compared mechanically.

## What is here

| file | what |
|---|---|
| `netlist.py` | the KiCad netlist parser — the single parsing path for everything |
| `claims.py` | one assertion per documented claim, each carrying the sentence it defends |
| `run.py` | runs them, prints a report, exits non-zero on any failure |
| `emit.py` | regenerates `netlists/*.md` using the same parser |
| `mutate.py` | corrupts the data one claim at a time and requires that claim to fail |

`emit.py` sharing `netlist.py` with `claims.py` is deliberate: the published tables and the
assertions cannot disagree about what the netlist says, because they read it the same way.

## How the parser is trusted

Everything rests on `netlist.py`, so it is checked rather than assumed. `run.py --self-test`
re-exports every board as **KiCad XML** — a different format, produced by a different code path
inside `kicad-cli` — and asserts three things agree:

- the component set and every value,
- the node set, every `(reference, pin)`,
- the **partition of pins into nets**, with net names discarded.

That last one is the important one. It answers "are these two wired the same" without being
fooled by a rename, which no comparison of net names can do.

All eleven boards pass: 1,690 components and 10,978 pin connections agreeing across two
independent parses. Those three numbers are themselves asserted, by
`self-test-totals-are-not-stale`, because a count in prose is exactly the thing that goes stale
without anyone noticing.

Two subtleties in the parser are covered by regression claims, because both are silent when
wrong: KiCad escapes `/` as `{slash}` inside a net name, and the hierarchy split must happen
*before* unescaping — otherwise `~{CLK{slash}2}` becomes `~{CLK/2}` and then splits to `2}`.

## The assertions are not vacuous

An assertion that cannot fail is worse than none: it looks like verification and provides none.
So the harness is mutation-tested, and the mutations are a committed script rather than
something done once by hand:

```sh
TRS80_SCHEMATICS=~/schematics TRS80_ROMS=~/roms python3 verify/mutate.py
```

Most mutations corrupt the parsed data in memory. Six write into the repository — a committed
netlist export, three documents, and two probe files that exist only while the claim reading
them runs — and one edits a KiCad source sheet, the only way to prove that
`enable-pins-are-clear-of-the-data-rows` really watches the drawing rather than a copy of it.
All seven restore from the original bytes, and the run then re-reads every one of them and
reports whether anything was left behind.

Each mutation corrupts the data in exactly the way one claim denies, and that claim is
then required to fail. **Sixty-seven mutations, sixty-seven caught.** A mutation the claim
survives is printed as `SURVIVED`, and that is a defect in the claim.

**49 of the 79 claims carry a mutation.** That figure is stated rather than floored, and
`harness-counts-are-not-stale` holds it to what `mutate.py` actually defines — a floor cannot
tell a claim that lost its mutation from one that never had one, and a number nothing compares
against is the trap this whole file exists to describe.

A mutation is only worth as much as its reach. `nets` is the authoritative structure and
`_pin2net`/`_pin2short` are derived from it, so a mutation that writes only the derived maps is
not a mutation at all — every claim using `pins_on` or `partition` reads straight past it. The
helpers here rewrite `nets` and rebuild the rest.

The mutations also decide how much a claim is really worth. A claim that checks the *set*
`A0`–`A7` appears somewhere on two packages passes a board with two rows swapped; a claim that
checks the DAC resistor values on one board passes a change to another. Both are the difference
between a passing assertion and a defended sentence, and both are only visible when something
tries to break them.

## Evidence classes

Only some claims can be mechanised. The rest say so rather than borrowing the confidence of the
ones that can:

| class | meaning | how it is checked |
|---|---|---|
| `NET` | connectivity | assertion against the exported netlists |
| `BOM` | a part's identity | assertion against the bill of materials |
| `ROM` | a byte in a ROM image | assertion against the images `TRS80_ROMS` points at |
| `RUN` | machine behaviour | running the emulator; `run.py` cannot do this, so the document carries the steps to reproduce it |
| `DOC` | a period document says it | quoted with a page number; not mechanisable |
| `DERIVED` | arithmetic over the above | assertion recomputing it |
| `UNRESOLVED` | sources conflict | carries the conflict table; never stated as fact |

## Claims about the documents themselves

Five assertions police the prose rather than the hardware, and all of them belong to this file:

- `claims-and-docs-do-not-drift`
- `documents-invent-no-designators`
- `documents-have-no-dangling-links`
- `harness-counts-are-not-stale`
- `self-test-totals-are-not-stale`

The second sweeps every netlist-backed document for `Z`/`R`/`C`/`CR`/`SW`/`J`/`CN`/`K`/`TP`/`RP`
references and requires each to name a real part on a board that document is about. It exists
because a reference to a part that does not exist reads exactly like a correct one. Documents
about boards with no KiCad source — the RS-232 card, the Percom Doubler — are
out of its scope and say so in the assertion, rather than being silently exempt.

It checks the *union* of a document's boards, which is weaker than it first reads: `keyboard.md`
is about the keyboard and the main boards, so a reference is accepted if any one of them has it.
Deleting the keyboard's `R2` does not fail the claim, because the main boards have an `R2` too.
It catches a designator that exists nowhere, not one attributed to the wrong board.

`documents-have-no-dangling-links` requires every relative link to resolve. A document still to
be written is named in prose and marked `*(planned)*` rather than linked, so the folder has no
dead link at any commit and the check catches a planned document that lands under a different
name. Nothing is outstanding at present.

Both are mutation-tested by writing into the repository — a probe file with a link to nothing, and a
stray `Z999` appended to `revisions.md` — and `restore()` puts the repository back from the original
bytes.

## Verified, not yet documented

A claim may declare no document. That means the fact is verified and the assertion runs, but no
prose has been written for it yet — the remaining documents are still being written. The drift
check requires every such claim to appear in this list, so nothing verified can be quietly
forgotten.

The list is empty: every claim currently declares a document.

## Adding a claim

Write the sentence in the document, then the assertion here with the same sentence as its text.
If you cannot write the assertion, the sentence is a `DOC` or `UNRESOLVED` claim and must be
marked as one in place.
