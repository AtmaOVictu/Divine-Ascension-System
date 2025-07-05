from typing import List
from .agent import Agent, DynamicAgent


def _advance(agent: Agent) -> str:
    """Advance agent state using either evolve or transition."""
    if isinstance(agent, DynamicAgent):
        return agent.evolve()
    return agent.transition()


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {_advance(agent1)}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {_advance(agent2)}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
