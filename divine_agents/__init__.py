"""Core module for the Divine Ascension ontological agents."""

from .agent import Agent, State, Emotions
from .dialogue import philosophical_dialogue, dialogue_step

__all__ = [
    "Agent",
    "State",
    "Emotions",
    "philosophical_dialogue",
    "dialogue_step",
]
