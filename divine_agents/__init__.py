"""Divine agent package exposing main classes and utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .conversation import emotional_conversation

__all__ = ["Agent", "philosophical_dialogue", "emotional_conversation"]
