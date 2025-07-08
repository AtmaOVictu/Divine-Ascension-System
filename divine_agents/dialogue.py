from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Conversing agents.
    rounds:
        Number of interaction rounds after the initial statements.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    for _ in range(rounds):
        # Emotions influence tension which may cause a transition
        agent1.update_emotion(0.8)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.6)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(agent1.speak("Kaj je resnica?"))
        lines.append(agent2.speak("Kaj je resnica?"))

    return lines
