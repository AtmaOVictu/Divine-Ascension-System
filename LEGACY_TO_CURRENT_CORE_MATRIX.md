# LEGACY TO CURRENT CORE MATRIX

Status: READ-ONLY  
Date: 2026-05-08  
Scope: mapping med legacy `src/views/*`, `src/domain/*`, `src/store/*` in current `src/jewik-core/index.ts`  
Boundary: brez sprememb kode, runtime, proof ali imen datotek

## Current Truth

- Current runtime surface je `src/main.tsx -> src/App.tsx -> src/jewik-core/index.ts`.
- Current proof surface je `src/proof/proofCheck.ts`.
- Legacy plast ni del aktivnega runtime toka.
- Legacy plast pa ostaja znotraj TypeScript compilation scope, ker se se vedno nahaja v `src`.

## Status Legend

- `CURRENT_CORE_MATCH`: koncept ze obstaja v current core z dovolj bliznjim contractom.
- `PARTIAL_MATCH`: obstaja delni current core ekvivalent, vendar shape ali pravila niso poravnani.
- `NO_CORE_EQUIVALENT`: current core za ta koncept nima contracta.
- `ARCHIVE_ONLY`: koncept ali datoteka je uporabna predvsem kot zgodovina, referenca ali UI ostanek.
- `NEEDS_DECISION`: migracija bi zahtevala novo produktno ali core pravilo.

## Compilation Scope Notes

- Vse datoteke v `src/views/*`, `src/domain/*` in `src/store/*` ostajajo v TypeScript compilation scope.
- `src/domain/types.ts` vpliva na typecheck cele legacy plasti, ker ga uvozijo views in store.
- `src/domain/sampleData.ts` vpliva na typecheck prek `src/store/localStore.ts`.
- `src/store/localStore.ts` vpliva na typecheck `src/views/ExportImportView.tsx`, ker izvozi `ImportMetadata`.
- Ceprav legacy plast ni runtime-aktivna, jo spremembe se vedno lahko zlomijo pri `tsc --noEmit`.

## Proof-Relevant Notes

- Aktivni proof contract ostaja omejen na `src/proof/proofCheck.ts` in `src/jewik-core/index.ts`.
- `src/domain/sampleData.ts` je proof-relevantna samo kot boundary/reference surface iz stare plasti, ne kot aktivna proof odvisnost.
- `src/store/localStore.ts` je proof-adjacent samo na ravni zgodovinske import/sanitize logike; trenutni proof ledger izrecno ne odpira nove import arhitekture.
- Noben legacy view ni del aktivnega proof surface.

## Do Not Migrate Without New Core Rule

- `ConsentStatus` in kanonizacijski UI tok
- `RelationType` / `UnitLink` / ontograph model
- `DocumentSource` kot samostojna truth/source plast
- `SimulationCase` / `SimulationStep` / simulation state machine
- `ImportMetadata`, envelope provenance in `truthbase_import.v1`
- bogatejsa `TruthType` / `TruthStatus` taksonomija izven trenutnega `EntryType` + `ProofStatus`

## Matrix

| legacy file | legacy concept | current core equivalent | migration status | risk | recommended next action |
|---|---|---|---|---|---|
| `src/domain/types.ts` | `StudioState` kot vec-zbirkovni model (`documents`, `truthUnits`, `evidenceRefs`, `definitions`, `counterAngles`, `links`, `simulationCases`) | `WorkbenchState` z eno kolekcijo `entries` | `PARTIAL_MATCH` | `HIGH` | Ne stiskaj vec-zbirkovnega modela v `entries`; najprej odpri locen core state-shape contract. |
| `src/domain/types.ts` | `TruthUnit` | `LexiconEntry` | `PARTIAL_MATCH` | `MEDIUM` | V prihodnje naredi samo field-level mapping prekrivanj; ne migriraj celotnega shape brez nove specifikacije. |
| `src/domain/types.ts` | `TruthType` + `TruthStatus` taksonomija | `EntryType` + `ProofStatus` | `PARTIAL_MATCH` | `HIGH` | Potrebna je odlocitev, katere legacy statuse se sploh sme prenesti v current core. |
| `src/domain/types.ts` | `ConsentStatus` | brez current core ekvivalenta | `NEEDS_DECISION` | `HIGH` | Ne migriraj brez novega core pravila za osebno soglasje in kanon gate. |
| `src/domain/types.ts` | `DocumentSource` | brez current core ekvivalenta | `NO_CORE_EQUIVALENT` | `HIGH` | Ce se vrne document layer, najprej definira nov source contract locen od `LexiconEntry`. |
| `src/domain/types.ts` | `EvidenceRef` z `quote`, `sourceLocation`, `confidence` | `EvidenceItem` z `text`, `source`, `createdAt` | `PARTIAL_MATCH` | `HIGH` | Ne izgubi `sourceLocation` in `confidence` tiho; odpri locen evidence-shape rule, ce je to se potrebno. |
| `src/domain/types.ts` | `DefinitionRef` | `dictionaryLayer.meaning` in delno `dictionaryLayer.notes` | `PARTIAL_MATCH` | `HIGH` | Scoped definicij in `linkedUnitIds` ne migriraj brez locenega dictionary/definition contracta. |
| `src/domain/types.ts` | `CounterAngle` | brez direktnega ekvivalenta; samo neformalni prostor v `proofNotes` ali `jewikCut.notes` | `NEEDS_DECISION` | `HIGH` | Ce je proti-kot se potreben, definira nov current-core shape namesto da se ga skrije v free-text polja. |
| `src/domain/types.ts` | `UnitLink` + `RelationType` | brez current core ekvivalenta | `NO_CORE_EQUIVALENT` | `HIGH` | Relacijskega modela ne migriraj brez novega graph contracta in proof meje. |
| `src/domain/types.ts` | `SimulationCase` + `SimulationStep` + `simulationPath` | brez current core ekvivalenta | `NO_CORE_EQUIVALENT` | `HIGH` | Simulation state machine zahteva loceno fazo; ne meci ga v trenutni proof status loop. |
| `src/domain/types.ts` | `ViewId` + `viewLabels` | brez current core ekvivalenta | `ARCHIVE_ONLY` | `LOW` | Ohrani kot UI zgodovino; ne migriraj JSX navigacijskih konceptov v core. |
| `src/domain/sampleData.ts` | `createEmptyState()` za legacy `StudioState` | `createInitialWorkbenchState()` in delno `createBlankEntry()` | `PARTIAL_MATCH` | `MEDIUM` | Ne zamenjuj shape-ov; prazno stanje za current core naj ostane v current-core contractu. |
| `src/domain/sampleData.ts` | `createSampleState()` kot seeded multi-unit demo korpus | `createSampleEntry()` in `createInitialWorkbenchState()` | `PARTIAL_MATCH` | `MEDIUM` | Ohrani kot referenco; ce bo potreben nov demo seed, ga zgradi neposredno nad `LexiconEntry`. |
| `src/domain/sampleData.ts` | demo relacije, definicije, counter-angle, simulation in document-origin trace | delno `evidence`, `antinomies`, `versionHistory`; vecina brez ekvivalenta | `NEEDS_DECISION` | `HIGH` | Ne migriraj kompleksnega demo korpusa brez novih pravil za graph, provenance in simulation. |
| `src/store/localStore.ts` | `sanitizeState()` z shape filteringom, dedupe, reference repair in envelope extraction | `sanitizeWorkbenchState()` | `PARTIAL_MATCH` | `HIGH` | Uporabi le kot referenco; nov import/sanitize contract mora ostati locen od legacy graph pravil. |
| `src/store/localStore.ts` | `readState()` / `writeState()` za `StudioState` localStorage tok | brez current core ekvivalenta | `ARCHIVE_ONLY` | `LOW` | Persistence bridge naj ostane UI/runtime odlocitev, ne current core migracija. |
| `src/store/localStore.ts` | `ImportMetadata`, `ImportSourceMetadata`, `TRUTHBASE_IMPORT_CONTRACT`, envelope provenance | brez current core ekvivalenta | `NO_CORE_EQUIVALENT` | `HIGH` | Ne migriraj brez novega import contracta in jasne odlocitve, kaj je official/community/derived metadata. |
| `src/views/LibraryView.tsx` | knjiznica dokumentov in rocni vnos dokumenta | brez current core ekvivalenta; current core zacne pri `LexiconEntry` | `ARCHIVE_ONLY` | `LOW` | Ohrani kot UI/view zgodovino; za vrnitev dokumentne plasti najprej odpri nov source-layer contract. |
| `src/views/TruthUnitsView.tsx` | rich editor za `TruthUnit`, evidence refs, definicije, proti-kot in links | delni ekvivalenti v `LexiconEntry`, `EvidenceItem`, `dictionaryLayer`, `proofStatus`, `operatorMapping`, `antinomies` | `PARTIAL_MATCH` | `HIGH` | Migriraj samo konceptualni overlap; ne prenasaj truth taxonomy, links ali consent polj brez novih core pravil. |
| `src/views/ConsentView.tsx` | eksplicitni user-consent in kanon gate UI | brez current core ekvivalenta | `NEEDS_DECISION` | `HIGH` | Ce se soglasje vrne, mora dobiti lasten current-core contract in proof boundary. |
| `src/views/OntographView.tsx` | relacijski prikaz `from -> relationType -> to` | brez current core ekvivalenta | `NO_CORE_EQUIVALENT` | `HIGH` | Graph UI nima kaj migrirati, dokler relation model ne obstaja v current core. |
| `src/views/SimulationLabView.tsx` | candidate-to-canon stepper in simulacijski prikaz | brez current core ekvivalenta | `NEEDS_DECISION` | `HIGH` | Ne migriraj simulacijskega toka v `ProofStatus`; ce se vrne, odpri loceno state-machine fazo. |
| `src/views/ExportImportView.tsx` | legacy JSON export/import UI in provenance prikaz | `buildJsonExport()` pokrije samo del izvoza; import metadata nima ekvivalenta | `PARTIAL_MATCH` | `HIGH` | Ne migriraj view logike; najprej definira nov import/export UI contract nad current core. |

## Summary Calls

- Najbolj migrabilen del legacy plasti je konceptualni overlap `TruthUnit -> LexiconEntry`, `EvidenceRef -> EvidenceItem` in legacy sanitize logika kot referenca, ne kot copy-paste target.
- Najvecji archive-only del so legacy views kot JSX implementacije in `ViewId` / `viewLabels`.
- Najvecji decision-needed del so `ConsentStatus`, relacijski model, document layer, simulation in provenance metadata.
- Najvecje typecheck tveganje ostaja `src/domain/types.ts`, ker ga uporablja prakticno vsa legacy plast.
- Najvecje proof tveganje bi nastalo, ce bi se import/provenance/simulation/consent preselili v current core brez novega explicitnega contracta.
