"""Divine Agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .box import (
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
