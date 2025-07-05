"""Public exports for the divine_agents package."""

from .agent import Agent
from .paradox import ParadoxicalAgent
from .dialogue import philosophical_dialogue, paradoxical_dialogue

__all__ = [
    "Agent",
    "ParadoxicalAgent",
    "philosophical_dialogue",
    "paradoxical_dialogue",
]
