"""Package exposing core agent classes for ontological simulations."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .dimension_agent import EmotionDimensionAgent

__all__ = ["Agent", "philosophical_dialogue", "EmotionDimensionAgent"]
