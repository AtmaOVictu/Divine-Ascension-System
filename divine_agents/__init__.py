"""Expose agent classes and dialogue helpers."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .dynamic_agent import DynamicAgent, MultiAgentSystem

__all__ = [
    "Agent",
    "DynamicAgent",
    "MultiAgentSystem",
    "philosophical_dialogue",
]
