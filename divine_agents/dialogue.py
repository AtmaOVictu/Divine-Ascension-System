from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agents form a relationship and emotions rise during debate
    agent1.add_relationship(agent2, 0.6)
    agent2.add_relationship(agent1, 0.6)

    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    agent1.update_tension_dynamically()
    agent2.update_tension_dynamically()

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    lines.append(agent1.make_moral_decision("debata"))
    lines.append(agent2.make_moral_decision("debata"))

    lines.append(agent1.team_decision([agent1, agent2]))
    return lines
