from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # initial statements on truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # emotions arise during the discussion
    agent1.update_emotion(0.6, 'anger')
    lines.append(f"{agent1.name} čuti {agent1.emotion_type}.")
    prev = agent1.state
    agent1.transition()
    if agent1.state != prev:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6, 'joy')
    lines.append(f"{agent2.name} čuti {agent2.emotion_type}.")
    prev = agent2.state
    agent2.transition()
    if agent2.state != prev:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # final responses after emotional shift
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
