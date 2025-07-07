from typing import List
from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a philosophical debate between two agents.

    Each round agents answer the same question about truth. After responding,
    their emotion is slightly increased which may lead to state transitions.
    """
    lines: List[str] = []
    question = "Kaj je resnica?"

    for _ in range(rounds):
        lines.append(agent1.speak(question))
        lines.append(agent2.speak(question))

        agent1.update_emotion(agent1.emotion + 0.4)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.4)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
