from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue where emotions drive transitions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    # Emotional reactions to the first exchange
    agent1.update_emotion(0.8, label="jeza")
    agent2.update_emotion(0.6, label="presenečenje")

    prev1, prev2 = agent1.state, agent2.state
    agent1.transition()
    agent2.transition()
    if agent1.state != prev1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != prev2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Second round of statements reflecting new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    return lines

