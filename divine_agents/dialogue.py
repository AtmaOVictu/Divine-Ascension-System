from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Simulate a philosophical dialogue with emotional transitions."""
    lines: List[str] = []
    emotions = [
        ("jeza", 0.4),
        ("sreča", 0.4),
        ("strah", 0.4),
    ]

    for i in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        e1_type, e1_val = emotions[i % len(emotions)]
        agent1.set_emotion(e1_type, e1_val)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        e2_type, e2_val = emotions[(i + 1) % len(emotions)]
        agent2.set_emotion(e2_type, e2_val)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
