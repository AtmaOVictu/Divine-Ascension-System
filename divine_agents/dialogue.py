from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation increases emotion and tension to demonstrate dynamic
    state transitions and the creation of new boxes.
    """

    lines: List[str] = []

    # Initial statements based on their starting states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Escalate emotional intensity and tension
    msg1 = agent1.update_emotion(0.9)
    msg2 = agent2.update_tension(0.85)
    if msg1:
        lines.append(msg1)
    if msg2:
        lines.append(msg2)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again from their new perspectives
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Report newly created boxes for clarity in tests
    lines.append(f"{agent1.name} new boxes: {agent1.new_boxes}")
    lines.append(f"{agent2.name} new boxes: {agent2.new_boxes}")

    return lines
