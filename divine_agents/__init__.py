"""Convenience imports for the divine_agents package."""

from .agent import Agent, OracleAgent
from .dialogue import philosophical_dialogue, oracle_dialogue

__all__ = [
    "Agent",
    "OracleAgent",
    "philosophical_dialogue",
    "oracle_dialogue",
]
