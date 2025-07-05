"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial statements based on current states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reaction to the first exchange
    agent1.update_emotion(0.6, "jeza")
    agent2.update_emotion(0.4, "empatija")

    # Possible transitions triggered by emotion/tension
    previous = agent1.state
    new_state = agent1.transition()
    if new_state != previous:
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    previous = agent2.state
    new_state = agent2.transition()
    if new_state != previous:
        lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    # Second exchange after transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
