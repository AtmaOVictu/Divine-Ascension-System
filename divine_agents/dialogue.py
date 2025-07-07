from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function modifies agents' emotional states, which may trigger
    ontological transitions based on predefined thresholds.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts with anger to Agent2's relativism
    agent1.experience_emotion("jeza", 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 responds with joy, feeling understood
    agent2.experience_emotion("veselje", 0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round after emotional changes
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
