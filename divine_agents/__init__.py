"""Core package for ontological agents and surreal transitions."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .surreal import surreal_transition, logistic_function

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "surreal_transition",
    "logistic_function",
]

