from typing import List
from random import choice
from .agent import Agent


EMOTIONS = ["fear", "joy", "anger"]


def philosophical_dialogue(agent1: Agent, agent2: Agent, iterations: int = 1) -> List[str]:
    """Simulate a philosophical dialogue where agents may transition states."""
    lines = []
    for _ in range(iterations):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.set_emotion(choice(EMOTIONS), 0.8)
        prev = agent1.history[-1]
        if agent1.transition() != prev:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        agent2.set_emotion(choice(EMOTIONS), 0.6)
        prev2 = agent2.history[-1]
        if agent2.transition() != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
