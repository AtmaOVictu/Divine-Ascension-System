from .agent import Agent
from .dialogue import philosophical_dialogue
from .transformation import (
    logistic_function,
    surreal_transition,
    DEFAULT_K_VALUES,
    DEFAULT_C_VALUES,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "logistic_function",
    "surreal_transition",
    "DEFAULT_K_VALUES",
    "DEFAULT_C_VALUES",
]
