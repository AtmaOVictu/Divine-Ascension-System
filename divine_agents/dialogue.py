from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue.

    Parameters
    ----------
    agent1, agent2 : Agent
        Participants in the debate.
    rounds : int, optional
        Number of conversational exchanges to simulate.

    Returns
    -------
    List[str]
        Lines representing the dialogue.
    """
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(agent1.speak("Kaj je resnica?"))
        lines.append(agent2.speak("Kaj je resnica?"))

        # escalate emotional involvement through conversation
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
