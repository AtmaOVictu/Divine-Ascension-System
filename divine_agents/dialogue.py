from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []
    # Initial statements about truth
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional escalation leading to possible transitions
    agent1.update_emotion(0.8, "jeza")
    lines.append(
        f"{agent1.name} cuti {agent1.emotion_name} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.update_emotion(0.6, "radovednost")
    lines.append(
        f"{agent2.name} cuti {agent2.emotion_name} in prehaja v stanje: {agent2.transition()}"
    )

    # Final statements after transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
