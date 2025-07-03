from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Both agents express their current view of truth, experience an increase of
    emotion (thereby tension) and possibly transition to a new ontological
    state.  The responses after the transition reflect their new state and
    emotional intensity.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during debate
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.6)

    new_state1 = agent1.transition()
    new_state2 = agent2.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # Responses after potential transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa zdaj?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa zdaj?')}")

    return lines
