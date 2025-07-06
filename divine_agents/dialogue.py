from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Simulate a multi-turn philosophical dialogue between two agents."""
    lines: List[str] = []
    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0))
        agent1.update_tension(agent1.tension + 0.2)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0))
        agent2.update_tension(agent2.tension + 0.2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
