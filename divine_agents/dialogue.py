from typing import List
from .agent import Agent, EmotionDimensionAgent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dimension_dialogue(agent1: EmotionDimensionAgent, agent2: EmotionDimensionAgent) -> List[str]:
    """Dialogue that also processes emotions within dimensions."""
    lines = philosophical_dialogue(agent1, agent2)
    # Process emotions with respect to dimensions after initial exchange
    influence1 = agent1.process_emotion()
    influence2 = agent2.process_emotion()
    lines.append(
        f"{agent1.name} vpliv v dimenziji {agent1.dimension}: {influence1}"
    )
    lines.append(
        f"{agent2.name} vpliv v dimenziji {agent2.dimension}: {influence2}"
    )
    return lines
