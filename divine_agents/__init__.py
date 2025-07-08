"""Divine agents package exposing agent utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .superpositional import SuperpositionalAgent
from .hybrid_dialogue import hybrid_dialogue

__all__ = [
    "Agent",
    "SuperpositionalAgent",
    "philosophical_dialogue",
    "hybrid_dialogue",
]
