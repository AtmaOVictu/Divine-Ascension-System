from typing import List
from .agent import Agent
from .memory import Memory, parse_philosophical_statement


def philosophical_dialogue(agent1: Agent, agent2: Agent, memory: Memory | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    if memory is None:
        memory = Memory()

    lines = []

    answer1 = agent1.respond("Kaj je resnica?")
    parse_philosophical_statement(answer1, memory)
    lines.append(f"{agent1.name} ({agent1.state}): {answer1}")

    answer2 = agent2.respond("Kaj je resnica?")
    parse_philosophical_statement(answer2, memory)
    lines.append(f"{agent2.name} ({agent2.state}): {answer2}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    answer1 = agent1.respond("Kaj je resnica?")
    parse_philosophical_statement(answer1, memory)
    lines.append(f"{agent1.name}: {answer1}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    answer2 = agent2.respond("Kaj je resnica?")
    parse_philosophical_statement(answer2, memory)
    lines.append(f"{agent2.name}: {answer2}")
    return lines
