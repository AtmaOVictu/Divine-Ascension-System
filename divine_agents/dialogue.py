from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical exchange where emotions drive transitions."""

    lines: List[str] = []

    # Initial statements rooted in their current ontological states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts with anger which increases tension
    agent1.update_emotion(0.6, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 responds with joy, potentially moving to a higher state
    agent2.update_emotion(0.7, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents reply again from their (potentially) new perspectives
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
