"""Divine Agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .time_utils import get_local_time, get_time_from_ip

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "get_local_time",
    "get_time_from_ip",
]
