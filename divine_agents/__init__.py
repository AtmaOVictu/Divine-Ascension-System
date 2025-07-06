"""Top-level package for divine agent system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .meta import MetaAgent, RandomCodeTester

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "MetaAgent",
    "RandomCodeTester",
]
