"""Exposes the main public API for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
__version__ = "0.1.0"
