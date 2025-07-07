from typing import List
from .voice_agent import VoiceAgent


def philosophical_dialogue(agent1: VoiceAgent, agent2: VoiceAgent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}")

    agent1.update_emotion(agent1.mood, 0.8)
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    agent2.update_emotion(agent2.mood, 0.6)
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name}: {agent2.respond('What is truth?')}")
    return lines
