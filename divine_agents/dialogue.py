from typing import List
from .agent import Agent
from .environment import Environment


def philosophical_dialogue(agent1: Agent, agent2: Agent, env: Environment | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The optional ``env`` parameter allows environmental factors to modify
    the agents before they transition states.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    if env is not None:
        env.influence(agent1)
        env.influence(agent2)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
