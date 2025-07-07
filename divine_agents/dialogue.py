from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""

    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.6, "fear")
    lines.append(f"{agent1.name} čuti strah.")
    agent1.transition()
    lines.append(f"{agent1.name} je zdaj v stanju: {agent1.state}")

    agent2.update_emotion(0.8, "joy")
    lines.append(f"{agent2.name} čuti veselje.")
    agent2.transition()
    lines.append(f"{agent2.name} je zdaj v stanju: {agent2.state}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
