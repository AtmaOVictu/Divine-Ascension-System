"""Utilities and agent definitions for philosophical simulations."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .utils import logistic_growth, logarithmic_progress

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "logistic_growth",
    "logarithmic_progress",
]
