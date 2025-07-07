from typing import List
from .membership import MembershipAgent


def philosophical_debate(agent1: MembershipAgent, agent2: MembershipAgent) -> List[str]:
    """Conduct a dialogue between two agents with emotional influence."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents update emotion and may transition
    agent1.update_emotion(0.6)
    prev1 = agent1.state
    agent1.transition()
    if agent1.state != prev1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.8)
    prev2 = agent2.state
    agent2.transition()
    if agent2.state != prev2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines

