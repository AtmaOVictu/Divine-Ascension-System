from typing import List
from .agent import Agent


def interactive_interplay(agent1: Agent, agent2: Agent, iterations: int = 3) -> List[str]:
    """Run an interactive philosophical interplay between two agents.

    Each iteration both agents express their current view of truth, then
    their emotional intensity is increased which may trigger state
    transitions. Collected dialogue lines are returned for inspection.
    """
    lines: List[str] = []
    for i in range(iterations):
        lines.append(f"Krog {i + 1}")
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotional intensity gradually to simulate tension growth
        agent1.update_emotion(0.3 + 0.2 * i)
        agent2.update_emotion(0.4 + 0.1 * i)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
        lines.append("")
    return lines
