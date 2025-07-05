from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Agents first answer from their current state. Hearing each other
    raises their emotional intensity which may trigger a state transition.
    They then answer again from their new perspective.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate enough to potentially trigger transitions
    agent1.update_emotion(min(agent1.emotion + 0.6, 1.0))
    agent2.update_emotion(min(agent2.emotion + 0.6, 1.0))

    prev_state1 = agent1.state
    prev_state2 = agent2.state

    agent1.transition()
    agent2.transition()

    # Announce transitions if they occurred
    if agent1.state != prev_state1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != prev_state2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Responses after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
