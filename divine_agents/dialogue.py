from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue where emotions can trigger state changes."""
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate
    agent1.update_emotion(0.6)
    agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_tension(0.8)
    agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final statements after possible transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kako dojemaš resnico?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kako dojemaš resnico?')}"
    )
    return lines
