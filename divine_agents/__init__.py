"""Convenience imports for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .symbols import SYMBOLS, Symbol, get_symbol_description

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "SYMBOLS",
    "get_symbol_description",
    "Symbol",
]
