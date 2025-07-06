from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.feel("joy", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.feel("fear", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_debate(agent1: Agent, agent2: Agent, turns: int = 3) -> List[str]:
    """Run a multi-turn debate adjusting emotions and tension."""
    debate = []
    intensity1 = 0.3
    intensity2 = 0.3
    for _ in range(turns):
        debate.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        debate.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.feel("anger", intensity1)
        debate.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.feel("fear", intensity2)
        debate.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        intensity1 += 0.2
        intensity2 += 0.2

    return debate
