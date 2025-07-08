from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_name}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_name}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise during the debate
    agent1.update_emotion(0.8, name="anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, name="joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Reflection after transition
    agent1.reflect()
    agent2.reflect()

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
