from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Transition timestamps are included in the dialogue output.
    """
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    agent1_state = agent1.transition()
    if agent1.transition_history:
        ts1 = agent1.transition_history[-1][2].isoformat()
        lines.append(f"{agent1.name} prehaja v stanje: {agent1_state} ob {ts1}")
    else:
        lines.append(f"{agent1.name} ostaja v stanju: {agent1_state}")

    agent2.update_emotion(0.6)
    agent2_state = agent2.transition()
    if agent2.transition_history:
        ts2 = agent2.transition_history[-1][2].isoformat()
        lines.append(f"{agent2.name} prehaja v stanje: {agent2_state} ob {ts2}")
    else:
        lines.append(f"{agent2.name} ostaja v stanju: {agent2_state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
