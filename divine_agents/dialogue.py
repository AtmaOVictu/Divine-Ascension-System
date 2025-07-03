from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # initial statements
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # emotions rise during conversation
    agent1.update_emotion(0.8, "jezo")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "strah")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # second round after transitions
    lines.append(agent1.speak("Kaj pa sedaj meniš?"))
    lines.append(agent2.speak("Kaj pa sedaj meniš?"))
    return lines
