from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents."""
    lines: List[str] = []

    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Update emotions and tension dynamically
        agent1.update_emotion(0.4 + 0.3 * i, "jeza" if i == 0 else "radovednost")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.5 + 0.2 * i, "navdušenje")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
