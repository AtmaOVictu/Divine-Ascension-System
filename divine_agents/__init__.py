"""Public API for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue, philosophical_debate

__all__ = ["Agent", "philosophical_dialogue", "philosophical_debate"]
