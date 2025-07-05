from .agent import Agent
from .dialogue import philosophical_dialogue
from .dynamic import (
    DynamicAgent,
    MultiAgentSystem,
    biological_transition,
    social_transition,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "DynamicAgent",
    "MultiAgentSystem",
    "biological_transition",
    "social_transition",
]
