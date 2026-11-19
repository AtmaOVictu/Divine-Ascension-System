from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotion."""
    lines: List[str] = []

    # Initial positions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotion increases after hearing arguments
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    if agent1.tension > 0.7 or agent1.emotion > 0.5:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    if agent2.tension > 0.7 or agent2.emotion > 0.5:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
