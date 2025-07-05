"""Public API for the divine_agents package."""

from .agent import Agent, SecondaryAgent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "SecondaryAgent", "philosophical_dialogue"]
