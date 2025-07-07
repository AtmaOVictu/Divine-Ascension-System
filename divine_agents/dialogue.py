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

    # Agents express emotions which may trigger state changes
    agent1.set_emotion("anger", 0.6)
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_type} in prehaja v: {agent1.transition()}"
    )

    agent2.set_emotion("joy", 0.8)
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_type} in prehaja v: {agent2.transition()}"
    )

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
