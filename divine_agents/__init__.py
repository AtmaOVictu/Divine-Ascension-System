"""Public exports for the Divine Ascension agent system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .knowledge import KnowledgeBase, AutoLearningSystem

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "KnowledgeBase",
    "AutoLearningSystem",
]
