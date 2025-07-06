from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Agents experience emotions that may trigger transitions
    old_state = agent1.state
    agent1.update_emotion(0.8, "fear")
    new_state = agent1.transition()
    if new_state != old_state:
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    old_state = agent2.state
    agent2.update_emotion(0.6, "joy")
    new_state = agent2.transition()
    if new_state != old_state:
        lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
