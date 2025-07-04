from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue with emotional influence."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts with doubt after hearing agent2
    agent1.update_emotion(0.6, label="dvom")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 becomes passionate
    agent2.update_emotion(0.8, label="strast")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of statements reflecting new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
