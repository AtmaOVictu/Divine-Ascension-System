from typing import Callable, List, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    inc1: float = 0.0,
    inc2: float = 0.0,
    hooks: Optional[List[Callable[[Agent, Agent], str]]] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First participating agent.
    agent2 : Agent
        Second participating agent.
    inc1 : float, optional
        Emotion increment for ``agent1``.
    inc2 : float, optional
        Emotion increment for ``agent2``.
    hooks : list of callables, optional
        Optional callbacks that return additional dialogue lines.
    """
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(inc1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(inc2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    if hooks:
        for hook in hooks:
            result = hook(agent1, agent2)
            if result:
                lines.append(result)

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
