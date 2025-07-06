"""Expose package components for external use."""
from .agent import Agent
from .dialogue import philosophical_dialogue
from .modules import AwarenessModule, OppositionModule, TransitionModule
from .containers import AwarenessContainer, OppositionContainer, TransitionContainer

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "AwarenessModule",
    "OppositionModule",
    "TransitionModule",
    "AwarenessContainer",
    "OppositionContainer",
    "TransitionContainer",
]
