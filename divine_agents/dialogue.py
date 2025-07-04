from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0))

        new_state1 = agent1.transition()
        new_state2 = agent2.transition()

        lines.append(f"{agent1.name} se premakne v: {new_state1}")
        lines.append(f"{agent2.name} se premakne v: {new_state2}")
    return lines
