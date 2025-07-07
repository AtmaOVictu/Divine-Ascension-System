from typing import List
from .agent import Agent, EtnegA


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


def reflective_dialogue(agent: Agent) -> List[str]:
    """Generate dialogue between an agent and its reflective counterpart."""
    mirror = EtnegA(agent)
    lines = []
    lines.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
    lines.append(f"{mirror.name} ({mirror.state}): {mirror.respond('Kaj je resnica?')}")

    agent.update_emotion(0.8)
    mirror.update_emotion(agent.emotion)
    lines.append(f"{agent.name} prehaja v stanje: {agent.transition()}")
    lines.append(f"{mirror.name} prehaja v stanje: {mirror.transition()}")

    lines.append(f"{agent.name}: {agent.respond('Kaj je resnica?')}")
    lines.append(f"{mirror.name}: {mirror.respond('Kaj je resnica?')}")
    return lines
