# TRUTHUNIT TO LEXICONENTRY FIELD CONTRACT

Status: READ-ONLY  
Date: 2026-05-08  
Scope: legacy `TruthUnit` in povezane reference -> current-core `LexiconEntry`  
Boundary: brez sprememb `src/*`, proof kode, App shella ali migracijske implementacije

## Canonical Rules

- `LexiconEntry` je trenutna core resnica.
- `TruthUnit` je legacy koncept in ni avtoritativni truth model za current core.
- Nobeno legacy polje ne sme razsiriti current core brez novega pravila.
- `proofStatus`, `consentStatus`, `CANON` in provenance se ne smejo zliti v isto polje.
- Graph, consent, document, simulation in provenance plasti se v tej fazi ne uvajajo.
- Evidence relation se sme obravnavati samo tam, kjer obstaja varen `EvidenceItem` ekvivalent.

## Mapping Status Legend

- `DIRECT_ALLOWED`: polje se lahko prenese neposredno brez spremembe pomena.
- `NORMALIZED_ALLOWED`: polje se lahko prenese z omejeno normalizacijo brez spremembe pomena.
- `DERIVED_ALLOWED`: current-core vrednost se lahko varno izdela iz legacy polja brez sirjenja scope.
- `REJECTED_NO_CORE_HOME`: current core za to polje nima varnega doma.
- `REJECTED_SCOPE_EXPANSION`: mapping bi odprl prepovedan nov sloj ali zmes konceptov.
- `NEEDS_DECISION`: obstaja kandidatni current-core dom, vendar brez novega pravila mapping ni varen.

## Current Core Constraints

- `LexiconEntry.term` je obvezen za veljaven entry.
- `LexiconEntry.dictionaryLayer.meaning` je obvezen, kadar `dictionaryLayer.kind !== "UNAVAILABLE"`.
- `LexiconEntry.proofStatus === "PROVEN"` je dovoljen samo ob vsaj enem `EvidenceItem`.
- `LexiconEntry.type === "INTERNAL_OPERATOR"` aktivira `MISSING_OPERATOR_MAPPING`, ce `operatorMapping` manjka.
- Trenutni proof ledger ne odpira consent, document, graph, simulation ali provenance arhitekture.

## Field Contract

| legacy field | legacy meaning | candidate LexiconEntry field | mapping status | allowed transform | forbidden transform | proof implication | decision needed | recommended next action |
|---|---|---|---|---|---|---|---|---|
| `TruthUnit.id` | stabilni identifikator legacy enote | `LexiconEntry.id` | `DIRECT_ALLOWED` | Ohrani isti neprazen niz identifikatorja. | Ne generiraj novega `id`, ce legacy `id` obstaja; ne vezi ga na `documentId` ali `title`. | Ne odpira novega proof pravila; vpliva le na stabilnost future roundtripa in sledljivost izvoza. | Ne | V Fazi D ga kopiraj neposredno z zavrnitvijo praznega ali podvojenega `id`. |
| `TruthUnit.title` | naslov ali label trditve | `LexiconEntry.term` | `NEEDS_DECISION` | Trenutno brez varnega transforma. | Ne kopiraj `title` slepo v `term`; ne uporabljaj ga za umetno zapiranje `MISSING_TERM`. | Napačen mapping bi prikril manjkajoci lexical headword in dal navidezno veljaven entry. | Da: ali `term` prihaja iz `title`, `keyDefinitions[0]` ali izven `TruthUnit`? | Najprej sprejmi loceno headword pravilo; do takrat brez mape. |
| `TruthUnit.claim` | jedrna izjava ali proposition body | `dictionaryLayer.meaning` ali `jewikCut.expression` | `NEEDS_DECISION` | Trenutno brez varnega transforma. | Ne mapiraj istega `claim` hkrati v `meaning` in `cut`; ne uporabi ga za avtomatsko zaprtje praznega cut/meaning. | Naiven mapping lahko lazno zadosti `MISSING_DICTIONARY_MEANING` ali skrije prazen `JEWIK cut`. | Da: ali je `claim` definicija, cut ali samo proposition? | Odpri eno samo odlocitev za “claim home”, preden se dotaknes current core. |
| `TruthUnit.type` | legacy truth taxonomy (`AKSIOM_APD`, `DEFINICIJA`, `OSEBNA_RESNICA` ...) | `LexiconEntry.type` | `NEEDS_DECISION` | Trenutno brez varnega transforma. | Ne sesuj vseh legacy tipov v `ORDINARY_WORD`; ne inferiraj `INTERNAL_OPERATOR` heuristično. | Mapping v `INTERNAL_OPERATOR` bi aktiviral `MISSING_OPERATOR_MAPPING`; mapping vseh v `ORDINARY_WORD` bi to proof pot prikril. | Da: potreben je ekspliciten lookup table ali pravilo “type subset only”. | Do takrat pusti `type` izven minimalnega patcha. |
| `TruthUnit.status` | legacy workflow (`CANDIDATE`, `TESTABLE`, `CANON`, `READY_FOR_MY_CONSENT` ...) | `LexiconEntry.proofStatus` | `REJECTED_SCOPE_EXPANSION` | Noben. | Ne zlivaj `CANDIDATE`, `CANON` ali `READY_FOR_MY_CONSENT` v `DRAFT`, `UNDER_REVIEW` ali `PROVEN`. | To bi zmesalo workflow/canon logiko s proof guardraili in porusilo mejo “no blended truth”. | Ne | Ohraniti izven current core; ce bo potreben, zahteva nov workflow sloj. |
| `TruthUnit.consentStatus` | osebno soglasje in kanon gate | brez current-core doma | `REJECTED_SCOPE_EXPANSION` | Noben. | Ne mapiraj v `proofStatus`, `versionHistory`, `dictionaryLayer.kind` ali `proofNotes`. | Consent ni del current proof modela; zlitje bi ustvarilo lazen signal o kanonu ali dokazni jakosti. | Ne | Ostane izven current core, dokler ni odobren locen consent sloj. |
| `TruthUnit.documentId` | povezava na izvorni dokument | brez current-core doma | `REJECTED_SCOPE_EXPANSION` | Noben. | Ne serializiraj ga v `term`, `source`, `dictionaryLayer.notes` ali `versionHistory`. | Dokumentni izvor trenutno ni del proof contracta; tihi mapping bi uvedel skriti source layer. | Ne | Pusti zunaj; document model je ločena prihodnja faza. |
| `TruthUnit.keyDefinitions[]` | seznam ključnih pojmov okrog trditve | brez varnega current-core doma | `REJECTED_NO_CORE_HOME` | Noben. | Ne uporabljaj prvega elementa kot `term`; ne potiskaj arraya v `antinomies` ali `dictionaryLayer.meaning`. | Napačen mapping lahko lazno zapolni `term` ali zamegli pomen dictionary layerja. | Ne | Brez migracije; po potrebi kasneje odpri ločen definitions contract. |
| `TruthUnit.evidenceFromDocument[]` | inline besedilni dokaz znotraj `TruthUnit` | `LexiconEntry.evidence[]` | `DERIVED_ALLOWED` | Vsak neprazen niz postane en `EvidenceItem` z novim ali determinističnim `id`, `text = trim(vrednost)`, `source = "legacy:evidenceFromDocument"`, `createdAt = TruthUnit.updatedAt` ali `createdAt`. | Ne zdruzuj vseh vrstic v en sam blob; ne uporabljaj njihove prisotnosti za avtomatski `PROVEN`. | To neposredno vpliva na `evidence.length`, `canMarkProven`, downgrade iz `PROVEN` in future proofCheck scenarije. | Ne | To je kandidat za Fazo D, vendar samo brez avtomatskega mapiranja `proofStatus`. |
| `TruthUnit.counterAngle` | besedilni proti-kot ali opozorilo | `proofNotes` ali `antinomies` | `NEEDS_DECISION` | Trenutno brez varnega transforma. | Ne potiskaj celega stavka v `antinomies`; ne pretvarjaj ga v `proofStatus`. | Trenutni proofCheck ga ne uporablja, vendar bi napačen mapping zameglil razliko med evidence, proof notes in semantic opozorili. | Da: ali current core sploh potrebuje ločen counter-angle dom? | Brez migracije do odobritve namenskega pravila. |
| `TruthUnit.proposedLinks[]` | predlogi za prihodnje relacije | brez current-core doma | `REJECTED_SCOPE_EXPANSION` | Noben. | Ne mapiraj v `antinomies`, `proofNotes` ali `versionHistory`. | Relacijski predlogi niso del current proof modela; tihi mapping bi odprl graph sloj. | Ne | Ostane izven current core. |
| `TruthUnit.notes` | splošne uredniske ali interpretativne opombe | `dictionaryLayer.notes` ali `proofNotes` ali `jewikCut.notes` | `NEEDS_DECISION` | Trenutno brez varnega transforma. | Ne razdeli istih opomb po vec note poljih; ne jih obravnavaj kot dokaz. | Lahko vpliva na izvoz in razlago entryja, ne pa neposredno na trenutne proof invariants. | Da: potrebna je ena sama note-destination politika. | Dokler ni pravila, brez migracije v current core. |
| `TruthUnit.createdAt` | cas ustvaritve legacy enote | `LexiconEntry.createdAt` | `DIRECT_ALLOWED` | Ohrani isti casovni zig, ce je prisoten kot niz. | Ne zamenjaj ga z import casom ali `DocumentSource.createdAt`. | Ne odpira novega proof pravila; vpliva le na kronologijo in audit trail. | Ne | V Fazi D ga kopiraj neposredno. |
| `TruthUnit.updatedAt` | cas zadnje posodobitve legacy enote | `LexiconEntry.updatedAt` | `DIRECT_ALLOWED` | Ohrani isti casovni zig, ce je prisoten kot niz. | Ne prepisuj z `stamp()` med read-only migracijskim mapiranjem. | Ne odpira novega proof pravila; vpliva na casovno sled v izvozu in morebitni future history logiki. | Ne | V Fazi D ga kopiraj neposredno. |
| `EvidenceRef.id` prek `truthUnitId` relacije | identifikator zunanjega evidence zapisa | `EvidenceItem.id` | `DERIVED_ALLOWED` | Ce se `EvidenceRef` sploh uvaža, naj njegov `id` postane `EvidenceItem.id`. | Ne generiraj nakljucnega `id`, ce stabilni `EvidenceRef.id` že obstaja. | Ne spreminja proof logike, vendar izboljsa sledljivost future exporta in debugiranja. | Ne | Uporabi samo v sklopu evidence-only mape, ne samostojno. |
| `EvidenceRef.quote` prek `truthUnitId` relacije | citat kot dokazna vsebina | `EvidenceItem.text` | `DERIVED_ALLOWED` | `text = trim(quote)` za vsak `EvidenceRef`, vezan na trenutni `TruthUnit`. | Ne lepi `confidence` ali `sourceLocation` v `text`; ne dupliraj istega citata v vec itemov brez pravila. | Dodajanje takih itemov poveca `evidence.length` in vpliva na future `PROVEN` guardraile. | Ne | V Fazi D dovoljen samo skupaj z zelo ozkim evidence patchom. |
| `EvidenceRef.sourceLocation` prek `truthUnitId` relacije | lokacija citata znotraj vira | `EvidenceItem.source` | `NORMALIZED_ALLOWED` | Ce obstaja, se kot navaden niz prenese v `source`. | Ne zdruzuj ga s `confidence`, `documentId` ali `filename`; ne ga obravnavaj kot dictionary source authority. | Ne vpliva na active proof invariants, izboljsa pa cloveko-berljivo audit sled izvoza. | Ne | V Fazi D dovoljena omejena normalizacija na string source. |
| `EvidenceRef.confidence` prek `truthUnitId` relacije | numericna ocena zaupanja | brez current-core doma | `REJECTED_NO_CORE_HOME` | Noben. | Ne mapiraj v `proofStatus`, `dictionaryLayer.kind`, `source` ali `proofNotes`. | Vnos confidence v current core bi lazno predstavljal dokazno jakost, ki je current proof model ne pozna. | Ne | Ostane zunaj, dokler ni odobren ločen evidence-confidence contract. |
| `DefinitionRef.definition` prek `linkedUnitIds` relacije | zunanja definicijska vsebina, povezana z enoto | `dictionaryLayer.meaning` | `NEEDS_DECISION` | Trenutno brez varnega transforma. | Ne uporabi “prve zadetne definicije”; ne zdruzuj vec definicij v en `meaning` blob. | Naivni mapping bi lahko lazno zaprl `MISSING_DICTIONARY_MEANING` brez resne dictionary-layer politike. | Da: potrebna je odlocitev o eni avtoritativni definiciji in `DictionaryLayerKind`. | Brez migracije do ločenega dictionary-layer pravila. |
| `DefinitionRef.term`, `scope`, `linkedUnitIds` | relacijska definicijska struktura | brez current-core doma | `REJECTED_SCOPE_EXPANSION` | Noben. | Ne potiskaj `scope` v `notes`; ne mapiraj `linkedUnitIds` v `antinomies`. | To ni del trenutnega proof contracta; mapping bi odprl definitions relation sloj. | Ne | Ostane izven minimalnega core patcha. |
| `DocumentSource.title`, `filename`, `content`, `createdAt`, `updatedAt` prek `documentId` | izvorni dokumentni zapis | brez current-core doma | `REJECTED_SCOPE_EXPANSION` | Noben. | Ne zlivaj dokumentnega naslova ali vsebine v `term`, `meaning`, `source` ali `proofNotes`. | Document layer trenutno ni del proof meje; tihi mapping bi ustvaril neodobren source model. | Ne | Pusti zunaj current core. |
| `UnitLink.*` prek `fromUnitId` / `toUnitId` | eksplicitne med-enotne relacije | brez current-core doma | `REJECTED_SCOPE_EXPANSION` | Noben. | Ne serializiraj linkov v `antinomies`, `notes` ali `versionHistory`. | Relacijski graph ni del current proof modela; migracija bi odprla novo arhitekturo. | Ne | Ostane izven current core, dokler ni odobren graph contract. |
| `SimulationCase.*` in `SimulationStep.*` | state-machine / procesni tok kandidat -> kanon | brez current-core doma | `REJECTED_SCOPE_EXPANSION` | Noben. | Ne mapiraj v `proofStatus`, `versionHistory` ali `jewikCut`. | To bi neposredno zmesalo workflow simulacijo s proof statusom in kršilo “no blended truth”. | Ne | Ne migrirati brez ločene simulation faze. |
| `ImportMetadata`, `ImportSourceMetadata`, `truthbase_import.v1` | envelope provenance, generator in source sled | brez current-core doma | `REJECTED_SCOPE_EXPANSION` | Noben. | Ne serializiraj provenance v `proofNotes`, `dictionaryLayer.notes`, `source` ali `versionHistory`. | Current proof ledger izrecno ne odpira nove import arhitekture; provenance ne sme ustvariti navideznega dokaza. | Ne | Ostane izven current core in izven Faze D. |

## Safe-For-Future-Patch Set

Naslednji minimalni core patch sme obravnavati samo:

- `TruthUnit.id -> LexiconEntry.id`
- `TruthUnit.createdAt -> LexiconEntry.createdAt`
- `TruthUnit.updatedAt -> LexiconEntry.updatedAt`
- `TruthUnit.evidenceFromDocument[] -> LexiconEntry.evidence[]`
- `EvidenceRef.id -> EvidenceItem.id`
- `EvidenceRef.quote -> EvidenceItem.text`
- `EvidenceRef.sourceLocation -> EvidenceItem.source`

Vse ostalo ostane zunaj, dokler ni odobreno novo pravilo.

## Explicit Rejections

- `TruthUnit.status` se ne sme pretvoriti v `proofStatus`.
- `TruthUnit.consentStatus` se ne sme pretvoriti v `proofStatus`, `versionHistory` ali katerokoli drugo current-core polje.
- `DocumentSource`, `UnitLink`, `SimulationCase` in `ImportMetadata` nimajo dovoljenega current-core doma v tej fazi.
- `EvidenceRef.confidence` se ne sme pretvoriti v noben current-core signal dokazne jakosti.

## Proof Notes For Future Phase

- Vsaka prihodnja implementacija evidence-only mape bo morala razsiriti proof coverage, ker `evidence.length` neposredno vpliva na:
  - `canMarkProven`
  - blokado `PROVEN` brez evidence
  - downgrade `PROVEN -> UNDER_REVIEW`, ko evidence izgine
- Prihodnja implementacija ne sme avtomatsko mapirati nobenega legacy workflow ali consent polja v `proofStatus`.
- Prihodnja implementacija ne sme spremeniti operator-mapping pravil; `TruthUnit.type` ostaja zunaj scope minimalnega patcha.
