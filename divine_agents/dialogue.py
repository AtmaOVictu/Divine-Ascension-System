from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reaction from agent1 hearing agent2
    agent1.update_emotion(0.6, emotion_type="anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )

    # Agent2 responds with joy after convincing agent1
    agent2.update_emotion(0.8, emotion_type="joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
