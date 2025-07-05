"""Package exposing divine agent types."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .extensions import (
    SimulationPhase,
    LearningAgent,
    InteractionAgent,
    FreeWillAgent,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "SimulationPhase",
    "LearningAgent",
    "InteractionAgent",
    "FreeWillAgent",
]

