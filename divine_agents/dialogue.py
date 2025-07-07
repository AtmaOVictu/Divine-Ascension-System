from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue with emotional dynamics."""
    lines: List[str] = []

    # Initial statements from both agents
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # Emotions rise during the discussion
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    # Agents transition based on updated emotions
    agent1.transition()
    agent2.transition()

    # Record transitions
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Final statements reflecting new states
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    return lines
