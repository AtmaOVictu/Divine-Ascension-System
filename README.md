# Divine-Ascension-System

The Divine Ascension System models philosophical agents that transition
between ontological states (**Ego**, **Jaz**, **Enotnost**) according to their
emotions and tension levels. Agents engage in dialogue where each state
reflects a different understanding of truth:

- **Ego** – truth is absolute and independent of others.
- **Jaz** – truth is relative, shaped by relationships.
- **Enotnost** – all truths are unified and interconnected.

The project contains no external dependencies aside from Python 3. It is
structured as a small package under `divine_agents` with accompanying unit
tests in `tests/`.

## Running Unit Tests

Use `pytest` or the standard library `unittest` runner. Ensure that the
package is discoverable via `PYTHONPATH`:

```bash
PYTHONPATH=. pytest -q
```

## Using `philosophical_dialogue`

The `philosophical_dialogue` function simulates a brief conversation and
shows how agents change state when emotion or tension thresholds are
exceeded.

```python
from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue

agent1 = Agent("A1")
agent2 = Agent("A2", state="Jaz")
for line in philosophical_dialogue(agent1, agent2):
    print(line)
```

Example output:

```
A1 (Ego): Resnica je absolutna in neodvisna od drugih.
A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
A1 prehaja v stanje: Jaz
A2 prehaja v stanje: Enotnost
A1: Resnica je relativna, oblikovana z našimi odnosi.
A2: Vse resnice so eno, medsebojno povezane.
```

This output demonstrates the transition of `A1` from **Ego** to **Jaz** and
`A2` from **Jaz** to **Enotnost** when their emotional intensity rises.
