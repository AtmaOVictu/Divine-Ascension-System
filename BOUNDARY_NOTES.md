# PHASE 3D Boundary Notes

## Current Contract

- `CounterAngle.severity` je TypeScript contract: `"nizka" | "srednja" | "visoka"`.
- `sanitizeState()` trenutno ostaja tolerant runtime filter za `severity`.
- Invalid `severity` runtime policy je `DEFER`.
- `STRICT_DROP_INVALID` ni odobren.
- `STRICT_NORMALIZE_INVALID` ni odobren.

## Proof Boundaries

- `proofCheck.ts` loči:
  - valid partial roundtrip
  - orphan sanitizer behavior
- `links` partial roundtrip mora vključiti oba endpoint `truthUnit`-a.
- `simulationCases` partial roundtrip mora vključiti vse `involvedUnitIds`.

## Fixture Boundaries

- `sampleData.ts` loči:
  - contract/base factory
  - sacred fixture/demo exercise
  - internal evidence trace
  - proposed links
  - fixture confidence
  - simulation flow
- `createEmptyState()` je canonical empty `StudioState` factory.
- `createSampleState()` je demo/regression fixture factory.
- Contract shape izhaja iz tipov, ne iz sample seeda.
- `evidenceRefs` v `sampleData.ts` so notranje demo reference, ne zunanje verificirani viri.
- `proposedLinks` so človeški predlogi, ne canonical graph edges.
- `confidence` v `sampleData.ts` je fixture signal, ne production trust score.
- `simulationCases` opisujejo demo procesni tok in ne izvršijo kanonizacije.
- Fixture je real internal trace, vendar ni automatic canonization.
- Kanon nastane šele z eksplicitnim uporabniškim soglasjem.

## Proof Record

- External PowerShell proof:
  - `.\node_modules\.bin\tsx.cmd src\proof\proofCheck.ts`
  - `PROOF PASS`
- Codex sandbox `EPERM` pri `node_modules\.pnpm` je environment hold, ne code fail.

## Do Not Change

- Ne zaostruj `sanitizeState()` severity politike brez ločene `3D.5` odobritve.
- Ne vračaj `proofCheck` partial roundtrip na neveljavne referenčne inpute.
- Ne spreminjaj `sampleData` seedov pod pretvezo komentarjev.
- Ne obravnavaj fixture kot ničvreden demo; fixture je sveta vaja sistema, a ne avtomatski kanon.
