"""Public package exports for divine agents."""

from .agent import Agent
from .emotional_agent import EmotionalAgent
from .dialogue import philosophical_dialogue, emotional_dialogue

__all__ = [
    "Agent",
    "EmotionalAgent",
    "philosophical_dialogue",
    "emotional_dialogue",
]

