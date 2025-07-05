"""Divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .math_model import transition_score, transition_allowed, error_value

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "transition_score",
    "transition_allowed",
    "error_value",
]
