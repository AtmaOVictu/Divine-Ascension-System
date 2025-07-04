from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        The agents participating in the conversation.
    rounds:
        Number of conversational rounds to simulate.
    """

    lines: List[str] = []

    for _ in range(rounds):
        # Each agent responds according to their current state and emotion.
        lines.append(
            f"{agent1.name} ({agent1.state}): " f"{agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): " f"{agent2.respond('Kaj je resnica?')}"
        )

        # Emotions rise as discussion continues.
        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0))

        previous_state_a1 = agent1.state
        previous_state_a2 = agent2.state

        agent1.transition()
        agent2.transition()

        if agent1.state != previous_state_a1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != previous_state_a2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
