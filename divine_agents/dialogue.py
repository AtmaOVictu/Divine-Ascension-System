from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial positions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions to the initial statements
    agent1.update_emotion(0.8, "anger")
    agent2.update_emotion(0.6, "joy")

    # State transitions if thresholds are exceeded
    prev_state_a1 = agent1.state
    prev_state_a2 = agent2.state
    agent1.transition()
    agent2.transition()

    if agent1.state != prev_state_a1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != prev_state_a2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Second round of answers reflecting new states and emotions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
