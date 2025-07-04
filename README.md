# Divine-Ascension-System

Dynamic agents that explore philosophical states through emotion and tension.

## Overview

This project implements a small framework for simulating ontological agents.
Agents transition between the states **Ego**, **Jaz** and **Enotnost** when
their internal tension or emotion exceeds defined thresholds. A dialogue module
provides simple interactions illustrating how agents debate absolute,
relative and unified truths.

## Usage

Run the example dialogue from the repository root:

```bash
python -m divine_agents.dialogue
```

## Running Tests

Execute unit tests with:

```bash
python -m pytest -q
```

The tests validate state transitions and the philosophical responses of the
agents.
