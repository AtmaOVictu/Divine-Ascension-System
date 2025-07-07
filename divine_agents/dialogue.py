from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, topic: str = "Kaj je resnica?") -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotion levels are increased during the debate, which may trigger state
    transitions depending on the defined thresholds.
    """
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(topic)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(topic)}")

    # escalate emotions and tension
    agent1.update_emotion(0.8)
    previous_state = agent1.state
    agent1.transition()
    if agent1.state != previous_state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6)
    previous_state = agent2.state
    agent2.transition()
    if agent2.state != previous_state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(topic)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(topic)}")

    return lines
