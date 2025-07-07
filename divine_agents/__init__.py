from .agent import Agent
from .dialogue import philosophical_dialogue
from .box import (
    SymbolicBox,
    SelfBoxedAgent,
    RecursiveTaskBox,
    RecursiveSelfReflectionAgent,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "SymbolicBox",
    "SelfBoxedAgent",
    "RecursiveTaskBox",
    "RecursiveSelfReflectionAgent",
]

