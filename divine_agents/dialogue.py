from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1:
        The first participating :class:`Agent`.
    agent2:
        The second participating :class:`Agent`.

    The function increases each agent's emotional state to provoke
    potential transitions and returns every line of the conversation.

    Returns
    -------
    List[str]
        Ordered list of dialogue lines.

    Example
    -------
    >>> a1 = Agent("A1")
    >>> a2 = Agent("A2", state="Jaz")
    >>> philosophical_dialogue(a1, a2)[0].startswith("A1")
    True
    """
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
