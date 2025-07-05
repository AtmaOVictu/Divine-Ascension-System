"""Package providing agent implementations for the RES system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .pravi import PraviPrimarniAgent, InstancaAgenta, Stance

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "PraviPrimarniAgent",
    "InstancaAgenta",
    "Stance",
]
