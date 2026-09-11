"""Core package for the Divine Agents system."""

from .agent import (
    Agent,
    BasicAgent,
    IntermediateAgent,
    MasterAgent,
    HighMasterAgent,
    GodLikeAgent,
)
from .dialogue import philosophical_dialogue

__all__ = [
    "Agent",
    "BasicAgent",
    "IntermediateAgent",
    "MasterAgent",
    "HighMasterAgent",
    "GodLikeAgent",
    "philosophical_dialogue",
]
