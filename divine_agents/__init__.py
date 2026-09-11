"""Public package interface."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .interface import run_interface, AgentFrame

__all__ = ["Agent", "philosophical_dialogue", "run_interface", "AgentFrame"]
