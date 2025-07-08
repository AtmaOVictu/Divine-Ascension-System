from typing import List
from .agent import Agent, emotional_state
from .reputation import ReputationSystem


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.fame_tier}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.fame_tier}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agents interact by helping each other which increases their fame
    rep = ReputationSystem()
    rep.interact(agent1, agent2, action="help")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{agent1.name} ({emotional_state(agent1)}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({emotional_state(agent2)}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
