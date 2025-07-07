from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The dialogue demonstrates how emotions influence tension and can lead to
    state transitions.  Each agent responds according to its ontological and
    emotional state.
    """

    lines: List[str] = []

    # Initial perspectives
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise during the debate
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again after transitions
    lines.append(
        f"{agent1.name} ({agent1.emotion_label}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.emotion_label}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
