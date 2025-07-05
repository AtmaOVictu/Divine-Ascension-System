from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The agents update their emotional state during the conversation and may
    transition to a new ontological phase when their internal energy exceeds
    the required thresholds.
    """

    lines: List[str] = []
    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional escalation
    agent1.update_emotion(agent1.emotion + 0.8)
    agent1.sync_pathos()
    lines.append(
        f"{agent1.name} -> {agent1.state}: {agent1.respond('Kaj je resnica?')}"
    )

    agent2.update_emotion(agent2.emotion + 0.7)
    agent2.sync_pathos()
    lines.append(
        f"{agent2.name} -> {agent2.state}: {agent2.respond('Kaj je resnica?')}"
    )

    return lines
