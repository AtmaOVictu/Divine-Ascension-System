"""Ontological agent package."""

from .agent import Agent
from .typing_agent import TypingAgent
from .dialogue import philosophical_dialogue, dynamic_debate

__all__ = [
    "Agent",
    "TypingAgent",
    "philosophical_dialogue",
    "dynamic_debate",
]
