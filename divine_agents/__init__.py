"""Public API for divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue, reflective_dialogue
from .dictionary import OntologicalDictionary
from .writer import WritingAgent

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "reflective_dialogue",
    "OntologicalDictionary",
    "WritingAgent",
]
