"""Top-level package for Divine Agents.

This package exports :class:`Agent` for ontological state management and
:func:`philosophical_dialogue` to simulate conversations between agents.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
