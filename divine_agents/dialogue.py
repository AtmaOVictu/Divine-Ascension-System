from typing import List
from .agent import Agent

QUESTIONS = {
    "sl": "Kaj je resnica?",
    "en": "What is truth?",
}


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    q1 = QUESTIONS[agent1.language]
    q2 = QUESTIONS[agent2.language]
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(q1)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(q2)}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond(q1)}")
    lines.append(f"{agent2.name}: {agent2.respond(q2)}")
    return lines
