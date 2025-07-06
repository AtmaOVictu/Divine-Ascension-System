from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    # emotional update and possible transitions
    agent1.update_emotion(0.6, "fear")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # follow-up statements after emotion change
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )
    return lines
