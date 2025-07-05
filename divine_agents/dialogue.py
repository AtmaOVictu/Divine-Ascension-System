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

    # Emotional reactions influencing tension
    agent1.update_emotion(0.8, "anger")
    agent2.update_emotion(0.6, "joy")

    # State transitions due to emotions
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_type} in prehaja v stanje: {agent1.transition()}"
    )
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_type} in prehaja v stanje: {agent2.transition()}"
    )

    # Responses after transition
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica sedaj?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica sedaj?')}")

    return lines
