"""Helper module exporting main components."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .interactive import Kapacitor

__all__ = ["Agent", "philosophical_dialogue", "Kapacitor"]
