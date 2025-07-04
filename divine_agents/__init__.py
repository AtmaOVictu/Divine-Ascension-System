"""Exposes main classes and functions for the Divine Ascension system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .phases import RESPhase, create_res_phases

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "RESPhase",
    "create_res_phases",
]
