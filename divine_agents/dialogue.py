from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    question = "Kaj je resnica?"
    lines = []

    # Initial statements based on current state
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_name}): "
        f"{agent1.respond(question)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_name}): "
        f"{agent2.respond(question)}"
    )

    # Emotional reactions influencing transitions
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "curiosity")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections after potential transitions
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_name}): "
        f"{agent1.respond(question)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_name}): "
        f"{agent2.respond(question)}"
    )

    return lines
