"""Utilities for generating rhythmic representations of agent states."""
from typing import List
from .agent import Agent

STATE_RHYTHM = {
    "Ego": "E-G-O",
    "Jaz": "J-A-Z",
    "Enotnost": "E-N-O-T-N-O",
}

def state_rhythm(state: str) -> str:
    """Return the rhythmic representation of a single state."""
    return STATE_RHYTHM.get(state, "")


def generate_rhythm_sequence(agent: Agent) -> List[str]:
    """Return the rhythm sequence for an agent's history of states."""
    return [state_rhythm(st) for st in agent.history]
