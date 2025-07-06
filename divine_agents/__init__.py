"""Core package for the Divine Ascension agent system.

This package exposes the :class:`Agent` class and the
:func:`philosophical_dialogue` function used to simulate
interactions between ontological agents.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
