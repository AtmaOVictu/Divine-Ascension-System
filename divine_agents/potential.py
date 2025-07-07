"""Utilities for representing agent state history in hex form."""

from typing import List


def hexdump_potential(states: List[str]) -> str:
    """Return a hex representation of the given state sequence."""
    return " ".join(s.encode("utf-8").hex() for s in states)
