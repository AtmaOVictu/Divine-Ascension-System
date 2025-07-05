from typing import List
from .agent import Agent


def engage_agents(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Conduct a multi-round dialogue updating emotions and checking transitions."""
    transcript: List[str] = []
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        if agent1.state != agent2.state:
            agent1.update_emotion(0.6, 'anger')
            agent2.update_emotion(0.6, 'fear')
        else:
            agent1.update_emotion(0.3, 'joy')
            agent2.update_emotion(0.3, 'joy')
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return transcript
