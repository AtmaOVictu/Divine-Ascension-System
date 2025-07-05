"""Convenience imports for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .enums import EmotionType, OntologicalState

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "EmotionType",
    "OntologicalState",
]
