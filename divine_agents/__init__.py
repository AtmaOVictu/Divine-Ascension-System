"""Package exposing agent classes and dialogue helpers."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .omnipotent_agent import OmnipotentAgent

__all__ = ["Agent", "philosophical_dialogue", "OmnipotentAgent"]
