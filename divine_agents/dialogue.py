from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue and trigger state transitions."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agent 2's argument influences Agent 1
    agent1.update_emotion(0.6, "fear")
    if agent1.transition() != "Ego":
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )

    # Agent 1's new stance affects Agent 2
    agent2.update_emotion(0.8, "joy")
    if agent2.transition() != "Jaz":
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
