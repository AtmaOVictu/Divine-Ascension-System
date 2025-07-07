"""Public package API for :mod:`divine_agents`."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .tasks import get_weather, send_email

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "get_weather",
    "send_email",
]
