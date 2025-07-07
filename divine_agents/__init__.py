"""Ontological agents package."""

from .agent import Agent
from .selfaware_agent import SelfAwareAgent
from .dialogue import philosophical_dialogue, self_aware_dialogue

__all__ = [
    "Agent",
    "SelfAwareAgent",
    "philosophical_dialogue",
    "self_aware_dialogue",
]
