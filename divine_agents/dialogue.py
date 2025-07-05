from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a dynamic philosophical dialogue between two agents."""
    lines: List[str] = []

    for i in range(rounds):
        # Each agent responds according to its current state and mood
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # Update emotion and tension to drive possible transitions
        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0), mood="anger")
        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0), mood="curiosity")

        # Add transition info if state changed
        prev1 = agent1.state
        prev2 = agent2.state
        agent1.transition()
        agent2.transition()
        if agent1.state != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
