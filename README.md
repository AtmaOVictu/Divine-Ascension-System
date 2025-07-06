# Divine-Ascension-System
UX HUB FOR INTERACTIVE COMMAND/

Divine-Ascension-System je okvir za raziskovanje ontoloških prehodov.
Agenti prehajajo med stanjema **Ego**, **Jaz** in **Enotnost**,
odvisno od stopnje napetosti in čustev. Vsako stanje odraža drugačen
filozofski pogled na resnico.

## Namestitev in zagon

1. Klonirajte repozitorij:
   ```bash
   git clone <repo>
   ```
2. Zaženite enotske teste:
   ```bash
   python -m unittest
   ```

## Primer uporabe

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

a1 = Agent("A1")
a2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(a1, a2):
    print(line)
```
