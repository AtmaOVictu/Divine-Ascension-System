"""Ontological agent framework for philosophical dialogues.

This package defines the Agent class and utilities for simulating
philosophical conversations where agents transition between Ego, Jaz,
and Enotnost states based on emotions and tension."""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
