from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotion."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions arise from the initial exchange
    agent1.set_emotion('anger', 0.6)
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_label} in ima napetost {agent1.tension:.1f}"
    )
    agent2.set_emotion('joy', 0.8)
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_label} in ima napetost {agent2.tension:.1f}"
    )

    # Perform transitions if thresholds are met
    new_state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
