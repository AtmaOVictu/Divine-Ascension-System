from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements reflecting each agent's current philosophy
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # First emotional reaction and possible transition
    agent1.apply_emotion("strah", 0.6)
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_name}, napetost {agent1.tension:.2f} -> {agent1.transition()}"
    )

    agent2.apply_emotion("veselje", 0.4)
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_name}, napetost {agent2.tension:.2f} -> {agent2.transition()}"
    )

    # Second round after emotions
    agent1.apply_emotion("radovednost", 0.6)
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_name}, napetost {agent1.tension:.2f} -> {agent1.transition()}"
    )

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
