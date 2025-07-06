from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents experience emotions during the debate
    agent1.update_emotion(0.6, "jeza")
    prev_state = agent1.state
    agent1.transition()
    if agent1.state != prev_state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.8, "veselje")
    prev_state = agent2.state
    agent2.transition()
    if agent2.state != prev_state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Follow-up statements reflecting new states and emotions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
