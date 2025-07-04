"""Divine Agents package with ontological agents and utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .translator import Translator, EternalAnalysis

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Translator",
    "EternalAnalysis",
]
