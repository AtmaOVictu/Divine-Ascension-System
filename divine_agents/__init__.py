"""Public package interface for divine_agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue, philosophical_debate

__all__ = ["Agent", "philosophical_dialogue", "philosophical_debate"]

