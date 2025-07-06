from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally to the dialogue
    agent1.update_emotion(0.6)
    prev_state = agent1.state
    new_state = agent1.transition()
    if new_state != prev_state:
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    agent2.update_emotion(0.8)
    prev_state = agent2.state
    new_state = agent2.transition()
    if new_state != prev_state:
        lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    # Final statements after emotional change
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
