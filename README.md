# Divine-Ascension-System

Divine-Ascension-System je preprost sistem ontoloških agentov, ki prehajajo med
stanjema **Ego**, **Jaz** in **Enotnost** glede na svoje čustveno stanje in
napetost. Projekt vsebuje nekaj osnovnih komponent in enote za testiranje
prehodov ter odzivov agentov.

## Komponente

- **`divine_agents/agent.py`** &ndash; definicija agenta, posodobitve čuste in
  napetosti ter prehodov med ontološkimi stanjema.
- **`divine_agents/dialogue.py`** &ndash; primer kratkega filozofskega dialoga med
  dvema agentoma, ki prikazuje, kako čustva vplivajo na prehode.
- **`tests/`** &ndash; zbirka enotnih testov, ki preverjajo pravilnost prehodov in
  filozofskih odgovorov.

## Hitra uporaba

1. Klonirajte repozitorij:
   ```bash
   git clone <repo-url>
   cd Divine-Ascension-System
   ```
2. Uporabite knjižnico v svojem projektu ali za kratek preizkus:
   ```python
   from divine_agents.agent import Agent
   from divine_agents.dialogue import philosophical_dialogue

   a1 = Agent("Agent A")
   a2 = Agent("Agent B", state="Jaz")
   for line in philosophical_dialogue(a1, a2):
       print(line)
   ```

## Testiranje

Za zagon testov, ki preverijo prehode in odzive agentov, uporabite:

```bash
python -m unittest discover
```

## Licenca

Ta projekt zaenkrat nima izrecno dodane licence. Po potrebi lahko dodate
**LICENSE** datoteko (npr. MIT), da boste jasno definirali pogoje uporabe.
