"""Top-level package for divine agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .conversation import Conversation

__all__ = ["Agent", "philosophical_dialogue", "Conversation"]
