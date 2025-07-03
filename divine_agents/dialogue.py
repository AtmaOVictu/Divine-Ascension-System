from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue with emotional influence."""
    lines: List[str] = []

    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during debate
    agent1.update_emotion(0.8, label="jeza")
    lines.append(f"{agent1.name} povečuje napetost na {agent1.tension:.1f}")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, label="sreča")
    lines.append(f"{agent2.name} povečuje napetost na {agent2.tension:.1f}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of statements after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
