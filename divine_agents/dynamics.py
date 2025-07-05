# Utilities for SODO/LIHO based tension dynamics
from typing import List
from .agent import Agent


def sodo_liho_delta(step: int, k_sodo: float = -0.2, k_liho: float = 0.5) -> float:
    """Return tension delta for a given step using SODO/LIHO logic."""
    return k_sodo if step % 2 == 0 else 2 * k_liho


def dynamic_philosophical_dialogue(agent1: Agent, agent2: Agent, steps: int = 3) -> List[str]:
    """Simulate a dialogue with tension changes following SODO/LIHO steps."""
    lines: List[str] = []
    for step in range(1, steps + 1):
        # Each agent responds according to its current state
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Apply SODO/LIHO tension updates
        delta = sodo_liho_delta(step)
        agent1.update_tension(agent1.tension + delta)
        agent2.update_tension(agent2.tension + delta)

        # Emotions follow magnitude of change
        agent1.update_emotion(abs(delta))
        agent2.update_emotion(abs(delta))

        # Attempt state transitions
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
