from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, e1: float = 0.8, e2: float = 0.6) -> List[str]:
    """Simulate a philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Update emotions and attempt transitions
    agent1.update_emotion(e1)
    old_state = agent1.history[-1]
    new_state = agent1.transition()
    if new_state != old_state:
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    agent2.update_emotion(e2)
    old_state2 = agent2.history[-1]
    new_state2 = agent2.transition()
    if new_state2 != old_state2:
        lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # Final statements after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
