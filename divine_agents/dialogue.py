from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a dynamic philosophical dialogue between two agents."""
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions which in turn increase tension
        agent1.update_emotion(agent1.emotion + 0.4, "anger" if agent1.state == 'Ego' else "joy")
        agent2.update_emotion(agent2.emotion + 0.4, "joy" if agent2.state == 'Jaz' else "fear")

        previous_state1 = agent1.state
        previous_state2 = agent2.state
        new_state1 = agent1.transition()
        new_state2 = agent2.transition()
        if new_state1 != previous_state1:
            lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        if new_state2 != previous_state2:
            lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    return lines
