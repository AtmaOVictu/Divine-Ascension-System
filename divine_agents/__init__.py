"""Utility module exposing agent classes and dialogue helpers."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .moderator import HiddenModerator, LatentAgent

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "HiddenModerator",
    "LatentAgent",
]
