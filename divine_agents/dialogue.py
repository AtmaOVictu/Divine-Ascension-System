from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, question: str = "Kaj je resnica?") -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # Emotional shift for agent1 triggered by agent2's argument
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent1 responds again from new perspective
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")

    # Agent2 also reacts emotionally and may transition
    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    return lines
