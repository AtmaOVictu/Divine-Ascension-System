from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue with emotional influence."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(min(agent1.emotion + 0.6, 1.0), emotion_type="strah")
        prev1 = agent1.history[-1]
        new1 = agent1.transition()
        if new1 != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {new1}")

        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0), emotion_type="veselje")
        prev2 = agent2.history[-1]
        new2 = agent2.transition()
        if new2 != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {new2}")
    return lines
