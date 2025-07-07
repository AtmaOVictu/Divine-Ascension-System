from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate influenced by emotions."""

    lines: List[str] = []
    # Initial positions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions escalate during the discussion
    agent1.update_emotion(0.6, 'jeza')
    lines.append(f"{agent1.name} \u010cutil jezo in napetost naraste.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, 'strah')
    lines.append(f"{agent2.name} \u010duti strah.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of answers
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
