"""Public API for divine_agents package."""

from .agent import Agent, EmotionDimensionAgent
from .dialogue import philosophical_dialogue, dimension_dialogue

__all__ = [
    "Agent",
    "EmotionDimensionAgent",
    "philosophical_dialogue",
    "dimension_dialogue",
]
