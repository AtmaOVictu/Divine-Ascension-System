from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The agents initially answer a question about truth. Their emotions are
    then adjusted which may cause state transitions.  The final responses are
    returned as a list of dialogue lines.
    """

    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # emotions rise during the debate
    agent1.update_emotion(0.8, 'anger')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, 'joy')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # final responses reflect new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa sedaj?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa sedaj?')}")

    return lines
