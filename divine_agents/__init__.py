"""Dynamic ontological agents and dialogue utilities.

This package provides the :class:`Agent` class for representing agents that
transition between philosophical states based on emotion and tension, and the
:func:`philosophical_dialogue` helper for simulating conversations.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
