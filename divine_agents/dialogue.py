from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Both agents start in their current states, express their views, then their
    emotions are updated which may trigger state transitions. They respond once
    more after any transitions occur.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Update emotional states which influences tension and may trigger changes.
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.4)

    new_state1 = agent1.transition()
    new_state2 = agent2.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
