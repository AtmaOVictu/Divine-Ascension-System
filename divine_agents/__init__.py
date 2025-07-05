"""Public API for the :mod:`divine_agents` package."""

from .agent import Agent, AgentState
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "AgentState", "philosophical_dialogue"]
