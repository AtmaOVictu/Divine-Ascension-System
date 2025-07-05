"""Expose main classes and utilities for divine agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .extensions import (
    SimulationPhase,
    LearningAgent,
    InteractionAgent,
    FreeWillAgent,
    visualize_agent,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "SimulationPhase",
    "LearningAgent",
    "InteractionAgent",
    "FreeWillAgent",
    "visualize_agent",
]

