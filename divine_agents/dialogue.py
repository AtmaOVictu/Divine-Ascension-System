from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]

    agent1.update_emotion(0.8)
    agent1.move()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(
        f"{agent1.name} se premakne na pozicijo {agent1.position:.1f} s hitrostjo {agent1.speed:.1f}"
    )

    agent2.update_emotion(0.6)
    agent2.move()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(
        f"{agent2.name} se premakne na pozicijo {agent2.position:.1f} s hitrostjo {agent2.speed:.1f}"
    )

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
