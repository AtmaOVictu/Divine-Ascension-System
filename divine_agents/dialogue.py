from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Update emotions which may trigger transitions
    agent1.update_emotion(0.8)
    old_state = agent1.state
    new_state = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    agent2.update_emotion(0.6)
    old_state2 = agent2.state
    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # Simple reward: +1 if moved toward Enotnost
    reward1 = 1.0 if new_state != old_state else 0.0
    reward2 = 1.0 if new_state2 != old_state2 else 0.0

    if hasattr(agent1, "update_policy"):
        agent1.update_policy(old_state, "respond", reward1, new_state)
    if hasattr(agent2, "update_policy"):
        agent2.update_policy(old_state2, "respond", reward2, new_state2)

    # Reflection after transition
    if hasattr(agent1, "reflect"):
        agent1.reflect(agent2.respond(''))
    if hasattr(agent2, "reflect"):
        agent2.reflect(agent1.respond(''))

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
