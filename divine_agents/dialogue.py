from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions affect tension and may trigger transitions
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    prev1, prev2 = agent1.state, agent2.state
    new1 = agent1.transition()
    new2 = agent2.transition()

    if new1 != prev1:
        lines.append(f"{agent1.name} prehaja v stanje: {new1}")
    if new2 != prev2:
        lines.append(f"{agent2.name} prehaja v stanje: {new2}")

    # Follow-up statements reflecting potential new states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
