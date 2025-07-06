from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue where agents evolve through states."""
    lines: List[str] = []

    while agent1.state != "Enotnost" and agent2.state != "Enotnost":
        # agents answer according to their current state
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # emotions rise in the discussion which in turn increase tension
        agent1.update_emotion(0.1)
        agent2.update_emotion(0.1)

        # record previous states to detect transitions
        prev1, prev2 = agent1.state, agent2.state
        agent1.transition()
        agent2.transition()

        if agent1.state != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

        # safeguard against infinite loops
        if len(lines) > 50:
            break

    return lines
