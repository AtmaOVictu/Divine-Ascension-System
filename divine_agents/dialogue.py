from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    agent1.recognize_problem("Iskanje resnice")
    agent2.recognize_problem("Razumevanje odnosov")
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)
    return agent1.dialogue(agent2)
