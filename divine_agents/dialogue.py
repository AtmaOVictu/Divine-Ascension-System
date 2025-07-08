from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive state changes."""
    lines: List[str] = []

    # Initial statements reflecting current philosophical stance
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions arise from the discussion
    agent1.update_emotion(0.6, "anger")
    agent2.update_emotion(0.4, "fear")
    lines.append(f"{agent1.name} cuti {agent1.emotion_name}, napetost {agent1.tension:.1f}")
    lines.append(f"{agent2.name} cuti {agent2.emotion_name}, napetost {agent2.tension:.1f}")

    # First transition based on new tension/emotion levels
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Additional emotion to drive potential second transition
    agent2.update_emotion(0.7, "joy")
    lines.append(f"{agent2.name} cuti {agent2.emotion_name}, napetost {agent2.tension:.1f}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
