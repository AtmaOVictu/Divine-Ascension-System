from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical debate between two agents.

    The function showcases emotional influence on tension and resulting state
    transitions. Each agent responds to the same question twice, potentially in
    different states.
    """

    lines: List[str] = []

    # Initial statements based on starting states
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # Emotional reaction to the discussion increases tension
    agent1.update_emotion(0.6, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, "navdih")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round after potential transitions
    lines.append(agent1.speak("Kako vidiš resnico zdaj?"))
    lines.append(agent2.speak("Kako vidiš resnico zdaj?"))

    return lines
