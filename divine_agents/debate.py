from typing import List
from .emotional_agent import EmotionalAgent


def dynamic_philosophical_debate(agent1: EmotionalAgent, agent2: EmotionalAgent) -> List[str]:
    """Simulate an emotionally driven philosophical debate between two agents."""
    transcript: List[str] = []

    transcript.append(f"{agent1.name} ({agent1.state}): {agent1.philosophy('Kaj je resnica?')}")
    transcript.append(f"{agent2.name} ({agent2.state}): {agent2.philosophy('Kaj je resnica?')}")

    agent1.feel('anger')
    prev_state = agent1.state
    agent1.transition()
    if agent1.state != prev_state:
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.feel('fear')
    prev_state = agent2.state
    agent2.transition()
    if agent2.state != prev_state:
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    transcript.append(f"{agent1.name}: {agent1.philosophy('Kaj je resnica?')}")
    transcript.append(f"{agent2.name}: {agent2.philosophy('Kaj je resnica?')}")

    return transcript
