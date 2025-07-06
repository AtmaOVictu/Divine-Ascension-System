from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate
    agent1.update_emotion(0.8, "jeza")
    agent2.update_emotion(0.6, "radovednost")
    lines.append(f"{agent1.name} čuti {agent1.emotion_type} in napetost {agent1.tension:.1f}")
    lines.append(f"{agent2.name} čuti {agent2.emotion_type} in napetost {agent2.tension:.1f}")

    # Perform transitions based on updated states
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses from the new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
