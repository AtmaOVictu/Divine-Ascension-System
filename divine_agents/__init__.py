"""Convenience imports for the :mod:`divine_agents` package.

This package contains agent classes and dialogue helpers used to simulate
philosophical conversations. ``Agent`` and ``philosophical_dialogue`` are
re-exported here for easier access.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
