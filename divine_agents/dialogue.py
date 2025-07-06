from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, topic: str = "Kaj je resnica?") -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}, e={agent1.emotion:.1f}): {agent1.respond(topic)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, e={agent2.emotion:.1f}): {agent2.respond(topic)}"
    )

    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} čustvo {agent1.emotion:.1f}, napetost {agent1.tension:.1f} -> {agent1.transition()}"
    )

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} čustvo {agent2.emotion:.1f}, napetost {agent2.tension:.1f} -> {agent2.transition()}"
    )

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(topic)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(topic)}")
    return lines
