from typing import List
from .agent import Agent


def debate(agent1: Agent, agent2: Agent, turns: int = 3) -> List[str]:
    """Run a dynamic debate about truth between two agents.

    Each turn agents respond based on their current ontological state. Emotions
    are increased to raise tension and may cause state transitions when the
    thresholds are met.
    """
    lines: List[str] = []
    for turn in range(turns):
        # Agents express their view on truth.
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotion to simulate rising tension in the debate.
        agent1.update_emotion(0.3 + 0.1 * turn)
        previous1 = agent1.state
        new1 = agent1.transition()
        if new1 != previous1:
            lines.append(f"{agent1.name} prehaja v stanje: {new1}")

        agent2.update_emotion(0.2 + 0.2 * turn)
        previous2 = agent2.state
        new2 = agent2.transition()
        if new2 != previous2:
            lines.append(f"{agent2.name} prehaja v stanje: {new2}")

    return lines
