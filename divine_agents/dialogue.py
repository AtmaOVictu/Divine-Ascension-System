from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents influence each other's tension based on emotions
    agent1.update_emotion(0.8)
    agent1.interact_with(agent2)
    agent2.update_emotion(0.6)
    agent2.interact_with(agent1)

    agent1.transition()
    agent2.transition()

    s1, d1 = agent1.move()
    s2, d2 = agent2.move()

    lines.append(f"{agent1.name} se premika s hitrostjo {s1:.2f} v smeri {d1}")
    lines.append(f"{agent2.name} se premika s hitrostjo {s2:.2f} v smeri {d2}")

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
