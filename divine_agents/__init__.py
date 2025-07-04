"""Divine agent modules for ontological simulations."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .word_agent import WordAgent
from .library import create_word_library

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "WordAgent",
    "create_word_library",
]
