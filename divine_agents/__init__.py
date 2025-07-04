"""Divine Ascension agent modules."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .body_soul_spirit import BodyAgent, SoulAgent, SpiritAgent

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "BodyAgent",
    "SoulAgent",
    "SpiritAgent",
]
