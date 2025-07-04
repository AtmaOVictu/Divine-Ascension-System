from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2 : Agent
        Participants of the dialogue.
    rounds : int, optional
        Number of interaction rounds to perform.

    Returns
    -------
    List[str]
        Dialogue lines generated during the interaction.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"

    for _ in range(rounds):
        lines.append(agent1.speak(question))
        lines.append(agent2.speak(question))

        # Increase emotions and attempt transitions
        agent1.update_emotion(agent1.emotion + 0.3)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.3)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflection
    lines.append(agent1.speak(question))
    lines.append(agent2.speak(question))
    return lines
