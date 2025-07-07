from typing import List
from .agent import Agent


def dynamic_conversation(agent1: Agent, agent2: Agent, emotions1: List[float], emotions2: List[float]) -> List[str]:
    """Run a multi-step dialogue with state transitions based on emotions.

    Each step consists of both agents responding according to their current
    ontological state. Emotions provided for that step will update each agent
    and may trigger a state transition if thresholds are met.
    """
    lines: List[str] = []
    steps = min(len(emotions1), len(emotions2))
    for i in range(steps):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(emotions1[i])
        agent2.update_emotion(emotions2[i])

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return lines
