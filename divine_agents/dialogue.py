from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements about truth
    lines.append(
        f"{agent1.name} ({agent1.state}, RES{agent1.phase:03}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, RES{agent2.phase:03}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions that may trigger transitions and phase changes
    agent1.update_emotion(0.8)
    agent1.evolve()
    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.transition()}, faza: RES{agent1.phase:03}"
    )

    agent2.update_emotion(0.6)
    agent2.permute(1)
    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.transition()}, faza: RES{agent2.phase:03}"
    )

    # Follow-up answers from the new perspectives
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
