from .agent import Agent
from .dialogue import philosophical_dialogue
from .memory import Memory, parse_philosophical_statement

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Memory",
    "parse_philosophical_statement",
]
