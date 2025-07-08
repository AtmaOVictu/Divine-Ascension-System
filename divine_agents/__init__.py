"""Utility package for ontological agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .environment import Environment
from .word import Word
from .frame import Frame

__all__ = ["Agent", "philosophical_dialogue", "Environment", "Word", "Frame"]
