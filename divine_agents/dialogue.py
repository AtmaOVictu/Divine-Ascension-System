from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions arise during debate
    agent1.feel("anger", 0.8)
    previous = agent1.state
    new_state = agent1.transition()
    if new_state != previous:
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    agent2.feel("joy", 0.6)
    previous = agent2.state
    new_state = agent2.transition()
    if new_state != previous:
        lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    # Second exchange reflecting new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
