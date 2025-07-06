"""Alphabet agent utilities for ontological simulations."""
import string
from typing import List
from .agent import Agent
from .dialogue import philosophical_dialogue


def create_alphabet_agents() -> List[Agent]:
    """Return a list of agents, one for each uppercase letter."""
    return [Agent(name=f"Agent_{char}") for char in string.ascii_uppercase]


def run_alphabet_dialogues() -> List[str]:
    """Run dialogues between sequential alphabet agents."""
    agents = create_alphabet_agents()
    lines: List[str] = []
    for first, second in zip(agents[:-1], agents[1:]):
        lines.extend(philosophical_dialogue(first, second))
    return lines
