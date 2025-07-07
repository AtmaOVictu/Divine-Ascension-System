"""Divine agents package exposing core classes."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .emotion import Emotion

__all__ = ["Agent", "Emotion", "philosophical_dialogue"]
