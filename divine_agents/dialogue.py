from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    # First exchange
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Update emotional states which may trigger transitions
    agent1.update_emotion(0.8, "strah")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange after potential transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaksna je narava resnice?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaksna je narava resnice?')}"
    )

    return lines
