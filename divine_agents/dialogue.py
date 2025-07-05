from typing import List
from .agent import Agent


def _transition_and_record(agent: Agent, t: float) -> str:
    """Helper to evolve agent and return a descriptive string."""
    new_state = agent.evolve(t)
    return f"{agent.name} prehaja v stanje: {new_state}"


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    lines.append(_transition_and_record(agent1, 0.8))
    lines.append(_transition_and_record(agent2, 0.6))

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
