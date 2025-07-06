from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional shifts influence tension
    agent1.update_emotion(0.6, mood="fear")
    lines.append(f"{agent1.name} čuti {agent1.mood}, napetost {agent1.tension:.2f}")
    prev_state = agent1.state
    agent1.transition()
    if agent1.state != prev_state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6, mood="joy")
    lines.append(f"{agent2.name} čuti {agent2.mood}, napetost {agent2.tension:.2f}")
    prev_state = agent2.state
    agent2.transition()
    if agent2.state != prev_state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Second round of statements after emotional change
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako dojemaš resnico?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Zakaj meniš tako?')}")

    return lines
