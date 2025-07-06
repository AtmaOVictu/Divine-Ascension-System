# Divine-Ascension-System

Divine-Ascension-System je preprosta simulacija ontoloških agentov, ki se premikajo med stanjema **Ego**, **Jaz** in **Enotnost**. Prehodi so sproženi z intenzivnostjo čustev in napetosti. Agenti se na podlagi svojega stanja odzivajo na filozofska vprašanja.

## Namestitev

```bash
pip install -r requirements.txt  # ce so potrebne odvisnosti
```

## Zagon

```bash
python -m divine_agents
```

## Testiranje

```bash
python -m unittest discover
```

## Struktura

- `divine_agents/agent.py` definira razred `Agent` z metodami za posodabljanje čustev, prehode in moralne odločitve.
- `divine_agents/dialogue.py` vsebuje funkcijo za simulacijo filozofskega dialoga in skupinskih nalog.
- `tests/` hrani enote za preverjanje delovanja sistema.

## Primer uporabe

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

for line in philosophical_dialogue(alice, bob):
    print(line)
```
