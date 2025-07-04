"""Utility package for ontological agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .simulation import debug_cycle

__all__ = ["Agent", "philosophical_dialogue", "debug_cycle"]
