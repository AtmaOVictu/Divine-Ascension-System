from typing import List
from .agent import Agent
import random


def debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a philosophical debate influenced by emotions."""
    transcript = []
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # emotions rise based on interaction
        agent1.feel(random.choice(['fear', 'joy', 'anger']), random.uniform(0.2, 0.4))
        agent2.feel(random.choice(['fear', 'joy', 'anger']), random.uniform(0.2, 0.4))

        new_state1 = agent1.transition()
        new_state2 = agent2.transition()
        transcript.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        transcript.append(f"{agent2.name} prehaja v stanje: {new_state2}")
    return transcript
