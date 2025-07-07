from __future__ import annotations

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, *, turns: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Participants in the dialogue.
    turns:
        Number of conversational exchanges.  Each turn consists of a statement
        from ``agent1`` followed by a response from ``agent2``.  After each
        response both agents attempt a state transition based on their updated
        emotional tension.
    """

    lines: List[str] = []
    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        # Agent2 reacts with slightly increased emotion which may trigger a transition.
        agent2.update_emotion(min(agent2.emotion_level + 0.3, 1.0), emotion_type=agent2.emotion_type or 'sorrow')
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        # Agent1 reacts to agent2's response as well.
        agent1.update_emotion(min(agent1.emotion_level + 0.4, 1.0), emotion_type=agent1.emotion_type or 'anger')
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    return lines
