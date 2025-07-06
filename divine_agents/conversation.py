from typing import List
from .agent import Agent


def dynamic_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a dialogue with emotional escalation and state transitions."""
    transcript: List[str] = []
    for i in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions
        agent1.set_emotion('anger', 0.3 + 0.2 * i)
        agent2.set_emotion('joy', 0.2 + 0.2 * i)

        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return transcript
