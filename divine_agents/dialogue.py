from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Interacting :class:`Agent` instances.
    turns:
        Number of conversational turns.
    """
    lines: List[str] = []
    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(agent1.emotion + 0.3)
        agent2.update_emotion(agent2.emotion + 0.3)

        if agent1.should_transition():
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        if agent2.should_transition():
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
