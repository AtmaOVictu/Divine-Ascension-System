from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 3) -> Tuple[List[str], Tuple[str, str]]:
    """Simulate a multi-turn philosophical dialogue.

    Parameters
    ----------
    agent1 : Agent
        First participant in the dialogue.
    agent2 : Agent
        Second participant in the dialogue.
    turns : int, optional
        Number of conversational turns to simulate, by default 3.

    Returns
    -------
    Tuple[List[str], Tuple[str, str]]
        The generated dialogue lines and the final states of both agents.
    """

    lines: List[str] = []

    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Escalate emotions each turn influencing tension and possible transitions
        agent1.update_emotion(min(1.0, agent1.emotion + 0.4))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(1.0, agent2.emotion + 0.3))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    final_states = (agent1.state, agent2.state)
    return lines, final_states
