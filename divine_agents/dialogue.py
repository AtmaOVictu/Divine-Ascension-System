from typing import List
from .agent import Agent
from .translator import text_to_binary


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    question = "Kaj je resnica?"
    r1 = agent1.respond(question)
    lines.append(f"{agent1.name} ({agent1.state}): {r1}")
    lines.append(f"{agent1.name} binarno: {text_to_binary(r1)}")

    r2 = agent2.respond(question)
    lines.append(f"{agent2.name} ({agent2.state}): {r2}")
    lines.append(f"{agent2.name} binarno: {text_to_binary(r2)}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    r1 = agent1.respond(question)
    lines.append(f"{agent1.name}: {r1}")
    lines.append(f"{agent1.name} binarno: {text_to_binary(r1)}")

    r2 = agent2.respond(question)
    lines.append(f"{agent2.name}: {r2}")
    lines.append(f"{agent2.name} binarno: {text_to_binary(r2)}")

    return lines
