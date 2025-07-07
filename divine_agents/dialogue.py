from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents experience emotions after hearing each other
    agent1.update_emotion('anger', 0.6)
    agent2.update_emotion('joy', 0.8)
    lines.append(f"{agent1.name} cuti {agent1.emotion_type} in napetost {agent1.tension:.2f}")
    lines.append(f"{agent2.name} cuti {agent2.emotion_type} in napetost {agent2.tension:.2f}")

    # Possible state transitions
    prev1 = agent1.state
    prev2 = agent2.state
    agent1.transition()
    agent2.transition()
    if agent1.state != prev1:
        lines.append(f"{agent1.name} se premakne v stanje: {agent1.state}")
    if agent2.state != prev2:
        lines.append(f"{agent2.name} se premakne v stanje: {agent2.state}")

    # Final statements after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
