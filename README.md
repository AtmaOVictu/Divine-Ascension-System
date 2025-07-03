# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

## Namestitev okolja
Priporočamo uporabo virtualnega okolja:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # trenutno brez dodatnih odvisnosti
```

## Poganjanje testov
Za zagon enotskih testov uporabite:

```bash
python -m unittest discover -s tests
```

## Primer uporabe modulov
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in philosophical_dialogue(agent1, agent2):
    print(line)
```
Modul `agent` omogoča prehode med stanjema **Ego**, **Jaz** in **Enotnost** glede na napetost in čustva. Funkcija `philosophical_dialogue` prikaže kratek primer pogovora med agentoma.

## Licenca
Projekt uporablja licenco [MIT](LICENSE).
