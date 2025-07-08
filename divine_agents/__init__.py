"""Convenience imports for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .emotions import Emotion
from .karma import Karma
from .analytics import track_emotional_trends

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Emotion",
    "Karma",
    "track_emotional_trends",
]
