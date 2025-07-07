from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Both agents update their emotional state during the conversation, which may
    trigger state transitions. The dialogue reflects their current ontological
    perspectives and emotions.
    """

    lines: List[str] = []

    # Initial exchange about truth
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions leading to possible transitions
    agent1.update_emotion(0.6, "fear")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again from their new states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kako vidiš resnico?')}"
    )
    return lines
