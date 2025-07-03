
"""Convenience imports and utilities for the ``divine_agents`` package."""

from .agent import Agent
from .dialogue import philosophical_dialogue


def run_tests() -> None:
    """Run the package's unit tests using ``pytest``."""
    import pytest
    pytest.main(["-q"])  # pragma: no cover

__all__ = ["Agent", "philosophical_dialogue", "run_tests"]
