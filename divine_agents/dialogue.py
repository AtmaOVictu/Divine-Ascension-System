from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent,
                           emotion1: str | None = None,
                           emotion2: str | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    emotion1, emotion2:
        Optional names of emotions that influence each agent during the
        conversation. The intensity is fixed to ``0.6`` which is enough to
        trigger a state change.
    """

    if emotion1:
        agent1.set_emotion(emotion1, 0.6)
    if emotion2:
        agent2.set_emotion(emotion2, 0.6)

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
