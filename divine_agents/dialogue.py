from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions: Tuple[Tuple[str, float], Tuple[str, float]] = (("anger", 0.8), ("joy", 0.6)),
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participating agent.
    agent2 : Agent
        Second participating agent.
    emotions : tuple
        Pairs defining emotion type and intensity for each agent.
    """
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Apply emotions which may trigger state transitions
    e1, e2 = emotions
    agent1.update_emotion(e1[1], e1[0])
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(e2[1], e2[0])
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
