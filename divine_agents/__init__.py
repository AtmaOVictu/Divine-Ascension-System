from .agent import Agent
from .dialogue import philosophical_dialogue
from .emotional_agent import EmotionalAgent
from .thresholds import SymbolicBox, EmotionalBox

__all__ = [
    "Agent",
    "EmotionalAgent",
    "SymbolicBox",
    "EmotionalBox",
    "philosophical_dialogue",
]
