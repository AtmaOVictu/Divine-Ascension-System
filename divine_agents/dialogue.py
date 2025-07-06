from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue until one agent reaches Enotnost."""
    lines: List[str] = []
    steps = 0
    while agent1.state != "Enotnost" and agent2.state != "Enotnost" and steps < 10:
        # Each agent responds from their current state
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions rise during the debate
        agent1.update_emotion(0.1)
        agent2.update_emotion(0.1)

        # Additional tension builds up
        agent1.update_tension(0.05)
        agent2.update_tension(0.05)

        # Possible transitions
        prev1 = agent1.state
        prev2 = agent2.state
        agent1.transition()
        agent2.transition()

        if agent1.state != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

        steps += 1

    # Final responses from current states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
