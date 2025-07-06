"""Divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .utils import evaluate_equation, generate_major_scale

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "evaluate_equation",
    "generate_major_scale",
]
