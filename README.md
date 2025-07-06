# Divine-Ascension-System

UX HUB FOR INTERACTIVE COMMAND/

## Opis
Divine-Ascension-System je sistem za ontološke agente, ki prehajajo skozi različna stanja zavesti. Agenti sprejemajo **moralne odločitve**, sodelujejo v **filozofskih dialogih** in se premikajo iz stanja **Ego** v **Jaz** ter naprej v **Enotnost**. Uporabniki lahko interagirajo z agenti preko ukazne vrstice.

## Namestitev
1. Klonirajte repozitorij:
   ```bash
   git clone <repo-url>
   ```
2. (Izbirno) Namestite odvisnosti:
   ```bash
   pip install -r requirements.txt
   ```

## Hitri zagon
Primer uporabe modulov v Pythonu:
```python
from divine_agents.agent import Agent
from divine_agents.dialogue import debate

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")

for line in debate(agent1, agent2):
    print(line)
```

## Testiranje
Testno okolje lahko zažgete z ukazom:
```bash
python -m pytest -q
```

## Licence
Projekt je odprtokoden pod licenco MIT.
