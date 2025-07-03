"""Dialogue utilities for agent conversations."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue where emotions can trigger state transitions."""
    lines: List[str] = []

    # Initial statements about truth
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions arise during the discussion
    agent1.update_emotion("anger", 0.8)
    lines.append(f"{agent1.name} občuti jezo.")
    prev_state = agent1.state
    agent1.transition()
    if agent1.state != prev_state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} občuti veselje.")
    prev_state = agent2.state
    agent2.transition()
    if agent2.state != prev_state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Follow-up statements influenced by new states and emotions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines

