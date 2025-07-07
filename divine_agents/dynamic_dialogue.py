"""Dialogue utilities for reflective agents."""

from typing import List
from .reflective_agent import ReflectiveAgent


def dynamic_philosophical_dialogue(agent1: ReflectiveAgent, agent2: ReflectiveAgent) -> List[str]:
    """Run a short dialogue updating emotions and beliefs."""
    lines = []
    # initial responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # emotional reactions influence tension
    agent1.update_emotion(0.6)
    agent1.update_belief("Poslušam tvoje argumente.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8)
    agent2.update_belief("Premišljujem tvoje besede.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # final responses after reflection
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
