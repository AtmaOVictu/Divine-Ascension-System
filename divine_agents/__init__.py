"""Divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .math_music import evaluate_expression, generate_scale

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "evaluate_expression",
    "generate_scale",
]
