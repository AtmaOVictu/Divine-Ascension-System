"""Utilities to create and interact with alphabet agents."""
from __future__ import annotations
import string
from typing import List
from .agent import Agent
from .dialogue import philosophical_dialogue


def create_alphabet_agents() -> List[Agent]:
    """Return agents representing each letter of the alphabet."""
    return [Agent(char) for char in string.ascii_uppercase]


def alphabet_dialogue() -> List[str]:
    """Simulate dialogues sequentially between alphabet agents."""
    agents = create_alphabet_agents()
    lines: List[str] = []
    for first, second in zip(agents, agents[1:]):
        lines.extend(philosophical_dialogue(first, second))
    return lines
