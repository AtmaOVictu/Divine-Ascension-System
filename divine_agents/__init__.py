"""Public package interface for divine agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .transformer import EmotionTransformer

__all__ = ["Agent", "philosophical_dialogue", "EmotionTransformer"]
