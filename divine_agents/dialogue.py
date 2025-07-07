from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    *,
    emotion1: float = 0.8,
    emotion2: float = 0.6,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First agent participating in the dialogue.
    agent2 : Agent
        Second agent participating in the dialogue.
    emotion1 : float, optional
        Emotion intensity applied to ``agent1`` during the dialogue.
    emotion2 : float, optional
        Emotion intensity applied to ``agent2`` during the dialogue.
    """
    lines: List[str] = []

    # Initial responses based on current states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Apply emotion adjustments and perform transitions
    agent1.update_emotion(emotion1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses after state changes
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
