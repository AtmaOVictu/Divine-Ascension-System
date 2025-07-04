from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2, emotion_step: float = 0.6) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive transitions."""
    lines: List[str] = []
    question = "Kaj je resnica?"

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        old1, old2 = agent1.state, agent2.state
        agent1.advance(emotion_step)
        agent2.advance(emotion_step)

        if agent1.state != old1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != old2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond(question)}")
    lines.append(f"{agent2.name}: {agent2.respond(question)}")
    return lines
