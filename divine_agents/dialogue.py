from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue updating emotions and states."""

    lines: List[str] = []
    for step in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(0.6 + 0.1 * step, "anger")
        prev_state = agent1.history[-1]
        if agent1.transition() != prev_state:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        agent2.update_emotion(0.6 + 0.1 * step, "joy")
        prev_state = agent2.history[-1]
        if agent2.transition() != prev_state:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
