from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a dynamic philosophical dialogue between two agents."""
    lines: List[str] = []
    question = "Kaj je resnica?"

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        agent1.set_emotion("joy", agent1.emotion + 0.4)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.set_emotion("fear", agent2.emotion + 0.5)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
