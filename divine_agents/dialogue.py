from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent,
                           emotions: Tuple[Tuple[str, float], Tuple[str, float]]) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First debating agent.
    agent2 : Agent
        Second debating agent.
    emotions : Tuple
        A pair of (emotion_label, intensity) tuples defining how each agent feels
        during the exchange.
    """
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(*emotions[0])
    lines.append(f"{agent1.name} doživlja {agent1.emotion_label} in prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(*emotions[1])
    lines.append(f"{agent2.name} doživlja {agent2.emotion_label} in prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
