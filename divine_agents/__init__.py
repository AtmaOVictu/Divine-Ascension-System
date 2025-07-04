"""Divine Agents package.

This package offers ontological agents capable of transitioning between
philosophical states (Ego, Jaz, Enotnost) based on emotion and tension.
It exposes the :class:`Agent` class and dialogue helpers for simulating
philosophical debates.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
__version__ = "0.1.0"
