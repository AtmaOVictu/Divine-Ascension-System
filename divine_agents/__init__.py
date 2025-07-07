"""Package exposing agent logic and utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .tasks import get_weather, send_email

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "get_weather",
    "send_email",
]
