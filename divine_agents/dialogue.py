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


def emotional_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a multi-round debate where emotions drive state transitions."""
    conversation = []
    for _ in range(rounds):
        conversation.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        conversation.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        conversation.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))
        conversation.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return conversation
