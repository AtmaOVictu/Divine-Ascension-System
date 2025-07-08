from typing import List

from .agent import Agent
from .reputation import ReputationSystem


def philosophical_dialogue(agent1: Agent, agent2: Agent, action: str = "help") -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    rep = ReputationSystem()
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.fame_tier()}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.fame_tier()}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    rep.interact(agent1, agent2, action)

    lines.append(
        f"{agent1.name} ({agent1.fame_tier()}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.fame_tier()}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
