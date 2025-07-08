from typing import List
from .agent import (
    Agent,
    emotional_state,
    social_influence,
)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Increase emotions which in turn might trigger state transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Fame interactions
    agent1.update_fame(0.3, 0.1, 0.7)
    agent2.update_fame(0.4, 0.2, 0.6)

    if social_influence(agent1, agent2):
        lines.append(f"{agent1.name} vpliva na {agent2.name}.")
    else:
        lines.append(f"{agent1.name} nima vpliva na {agent2.name}.")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # Report emotional state influenced by fame
    lines.append(f"{agent1.name} se počuti: {emotional_state(agent1)}")
    lines.append(f"{agent2.name} se počuti: {emotional_state(agent2)}")

    return lines
