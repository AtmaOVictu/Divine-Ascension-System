from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "joy")
    lines.append(
        f"{agent1.name} čuti {agent1.emotion.name} in prehaja v stanje: {agent1.transition()}"
    )

    agent2.update_emotion(0.6, "hope")
    lines.append(
        f"{agent2.name} čuti {agent2.emotion.name} in prehaja v stanje: {agent2.transition()}"
    )

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
