# Divine-Ascension-System

Divine-Ascension-System je napreden sistem ontoloških agentov, ki prehajajo med filozofskimi stanjami **Ego**, **Jaz** in **Enotnost**. Agenti razvijajo svoja stališča glede resnice na podlagi napetosti in čustev ter v dialogu razpravljajo o absolutnih, relativnih in enotnih resnicah.

## Komponente

- **`divine_agents/agent.py`** &ndash; implementacija razreda `Agent` z metodami za posodabljanje čustev, napetosti in prehode med stanjema.
- **`divine_agents/dialogue.py`** &ndash; funkcije za generiranje kratkih filozofskih dialogov med agenti.
- **`tests/`** &ndash; enotski testi, ki preverjajo pravilnost prehodov, odgovorov in dialogov.

## Namestitev

```bash
git clone <repo>
pip install -r requirements.txt  # če obstajajo odvisnosti
```

## Zagon simulacije

```bash
python -m divine_agents.dialogue
```

## Primer uporabe

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("Agent A")
agent2 = Agent("Agent B", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Testiranje

Za zagon testov uporabite:

```bash
pytest -q
```

## Licenca

Projekt je na voljo pod licenco MIT. Več informacij v datoteki [LICENSE](LICENSE).
