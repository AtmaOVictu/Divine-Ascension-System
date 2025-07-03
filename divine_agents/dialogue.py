from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    first = f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    lines.append(first)

    second = f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    lines.append(second)

    agent1.update_emotion(0.8)
    transition1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {transition1}")

    agent2.update_emotion(0.6)
    transition2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {transition2}")

    follow1 = f"{agent1.name}: {agent1.respond('Kaj je resnica?')}"
    lines.append(follow1)

    follow2 = f"{agent2.name}: {agent2.respond('Kaj je resnica?')}"
    lines.append(follow2)

    # Record the entire dialogue in each agent's legend
    agent1.legend.extend(lines)
    agent2.legend.extend(lines)

    return lines
