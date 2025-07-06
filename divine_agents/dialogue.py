"""Tools for simulating philosophical conversations between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The agents begin by stating their current view of truth. Their emotions are
    then adjusted which may cause state transitions. The resulting dialogue
    reflects any changes in state and mood.
    """

    lines: List[str] = []
    # initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # update emotions which influences tension and may trigger transitions
    agent1.update_emotion(0.8, mood="anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, mood="joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # responses after possible transitions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
