"""Ontological agent package."""

from .agent import (
    Agent,
    SimulationPhase,
    LearningAgent,
    InteractionAgent,
    FreeWillAgent,
)
from .dialogue import philosophical_dialogue

try:  # matplotlib might be unavailable in minimal environments
    from .visualization import visualize_agent
except Exception:  # pragma: no cover - optional dependency
    visualize_agent = None

__all__ = [
    "Agent",
    "SimulationPhase",
    "LearningAgent",
    "InteractionAgent",
    "FreeWillAgent",
    "philosophical_dialogue",
    "visualize_agent",
]
