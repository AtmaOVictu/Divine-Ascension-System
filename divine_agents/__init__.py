"""Divine Agents package."""

from .agent import Agent
from .emotional_agent import EmotionalAgent
from .dialogue import philosophical_dialogue
from .debate import dynamic_philosophical_debate

__all__ = [
    "Agent",
    "EmotionalAgent",
    "philosophical_dialogue",
    "dynamic_philosophical_debate",
]
