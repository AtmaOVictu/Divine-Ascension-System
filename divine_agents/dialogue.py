from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on their current ontological states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions influence tension and may trigger transitions
    agent1.update_emotion(0.8, "jeza")
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_name} in napetost {agent1.tension:.1f}"
    )
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, "veselje")
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_name} in napetost {agent2.tension:.1f}"
    )
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Concluding statements after transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
