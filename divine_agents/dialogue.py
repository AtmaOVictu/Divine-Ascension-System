from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where agents may transition states."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(agent1.emotion + 0.4)
        new_state1 = agent1.transition()
        if agent1.history[-1] != agent1.history[-2]:
            lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

        agent2.update_emotion(agent2.emotion + 0.3)
        new_state2 = agent2.transition()
        if agent2.history[-1] != agent2.history[-2]:
            lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")
    return lines
