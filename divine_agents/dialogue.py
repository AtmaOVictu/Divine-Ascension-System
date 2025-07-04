from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, cycles: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each cycle updates emotions, attempts state transitions and records responses.
    """
    lines: List[str] = []

    for _ in range(cycles):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Update emotions based on dialogue tension
        agent1.update_emotion('anger' if agent1.state == 'Ego' else 'joy', 0.4)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion('joy', 0.5)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections after dialogue
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
