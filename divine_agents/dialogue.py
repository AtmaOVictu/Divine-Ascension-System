from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate and capture state transitions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Update emotions based on discussion
    agent1.update_emotion(0.8, "anger")
    agent2.update_emotion(0.6, "joy")

    # Perform transitions if thresholds are met
    old_state1 = agent1.state
    old_state2 = agent2.state
    agent1.transition()
    agent2.transition()

    if agent1.state != old_state1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != old_state2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final statements after transition
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
