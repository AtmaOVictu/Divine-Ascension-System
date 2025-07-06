# Agentni sistem

Ta dokument opisuje ontološke agente in njihovo vedenje v projektu **Divine-Ascension-System**.

## Stanja agenta

1. **Ego** – resnica je absolutna in neodvisna od drugih.
2. **Jaz** – resnica je relativna in oblikovana z odnosi.
3. **Enotnost** – vse resnice so eno, medsebojno povezane.

## Prehodi

Agent preide v naslednje stanje, ko preseže prag **napetosti** `> 0.7` ali **čustev** `> 0.5`:

- `Ego -> Jaz` kadar so pragovi doseženi.
- `Jaz -> Enotnost` po ponovnem preseganju pragov.

Vsaka sprememba stanja je shranjena v `history` agenta.

## Moralne odločitve

Metoda `make_moral_decision` vrača odločitev, ki je odvisna od trenutnega stanja in intenzitete čustev ali napetosti. Višja napetost ali čustva vodijo v aktivnejše odločitve.

## Skupinske naloge

Funkcija `group_task` preveri, ali so vsi agenti v stanju **Enotnost**. Če so, je skupinska naloga uspešna, sicer potrebujejo več usklajevanja.

## Primer

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue, group_task

alice = Agent("Alice")
bob = Agent("Bob", state="Jaz")

print(group_task([alice, bob]))
for line in philosophical_dialogue(alice, bob):
    print(line)
```
