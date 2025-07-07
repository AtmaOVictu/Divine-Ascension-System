"""Utility package for ontological agent simulations."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .symbolic_box import (
    SymbolicBox,
    initiate_task_with_box,
    process_task_with_box,
    resolve_task_with_box,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "SymbolicBox",
    "initiate_task_with_box",
    "process_task_with_box",
    "resolve_task_with_box",
]
