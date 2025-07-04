from typing import List
from .agent import Agent
from .shumnik import shumnik_tension, shumnik_reflection


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    lines.append(f"{agent1.name} se sreča s {shumnik_tension.symbol}")
    shumnik_tension.activate(agent1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    lines.append(f"{agent2.name} se sreča s {shumnik_reflection.symbol}")
    shumnik_reflection.activate(agent2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
