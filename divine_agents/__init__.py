"""Utilities for the Divine Ascension agent system."""

from .agent import Agent
from .companions import ShadowAgent, AngelAgent
from .dialogue import philosophical_dialogue

__all__ = [
    "Agent",
    "ShadowAgent",
    "AngelAgent",
    "philosophical_dialogue",
]
