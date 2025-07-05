"""Public interface for divine agent utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .conversation import debate

__all__ = ["Agent", "philosophical_dialogue", "debate"]
