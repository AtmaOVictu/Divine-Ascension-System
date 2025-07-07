"""Expose agent classes and dialogue helpers."""

from .agent import Agent
from .advanced_agents import (
    ReasonAgent,
    InterpolationAgent,
    IntercontinentalizationAgent,
)
from .dialogue import philosophical_dialogue, extended_dialogue

__all__ = [
    "Agent",
    "ReasonAgent",
    "InterpolationAgent",
    "IntercontinentalizationAgent",
    "philosophical_dialogue",
    "extended_dialogue",
]
