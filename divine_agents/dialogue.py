from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Simulate a dialogue where agents may change states based on emotion."""
    lines: List[str] = []
    question = "Kaj je resnica?"

    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        # Increase emotion slightly to trigger possible transitions
        agent1.update_emotion(agent1.emotion + 0.3)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.3)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
