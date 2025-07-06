from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate an emotionally influenced philosophical dialogue."""
    lines = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise during the debate
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after emotional shift
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
