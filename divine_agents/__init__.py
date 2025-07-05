"""Ontological agents and utilities for philosophical simulations."""

from .agent import Agent, ReflectiveAgent
from .dialogue import philosophical_dialogue
from .system import MultiAgentSystem

__all__ = [
    "Agent",
    "ReflectiveAgent",
    "MultiAgentSystem",
    "philosophical_dialogue",
]
