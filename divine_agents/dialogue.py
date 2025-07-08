"""Dialogue helpers allowing agents to debate philosophical concepts."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical debate between two agents.

    The function updates each agent's emotional state, triggers potential
    transitions and collects their responses before and after the change.
    """

    lines: List[str] = []

    # Initial perspectives
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional impact of the discussion
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.4)

    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    # Perspectives after emotions influenced their states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako razumes resnico sedaj?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako razumes resnico sedaj?')}")

    return lines
