from typing import Iterable, List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def group_dialogue(agents: Iterable[Agent]) -> List[str]:
    """Simulate dialogue among multiple agents with automatic transitions."""
    agents = list(agents)
    lines: List[str] = []

    for ag in agents:
        lines.append(f"{ag.name} ({ag.state}): {ag.respond('Kaj je resnica?')}")

    for ag in agents:
        ag.update_emotion(0.8)
        lines.append(f"{ag.name} prehaja v stanje: {ag.transition()}")

    for ag in agents:
        lines.append(f"{ag.name}: {ag.respond('Kaj je resnica?')}")

    return lines
