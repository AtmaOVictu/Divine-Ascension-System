from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

from .system import logistic


def dynamic_philosophical_dialogue(agent1: Agent, agent2: Agent, steps: int = 3, k: float = 1.0, c: float = 0.5) -> List[str]:
    """Simulate a dialogue where emotion evolves via a logistic curve."""
    lines: List[str] = []
    if steps <= 1:
        time_steps = [1.0]
    else:
        step = 1 / (steps - 1)
        time_steps = [i * step for i in range(steps)]
    for t in time_steps:
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        new_em1 = logistic(t, k, c)
        new_em2 = logistic(t, k, c)
        agent1.update_emotion(new_em1)
        agent2.update_emotion(new_em2)
        agent1.transition()
        agent2.transition()
    return lines
