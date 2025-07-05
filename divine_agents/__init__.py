"""Utility package for ontological agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .hidden_agent import HiddenModerator

__all__ = ["Agent", "philosophical_dialogue", "HiddenModerator"]
