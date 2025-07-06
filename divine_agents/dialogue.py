from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue influenced by emotions."""

    lines: List[str] = []

    # Initial statements
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # Agents feel emotions which may lead to transitions
    agent1.feel("anger", 0.8)
    lines.append(agent1.speak("Kako vidiš resnico sedaj?"))

    agent2.feel("joy", 0.6)
    lines.append(agent2.speak("Kakšna je tvoja resnica sedaj?"))

    return lines
