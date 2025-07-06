from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a dialogue where emotions and tension influence state changes."""

    lines: List[str] = []

    for _ in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(min(1.0, agent1.emotion + 0.4))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.4))

        agent1.influence(agent2)
        agent2.influence(agent1)

        transitioned1 = agent1.transition()
        transitioned2 = agent2.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {transitioned1}")
        lines.append(f"{agent2.name} prehaja v stanje: {transitioned2}")

    return lines
