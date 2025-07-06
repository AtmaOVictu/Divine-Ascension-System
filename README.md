# Divine-Ascension-System

Divine-Ascension-System je preprost okvir za ontološke agente, ki prehajajo med
stanjema **Ego**, **Jaz** in **Enotnost**. Prehodi temeljijo na napetosti in
čustvih, medtem ko dialogi odražajo filozofska načela vsakega stanja.

## Funkcionalnosti
- Prehodi agentov med filozofskimi stanji, če napetost preseže `0.7` ali čustva `0.5`.
- Enostavna simulacija dialogov med agenti.
- Zgodovina stanj za vsakega agenta.
- Enotski testi za preverjanje prehodov in odgovorov agentov.

## Uporaba
1. Klonirajte repozitorij:
   ```bash
   git clone <repo-url>
   cd Divine-Ascension-System
   ```
2. Zaženite primer dialoga ali teste:
   ```bash
   python -m unittest discover
   ```
   Testi preverijo, ali agenti pravilno prehajajo med stanjema in kako odgovarjajo v dialogu.

## Struktura projekta
- `divine_agents/agent.py` – definicija razreda `Agent` z metodami za posodabljanje čustev, napetosti in prehode stanj.
- `divine_agents/dialogue.py` – funkcija `philosophical_dialogue` za kratko simulacijo pogovora.
- `tests/` – enotski testi, ki preverjajo logiko prehodov in dialogov.
- `TESTI.ipynb` – zvezek z eksperimentalnimi primeri.

## Primer
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

