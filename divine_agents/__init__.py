"""Divine Agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .tension import tension_keywords, tension_stage

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "tension_keywords",
    "tension_stage",
]
