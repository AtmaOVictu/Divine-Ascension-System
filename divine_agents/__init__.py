"""Ontological agent system utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .emotional_contagion import EmotionalContagion
from .history import AgentWithHistory

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "EmotionalContagion",
    "AgentWithHistory",
]
