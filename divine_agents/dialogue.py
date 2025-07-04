from typing import List

from .agent import Agent
from .emotion import Emotion


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Update emotions and tension to trigger transitions
    agent1.update_emotion(Emotion(energy=0.5, tension=0.5))
    agent1.update_tension(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(Emotion(energy=0.4, tension=0.4))
    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Follow-up statements in new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
