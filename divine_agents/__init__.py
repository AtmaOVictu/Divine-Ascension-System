"""Public package interface for Divine Agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .conversation import dynamic_conversation

__all__ = ["Agent", "philosophical_dialogue", "dynamic_conversation"]
