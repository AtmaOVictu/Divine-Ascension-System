from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents."""
    lines: List[str] = []

    for i in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # escalate emotions which in turn increases tension
        agent1.update_emotion(0.6, "anger" if i == 0 else agent1.emotion_type)
        agent2.update_emotion(0.6, "joy" if i == 0 else agent2.emotion_type)

        prev_state1 = agent1.state
        prev_state2 = agent2.state
        state1 = agent1.transition()
        state2 = agent2.transition()

        if state1 != prev_state1:
            lines.append(f"{agent1.name} prehaja v stanje: {state1}")
        if state2 != prev_state2:
            lines.append(f"{agent2.name} prehaja v stanje: {state2}")

    return lines
