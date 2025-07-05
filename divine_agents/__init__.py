"""Divine Agents package providing agent models and dialogues."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .moderator import HiddenModerator

__all__ = ["Agent", "philosophical_dialogue", "HiddenModerator"]
