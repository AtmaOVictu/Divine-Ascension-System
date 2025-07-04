from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Conversing :class:`Agent` instances.
    rounds:
        Number of interaction rounds to perform.
    """

    lines: List[str] = []
    topic = "Kaj je resnica?"

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak(topic)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak(topic)}")

        # Emotions escalate slightly after each exchange
        agent1.adjust_emotion(0.3)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.adjust_emotion(0.4)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
