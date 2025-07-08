"""Convenience imports for the divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .interaction import EmotionalNetwork
from .karma import Karma

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "EmotionalNetwork",
    "Karma",
    # Visualization utilities require matplotlib, which may not be available.
]
