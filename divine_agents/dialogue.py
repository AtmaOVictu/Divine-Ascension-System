from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during debate
    agent1.update_emotion(0.6, "anger")
    agent2.update_emotion(0.4, "joy")

    # Possible transitions due to increased tension/emotion
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(agent1.analyze())

    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(agent2.analyze())

    # Second exchange after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Further escalation can trigger another transition
    agent1.update_emotion(0.8, "fear")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    agent2.update_emotion(0.8, "anger")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
