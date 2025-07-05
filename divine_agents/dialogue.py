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


def advanced_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Conduct a multi-round debate where emotions influence transitions."""
    conversation: List[str] = []

    for i in range(rounds):
        conversation.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        conversation.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # escalate emotions to trigger possible transitions
        agent1.update_emotion(0.4 + i * 0.2, emotion_type="fear")
        conversation.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.3 + i * 0.2, emotion_type="joy")
        conversation.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # final philosophical statements after transitions
    conversation.append(
        f"{agent1.name}: {agent1.respond('Kaj je resnica?')}"
    )
    conversation.append(
        f"{agent2.name}: {agent2.respond('Kaj je resnica?')}"
    )

    return conversation
