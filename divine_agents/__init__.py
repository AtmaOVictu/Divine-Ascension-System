"""Convenience access to package components."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .ontology import validate, oppose, invalidate

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "validate",
    "oppose",
    "invalidate",
]
