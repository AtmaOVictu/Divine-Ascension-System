from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # Emotional reactions influence tension and state transitions
    agent1.update_emotion("anger", 0.6)
    lines.append(agent1.transition_line())

    agent2.update_emotion("fear", 0.8)
    lines.append(agent2.transition_line())

    # Responses after transition
    lines.append(agent1.speak("Kako dojemaš resnico?"))
    lines.append(agent2.speak("Kako dojemaš resnico?"))

    return lines
