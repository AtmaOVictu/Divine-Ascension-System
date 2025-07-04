from typing import List
from .agent import Agent


def debate(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Conduct a simple philosophical debate between two agents.

    Each turn agents respond according to their state. If their states differ,
    their emotion increases, which may lead to a state transition.
    """
    lines: List[str] = []
    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotion if agents disagree; otherwise a smaller rise occurs
        if agent1.state != agent2.state:
            agent1.update_emotion(0.4)
            agent2.update_emotion(0.4)
        else:
            agent1.update_emotion(0.2)
            agent2.update_emotion(0.2)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
