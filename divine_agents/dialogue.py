from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    # Initial exchange of views on truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reaction to the debate
    agent1.set_emotion('anger', 0.6)
    lines.append(f"{agent1.name} \u010duti jezo in prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion('joy', 0.4)
    lines.append(f"{agent2.name} ostaja miren v stanju: {agent2.state}")

    # Continued discussion in new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent2 reaches unity through joy
    agent2.set_emotion('joy', 0.7)
    lines.append(f"{agent2.name} \u010duti radost in prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
