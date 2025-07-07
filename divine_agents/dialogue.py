from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation evolves as each agent experiences emotions that may
    trigger state transitions, reflecting how perspective on truth changes.
    """

    lines: List[str] = []

    # Initial statements reflecting their starting states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions arise during the debate
    agent1.update_emotion(0.8, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # After emotions influence their perspective, ask again
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
