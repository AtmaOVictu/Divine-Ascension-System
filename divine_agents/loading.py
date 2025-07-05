from typing import List
import time


def simulate_loading_screen(agent_name: str, max_cycles: int = 5) -> List[str]:
    """Return lines representing a loading screen simulation."""
    lines = []
    for cycle in range(max_cycles):
        lines.append(f"Loading: {cycle + 1}/{max_cycles} - {agent_name}")
        time.sleep(0.1)
        if cycle == max_cycles // 2:
            lines.append(f"Agent {agent_name} je dosegel polovico nalog.")
    lines.append(f"Loading Screen končan za {agent_name}.")
    return lines
