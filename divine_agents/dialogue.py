from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, iterations: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2: Agent
        The agents engaging in conversation.
    iterations: int
        Number of exchanges to simulate.
    """

    lines: List[str] = []
    for i in range(iterations):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions rise as the debate continues
        agent1.update_emotion(agent1.emotion + 0.4, label=agent1.emotion_label or 'jeza')
        agent2.update_emotion(agent2.emotion + 0.4, label=agent2.emotion_label or 'strah')

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
