"""Dynamic agent-based ontology package.

This package provides the :class:`Agent` class and supporting dialogue
utilities to simulate ontological state transitions influenced by
emotions and tension.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]

