from typing import List
import numpy as np

from .agent import Agent
from .emotion import Emotion
from .karma import Karma


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


def emotional_dialogue(agent1: Agent, agent2: Agent, emotion1: Emotion, emotion2: Emotion) -> List[str]:
    """Dialogue demonstrating emotional influence and karma."""
    karma1 = Karma()
    karma2 = Karma()
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions influence tension
    agent1.update_emotion(emotion1.anger + emotion1.fear)
    emotion1.transition()
    karma1.update(emotion1, np.random.rand(2, 2))
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion2.anger + emotion2.fear)
    emotion2.transition()
    karma2.update(emotion2, np.random.rand(2, 2))
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    lines.append(f"Karma1: {karma1.karma_value}, Karma2: {karma2.karma_value}")
    return lines
