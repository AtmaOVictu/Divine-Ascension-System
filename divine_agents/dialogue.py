from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial exchange
    lines.append(agent1.respond("Kaj je resnica?"))
    lines.append(agent2.respond("Kaj je resnica?"))

    # Emotional reactions influence tension and possible transitions
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "wonder")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agent1 reaches enlightenment through wisdom key
    agent1.set_key("wisdom")
    lines.append(f"{agent1.name} aktivira kljuc 'wisdom' in prehaja v stanje: {agent1.state}")

    # Final responses after transitions
    lines.append(agent1.respond("Kaj je resnica?"))
    lines.append(agent2.respond("Kaj je resnica?"))

    return lines
