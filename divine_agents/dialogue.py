from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def emotional_dialogue(agent1: Agent, agent2: Agent, increments: List[tuple]) -> List[str]:
    """Run a dialogue where emotion updates drive state transitions.

    Parameters
    ----------
    agent1, agent2 : Agent
        The agents participating in the conversation.
    increments : List[tuple]
        A list of ``(emotion1, emotion2)`` pairs representing emotional
        intensity applied at each step. Each value also increases the agent's
        tension via ``update_emotion``.

    Returns
    -------
    List[str]
        Generated dialogue lines describing the conversation and state
        transitions.
    """

    lines: List[str] = []
    for idx, (e1, e2) in enumerate(increments, start=1):
        agent1.update_emotion(e1)
        agent2.update_emotion(e2)

        # Perform transitions after emotion updates
        new_state1 = agent1.transition()
        new_state2 = agent2.transition()

        lines.append(
            f"Krok {idx} - {agent1.name} ({new_state1}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"Krok {idx} - {agent2.name} ({new_state2}): {agent2.respond('Kaj je resnica?')}"
        )

    return lines
