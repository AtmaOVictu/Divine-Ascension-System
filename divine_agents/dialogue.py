from __future__ import annotations

from typing import List

from .agent import Agent
from .state import OntoState


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state.name}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state.name}): {agent2.respond('Kaj je resnica?')}")

    # agent1 experiences fear increasing tension
    agent1.update_emotion(0.8)
    agent1_state = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1_state.name}")

    # agent2 experiences joy increasing tension
    agent2.update_emotion(0.6)
    agent2_state = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2_state.name}")

    lines.append(f"{agent1.name} ({agent1.state.name}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state.name}): {agent2.respond('Kaj je resnica?')}")

    return lines
