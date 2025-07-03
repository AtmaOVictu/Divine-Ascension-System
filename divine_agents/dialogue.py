from typing import List, Sequence, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    prompts: List[str],
    emotion_increments: Optional[Sequence[float]] = None,
) -> List[str]:
    """Simulate a philosophical dialogue using provided prompts.

    Parameters
    ----------
    agent1 : Agent
        First participating agent.
    agent2 : Agent
        Second participating agent.
    prompts : List[str]
        Questions or statements to guide the dialogue.
    emotion_increments : Optional[Sequence[float]], default ``None``
        Two values representing the emotion level each agent should
        update to during the exchange. Defaults to ``(0.8, 0.6)`` when
        not provided.
    """

    increments = (0.8, 0.6) if emotion_increments is None else emotion_increments
    if len(increments) != 2:
        raise ValueError("emotion_increments must contain two values")

    lines: List[str] = []
    for prompt in prompts:
        lines.append(
            f"{agent1.name} ({agent1.state}) na '{prompt}': {agent1.respond(prompt)}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}) na '{prompt}': {agent2.respond(prompt)}"
        )

    agent1.update_emotion(increments[0])
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(increments[1])
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    for prompt in prompts:
        lines.append(f"{agent1.name}: {agent1.respond(prompt)}")
        lines.append(f"{agent2.name}: {agent2.respond(prompt)}")

    return lines
