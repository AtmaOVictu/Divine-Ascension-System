from typing import List
from .agent import Agent, fame_tiers, social_influence


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions escalate during the discussion
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Fame updates based on their participation in discussion
    agent1.update_fame(0.3, 0.1, 0.7)
    agent2.update_fame(0.4, 0.2, 0.6)

    lines.append(f"{agent1.name} slovi kot: {fame_tiers(agent1)}")
    lines.append(f"{agent2.name} slovi kot: {fame_tiers(agent2)}")

    influence = social_influence(agent1, agent2)
    if influence:
        lines.append(f"{agent1.name} vpliva na {agent2.name}.")
    else:
        lines.append(f"{agent1.name} ne vpliva na {agent2.name}.")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
