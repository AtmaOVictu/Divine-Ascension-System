"""Ontological agent system with clustering capabilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .cluster import AgentCluster

__all__ = ["Agent", "AgentCluster", "philosophical_dialogue"]
