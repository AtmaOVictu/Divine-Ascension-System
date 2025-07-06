"""Simple ontological agent framework."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .ontological import OntologicalAgent, OppositeAgent

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "OntologicalAgent",
    "OppositeAgent",
]
