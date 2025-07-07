from typing import List

from .agent import Agent
from .emotions import EmotionType


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # First emotional reactions and possible transitions
    agent1.update_emotion(EmotionType.ANGER, 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(EmotionType.JOY, 0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round - agents may reach higher state
    agent1.update_emotion(EmotionType.JOY, 0.7)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Final statements influenced by new states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
