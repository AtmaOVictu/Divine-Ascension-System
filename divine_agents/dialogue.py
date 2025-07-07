from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []
    # Initial statements based on current ontological states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agents react emotionally to each other's statements
    agent1.update_emotion("anger", 0.6)
    lines.append(f"{agent1.name} \u010duti {agent1.emotion} in ima napetost {agent1.tension:.2f}.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("sočutje", 0.8)
    lines.append(f"{agent2.name} \u010duti {agent2.emotion} in ima napetost {agent2.tension:.2f}.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections after potential transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
