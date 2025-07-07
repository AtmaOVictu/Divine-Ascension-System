"""Core package for the Divine Ascension agent framework.

This package provides tools to create agents and simulate philosophical
conversations between them. Each agent can transition between ontological
states based on emotions and tension levels.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
