"""Package exposing agent classes and dialogue utilities."""

from .agent import Agent
from .optimized_agent import OptimizedAgent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "OptimizedAgent", "philosophical_dialogue"]
