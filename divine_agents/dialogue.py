from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions: Tuple[Tuple[str, float], Tuple[str, float]] = (("joy", 0.8), ("anger", 0.6)),
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participating agent.
    agent2 : Agent
        Second participating agent.
    emotions : tuple(tuple(str, float), tuple(str, float)), optional
        Pairs describing emotion type and intensity for ``agent1`` and ``agent2``.
    """
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    e1_type, e1_value = emotions[0]
    agent1.update_emotion(e1_value, e1_type)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    e2_type, e2_value = emotions[1]
    agent2.update_emotion(e2_value, e2_type)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
