from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate and cause movement
    agent1.update_emotion(0.8, emotion_type='anger')
    agent1.move(1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()} in se premakne na {agent1.position}")

    agent2.update_emotion(0.8, emotion_type='joy')
    agent2.move(1)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()} in se premakne na {agent2.position}")

    # Closing statements reflecting new states and emotions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
