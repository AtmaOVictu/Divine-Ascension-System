from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agent 1 reacts emotionally to Agent 2's statement
    agent1.update_emotion(0.8, "jezo")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent 2 responds with joy
    agent2.update_emotion(0.6, "veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round with updated states and emotions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
