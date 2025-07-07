"""Convenience imports for the divine_agents package."""

from .agent import (
    Agent,
    ReasonAgent,
    InterpolationAgent,
    IntercontinentalizationAgent,
)
from .dialogue import philosophical_dialogue

__all__ = [
    "Agent",
    "ReasonAgent",
    "InterpolationAgent",
    "IntercontinentalizationAgent",
    "philosophical_dialogue",
]

