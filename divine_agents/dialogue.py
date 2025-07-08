from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, question: str = "Kaj je resnica?") -> List[str]:
    """Simulate a philosophical dialogue and emotional evolution."""
    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # update emotions based on language and state
    agent1.emotional_box.update_emotion()
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    agent2.emotional_box.update_emotion()
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    # final statements reflecting new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
