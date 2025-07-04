"""Core package for divine agent simulations.

This package exposes the :class:`Agent` class and the
``philosophical_dialogue`` function for convenient imports.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]

