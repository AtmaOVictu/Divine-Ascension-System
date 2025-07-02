from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []
    for _ in range(rounds):
        # Initial statements about truth
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # Emotions rise during discussion which may trigger transitions
        agent1.update_emotion(0.6, "fear")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.6, "sorrow")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections
    lines.append(f"{agent1.name}: {agent1.reflect_on_dilemma()}")
    lines.append(f"{agent2.name}: {agent2.reflect_on_dilemma()}")
    return lines
