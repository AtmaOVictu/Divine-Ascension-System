from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each turn agents express their view on truth, update their emotions and
    potentially transition to a new ontological state.
    """

    lines: List[str] = []

    for _ in range(turns):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion("fear", 0.4)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion("joy", 0.6)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
