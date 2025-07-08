from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation influences each agent's emotion and may trigger a state
    transition when tension or emotion thresholds are exceeded.
    """

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 feels anger due to Agent2's disagreement
    agent1.update_emotion(0.6, 'anger')
    lines.append(f"{agent1.name} čuti {agent1.emotion_type}. Prehod v stanje: {agent1.transition()}")

    # Agent2 remains calm but gains some emotional intensity
    agent2.update_emotion(0.8, 'joy')
    lines.append(f"{agent2.name} čuti {agent2.emotion_type}. Prehod v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
