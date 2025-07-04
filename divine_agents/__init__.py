"""Top-level package for Divine Ascension agents."""

from .agent import Agent, PhaseModifier
from .dialogue import philosophical_dialogue
from .phase import RESPhase, generate_phases

__all__ = [
    "Agent",
    "PhaseModifier",
    "RESPhase",
    "generate_phases",
    "philosophical_dialogue",
]
