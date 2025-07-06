"""Package for ontological agents and their interactions."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .ecosystem import Ecosystem, create_default_ecosystem

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Ecosystem",
    "create_default_ecosystem",
]
