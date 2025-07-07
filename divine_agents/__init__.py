"""Top-level package for divine agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .krak_manager import Krak, KrakManager, GitHubHandler, VercelHandler

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Krak",
    "KrakManager",
    "GitHubHandler",
    "VercelHandler",
]
