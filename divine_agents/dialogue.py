from typing import List
from .agent import Agent, Emotion


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial views
    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond()}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond()}")

    # Debate raises emotions and tension
    agent1.update_emotion(Emotion.ANGER, 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition().value}")

    agent2.update_emotion(Emotion.JOY, 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition().value}")

    # Agents speak again from new states
    lines.append(f"{agent1.name}: {agent1.respond()}")
    lines.append(f"{agent2.name}: {agent2.respond()}")
    return lines
