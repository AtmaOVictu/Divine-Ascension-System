from typing import List
from .agent import Agent


def dynamic_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a dialogue where emotions influence state transitions."""
    transcript = []
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotion and tension
        agent1.update_emotion(agent1.emotion + 0.3, label="anger" if agent1.state == 'Ego' else 'joy')
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.3, label="fear" if agent2.state == 'Ego' else 'joy')
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return transcript
