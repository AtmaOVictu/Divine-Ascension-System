from typing import List
from .agent import Agent
from .philosophy import State


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue with emotional influence."""
    lines: List[str] = []

    # initial exchange
    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}")

    # update emotions which may trigger transitions
    agent1.update_emotion("anger", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition().value}")

    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition().value}")

    # final exchange after state changes
    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}")
    return lines
