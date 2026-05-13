# JEWIK Truthbase Studio

Lokalni React + TypeScript prototip za delo z dokumenti, truth units, soglasjem, relacijami in simulacijo prehoda od kandidata do kanona.

## Zahteve

- Node.js
- Corepack

## Namestitev

```bash
corepack pnpm install
```

## Zagon

```bash
corepack pnpm dev
```

## Build

```bash
corepack pnpm build
```

## Proof

```bash
corepack pnpm proof
```

## Preverjanje

- `Library`: preveri seznam dokumentov in ročni vnos dokumenta.
- `Truth Units`: izberi enoto, spremeni `ConsentStatus` ali besedilo in preveri takojšen odraz v UI.
- `Consent`: spremeni soglasje in osveži stran; vrednost mora ostati shranjena.
- `Ontograph`: preveri prikaz relacij `from -> relationType -> to`.
- `Simulation Lab`: preveri prehod statusov po stepperju.
- `Export / Import`: izvozi JSON, nato uvozi isti ali spremenjeni JSON in preveri, da se stanje obnovi.

## Opomba

- `localStorage` ključ ostaja `jewik-truthbase-studio:v1`.
- Import podpira tudi `truthbase_import.v1.json` envelope, če vsebuje `state` objekt v studio shape.
- Če je uvožen `truthbase_import.v1`, `Export / Import` prikaže source provenance metadata; to ni kanon, ampak izvor uvoza.
- `proof` uporablja tri `truthbase_import.v1` sample artifacte za preverjanje bridge robustnosti, vključno z RES_INDEX profilom.
- `export_truthbase_import_v1.py` podpira tudi `--profile res_index`, generated RES_INDEX artifact pa je del proofa.
- `proof` vključuje tudi long-chain generated RES_INDEX artifact za preverjanje daljše relacijske verige.
- `proof` vključuje tudi deterministic semantic fingerprint za generated RES_INDEX artefakte in ignorira `generatedAt`.
- `proof` preveri sample state shape, `ConsentStatus`, `localStorage` fallback in export/import top-level shape.
- Ta faza ne dodaja backenda, auth, payments ali desktop wrapperja.
