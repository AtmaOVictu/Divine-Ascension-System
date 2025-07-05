from __future__ import annotations

from typing import List, Tuple

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a brief philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond()}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond()}")

    # Agents react emotionally to the first exchange
    agent1.feel(anger=0.6)
    agent1.update_state()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state.value}")

    agent2.feel(joy=0.7)
    agent2.update_state()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state.value}")

    lines.append(f"{agent1.name}: {agent1.respond()}")
    lines.append(f"{agent2.name}: {agent2.respond()}")
    return lines


def dialogue_step(agent1: Agent, agent2: Agent) -> Tuple[str, str]:
    """Execute a single exchange and return responses."""
    agent1.update_state()
    agent2.update_state()
    return agent1.respond(), agent2.respond()
