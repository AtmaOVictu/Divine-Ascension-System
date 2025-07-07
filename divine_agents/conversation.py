from typing import List

from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a debate between two agents over multiple rounds."""
    lines: List[str] = []
    emotions = [
        {agent1.name: (0.6, "anger"), agent2.name: (0.4, "joy")},
        {agent1.name: (0.2, "joy"), agent2.name: (0.3, "fear")},
    ]

    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        if i < len(emotions):
            e1, t1 = emotions[i][agent1.name]
            e2, t2 = emotions[i][agent2.name]
            agent1.update_emotion(e1, t1)
            agent2.update_emotion(e2, t2)

            lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
