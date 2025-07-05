from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, emotion1: float = 0.8, emotion2: float = 0.6) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    question = "Kaj je resnica?"
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    agent1.update_emotion(emotion1)
    agent2.update_emotion(emotion2)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
