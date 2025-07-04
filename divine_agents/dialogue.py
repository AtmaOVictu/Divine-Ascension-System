from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial exchange about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # First emotional shift
    agent1.update_emotion(0.6, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.4, "curiosity")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange after emotions changed
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kako razumes resnico?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kako razumes resnico?')}"
    )

    # Second emotional shift leading to potential new transitions
    agent1.update_emotion(0.5, "wonder")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections
    lines.append(f"{agent1.name}: {agent1.respond('Sklep?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Sklep?')}")

    return lines
