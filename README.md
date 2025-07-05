# Codex: Dinamični Agenti in Ontološki Prehodi

Codex je sistem za dinamične agente, ki omogoča simulacijo prehodov skozi filozofska stanja **Ego**, **Jaz** in **Enotnost**. V njem lahko prilagajamo čustva in napetost agentov ter opazujemo njihove ontološke prehode v realnem času.

## Funkcionalnosti
- **Dinamični agenti** prehajajo skozi biološke in družbene faze.
- **Čustva** neposredno vplivajo na napetost in interakcije.
- **Ontološki prehodi** se zgodijo, ko napetost preseže `0.7` ali čustvo `0.5`.
- **Simulacija** in testiranje različnih scenarijev prek enotnih testov.

## Načrtovanje sistema
Sistem omogoča interaktivno programiranje: parametre agentov lahko spreminjamo in sproti vidimo njihove odzive. Napetost in čustva agentov so med seboj povezana, kar omogoča raziskovanje novih idej in optimizacijo ontoloških prehodov.

## Zahteve in namestitev
- Python 3.6+
- `pytest` za testiranje

Namestitev:
```bash
git clone https://github.com/your-username/codex.git
cd codex
pip install -r requirements.txt
```

## Uporaba
Zaženite osnovno simulacijo:
```bash
python -m divine_agents.run
```
Za interaktivno demonstracijo filozofskega dialoga med agenti:
```bash
python -m divine_agents.demo
```

## Testiranje
Zaženite vse enote testiranja:
```bash
pytest -q
```
Posamezne teste lahko poganjate neposredno iz mape `tests/`.

## Ontološke faze
- **Ego (⊘)**: resnica je absolutna in neodvisna od drugih.
- **Jaz (∫(dru/x))**: resnica je relativna in oblikovana z odnosi.
- **Enotnost (RES001)**: vse resnice so eno, medsebojno povezane.

## Optimizacija in razširljivost
Kodo je mogoče enostavno prilagoditi: dodajate lahko nove faze, parametre in metode za vizualizacijo ali naprednejše analize. Sistem je zasnovan modularno, zato je razširitev funkcionalnosti preprosta.

