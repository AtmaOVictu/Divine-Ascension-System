"""Divine Agents package.

This package provides a small framework for simulating ontological agents and
their philosophical dialogues.  Key classes and functions are exposed for easy
import.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
