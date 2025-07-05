"""Convenience imports for the divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .advanced_agents import LearningAgent, InteractionAgent, FreeWillAgent
from .simulation import SimulationPhase
try:  # Optional dependency
    from .visualization import visualize_agent
except Exception:  # pragma: no cover - visualization is optional
    visualize_agent = None

__all__ = [
    "Agent",
    "LearningAgent",
    "InteractionAgent",
    "FreeWillAgent",
    "SimulationPhase",
    "philosophical_dialogue",
    "visualize_agent",
]
