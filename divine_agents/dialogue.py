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

    # Emotions arise during debate
    agent1.update_emotion("fear", 0.6)
    lines.append(
        f"{agent1.name} doživlja {agent1.emotion_type} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.update_emotion("joy", 0.8)
    lines.append(
        f"{agent2.name} doživlja {agent2.emotion_type} in prehaja v stanje: {agent2.transition()}"
    )

    # Final statements after transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
