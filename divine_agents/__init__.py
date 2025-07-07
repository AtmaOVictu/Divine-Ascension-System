"""Agent-based philosophical system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .reflective_agent import ReflectiveAgent
from .dynamic_dialogue import dynamic_philosophical_dialogue

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "ReflectiveAgent",
    "dynamic_philosophical_dialogue",
]
