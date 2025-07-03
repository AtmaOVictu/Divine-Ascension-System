from .agent import Agent
from .dialogue import philosophical_dialogue
from .interpolation import (
    compute_differences,
    linear_interpolation,
    quadratic_interpolation,
)
__all__ = [
    "Agent",
    "philosophical_dialogue",
    "compute_differences",
    "linear_interpolation",
    "quadratic_interpolation",
]
