from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Izvede kratko filozofsko razpravo med dvema agentoma."""
    lines: List[str] = []

    # Začetni odgovori
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 se razburi zaradi nasprotnega mnenja
    agent1.update_emotion('jeza', 0.8)
    if agent1.transition() != agent1.history[-2]:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    # Agent2 reagira z veseljem in sočutjem
    agent2.update_emotion('veselje', 0.8)
    if agent2.transition() != agent2.history[-2]:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Ponovni odgovori po čustveni spremembi
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
