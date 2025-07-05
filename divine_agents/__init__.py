"""Init for divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .emotion_dimension import EmotionDimensionAgent

__all__ = ["Agent", "philosophical_dialogue", "EmotionDimensionAgent"]
