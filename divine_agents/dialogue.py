from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional updates influence tension and trigger transitions
    agent1.update_emotion(0.8)
    agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state} {agent1.last_symbol}")

    agent2.update_emotion(0.6)
    agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state} {agent2.last_symbol}")

    # Post-transition perspectives
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
