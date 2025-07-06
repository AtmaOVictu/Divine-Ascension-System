from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    # Emotions rise after the first exchange
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    # Attempt transitions if thresholds are met
    prev_state1 = agent1.state
    prev_state2 = agent2.state
    agent1.transition()
    agent2.transition()

    if agent1.state != prev_state1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != prev_state2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final statements reflect new states and emotions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    return lines
