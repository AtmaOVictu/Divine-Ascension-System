from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # Agents update emotions which may trigger transitions
    updates = [(0.8, 0.6), (0.3, 0.2)]
    for u1, u2 in updates:
        agent1.update_emotion(u1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(agent1.speak("Kaj je resnica?"))

        agent2.update_emotion(u2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
        lines.append(agent2.speak("Kaj je resnica?"))

    return lines
