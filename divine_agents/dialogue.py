from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a philosophical dialogue where emotions trigger transitions."""

    lines: List[str] = []
    for i in range(rounds):
        # Each agent answers based on current state and emotion
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # Emotion intensifies through the discussion
        agent1.set_emotion("anger" if i == 0 else "joy", 0.4)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.set_emotion("calm", 0.3)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
