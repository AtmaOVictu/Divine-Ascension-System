from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, questions: List[str]) -> List[str]:
    """Simulate a philosophical dialogue using custom questions."""
    lines: List[str] = []

    for question in questions:
        # Agents answer the question
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        # Hearing a statement slightly raises the other agent's emotion
        agent2.update_emotion(agent2.emotion + 0.2)

        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
        agent1.update_emotion(agent1.emotion + 0.2)

        # After exchanging statements, check if emotional levels cause transitions
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
