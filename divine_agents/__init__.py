"""Public interface for divine agents package."""

from .agent import Agent, State
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "State", "philosophical_dialogue"]
