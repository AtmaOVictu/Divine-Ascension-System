from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(agent1.dialogue_line("Kaj je resnica?"))
    lines.append(agent2.dialogue_line("Kaj je resnica?"))

    agent1.update_emotion(0.8, mood="anger")
    lines.append(agent1.transition_line())

    agent2.update_emotion(0.6, mood="joy")
    lines.append(agent2.transition_line())

    lines.append(agent1.dialogue_line("Kako vidiš resnico sedaj?"))
    lines.append(agent2.dialogue_line("Kako vidiš resnico sedaj?"))

    return lines
