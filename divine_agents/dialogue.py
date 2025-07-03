from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_debate(agent1: Agent, agent2: Agent,
                   emotions1: List[float], emotions2: List[float]) -> List[str]:
    """Simulate a multi-step debate applying emotions to agents.

    Each step updates the agents' emotions and triggers state transitions
    when thresholds are exceeded. The agents then respond based on their
    new states.

    Parameters
    ----------
    agent1 : Agent
        The first debating agent.
    agent2 : Agent
        The second debating agent.
    emotions1 : List[float]
        Sequence of emotion intensities applied to ``agent1`` in each step.
    emotions2 : List[float]
        Sequence of emotion intensities applied to ``agent2`` in each step.

    Returns
    -------
    List[str]
        Dialogue lines produced during the debate.
    """
    lines: List[str] = []
    for e1, e2 in zip(emotions1, emotions2):
        agent1.update_emotion(e1)
        agent2.update_emotion(e2)
        agent1.transition()
        agent2.transition()
        lines.append(f"{agent1.name} ({agent1.state}): "
                     f"{agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): "
                     f"{agent2.respond('Kaj je resnica?')}")
    return lines
