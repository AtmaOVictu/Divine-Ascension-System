"""Utility package for ontological agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .multi_dim_agent import MultiDimensionalMoralAgent

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "MultiDimensionalMoralAgent",
]
