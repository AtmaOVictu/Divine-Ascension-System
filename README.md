# Codex: Dinamični Agenti in Ontološki Prehodi

Codex je preprost sistem za raziskovanje ontoloških faz agentov. Agenti lahko prehajajo skozi stanja **Ego**, **Jaz** in **Enotnost**, pri čemer na prehod vplivata napetost in čustva. Projekt omogoča interaktivno spreminjanje parametrov in s tem takojšen vpogled v spremembe napetosti ter čustvenih prehodov.

## Funkcionalnosti
- **Dinamični agenti** z zgodovino stanj in možnostjo posodabljanja napetosti ter čustev.
- **Ontološki prehodi** med fazami Ego → Jaz → Enotnost, sproženi pri napetosti > 0.7 ali čustvu > 0.5.
- **Filozofski dialog** med agenti, kjer vsak agent odgovarja glede na svoje trenutno stanje.

## Namestitev
Za zagon klonirajte repozitorij in namestite odvisnosti:
```bash
git clone <repo-url>
cd Divine-Ascension-System
pip install -r requirements.txt  # trenutno brez zunanjih paketov
```

## Uporaba
Datoteka `divine_agents/dialogue.py` vsebuje primer interakcije agentov. Za zagon dialoga uporabite:
```bash
python -m divine_agents.dialogue
```
ali za zagon testov:
```bash
python -m pytest -q
```

## Testiranje
V mapi `tests` so pripravljeni enotski testi, ki preverjajo pravilnost prehodov in odgovorov agentov. Testi se zaženejo z ukazom `python -m pytest -q`.

Codex je namenjen raziskovanju ontoloških konceptov na dinamičen način in se zlahka razširi z dodatnimi pravili, fazami ali vizualizacijo napetosti in čustev.
