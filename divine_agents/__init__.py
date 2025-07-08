"""Public package interface for Divine Agents."""

from .agent import Agent
from .philosophy import State, PHILOSOPHICAL_TRUTHS
from .dialogue import philosophical_dialogue

__all__ = [
    "Agent",
    "State",
    "PHILOSOPHICAL_TRUTHS",
    "philosophical_dialogue",
]
