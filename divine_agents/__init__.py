"""Utility package for ontological agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .philosophy import parse_philosophical_statement, analyze_concept
from .emotions import simulate_emotional_tension, calculate_tension_change
from .memory import Memory

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "parse_philosophical_statement",
    "analyze_concept",
    "simulate_emotional_tension",
    "calculate_tension_change",
    "Memory",
]
