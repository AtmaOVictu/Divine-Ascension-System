"""Divine agent package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .memory import Memory
from .utils import (
    parse_philosophical_statement,
    simulate_emotional_tension,
    handle_complex_query,
    handle_parallel_query,
    augment_knowledge_base,
    self_reflection,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Memory",
    "parse_philosophical_statement",
    "simulate_emotional_tension",
    "handle_complex_query",
    "handle_parallel_query",
    "augment_knowledge_base",
    "self_reflection",
]
