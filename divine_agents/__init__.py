"""Framework for modelling ontological agents and their dialogues.

This package contains simple classes for agents that transition between
philosophical states (``Ego``, ``Jaz`` and ``Enotnost``) based on
emotion and tension levels. It also provides utilities for generating
dialogue between agents as they reason about absolute, relative and
unified truths.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
