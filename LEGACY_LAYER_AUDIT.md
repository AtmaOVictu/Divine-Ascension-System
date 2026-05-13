# LEGACY LAYER AUDIT

## Current Active Runtime Surface

Current runtime entrypoint is:

- `src/main.tsx`

Current runtime app shell is:

- `src/App.tsx`

Current runtime domain contract is:

- `src/jewik-core/index.ts`

Current runtime state loop is:

- local `loadState()`
- local `saveState()`
- `WorkbenchState`
- `LexiconEntry`
- `jewik-core` validation, proof, and export helpers

Current runtime does **not** import:

- `src/views/*`
- `src/domain/*`
- `src/store/*`

## Current Proof Surface

Current proof contract file is:

- `src/proof/proofCheck.ts`

It imports only Phase 1 core functions from:

- `src/jewik-core/index.ts`

It does not import:

- `src/views/*`
- `src/domain/*`
- `src/store/*`

## Legacy Folders Status

### `src/views/*`

Legacy presentation layer from the previous multi-view studio.

Observed role:

- `LibraryView`
- `TruthUnitsView`
- `ConsentView`
- `OntographView`
- `SimulationLabView`
- `ExportImportView`

These files model the old runtime shell built around:

- documents
- truth units
- consent
- ontograph
- simulation
- JSON import/export

They are not imported by current `src/App.tsx`.

### `src/domain/*`

Legacy domain schema for the previous studio.

Observed role:

- `types.ts` defines `StudioState`, `TruthUnit`, `TruthType`, `TruthStatus`, `RelationType`, `SimulationCase`
- `sampleData.ts` seeds the old multi-view studio with document/truth-unit demo content

These files are not imported by current `src/App.tsx` or current proof surface.

### `src/store/*`

Legacy storage and import-provenance adapter for the previous studio.

Observed role:

- `localStore.ts` owns `StudioState` sanitize/read/write/import-metadata behavior

This file is not imported by current `src/App.tsx` or current proof surface.

## Import Graph Summary

### Active runtime chain

- `src/main.tsx` -> `src/App.tsx`
- `src/App.tsx` -> `src/jewik-core/index.ts`
- `src/proof/proofCheck.ts` -> `src/jewik-core/index.ts`

### Legacy chain

- `src/views/*` -> `src/domain/types.ts`
- `src/views/ExportImportView.tsx` -> `src/store/localStore.ts`
- `src/store/localStore.ts` -> `src/domain/sampleData.ts`
- `src/store/localStore.ts` -> `src/domain/types.ts`
- `src/domain/sampleData.ts` -> `src/domain/types.ts`

### Boundary finding

There is no import edge from the current runtime surface into:

- `src/views/*`
- `src/domain/*`
- `src/store/*`

There is also no import edge from legacy folders back into:

- `src/App.tsx`
- `src/jewik-core/index.ts`
- `src/proof/proofCheck.ts`

The legacy layer is therefore disconnected from runtime behavior, but still lives inside `src`, so it remains inside TypeScript compilation scope.

## Folder Classification

### `src/views/*`

- `TYPECHECK_ONLY`
- `REFERENCE_ONLY`
- `SAFE_TO_ARCHIVE_LATER`

Reason:

- Not imported by current runtime
- Still compiled by `tsc --noEmit`
- Useful as reference for prior UX surfaces and old studio concepts

### `src/domain/*`

- `TYPECHECK_ONLY`
- `REFERENCE_ONLY`
- `DO_NOT_TOUCH_YET`

Reason:

- Not imported by current runtime
- Still compiled by `tsc --noEmit`
- Still provides the type contract used by legacy `views` and `store`
- Contains older conceptual vocabulary that may still matter for future migration decisions

### `src/store/*`

- `TYPECHECK_ONLY`
- `REFERENCE_ONLY`
- `DO_NOT_TOUCH_YET`

Reason:

- Not imported by current runtime
- Still compiled by `tsc --noEmit`
- Depends on legacy `domain`
- Contains a non-trivial sanitize/import/provenance adapter that may be useful later

## Potentially Reusable Concepts From Legacy Layer

### From `src/domain/types.ts`

- richer truth taxonomy:
  - `TruthType`
  - `TruthStatus`
  - `RelationType`
- explicit graph relations between entries
- simulation path as a distinct concept
- document-linked evidence references

### From `src/domain/sampleData.ts`

- demo structure for document-originated claims
- example of multi-entry semantic linkage
- concept of staged review before canon

### From `src/store/localStore.ts`

- deterministic sanitize pipeline
- reference validation across linked entities
- import provenance metadata
- envelope-vs-direct import distinction

### From `src/views/*`

- separate views for:
  - library/documents
  - relation graph
  - simulation
  - consent
- useful as reference if a later phase wants to reintroduce those surfaces on top of `jewik-core`

## Recommendation For Phase 1.2B

Phase 1.2B should stay non-functional and focus only on boundary hardening:

- map legacy-to-current concepts explicitly
- decide which legacy concepts are migration candidates
- decide which files are archival-only
- prepare an archive/isolation plan before any move

Recommended rule for Phase 1.2B:

- do not delete legacy files yet
- do not move legacy files yet
- first produce a migration matrix from legacy concepts to `jewik-core` concepts

