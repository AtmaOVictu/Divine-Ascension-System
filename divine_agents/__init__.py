"""Top-level package for divine_agents.

Exposes main API objects for convenience.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
