from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue between two agents over several rounds."""
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotional intensity during the debate
        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0))

        prev1, prev2 = agent1.state, agent2.state
        agent1.transition()
        agent2.transition()

        if agent1.state != prev1:
            agent1.update_emotion(agent1.emotion, "joy")
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev2:
            agent2.update_emotion(agent2.emotion, "joy")
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
