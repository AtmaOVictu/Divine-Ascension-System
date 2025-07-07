from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate influenced by emotions and tension."""

    lines: List[str] = []

    # Initial positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions escalate during the debate
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of dialogue after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
