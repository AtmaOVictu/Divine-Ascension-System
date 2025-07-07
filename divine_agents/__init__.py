"""Package exposing agent simulation utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .xp import XPSystem

__all__ = ["Agent", "XPSystem", "philosophical_dialogue"]
