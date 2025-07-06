"""Divine agent system with ontological transitions."""
from .agent import Agent
from .dialogue import philosophical_dialogue
from .alphabet import create_alphabet_agents, alphabet_dialogue

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "create_alphabet_agents",
    "alphabet_dialogue",
]
