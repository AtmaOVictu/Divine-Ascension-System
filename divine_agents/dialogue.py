from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation showcases how emotions increase tension and trigger state
    transitions. Each agent states their view of truth, reacts emotionally and
    potentially changes state.
    """

    lines: List[str] = []

    # Initial statements reflecting current states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional responses influence tension and may cause transitions
    agent1.update_emotion(0.8, emotion_name="jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, emotion_name="radovednost")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of responses after potential transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
