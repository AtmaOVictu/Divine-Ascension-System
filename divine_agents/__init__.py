"""Convenience imports for the Divine Agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue, dynamic_philosophical_dialogue
from .emotion import Emotion

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "dynamic_philosophical_dialogue",
    "Emotion",
]
