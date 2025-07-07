"""Package for philosophical agent simulations."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .cluster import Cluster

__all__ = ["Agent", "philosophical_dialogue", "Cluster"]
