"""Utility package exposing ontological agents and dialogues."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .dynamic_dialogue import dynamic_philosophical_debate

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "dynamic_philosophical_debate",
]
