"""Divine Agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .transition import TransitionSystem

__all__ = ["Agent", "philosophical_dialogue", "TransitionSystem"]


def run_tests() -> None:
    """Run package unit tests using pytest."""
    import pytest
    pytest.main(["-q"])
