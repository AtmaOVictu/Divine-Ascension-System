from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate dialogue where agents may transition states."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents experience emotions affecting tension
    agent1.update_emotions({'fear': 0.6, 'anger': 0.2})
    agent2.update_emotions({'joy': 0.4, 'fear': 0.3})

    agent1.transition()
    agent2.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kako vidiš resnico?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kako vidiš resnico?')}")
    return lines
