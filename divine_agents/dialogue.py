from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial exchange
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # Emotions rise as debate unfolds
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.7)

    # Possible transitions triggered by increased tension or emotion
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange reflects new states
    lines.append(agent1.speak("Kako razumeš resnico?"))
    lines.append(agent2.speak("Kako razumeš resnico?"))

    return lines
