from typing import List

from .agent import Agent


def conduct_debate(agent1: Agent, agent2: Agent, iterations: int = 2) -> List[str]:
    """Simulate a debate between two agents.

    Each iteration both agents respond based on their ontological state. Their
    emotions are updated to showcase changing tension which may lead to state
    transitions.
    """
    transcript = []
    for _ in range(iterations):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Example emotion updates
        agent1.set_emotion('anger', agent1.emotions.get('anger', 0.0) + 0.3)
        agent2.set_emotion('joy', agent2.emotions.get('joy', 0.0) + 0.2)

        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return transcript
