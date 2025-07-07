from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function updates emotions which in turn may increase tension and
    trigger state transitions. Each agent answers a common question based
    on its current ontological state.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"

    # initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # emotions rise during debate
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.7)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # second round after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    return lines
