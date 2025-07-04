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


def dynamic_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Conduct a multi-round philosophical debate between agents.

    The function iteratively collects each agent's response, updates
    their emotional state to simulate rising tension when they disagree
    and triggers transitions where appropriate.
    """
    conversation: List[str] = []
    for _ in range(rounds):
        conversation.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        conversation.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        if agent1.state != agent2.state:
            agent1.update_emotion(0.6)
            agent2.update_emotion(0.6)
        else:
            agent1.update_emotion(0.2)
            agent2.update_emotion(0.2)

        conversation.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        conversation.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return conversation
