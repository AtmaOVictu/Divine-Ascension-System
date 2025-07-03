from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond()}")

    # Emotions arise during debate influencing tension and potential transitions
    agent1.update_tension(0.8)
    agent1.update_emotion("anger", 0.6)
    agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion("joy", 0.7)
    agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final statements after transitions
    lines.append(f"{agent1.name}: {agent1.respond()}")
    lines.append(f"{agent2.name}: {agent2.respond()}")
    return lines
