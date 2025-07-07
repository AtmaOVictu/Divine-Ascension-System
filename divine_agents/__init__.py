"""Package exposing ontological agent utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .cluster import Cluster

__all__ = ["Agent", "philosophical_dialogue", "Cluster"]
