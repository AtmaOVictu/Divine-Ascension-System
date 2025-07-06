from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where agents may change state."""

    lines: List[str] = []
    for i in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(0.6 + 0.2 * i, emotion_type="anger" if i == 0 else "joy")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.5 + 0.1 * i, emotion_type="calm" if i == 0 else "satisfaction")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} končno pravi: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} zaključi: {agent2.respond('Kaj je resnica?')}")
    return lines
