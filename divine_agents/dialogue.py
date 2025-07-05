from typing import List
from .agent import Agent
from .emotion import logistic_emotion


def philosophical_dialogue(agent1: Agent, agent2: Agent, time: float = 1.0) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]

    e1 = logistic_emotion(time, k=0.8, c=0.5)
    agent1.update_emotion(e1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    e2 = logistic_emotion(time, k=1.0, c=0.3)
    agent2.update_emotion(e2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
