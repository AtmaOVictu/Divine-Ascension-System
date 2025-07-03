from typing import List, Iterable
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    inc1: Iterable[float] | None = None,
    inc2: Iterable[float] | None = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Emotion increments control how much each agent's emotion is updated on each
    turn, influencing tension and possible state transitions.
    """

    if inc1 is None:
        inc1 = [0.8]
    if inc2 is None:
        inc2 = [0.6]

    rounds = min(len(inc1), len(inc2))
    lines: List[str] = []

    for i in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(inc1[i])
        previous_state = agent1.history[-1]
        if agent1.transition() != previous_state:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        agent2.update_emotion(inc2[i])
        previous_state = agent2.history[-1]
        if agent2.transition() != previous_state:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
