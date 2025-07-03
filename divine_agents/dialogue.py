from typing import List
from .agent import Agent


def _increment_emotion(agent: Agent, step: float) -> None:
    """Gradually increase an agent's emotion and tension."""
    new_emotion = min(agent.emotion + step, 1.0)
    agent.update_emotion(new_emotion)


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 3) -> List[str]:
    """Simulate a multi-turn philosophical dialogue between two agents."""
    lines: List[str] = []
    for _ in range(turns):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        _increment_emotion(agent1, 0.2)
        _increment_emotion(agent2, 0.2)

        prev1 = agent1.state
        prev2 = agent2.state
        new1 = agent1.transition()
        new2 = agent2.transition()
        if new1 != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {new1}")
        if new2 != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {new2}")

    return lines
