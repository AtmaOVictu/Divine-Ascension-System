from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, iterations: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each iteration both agents respond to the question "Kaj je resnica?" and
    their emotions are intensified, potentially triggering a state transition.
    """

    lines: List[str] = []
    emotions = ["fear", "anger", "joy"]

    for i in range(iterations):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0), emotions[i % len(emotions)])
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0), emotions[(i + 1) % len(emotions)])
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
