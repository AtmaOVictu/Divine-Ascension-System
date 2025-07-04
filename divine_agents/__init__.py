"""Divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .res_phases import RESPhase, create_res_phases

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "RESPhase",
    "create_res_phases",
]
