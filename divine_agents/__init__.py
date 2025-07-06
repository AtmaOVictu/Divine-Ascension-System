"""Public interface for divine agent simulations."""

from .agent import Agent
from .dialogue import philosophical_dialogue, dynamic_debate

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "dynamic_debate",
]

