from typing import List
from .agent import Agent


def run_debate(agent1: Agent, agent2: Agent, turns: int = 3) -> List[str]:
    """Run a multi-turn philosophical debate between two agents.

    Each turn agents respond according to their current state, then update
    their emotional intensity which may trigger state transitions.
    """
    lines: List[str] = []
    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotion to drive transitions
        agent1.update_emotion(min(1.0, agent1.emotion + 0.4))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.4))

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
