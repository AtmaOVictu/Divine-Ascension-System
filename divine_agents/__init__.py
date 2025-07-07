"""Public exports for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .insertion import InsertionAgent

__all__ = ["Agent", "philosophical_dialogue", "InsertionAgent"]
