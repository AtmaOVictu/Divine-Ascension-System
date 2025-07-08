"""Utilities for ontological agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .language import generate_anagram, create_amalgamation

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "generate_anagram",
    "create_amalgamation",
]
