"""Top-level package for divine_agents.

This module exposes the core :class:`Agent` class and the
:func:`philosophical_dialogue` helper for convenience.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
