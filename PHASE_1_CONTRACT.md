# PHASE 1 CONTRACT

## Namen Phase 1

Phase 1 dokaze en sam operativen loop:

`entry -> dictionary layer -> JEWIK cut -> evidence -> proof status -> export`

To ni popoln desktop truthbase. To je minimalni preverljiv contract za lokalni workbench.

## Kaj je LexiconEntry

`LexiconEntry` je osnovna Phase 1 enota. Vsebuje:

- `term`
- `type`
- `dictionaryLayer`
- `segmentation`
- `phoneticNotes`
- `operatorMapping`
- `antinomies`
- `jewikCut`
- `evidence`
- `proofStatus`
- `proofNotes`
- `versionHistory`
- `exportText`

Phase 1 ne meša več različnih truth-unit struktur. Dela z eno stabilno entry pogodbo.

## Kaj pomeni dictionary layer

`dictionaryLayer.kind` je ekspliciten status pomena in mora biti eden od:

- `OFFICIAL`
- `COMMUNITY`
- `DERIVED`
- `UNAVAILABLE`

Dictionary layer ne dokazuje resnice sam po sebi. Pove, iz katere vrste pomena trenutno bere entry.

## Kaj pomeni JEWIK cut

`jewikCut.expression` je delovni simbolni rez ali operatorni zapis, s katerim je entry strukturiran.

Phase 1 ga obravnava kot ločen sloj od:

- slovarskega pomena
- evidence
- proof statusa

## Kaj šteje kot evidence

Evidence v Phase 1 pomeni vsaj en neprazen `EvidenceItem.text`.

`source` je dovoljen kot dodatna sled, vendar prazno evidence besedilo ne šteje.

To pomeni:

- prazna evidence vrstica ni veljavna
- `PROVEN` brez vsaj enega veljavnega evidence itema ni dovoljen

## Kdaj je status PROVEN dovoljen

`PROVEN` je dovoljen samo, če entry vsebuje vsaj en veljaven evidence item.

Guardrails:

- `setProofStatus()` blokira direkten prehod v `PROVEN` brez evidence
- remove-evidence pot samodejno zruši neveljaven `PROVEN` nazaj v `UNDER_REVIEW`
- sanitizer in export guardrail ne dovolita, da bi neveljaven `PROVEN` ostal skrit v stanju ali izvozu

## Kaj export dokazuje in česa ne

Export v Phase 1 dokazuje:

- trenutni `proofStatus`
- trenutni `dictionaryLayer.kind`
- trenutni `evidenceCount`
- trenutno delovno vsebino entryja

Export ne dokazuje:

- zunanje verifikacije vira
- trajnega ledgerja
- kanona
- dokazne neizpodbitnosti

## Znane omejitve

- `localStorage` ni trajni proof ledger
- browser visual check še ni potrjen
- `jewik-core` še ni samostojen package
- version history v tej fazi beleži materialne contract dogodke, ne vsakega posameznega keystroke edit-a

