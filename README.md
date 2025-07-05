# Divine-Ascension-System

The **Divine-Ascension-System** models agents that debate philosophy and evolve
through three ontological phases: **Ego**, **Jaz**, and **Enotnost**. Each phase
represents a different understanding of truth and is influenced by an agent's
emotions and tension.

## Philosophical Framework
- **Ego (⊘)** – Truth is *absolute* and independent of others. Agents defend
  their individual perception of reality.
- **Jaz (∫(dru/x))** – Truth is *relative* and shaped through relationships.
  Agents acknowledge that experience and interaction construct reality.
- **Enotnost (RES001)** – Truth is *unified*. All truths are interconnected and
  separation is an illusion.

Agents start in a chosen state and can transition to the next one when their
`tension` exceeds `0.7` or their `emotion` intensity exceeds `0.5`. Dialogue
between agents reflects their current state and emotional tone.

## Installation
1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Only `pytest` is required for running tests.

## Running Unit Tests
Execute all tests with:
```bash
python -m unittest discover tests
```

## Demonstration
A simple demonstration script is provided:
```bash
python demo.py
```
This will print a short philosophical exchange where agents may transition
states based on emotional updates. Expected output resembles:
```
Agent 1 (Ego): Resnica je absolutna in neodvisna od drugih.
Agent 2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
Agent 1 prehaja v stanje: Jaz
Agent 2 prehaja v stanje: Enotnost
Agent 1: Resnica je relativna, oblikovana z našimi odnosi.
Agent 2: Vse resnice so eno, medsebojno povezane.
```

A Jupyter notebook named `TESTI.ipynb` is included for experimentation. Open
it with any notebook server to explore the API interactively.
