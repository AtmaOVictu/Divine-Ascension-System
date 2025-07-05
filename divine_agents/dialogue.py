from typing import List

from .agent import Agent
from .debate import Debate


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    debate = Debate(agent1, agent2)
    response1, response2 = debate.step()
    return [response1, response2]
