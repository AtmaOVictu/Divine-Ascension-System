from typing import List
from .agent import Agent
from .dialogue import philosophical_dialogue


def debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Run an extended debate where emotions drive further transitions."""
    lines = philosophical_dialogue(agent1, agent2)

    # Further emotional shifts
    agent1.set_emotion("fear", 0.4)
    agent1.update_tension(0.9)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("anger", 0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
