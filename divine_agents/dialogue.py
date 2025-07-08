from typing import List
from .agent import Agent


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


def dynamic_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue where emotions influence state transitions."""
    discussion = []

    # Initial statements
    discussion.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    discussion.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents adjust emotions based on the other's stance
    agent1.update_emotion(0.6, label="jeza")
    discussion.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.4, label="empatija")
    discussion.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Response after possible transition
    discussion.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    discussion.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return discussion
