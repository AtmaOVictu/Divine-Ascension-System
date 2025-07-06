# Agent Specification

This document describes the behaviour of ontological agents used in the **Divine-Ascension-System**.

## States
- **Ego**: Truth is absolute and independent of others.
- **Jaz**: Truth is relative and shaped by relationships.
- **Enotnost**: All truths are one, interconnected.

Agents store their current state and maintain a history of states visited during execution.

## Transitions
Agents transition when either of the following thresholds is exceeded:

- **Tension** > `0.7`
- **Emotion** > `0.5`

When a transition is triggered:
- `Ego` → `Jaz`
- `Jaz` → `Enotnost`
- `Enotnost` remains unchanged.

The new state is appended to the agent's history.

## Module Overview
- `divine_agents/agent.py` – core agent implementation and transition logic.
- `divine_agents/dialogue.py` – utilities for simulating philosophical dialogues.
- `tests/` – unit tests validating transitions and responses.

## Running Tests
Use `python -m unittest discover -s tests` from the project root to execute all tests.
