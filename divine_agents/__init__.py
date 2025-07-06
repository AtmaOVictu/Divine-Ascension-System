"""Expose package functionality."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .alphabet_system import create_alphabet_agents, transition_all, alphabet_dialogue

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "create_alphabet_agents",
    "transition_all",
    "alphabet_dialogue",
]
