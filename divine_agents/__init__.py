"""Utility package for simulating philosophical agents.

This package provides the :class:`Agent` class and the :func:`philosophical_dialogue` helper
for composing dialogues. It exposes high-level imports so consumers can simply do
``from divine_agents import Agent, philosophical_dialogue``.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
