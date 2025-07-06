"""Ontological agent framework."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .gui import SoulCompassApp

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "SoulCompassApp",
]
