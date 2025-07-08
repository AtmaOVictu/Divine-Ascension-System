from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent,
                           inc1: float = 0.1, inc2: float = 0.1) -> List[str]:
    """Simulate a dialogue where emotions gradually increase."""
    question = "Kaj je resnica?"
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    agent1.update_emotion(agent1.emotion + inc1)
    prev1 = agent1.state
    agent1.transition()
    if agent1.state != prev1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(agent2.emotion + inc2)
    prev2 = agent2.state
    agent2.transition()
    if agent2.state != prev2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond(question)}")
    lines.append(f"{agent2.name}: {agent2.respond(question)}")
    return lines
