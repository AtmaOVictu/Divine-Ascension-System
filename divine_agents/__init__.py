"""Package exposing agent-related classes and helpers."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .conversation import Conversation

__all__ = ["Agent", "philosophical_dialogue", "Conversation"]
