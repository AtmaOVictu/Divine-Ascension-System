"""Public interface for divine_agents package."""

from .agent import Agent, SelfDeceptionAgent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "SelfDeceptionAgent", "philosophical_dialogue"]
