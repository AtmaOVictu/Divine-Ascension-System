from typing import List, Tuple, Union
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1_inc: float = 0.8,
    emotion2_inc: float = 0.6,
    exchanges: int = 2,
    return_states: bool = False,
) -> Union[List[str], Tuple[List[str], Tuple[str, str]]]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Agents participating in the dialogue.
    emotion1_inc, emotion2_inc:
        How much to increase each agent's emotion after every exchange.
    exchanges:
        Number of dialogue exchanges (pairs of answers) to perform.
    return_states:
        If ``True`` return a tuple of lines and the agents' final states.
    """
    lines: List[str] = []

    for i in range(exchanges):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # Apply emotion increments and potential state transitions if another
        # exchange follows.
        if i < exchanges - 1:
            agent1.update_emotion(emotion1_inc)
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

            agent2.update_emotion(emotion2_inc)
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    if return_states:
        return lines, (agent1.state, agent2.state)
    return lines
