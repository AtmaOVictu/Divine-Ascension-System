"""Public interface for divine_agents package."""

from .agent import Agent
from .dialogue import DialogueManager, philosophical_dialogue

__all__ = ["Agent", "DialogueManager", "philosophical_dialogue"]
