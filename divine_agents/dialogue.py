from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial question about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Intensify emotions and tensions to trigger new boxes
    agent1.update_emotion(0.9)
    agent2.update_tension(0.9)

    if agent1.new_boxes:
        lines.append(f"{agent1.name} has entered a new phase: {agent1.new_boxes[-1]}")
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    if agent2.new_boxes:
        lines.append(f"{agent2.name} has entered a new phase: {agent2.new_boxes[-1]}")
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    # Final responses after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
