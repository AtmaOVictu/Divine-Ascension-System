"""Ontological agent framework for philosophical dialogues."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .cluster import AgentCluster

__all__ = ["Agent", "philosophical_dialogue", "AgentCluster"]
