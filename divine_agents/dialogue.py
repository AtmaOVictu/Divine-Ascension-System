from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The agents start by expressing their current view of truth. Their emotions
    are then updated which may lead to state transitions. Finally, they respond
    again from their new perspectives.
    """

    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8, "anger")
    lines.append(
        f"{agent1.name} čuti jezo in prehaja v stanje: {agent1.transition()}"
    )

    agent2.update_emotion(0.6, "joy")
    lines.append(
        f"{agent2.name} čuti veselje in prehaja v stanje: {agent2.transition()}"
    )

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
