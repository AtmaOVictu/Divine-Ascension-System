from typing import List

from .agent import Agent


def ontological_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate an ontological debate escalating emotions and triggering state changes.

    Parameters
    ----------
    agent1 : Agent
        First debating agent.
    agent2 : Agent
        Second debating agent.
    rounds : int, optional
        Number of exchanges in the debate, by default 3.

    Returns
    -------
    List[str]
        Transcript of the debate with state changes recorded.
    """
    transcript: List[str] = []
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions for both agents
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))

        new_state1 = agent1.transition()
        new_state2 = agent2.transition()

        transcript.append(f"{agent1.name} preide v stanje: {new_state1}")
        transcript.append(f"{agent2.name} preide v stanje: {new_state2}")

    return transcript
