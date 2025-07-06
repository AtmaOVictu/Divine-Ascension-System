from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents influence each other's emotions
    agent1.relationship_strength[agent2.name] = 0.8
    agent2.relationship_strength[agent1.name] = 0.8

    agent1.update_emotion(0.8, "fearful")
    lines.append(agent2.show_empathy(agent1))
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "happy")
    lines.append(agent1.show_empathy(agent2))
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Moral decisions after the state change
    lines.append(agent1.make_moral_decision("debate"))
    lines.append(agent2.make_moral_decision("debate"))

    # Final responses
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
