# Ontological debate module for divine_agents
from typing import List
from .agent import Agent


def ontological_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Conduct a debate escalating emotions and causing possible transitions."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        agent1.update_emotion(agent1.emotion + 0.4)
        agent2.update_emotion(agent2.emotion + 0.4)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
        if agent1.state == 'Enotnost' or agent2.state == 'Enotnost':
            lines.append("Dosežena je Enotnost.")
            break
    return lines
