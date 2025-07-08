from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, steps: int = 2) -> List[str]:
    """Simulate a dynamic philosophical dialogue between two agents.

    Each step the agents exchange responses, influence each other's tension
    levels and attempt state transitions. The conversation reflects their
    current ontological and emotional states.
    """

    lines: List[str] = []
    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)
    for _ in range(steps):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.influence(agent2)
        agent2.influence(agent1)
        agent1.decay_tension()
        agent2.decay_tension()

        new_state1 = agent1.transition()
        new_state2 = agent2.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    return lines
