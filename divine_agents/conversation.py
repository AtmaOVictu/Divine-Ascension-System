from typing import List
from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Conduct a short philosophical debate influenced by emotions."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # escalate emotions which may trigger transitions
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    prev1 = agent1.state
    prev2 = agent2.state
    agent1.transition()
    agent2.transition()

    if agent1.state != prev1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != prev2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
