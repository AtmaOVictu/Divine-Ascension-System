from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on current state
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reaction after hearing the other agent
    agent1.update_emotion(agent1.emotion + 0.8)
    agent2.update_emotion(agent2.emotion + 0.6)

    # Perform possible transitions based on updated states
    prev1, prev2 = agent1.state, agent2.state
    agent1.transition()
    agent2.transition()
    if agent1.state != prev1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != prev2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Exchange principles after transition
    lines.append(f"{agent1.name}: {agent1.philosophical_principle()}")
    lines.append(f"{agent2.name}: {agent2.philosophical_principle()}")

    return lines
