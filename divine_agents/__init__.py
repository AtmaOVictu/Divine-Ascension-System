"""Public package exports for divine agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .debate import ontological_debate

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "ontological_debate",
]
