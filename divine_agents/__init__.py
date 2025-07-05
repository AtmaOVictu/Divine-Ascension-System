"""Expose divine agent classes."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .codex import (
    CodexAgent,
    CodexSimulation,
    CriticalReflectionAgent,
    LoveHatePhilosophicalAgent,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "CodexAgent",
    "CodexSimulation",
    "CriticalReflectionAgent",
    "LoveHatePhilosophicalAgent",
]
