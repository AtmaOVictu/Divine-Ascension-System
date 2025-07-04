from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue between two agents discussing truth."""
    lines: List[str] = []

    # Opening statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotion increases after hearing each other
    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.transition()} (vrednost: {agent1.state_value})"
    )

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.transition()} (vrednost: {agent2.state_value})"
    )

    # Second round of responses after transitions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
