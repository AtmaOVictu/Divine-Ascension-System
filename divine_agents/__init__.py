"""Divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue, deep_thought_dialogue
from .ontology import deep_thought_key, deep_thought_language

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "deep_thought_dialogue",
    "deep_thought_key",
    "deep_thought_language",
]
