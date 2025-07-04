"""Convenient exports for the :mod:`divine_agents` package.

This module exposes the main :class:`Agent` class and the
``philosophical_dialogue`` helper so they can be imported directly from
``divine_agents``.
"""

from .agent import Agent  # core ontological agent
from .dialogue import philosophical_dialogue  # dialogue simulation utility

__all__ = ["Agent", "philosophical_dialogue"]

