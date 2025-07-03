"""Divine Agents package providing ontology-based agent classes."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .syntax import SyntaxAgent, create_syntax_agents

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "SyntaxAgent",
    "create_syntax_agents",
]
