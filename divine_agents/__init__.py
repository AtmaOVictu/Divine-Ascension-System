"""Divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .emotion import EmotionalAgent, EmotionalBox, MainTaskAgent

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "EmotionalAgent",
    "EmotionalBox",
    "MainTaskAgent",
]
