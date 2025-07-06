from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Agents taking part in the conversation.

    Returns
    -------
    List[str]
        A list of dialogue lines generated during the exchange.

    Examples
    --------
    >>> a1 = Agent("A1")
    >>> a2 = Agent("A2", state="Jaz")
    >>> philosophical_dialogue(a1, a2)
    ["A1 (Ego): ...", ...]
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Raise emotion above 0.5 so that a state transition will occur
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Slightly lower emotion but still above the threshold
    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
