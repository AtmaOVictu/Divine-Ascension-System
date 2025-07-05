from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the discussion
    agent1.apply_emotion('jeza', 0.6)
    lines.append(f"{agent1.name} čuti {agent1.emotion_name} (napetost: {agent1.tension:.2f})")
    agent2.apply_emotion('radovednost', 0.6)
    lines.append(f"{agent2.name} čuti {agent2.emotion_name} (napetost: {agent2.tension:.2f})")

    # Possible transitions due to emotion/tension
    prev1 = agent1.state
    prev2 = agent2.state
    agent1.transition()
    agent2.transition()
    if agent1.state != prev1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != prev2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Agents respond again from their possibly new state
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
