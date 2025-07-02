"""Public exports for the divine_agents package."""

from .agent import Agent, AgentWithBin
from .dialogue import philosophical_dialogue
from .bin_ui import TrashBinUI
from .trash_bin import TrashBin

__all__ = [
    "Agent",
    "AgentWithBin",
    "TrashBin",
    "philosophical_dialogue",
    "TrashBinUI",
]
