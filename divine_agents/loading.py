"""Utility functions for simulating loading screens."""

from typing import List


def simulate_loading_screen(agent_name: str, max_cycles: int = 10) -> List[str]:
    """Return messages representing a simulated loading screen."""
    progress = []
    for cycle in range(1, max_cycles + 1):
        progress.append(f"Loading: {cycle}/{max_cycles} - {agent_name}")
    progress.append(f"Loading Screen končan za {agent_name}.")
    return progress
