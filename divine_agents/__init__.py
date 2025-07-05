"""Expose public API for the divine agents package."""

from .agent import Agent, Emotions, State, Debate
from .dialogue import philosophical_dialogue

__all__ = [
    "Agent",
    "Emotions",
    "State",
    "Debate",
    "philosophical_dialogue",
]

