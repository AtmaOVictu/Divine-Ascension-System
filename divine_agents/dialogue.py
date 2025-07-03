from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a mini philosophical debate between two agents.

    The function has two phases. First, each agent answers the question
    "Kaj je resnica?" ("What is truth?") according to its current ontological
    state. Next, their emotions are heightened which may cause a state
    transition based on the thresholds documented in :class:`Agent`.

    Parameters
    ----------
    agent1, agent2:
        The participating agents.

    Returns
    -------
    List[str]
        Lines of dialogue representing the interaction.

    Example
    -------
    >>> a1 = Agent("A1")
    >>> a2 = Agent("A2", state="Jaz")
    >>> for line in philosophical_dialogue(a1, a2):
    ...     print(line)
    A1 (Ego): Resnica je absolutna in neodvisna od drugih.
    A2 (Jaz): Resnica je relativna, oblikovana z našimi odnosi.
    A1 prehaja v stanje: Jaz
    A2 prehaja v stanje: Enotnost
    A1: Resnica je relativna, oblikovana z našimi odnosi.
    A2: Vse resnice so eno, medsebojno povezane.
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
