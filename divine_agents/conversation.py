from typing import List
from .agent import Agent


def debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a debate where agents update emotions and transition states."""
    transcript: List[str] = []
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions and tension
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0), emotion_type="anger")
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0), emotion_type="joy")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return transcript
