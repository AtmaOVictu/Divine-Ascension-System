"""Divine agent framework."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .primary import PraviPrimarniAgent, InstancaAgenta, Stance

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "PraviPrimarniAgent",
    "InstancaAgenta",
    "Stance",
]
