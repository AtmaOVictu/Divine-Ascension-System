"""Utility to simulate philosophical debates between agents."""
from typing import List
from .agent import Agent


def simulate_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a debate where agents may change state based on tension/emotion.

    Parameters
    ----------
    agent1 : Agent
        First debating agent.
    agent2 : Agent
        Second debating agent.
    rounds : int, optional
        Number of dialogue exchanges, by default 3.

    Returns
    -------
    List[str]
        List of dialogue lines documenting the debate.
    """
    transcript = []
    for i in range(rounds):
        transcript.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotion slightly each round to trigger possible transitions
        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.2, 1.0))

        new_state1 = agent1.transition()
        new_state2 = agent2.transition()
        transcript.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        transcript.append(f"{agent2.name} prehaja v stanje: {new_state2}")
    return transcript
