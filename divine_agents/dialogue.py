from typing import Iterable, List, Tuple
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, script: Iterable[Tuple[float, float]]) -> List[str]:
    """Simulate a philosophical dialogue using an emotion script.

    Parameters
    ----------
    agent1 : Agent
        First conversational agent.
    agent2 : Agent
        Second conversational agent.
    script : Iterable[Tuple[float, float]]
        Sequence of emotion intensity pairs ``(e1, e2)`` applied to ``agent1`` and
        ``agent2`` for each dialogue turn.
    """

    lines: List[str] = []
    for e1, e2 in script:
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(e1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(e2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
