from typing import List
from .agent import Agent


def _set_initial_emotions(agent1: Agent, agent2: Agent) -> None:
    """Helper to set starting emotions for a conversation."""
    agent1.update_emotion("anger", 0.4)
    agent2.update_emotion("calm", 0.3)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    _set_initial_emotions(agent1, agent2)

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Escalate emotions to trigger potential transitions
    agent1.update_emotion("fear", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
