from typing import List, Iterable, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions: Iterable[Tuple[float, float]] | None = None,
) -> List[str]:
    """Simulate a philosophical dialogue influenced by emotions.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    emotions:
        Optional iterable of ``(e1, e2)`` emotion values applied at each step.
        Defaults to a single step that triggers both agents to transition.
    """

    if emotions is None:
        emotions = [(0.8, 0.6)]

    lines: List[str] = []
    for idx, (e1, e2) in enumerate(emotions, start=1):
        lines.append(f"Krog {idx}:")
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(e1)
        agent2.update_emotion(e2)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
