from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotions of the agents are increased during the exchange which may trigger
    state transitions.  The resulting lines capture each step of the debate.
    """
    lines: List[str] = []

    # Initial statements
    for ag in (agent1, agent2):
        lines.append(f"{ag.name} ({ag.state}): {ag.respond('Kaj je resnica?')}")

    # Emotion rises during conversation
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents answer again from their possibly new states
    for ag in (agent1, agent2):
        lines.append(f"{ag.name} ({ag.state}): {ag.respond('Kaj je resnica?')}")

    return lines
