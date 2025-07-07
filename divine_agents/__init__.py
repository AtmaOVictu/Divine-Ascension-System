"""Expose agent classes and dialogue helpers."""

from .agent import (
    Agent,
    HiddenAgent,
    SimultaneousAgent,
    FuturePredictingAgent,
)
from .dialogue import philosophical_dialogue, extended_dialogue

__all__ = [
    "Agent",
    "HiddenAgent",
    "SimultaneousAgent",
    "FuturePredictingAgent",
    "philosophical_dialogue",
    "extended_dialogue",
]
