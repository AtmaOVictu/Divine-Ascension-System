# Divine-Ascension-System

Divine-Ascension-System je sistem ontoloških agentov, ki prehajajo med stani (Ego, Jaz, Enotnost) na podlagi čustev in napetosti. Projekt omogoča simulacijo dialogov med agenti ter preverjanje prehodov skozi enostavne enotske teste.

## Struktura projekta

- **`divine_agents/agent.py`** – implementacija agentov in prehodov med stanji.
- **`divine_agents/dialogue.py`** – pomožni moduli za vodenje dialoga med agenti.
- **`tests/`** – enotski testi za preverjanje pravilnosti sistema.

## Namestitev

1. Klonirajte repozitorij:
   ```bash
   git clone https://github.com/yourname/Divine-Ascension-System.git
   cd Divine-Ascension-System
   ```
2. Izvedite teste, da preverite delovanje:
   ```bash
   python -m pytest -q
   ```

Projekt ne zahteva posebnih zunanjih odvisnosti; zadosten je Python 3.11.

## Primer uporabe

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# Ustvarimo dva agenta
agent1 = Agent("Agent A")
agent2 = Agent("Agent B", state="Jaz")

# Izvedemo kratek dialog
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

## Licenca

Koda v tem repozitoriju je objavljena pod licenco MIT. Več informacij najdete v datoteki [LICENSE](LICENSE).
