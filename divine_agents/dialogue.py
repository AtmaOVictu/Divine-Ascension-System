from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The agents initially answer a question about truth according to their
    current state.  Their emotions are then intensified which may trigger a
    state transition.  Afterwards they respond once more in their new states.
    """

    lines: List[str] = []

    # Initial responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Increase emotions which also raises tension
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after state changes
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
