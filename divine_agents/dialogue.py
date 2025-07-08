from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Each agent first states their view on truth based on their current
    ontological state. Their emotional intensity is then increased which may
    trigger a state transition. Fame is updated based on the participation in
    the conversation.
    """
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Increase emotional intensity which affects tension
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    # Transitions if thresholds exceeded
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Update fame and participation after speaking
    agent1.update_participation(70)
    agent2.update_participation(50)
    agent1.update_fame(1, 0, agent1.participation)
    agent2.update_fame(1, 0, agent2.participation)

    # Final statements reflecting new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
