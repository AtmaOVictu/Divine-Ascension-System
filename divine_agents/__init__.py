"""Public interface for the divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .shumnik import (
    Shumnik,
    tension_effect,
    reflection_effect,
    emotional_balance_effect,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Shumnik",
    "tension_effect",
    "reflection_effect",
    "emotional_balance_effect",
]
