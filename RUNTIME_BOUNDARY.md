# RUNTIME_BOUNDARY.md

## STATUS

- current boundary lock
- context: Phase G.6 documentation lock, 2026-05-08
- source: G.4 read-only audit + Graphify output as map, not absolute truth

## CURRENT RUNTIME SURFACE

### `src/main.tsx`

- vloga: React runtime entrypoint in bootstrap datoteka
- dokaz: datoteka uvozi `App` iz `./App`, pridobi `#root` in renderira `<App />`; boundary docs jo navajajo kot current runtime entrypoint
- patch status: `HOLD`
- utemeljitev: majhna bootstrap datoteka z visoko občutljivostjo; ni primeren prvi patch target brez eksplicitne potrebe

### `src/App.tsx`

- vloga: glavni runtime UI shell in local state loop za Phase 1 workbench
- dokaz: datoteka uvaža Phase 1 runtime API iz `./jewik-core`, definira `loadState()` / `saveState()`, `App()` komponento ter evidence/proof/export handlere
- patch status: `PATCHABLE`
- utemeljitev: potrjena runtime datoteka, neposredno povezana z aktivnim UI tokom in brez potrjene odvisnosti od legacy view plasti

### `src/jewik-core/index.ts`

- vloga: Phase 1 core model, sanitizer, proof guardrails in export builderji
- dokaz: datoteka definira `LexiconEntry`, `WorkbenchState`, `createInitialWorkbenchState()`, `sanitizeWorkbenchState()`, `validateEntry()`, `setProofStatus()`, `buildMarkdownExport()` in `buildJsonExport()`
- patch status: `PATCHABLE`
- utemeljitev: potrjen truth/proof core za current runtime surface; spremembe so možne samo z ozko dokazano nalogo

### `src/proof/proofCheck.ts`

- vloga: proof/check plast za Phase 1 invariants
- dokaz: datoteka uvaža samo iz `../jewik-core`, izvaja proof scenarije in izpiše `PROOF PASS`
- patch status: `PATCHABLE`
- utemeljitev: izolirana proof datoteka, primerna za prihodnje ozko proof hardening spremembe, ne pa v tej fazi

## PROOF SURFACE

- current proof/check logic is in `src/proof/proofCheck.ts`
- proof surface reads and validates Phase 1 behavior through `src/jewik-core/index.ts`
- ta faza ne predlaga nobene spremembe proof kode

## BOUNDARY DOCUMENTS

### `PHASE_1_CONTRACT.md`

- vloga: contract dokument za Phase 1 entry loop, dictionary layer in proof guardraile
- status: dokazni dokument

### `LEGACY_LAYER_AUDIT.md`

- vloga: izrecno loči current runtime surface od legacy `views/domain/store` plasti
- status: dokazni dokument

### `BOUNDARY_NOTES.md`

- vloga: ožji boundary lock za proof in fixture pravila okoli `sampleData.ts` in `sanitizeState()`
- status: dokazni dokument

### `PHASE_1_BROWSER_SMOKE.md`

- vloga: runtime smoke evidence za current active surface
- status: dokazni dokument

### `README.md`

- vloga: splošna orientacija projekta in operativna navodila; vsebuje tudi runtime/boundary reference
- status: orientacija, ne samostojen dokaz

## LEGACY SURFACE

- `src/views/*`
  - legacy presentation layer
  - ne patcha se v tej fazi
- `src/domain/*`
  - legacy domain plast
  - posebej `src/domain/sampleData.ts` ostaja boundary risk in fixture/reference surface
- `src/store/*`
  - legacy storage/import plast
  - posebej `src/store/localStore.ts` ostaja boundary risk in import/sanitize reference surface
- legacy datoteke so dovoljene kot referenca za audit, ne pa kot patch target v tej fazi

## GRAPHIFY CONFIDENCE RULE

- `EXTRACTED` edge = kandidat za dokaz, vendar ga je treba potrditi z vsebino datoteke
- `INFERRED` edge = karantena, signal za ročno preverbo, ne kanon
- Graphify output = zemljevid za orientacijo, ne dokaz sam po sebi

## DO-NOT-TOUCH IN THIS PHASE

- `src/*`
- `package.json`
- `graphify-out/*`
- legacy views
- `src/domain/*`
- `src/store/*`
- store/domain refaktor

## NEXT SAFE REVIEW

- zgodovinska opomba: začetno priporočilo `A) proof hardening` je bilo izčrpano skozi faze G.8-G.35
- priporočilo: `runtime/UI boundary review`
- razlog: proof-hardening cikel je trenutno zaključen, runtime/proof/legacy meja pa ostaja uporabna osnova za naslednji read-only pregled brez odpiranja legacy ali širše parity plasti
