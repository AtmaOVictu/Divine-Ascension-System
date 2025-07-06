from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function updates emotions, triggers transitions when thresholds are met
    and records each line of dialogue.
    """
    lines: List[str] = []
    question = "Kaj je resnica?"

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # escalate emotions which may lead to state transitions
    agent1.update_emotion(0.8)
    old_state = agent1.state
    agent1.transition()
    if agent1.state != old_state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6)
    old_state = agent2.state
    agent2.transition()
    if agent2.state != old_state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
