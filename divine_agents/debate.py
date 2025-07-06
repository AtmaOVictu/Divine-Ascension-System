"""Ontological debate module handling multi-round discussions."""
from typing import List

from .agent import Agent


def run_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Run several rounds of debate between two agents.

    Each round agents respond according to their state, then their emotions
    increase slightly which may trigger state transitions. The debate transcript
    is returned as a list of dialogue lines.
    """
    transcript: List[str] = []
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions to build tension
        agent1.update_emotion(min(1.0, agent1.emotion + 0.4))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.4))

        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return transcript
