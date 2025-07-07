from typing import List

from .agent import Agent
from .emotional_agent import EmotionalAgent


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


def emotional_dialogue(agent1: EmotionalAgent, agent2: EmotionalAgent) -> List[str]:
    """Dialogue that also tracks emotional descriptions."""
    lines = []
    lines.append(agent1.describe_emotion())
    lines.append(agent2.describe_emotion())
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "anger")
    lines.append(agent1.describe_emotion())
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "growth")
    lines.append(agent2.describe_emotion())
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.make_decision('Razmisli o resnici')}")
    lines.append(f"{agent2.name}: {agent2.make_decision('Razmisli o resnici')}")
    return lines
