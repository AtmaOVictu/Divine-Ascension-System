from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The dialogue consists of an initial question followed by each agent
    updating their emotional state, potentially triggering a state change,
    and responding again from the new perspective.
    """

    question = "Kaj je resnica?"
    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond(question)}",
        f"{agent2.name} ({agent2.state}): {agent2.respond(question)}",
    ]

    agent1.update_emotion("fear", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.extend([
        f"{agent1.name} ({agent1.state}): {agent1.respond(question)}",
        f"{agent2.name} ({agent2.state}): {agent2.respond(question)}",
    ])
    return lines
