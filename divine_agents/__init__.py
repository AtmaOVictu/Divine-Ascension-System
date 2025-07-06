"""Ontological agents package."""

from .agent import Agent
from .dynamic_agent import DynamicAgent
from .dialogue import philosophical_dialogue
from .system import dinamicka_inicializacija, reorganizacija_sistema

__all__ = [
    "Agent",
    "DynamicAgent",
    "philosophical_dialogue",
    "dinamicka_inicializacija",
    "reorganizacija_sistema",
]
