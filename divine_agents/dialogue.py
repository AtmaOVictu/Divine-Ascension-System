from typing import List

from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    rounds: int = 1,
    emotion_delta1: float = 0.0,
    emotion_delta2: float = 0.0,
    tension_delta1: float = 0.0,
    tension_delta2: float = 0.0,
) -> List[str]:
    """Simulate a philosophical dialogue over multiple rounds.

    Emotion and tension deltas are applied after each round and may trigger
    state transitions.
    """

    lines: List[str] = []
    for _ in range(rounds):
        # Agents respond based on their current state
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # Update emotions and tension
        agent1.update_emotion(agent1.emotion + emotion_delta1)
        agent1.update_tension(agent1.tension + tension_delta1)
        previous = agent1.state
        new_state = agent1.transition()
        if previous != new_state:
            lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

        agent2.update_emotion(agent2.emotion + emotion_delta2)
        agent2.update_tension(agent2.tension + tension_delta2)
        previous = agent2.state
        new_state = agent2.transition()
        if previous != new_state:
            lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    return lines
