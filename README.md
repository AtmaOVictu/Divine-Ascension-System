# Divine-Ascension-System

Ta repozitorij vsebuje preprost sistem ontoloških agentov, ki prehajajo med stanji **Ego**, **Jaz** in **Enotnost**. Prehodi so pogojeni z napetostjo in čustvi, pri čemer vsak agent odgovarja glede na svoje trenutno stanje.

## Namestitev

1. Uporabite Python 3.8 ali novejši.
2. Priporočamo uporabo virtualnega okolja:

```bash
python3 -m venv env
source env/bin/activate  # na Linux/macOS
# env\Scripts\activate  # na Windows
```

3. Namestite odvisnosti (za testiranje in morebitno vizualizacijo):

```bash
pip install -r requirements.txt  # če datoteka obstaja
```

## Zagon testov

Teste lahko zaženete z ukazom:

```bash
python -m unittest discover -s tests -p 'test*.py'
```

## Primer uporabe

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

# ustvarimo agenta v stanju Ego
agent1 = Agent("A1")
# drugi agent je že v stanju Jaz
agent2 = Agent("A2", state="Jaz")

# izpeljemo kratek dialog
lines = philosophical_dialogue(agent1, agent2)
for line in lines:
    print(line)
```

## Optimalne nastavitve

- Za stabilno delovanje naj bo začetna napetost nizka (pod 0.7).
- Prehodi med stanji se sprožijo, ko napetost preseže 0.7 ali čustvo preseže 0.5.
- Če želite hitrejše prehode, povečajte vnos čustvene intenzitete v `update_emotion`.

Sistem je namenjen raziskovanju filozofskih razprav in lahko služi kot osnova za nadaljnje razširitve.
