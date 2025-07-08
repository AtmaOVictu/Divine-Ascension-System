"""Package exposing ontological agent utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .ontoscience_box import (
    OntoscienceBox,
    initialize_agents,
    recursive_evolution,
    transition_function,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "OntoscienceBox",
    "initialize_agents",
    "recursive_evolution",
    "transition_function",
]
