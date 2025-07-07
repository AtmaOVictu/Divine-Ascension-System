from typing import List
from .agent import Agent


def debate(agent1: Agent, agent2: Agent, inc1: float = 0.4, inc2: float = 0.4) -> List[str]:
    """Conduct a small debate modifying emotions and causing possible transitions."""
    lines: List[str] = []
    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Update emotions which may increase tension
    agent1.update_emotion(inc1)
    agent2.update_emotion(inc2)

    # Perform transitions if thresholds reached
    new_state1 = agent1.transition()
    new_state2 = agent2.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # Second round of discussion after potential transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
