from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""

    def _exchange(a: Agent) -> str:
        return f"{a.name} ({a.state}): {a.respond('Kaj je resnica?')}"

    lines: List[str] = []
    lines.append(_exchange(agent1))
    lines.append(_exchange(agent2))

    agent1.update_emotion(0.6, "fear")
    prev = agent1.state
    agent1.transition()
    if agent1.state != prev:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6, "joy")
    prev = agent2.state
    agent2.transition()
    if agent2.state != prev:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(_exchange(agent1))
    lines.append(_exchange(agent2))
    return lines
