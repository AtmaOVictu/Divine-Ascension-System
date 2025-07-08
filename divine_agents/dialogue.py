from typing import List, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion_inc1: float = 0.8,
    emotion_inc2: float = 0.6,
    tension_inc1: float = 0.0,
    tension_inc2: float = 0.0,
    extra_turns: Optional[List[str]] = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2: Agent
        Participants in the conversation.
    emotion_inc1, emotion_inc2: float, optional
        Amount to increase each agent's emotion before transitioning.
    tension_inc1, tension_inc2: float, optional
        Amount to increase each agent's tension before transitioning.
    extra_turns: List[str], optional
        Additional custom lines to append to the dialogue.
    """

    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(emotion_inc1)
    agent1.update_tension(agent1.tension + tension_inc1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion_inc2)
    agent2.update_tension(agent2.tension + tension_inc2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    if extra_turns:
        lines.extend(extra_turns)

    return lines
