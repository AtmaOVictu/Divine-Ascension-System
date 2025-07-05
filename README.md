# Divine-Ascension-System

This repository contains a simple framework for philosophical agents.
Agents transition between ontological states **Ego**, **Jaz**, and **Enotnost**
based on tension and emotion. Dialogues demonstrate how agents reason about
absolute, relative, and unified truths.

## Math Agents

A `MathAgent` subclass adds symbolic mathematics capabilities using
[SymPy](https://www.sympy.org/). Special Slovene characters (Š, Č, Ž, Đ) are
used as symbolic variables for constructing and manipulating expressions.

## Running tests

Tests are written with `unittest` and can be executed via:

```bash
python -m pytest -q
```

The math related tests require `sympy` to be installed in your environment.
