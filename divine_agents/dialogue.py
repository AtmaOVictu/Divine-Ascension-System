from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive transitions."""
    lines = []
    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(0.4 + 0.2 * i)
        previous = agent1.state
        state = agent1.transition()
        if state != previous:
            lines.append(f"{agent1.name} prehaja v stanje: {state}")

        agent2.update_emotion(0.5 + 0.1 * i)
        previous = agent2.state
        state = agent2.transition()
        if state != previous:
            lines.append(f"{agent2.name} prehaja v stanje: {state}")

    return lines
