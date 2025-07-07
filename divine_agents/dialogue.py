from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each round both agents express their current understanding of truth, then
    their emotions are slightly increased which may trigger a state transition.
    The produced list of strings can be used for logging or display.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        agent1.increase_emotion(0.4)
        agent2.increase_emotion(0.4)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
