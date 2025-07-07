from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Generate a short philosophical dialogue influenced by emotions."""

    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}"
    )

    # Emotions rise as the debate intensifies
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    agent2.update_emotion(0.8, "joy")
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('And now?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('And now?')}"
    )
    return lines
