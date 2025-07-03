from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

from .emotion import apply_emotion


def emotional_dialogue(agent1: Agent, agent2: Agent, rounds: int, emotions1, emotions2) -> List[str]:
    """Simulate a multi-round dialogue where emotions influence transitions."""
    lines = []
    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        if i < len(emotions1):
            apply_emotion(agent1, emotions1[i])
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        if i < len(emotions2):
            apply_emotion(agent2, emotions2[i])
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return lines
