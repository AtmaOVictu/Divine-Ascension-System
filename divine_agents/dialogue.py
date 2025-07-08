from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, statement: str = "Kaj je resnica?") -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(statement)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(statement)}")

    agent1.parse_philosophical_statement(statement)
    agent2.parse_philosophical_statement(statement)

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond(statement)}")
    lines.append(f"{agent2.name}: {agent2.respond(statement)}")

    lines.append(agent1.self_reflection())
    lines.append(agent2.self_reflection())
    return lines
