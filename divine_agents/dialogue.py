from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents over several rounds."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        agent1.update_emotion(agent1.emotion + 0.4)
        new_state = agent1.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        agent2.update_emotion(agent2.emotion + 0.4)
        new_state = agent2.transition()
        lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    return lines
