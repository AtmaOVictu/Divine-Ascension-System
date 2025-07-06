from typing import List
from .agent import Agent
from .emotion import Emotion


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.apply_emotion(Emotion("jeza", 0.4, 0.3, 0.1, 0.1))
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.apply_emotion(Emotion("strah", 0.6, 0.2, 0.1, 0.1))
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Conduct multiple dialogue turns updating emotions each round."""
    conversation = []
    for _ in range(turns):
        conversation.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        conversation.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.apply_emotion(Emotion('anger', 0.3, 0.2, 0.1, 0.0))
        agent2.apply_emotion(Emotion('joy', 0.4, 0.3, 0.1, 0.1))

        conversation.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        conversation.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return conversation
