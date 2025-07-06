"""Utilities for creating and interacting with alphabet agents."""

from typing import List
import string

from .agent import Agent
from .dialogue import philosophical_dialogue


def create_alphabet_agents() -> List[Agent]:
    """Return a list of agents representing the alphabet."""
    return [Agent(name=f"Agent_{char}", state="Ego") for char in string.ascii_uppercase]


def alphabet_dialogue() -> List[str]:
    """Run dialogue sequences across the alphabet agents."""
    agents = create_alphabet_agents()
    lines: List[str] = []
    for i in range(len(agents) - 1):
        lines.extend(philosophical_dialogue(agents[i], agents[i + 1]))
    return lines
