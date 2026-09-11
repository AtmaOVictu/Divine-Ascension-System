from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Fame influenced by participation in debate
    agent1.update_fame(positive_actions=0.3, negative_actions=0.0, participation_score=0.7)
    agent2.update_fame(positive_actions=0.4, negative_actions=0.1, participation_score=0.7)

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def influence_in_cluster(agent: Agent, cluster_name: str) -> int:
    """Return influence percentage of an agent in a cluster based on boxes."""
    cluster = agent.get_cluster_boxes(cluster_name)
    influence = 0
    for box in cluster:
        if "Influential" in box or "Highly Active" in box:
            influence += 10
        elif "Frustrated" in box or "Unknown" in box:
            influence -= 5
    return influence
