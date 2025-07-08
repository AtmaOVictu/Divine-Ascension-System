"""Public API for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .memory import Memory
from .philosophy_utils import (
    parse_philosophical_statement,
    simulate_emotional_tension,
    self_reflection,
)

__all__ = [
    "Agent",
    "Memory",
    "philosophical_dialogue",
    "parse_philosophical_statement",
    "simulate_emotional_tension",
    "self_reflection",
]

