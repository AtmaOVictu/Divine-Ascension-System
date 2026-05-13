# PROOF_COVERAGE_LEDGER.md

## STATUS

- current proof coverage ledger
- context: Phase G.37 proof cycle closure, 2026-05-08
- source: G.8 + G.10 + G.13 + G.16 proof pass + G.19 Card summary boundary lock + G.22 JSON operator boundary guard + G.25 Markdown/Card operator boundary clarification + G.27 valid JSON roundtrip guard + G.30 fake PROVEN roundtrip clarification + G.32 invalid operator roundtrip guard + G.35 reconciliation patch + G.36 stabilization replay
- proof command: `corepack pnpm proof`
- cycle status: current proof-hardening cycle is closed after G.35 reconciliation and G.36 replay verification

## CONFIRMED INVARIANTS

- blank entry ne more v `PROVEN`
- `PROVEN` brez evidence je blokiran
- `PROVEN` z evidence uspe
- fake `PROVEN` brez evidence se pri Markdown/JSON exportu stabilizira v `UNDER_REVIEW`
- JSON export ohrani `evidence` count `0` pri fake `PROVEN`
- odstranitev zadnjega evidence itema zniža `PROVEN` v `UNDER_REVIEW`
- delna odstranitev evidence pri več evidence itemih ohrani `PROVEN`
- `versionHistory` je append-only pri `recordEntryEvent`
- JSON export ohrani dodani `versionHistory` event po `recordEntryEvent()`
- Markdown export ohrani dodani `versionHistory` event tekst po `recordEntryEvent()`
- invalid internal operator brez mappinga ostane invalid
- JSON export invalidnega `INTERNAL_OPERATOR` ohrani `type: INTERNAL_OPERATOR`
- JSON export invalidnega `INTERNAL_OPERATOR` ohrani prazen `operatorMapping`
- valid JSON export roundtrip through sanitize ohrani en entry in ključna polja
- invalid operator JSON roundtrip preserves invalid boundary
- invalid import fallback se stabilizira v prazno stanje

## RECENT PATCHES

### G.8

- kaj je dodal: JSON assertion za fake `PROVEN` brez evidence
- kateri invariant utrdi: `buildJsonExport()` ne ohrani neveljavnega `PROVEN` in ohrani `evidence` count `0`
- proof result: `PROOF PASS`

### G.10

- kaj je dodal: partial evidence removal assertion za `PROVEN` entry z dvema evidence itemoma
- kateri invariant utrdi: odstranitev enega evidence itema ne sme znižati `PROVEN`, dokler vsaj en evidence item ostane
- proof result: `PROOF PASS`

### G.13

- kaj je dodal: JSON `versionHistory` preservation assertion po `recordEntryEvent()`
- kateri invariant utrdi: `buildJsonExport()` po parsingu ohrani zadnji append-only `versionHistory` event
- proof result: `PROOF PASS`

### G.16

- kaj je dodal: Markdown `versionHistory` recorded-event assertion po `recordEntryEvent()`
- kateri invariant utrdi: `buildMarkdownExport()` ohrani konkretni dodani `versionHistory` event tekst
- proof result: `PROOF PASS`

### G.19

- kaj je dodal: documentation-only Card summary boundary
- kateri boundary utrdi: Card export ni archival/history format; odsotnost `versionHistory` trenutno ni proof bug
- proof result: `N/A (documentation-only)`

### G.22

- kaj je dodal: JSON operator mapping export boundary assertion
- kateri invariant utrdi: JSON export invalidnega `INTERNAL_OPERATOR` ohrani `type` in prazen `operatorMapping`
- proof result: `PROOF PASS`
- scope note: ne odpira Markdown/Card/full parity poti

### G.25

- kaj je dodal: documentation-only Markdown/Card operator mapping boundary clarification
- kateri boundary utrdi: JSON je trenutna dokazna operator-mapping export pot; Markdown/Card ostajata človeško-berljiva oziroma summary exporta brez full parity garancije
- proof result: `N/A (documentation-only)`

### G.27

- kaj je dodal: valid JSON export roundtrip assertion through sanitize
- kateri invariant utrdi: `buildJsonExport(validEntry)` -> `JSON.parse(...)` -> `sanitizeWorkbenchState({ entries: [parsed] })` ohrani en entry, ključna polja in validnost
- proof result: `PROOF PASS`
- scope note: ne odpira fake `PROVEN` roundtripa, invalid operator roundtripa, cross-export parity ali UI/import arhitekture

### G.30

- kaj je dodal: documentation-only fake `PROVEN` roundtrip boundary clarification
- kateri boundary utrdi: fake `PROVEN` export stabilizacija in fake `PROVEN` import downgrade sta že ločeno dokazana; dodatni kompozicijski roundtrip test trenutno ni obvezen contract
- proof result: `N/A (documentation-only)`

### G.32

- kaj je dodal: invalid operator JSON roundtrip assertion through sanitize
- kateri invariant utrdi: `buildJsonExport(invalidOperator)` -> `JSON.parse(...)` -> `sanitizeWorkbenchState({ entries: [parsed] })` ohrani `type: INTERNAL_OPERATOR`, prazen `operatorMapping` in `MISSING_OPERATOR_MAPPING`
- proof result: `PROOF PASS`
- scope note: ne odpira Markdown operator export boundary, Card operator export boundary, full cross-export parity, nove import arhitekture ali UI/runtime sprememb

### G.35

- kaj je dodal: reconciliation patch za manjkajoči invalid operator JSON roundtrip proof blok
- kateri invariant utrdi: G.32 ledger claim je zdaj neposredno podprt v `src/proof/proofCheck.ts`
- proof result: `PROOF PASS`
- scope note: odpravljen je bil G.32 overclaim/mismatch med ledgerjem in proof kodo

### G.36

- kaj je dodal: read-only stabilization replay po G.35
- kateri boundary utrdi: ledger claim za G.32 je preverjeno poravnan z `proofCheck.ts`, proof command pa ostaja zelen
- proof result: `PROOF PASS`
- scope note: read-only verification; brez novega proof patcha

## FORMAT BOUNDARIES

- JSON je trenutno dokazna operator-mapping export pot.
- JSON proof po G.22 dokazuje, da invalidni `INTERNAL_OPERATOR` ohrani `type: INTERNAL_OPERATOR`.
- JSON proof po G.22 dokazuje, da invalidni `INTERNAL_OPERATOR` ohrani prazen `operatorMapping`.
- Markdown za operator mapping ostaja človeško berljiv export z `operatorMapping` vrstico.
- Card za operator mapping ostaja summary export z `OPERATOR MAP` vrstico.
- Markdown/Card placeholderji trenutno niso full parity contract.
- Odsotnost dodatnega Markdown/Card proof assertiona trenutno ni bug.
- Če bo kasneje potrebna formalna parity zahteva, mora biti odprta v ločeni scope fazi.

## ROUNDTRIP BOUNDARIES

- G.27 dokazuje pot `buildJsonExport(validEntry)` -> `JSON.parse(...)` -> `sanitizeWorkbenchState({ entries: [parsed] })`.
- G.27 dokazuje, da po roundtripu ostane prisoten en entry.
- G.27 dokazuje, da roundtrip ne pade v prazen fallback.
- G.27 dokazuje, da se ohranijo ključna polja, najmanj `term`, `proofStatus` in evidence count.
- G.27 dokazuje, da roundtrip entry ostane veljaven po `validateEntry(...)`.
- G.27 ne odpira fake `PROVEN` roundtripa.
- G.27 ne odpira invalid operator roundtripa.
- G.27 ne odpira cross-export parity.
- G.27 ne odpira UI/import arhitekture.
- fake `PROVEN` export stabilizacija je že ločeno dokazana.
- fake `PROVEN` import/sanitize downgrade je že ločeno dokazan.
- `evidence.length === 0` pri fake `PROVEN` JSON exportu je že dokazano.
- dodatni kompozicijski fake `PROVEN` roundtrip test trenutno ni obvezen contract.
- razlog: dokazna vrednost bi bila predvsem podvajanje že potrjenih dveh polovic.
- G.32 dokazuje pot `buildJsonExport(invalidOperator)` -> `JSON.parse(...)` -> `sanitizeWorkbenchState({ entries: [parsed] })`.
- G.32 dokazuje, da roundtrip ohrani `type: INTERNAL_OPERATOR`.
- G.32 dokazuje, da roundtrip ohrani prazen `operatorMapping`.
- G.32 dokazuje, da `validateEntry(roundtripped)` še vedno vrne `MISSING_OPERATOR_MAPPING`.
- G.32 ne odpira Markdown operator export boundary.
- G.32 ne odpira Card operator export boundary.
- G.32 ne odpira full cross-export parity.
- G.32 ne odpira nove import arhitekture.
- G.32 ne odpira UI/runtime sprememb.
- G.35 je zaprl prej odkrit mismatch: ledger je trdil G.32 roundtrip dokaz, proof koda pa ga je pred reconciliation patchom še manjkala.
- G.36 je read-only potrdil, da G.32/G.35 roundtrip blok obstaja in da ledger po reconciliation ne trdi več, kot `proofCheck.ts` dejansko dokazuje.

## OPEN INVARIANTS

- cross-export parity (`DEFERRED`; ne odpira se kot active next patch v trenutnem ciklu)

## NEXT CANDIDATE

- priporočilo: `runtime/UI boundary review`
- razlog: proof-hardening cikel je po G.35/G.36 dokumentacijsko in dokazno zaprt; naslednji varen korak je read-only pregled aktivne runtime/UI meje zunaj proof patch plasti
- status: en sam naslednji kandidat po closure fazi; cross-export parity ostaja deferred

## DO-NOT-TOUCH

- `src/*`
- `package.json`
- `graphify-out/*`
- legacy views
- `src/domain/*`
- `src/store/*`
