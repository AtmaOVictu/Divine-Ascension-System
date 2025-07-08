"""Ontology-based agent system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .utils import (
    Memory,
    parse_philosophical_statement,
    simulate_emotional_tension,
    handle_complex_query,
    self_reflection,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Memory",
    "parse_philosophical_statement",
    "simulate_emotional_tension",
    "handle_complex_query",
    "self_reflection",
]
