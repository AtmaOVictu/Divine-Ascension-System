"""Dialogue utilities for interacting agents."""

from typing import List

from .agent import Agent, AgentState


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial statements on truth
    lines.append(
        f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}"
    )

    # Apply emotions which may drive transitions
    agent1.update_emotion(0.8)
    new_state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1.value}")

    agent2.update_emotion(0.6)
    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2.value}")

    # Second round of answers after transitions
    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}")

    return lines
