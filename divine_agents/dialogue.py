from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate and track emotional transitions."""
    lines: List[str] = []

    # Initial viewpoints
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agent 1 reacts with fear to Agent 2's argument
    agent1.update_emotion("strah", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent 2 feels joy from the exchange
    agent2.update_emotion("veselje", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of statements reflecting new states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agent 2 deepens joy and reaches unity
    agent2.update_emotion("veselje", 0.2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
