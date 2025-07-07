from typing import List
from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 1, step: float = 0.3) -> List[str]:
    """Engage two agents in a multi-round philosophical debate."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(agent1.emotion + step)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + step)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Backward-compatible wrapper around ``philosophical_debate``."""
    return philosophical_debate(agent1, agent2, rounds=1, step=0.6)
