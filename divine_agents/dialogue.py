from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial exchange
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise and influence tension
    agent1.update_emotion(0.8, emotion_type="angry")
    agent1.transition()
    agent1.decay_tension()
    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.state}"
    )

    agent2.update_emotion(0.6, emotion_type="fear")
    agent2.transition()
    agent2.decay_tension()
    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.state}"
    )

    # Second exchange after transitions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
