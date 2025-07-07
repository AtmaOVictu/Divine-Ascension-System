from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

from .emotions import EmotionalAgent, EmotionalBox


def emotional_dialogue(agent1: Agent, agent2: Agent, emotion1: str, emotion2: str) -> List[str]:
    """Simulate dialogue where emotions influence state transitions."""
    lines: List[str] = []
    e_agent = EmotionalAgent()
    box1 = EmotionalBox(emotion1)
    box2 = EmotionalBox(emotion2)

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    lines.append(f"{agent1.name} emotion -> {box1.process(e_agent)}")
    lines.append(f"{agent2.name} emotion -> {box2.process(e_agent)}")

    emotion_map = {'fear': 0.6, 'anger': 0.8, 'joy': 0.4}
    agent1.update_emotion(emotion_map.get(emotion1, 0.3))
    agent2.update_emotion(emotion_map.get(emotion2, 0.3))

    if agent1.tension > 0.7 or agent1.emotion > 0.5:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    if agent2.tension > 0.7 or agent2.emotion > 0.5:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
