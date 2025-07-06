from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each round both agents respond to the question "Kaj je resnica?". After
    responding their emotion is slightly increased which may trigger a state
    transition. Returned lines describe the conversation and any transitions.
    """

    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions to simulate tension
        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0), emotion_type=agent1.emotion_type or 'neznano')
        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0), emotion_type=agent2.emotion_type or 'neznano')

        prev_state1 = agent1.state
        prev_state2 = agent2.state
        agent1.transition()
        agent2.transition()

        if agent1.state != prev_state1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev_state2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
