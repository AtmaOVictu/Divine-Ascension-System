from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The dialogue demonstrates how emotional intensity can trigger
    ontological state transitions. Each agent responds according to its
    current state and emotional label.
    """

    lines: List[str] = []

    # Initial viewpoints
    lines.append(agent1.respond("Kaj je resnica?"))
    lines.append(agent2.respond("Kaj je resnica?"))

    # Emotional escalation leading to transitions
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final viewpoints after transition
    lines.append(agent1.respond("Kaj je resnica?"))
    lines.append(agent2.respond("Kaj je resnica?"))

    return lines
