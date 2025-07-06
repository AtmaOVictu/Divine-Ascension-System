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

    # Emotional reactions influence tension
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.4)

    # Paradoxical transitions
    lines.append(agent1.metaparadox.paradoxical_transition())
    lines.append(agent2.metaparadox.paradoxical_transition())

    lines.append(f"{agent1.name}: {agent1.respond('Kaj pa zdaj?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj pa zdaj?')}")
    return lines
