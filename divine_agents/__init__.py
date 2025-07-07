"""Public interface for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .cluster import Cluster

__all__ = ["Agent", "philosophical_dialogue", "Cluster"]

