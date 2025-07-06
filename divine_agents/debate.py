from typing import List

from .agent import Agent


def run_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a multi-round philosophical debate between two agents.

    Each round both agents present their view of truth according to their
    current ontological state. Their emotions are increased to raise tension
    which may trigger state transitions.
    """
    transcript: List[str] = []
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions influencing tension
        agent1.update_emotion(0.6)
        agent2.update_emotion(0.6)
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return transcript
