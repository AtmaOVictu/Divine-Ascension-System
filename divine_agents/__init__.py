"""Divine agent package."""

from .agent import Agent
from .dynamic_agent import DynamicAgent, dinamicka_inicializacija
from .dialogue import philosophical_dialogue

__all__ = [
    "Agent",
    "DynamicAgent",
    "dinamicka_inicializacija",
    "philosophical_dialogue",
]
