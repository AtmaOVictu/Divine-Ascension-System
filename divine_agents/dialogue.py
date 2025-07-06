from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a multi-round philosophical dialogue between two agents."""
    lines: List[str] = []
    question = "Kaj je resnica?"

    for step in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        agent1.update_emotion(0.4 + 0.2 * step)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.5 + 0.2 * step)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
