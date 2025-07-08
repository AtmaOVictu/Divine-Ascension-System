"""Ontological agent framework."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .history import History
from .timeline import Timeline
from .space import Space
from .language import Language

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "History",
    "Timeline",
    "Space",
    "Language",
]
