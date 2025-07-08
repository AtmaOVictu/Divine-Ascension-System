"""Ontological agent package."""

from .agent import Agent
from .rl_agent import RLAgent, ReflectiveAgent, reflective_dialogue
from .dialogue import philosophical_dialogue

__all__ = [
    "Agent",
    "RLAgent",
    "ReflectiveAgent",
    "philosophical_dialogue",
    "reflective_dialogue",
]
