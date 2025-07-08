from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements about truth
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional responses increase tension leading to transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Fame increases due to participation in the dialogue
    agent1.update_fame(positive=3, negative=1, participation=5)
    agent2.update_fame(positive=2, negative=2, participation=4)

    lines.append(
        f"{agent1.name} (fama {agent1.fame}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} (fama {agent2.fame}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
