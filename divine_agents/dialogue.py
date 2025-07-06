from typing import List, Optional
from .agent import Agent
from .environment import Environment


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    env1: Optional[Environment] = None,
    env2: Optional[Environment] = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    if env1:
        lines.append(f"{agent1.name} prehaja v stanje: {env1.influence(agent1)}")
    else:
        agent1.update_emotion(0.8)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    if env2:
        lines.append(f"{agent2.name} prehaja v stanje: {env2.influence(agent2)}")
    else:
        agent2.update_emotion(0.6)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
