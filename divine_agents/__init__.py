"""Divine agent framework for ontological dialogues."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .network import Module, AgentNetwork

__all__ = ["Agent", "philosophical_dialogue", "Module", "AgentNetwork"]
