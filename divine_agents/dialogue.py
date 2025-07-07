from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during discussion
    agent1.update_emotion(agent1.emotion + 0.6)
    prev = agent1.state
    agent1.transition()
    if prev != agent1.state:
        lines.append(f"{agent1.name} prehaja iz {prev} v {agent1.state}")

    agent2.update_emotion(agent2.emotion + 0.6)
    prev = agent2.state
    agent2.transition()
    if prev != agent2.state:
        lines.append(f"{agent2.name} prehaja iz {prev} v {agent2.state}")

    # Final responses reflecting new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
