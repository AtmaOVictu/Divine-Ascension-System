from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The dialogue showcases how ontological state and fame related boxes
    influence the exchange.
    """

    lines: List[str] = []

    # Opening statements reflecting current state and fame box
    lines.append(
        f"{agent1.name} ({agent1.state} - {agent1.boxes['fame']}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state} - {agent2.boxes['fame']}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    # Intensify emotions to trigger possible transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Follow up statements after transition
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # Show social cluster composition
    lines.append(f"{agent1.name} social cluster: {agent1.get_cluster_boxes('social_cluster')}")
    lines.append(f"{agent2.name} social cluster: {agent2.get_cluster_boxes('social_cluster')}")
    return lines
