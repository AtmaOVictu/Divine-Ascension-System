from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue where agents may change state."""
    lines: List[str] = []

    # Initial statements reflecting current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions escalate during the discussion
    agent1.update_emotion(0.6)
    prev_state = agent1.state
    agent1.transition()
    if agent1.state != prev_state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.8)
    prev_state = agent2.state
    agent2.transition()
    if agent2.state != prev_state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Responses after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako razumes resnico?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako razumes resnico?')}")

    return lines
