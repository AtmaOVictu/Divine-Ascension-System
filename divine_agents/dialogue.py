"""Utilities for simulating philosophical dialogues between agents."""

from typing import List

from .agent import Agent, EmotionType


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond()}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond()}")

    agent1.update_emotion(EmotionType.ANGER, 0.8)
    agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state.value}")

    agent2.update_emotion(EmotionType.JOY, 0.6)
    agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state.value}")

    lines.append(f"{agent1.name}: {agent1.respond()}")
    lines.append(f"{agent2.name}: {agent2.respond()}")

    return lines
