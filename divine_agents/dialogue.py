from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # Emotional reactions influence tension and potential transitions
    agent1.update_emotion(0.8, "anger")
    lines.append(agent1.transition_line())

    agent2.update_emotion(0.6, "joy")
    lines.append(agent2.transition_line())

    # Follow-up statements after transitions
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    return lines
