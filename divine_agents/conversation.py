from typing import List
from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a multi-round debate adjusting emotions and states."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

        # escalate emotions and check for transitions
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return lines
