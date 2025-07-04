"""Public interface for the ``divine_agents`` package."""

from .agent import Agent, Emotion
from .dialogue import philosophical_dialogue
from .external import ExternalIntegrationLayer

__all__ = [
    "Agent",
    "Emotion",
    "philosophical_dialogue",
    "ExternalIntegrationLayer",
]
