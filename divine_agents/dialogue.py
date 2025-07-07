from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The dialogue illustrates how emotions influence tension and subsequently
    trigger state transitions. Both agents respond according to their current
    ontological state and emotional feeling.
    """

    lines = []
    # Initial exchange
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise after the first exchange
    agent1.update_emotion(0.6, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_tension(0.8)
    agent2.update_emotion(0.4, "strah")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again from their new states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa absolutna resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa absolutna resnica?')}"
    )

    return lines
