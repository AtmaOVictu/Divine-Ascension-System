"""Convenience exports for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .interpolation import interpolate_differences

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "interpolate_differences",
]
