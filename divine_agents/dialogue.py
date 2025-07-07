from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotions rise with each exchange causing potential state transitions.
    """

    lines: List[str] = []

    for _ in range(2):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # escalate emotions and attempt transitions
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        new_state = agent1.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))
        new_state = agent2.transition()
        lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    return lines
