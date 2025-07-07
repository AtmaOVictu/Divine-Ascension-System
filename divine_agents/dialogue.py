from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on current ontological state
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Increase tension if agents disagree on their view of truth
    if agent1.state != agent2.state:
        agent1.update_tension(agent1.tension + 0.3)
        agent2.update_tension(agent2.tension + 0.3)
        lines.append("Napetost narašča zaradi nesoglasja.")

    # Emotional reaction further raises tension and may trigger transitions
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again from their (possibly new) states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
