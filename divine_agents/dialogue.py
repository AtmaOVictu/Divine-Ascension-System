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


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a debate where emotion influences state transitions."""
    transcript: List[str] = []
    for _ in range(rounds):
        # Emotional reactions influence tension before answering.
        agent1.update_emotion(agent1.emotion + 0.6, "anger")
        agent2.update_emotion(agent2.emotion + 0.6, "joy")

        transcript.append(
            f"{agent1.name} prehaja v stanje: {agent1.transition()}"
        )
        transcript.append(
            f"{agent2.name} prehaja v stanje: {agent2.transition()}"
        )

        # Agents respond from their new states and emotional viewpoints.
        transcript.append(
            f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): "
            f"{agent1.respond('Kaj je resnica?')}"
        )
        transcript.append(
            f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): "
            f"{agent2.respond('Kaj je resnica?')}"
        )
    return transcript
