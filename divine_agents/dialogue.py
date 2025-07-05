from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotion influences
    agent1.express_emotion("anger", 0.6)
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_name} in ima napetost {agent1.tension:.1f}"
    )

    agent2.express_emotion("joy", 0.8)
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_name} in ima napetost {agent2.tension:.1f}"
    )

    # Possible transitions after emotions are expressed
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
