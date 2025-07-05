"""Divine agents package exposing core components."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .interface import Kapacitor, OkenskoSporocilo, interactive_session

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Kapacitor",
    "OkenskoSporocilo",
    "interactive_session",
]

