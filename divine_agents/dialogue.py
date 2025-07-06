from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate between two agents."""
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # Emotions rise during debate triggering possible transitions
    agent1.update_emotion(0.6, label="anger")
    agent2.update_emotion(0.8, label="joy")

    previous_state_a1 = agent1.state
    previous_state_a2 = agent2.state
    agent1.transition()
    agent2.transition()
    if agent1.state != previous_state_a1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != previous_state_a2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Agents respond again from new perspectives
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    return lines
