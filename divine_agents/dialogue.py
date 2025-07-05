from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.set_emotion("anger", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("joy", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Engage two agents in a philosophical debate.

    Parameters
    ----------
    agent1, agent2:
        Participating agents.
    rounds:
        Number of exchange rounds.
    """
    transcript: List[str] = []

    for i in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # shift emotions to trigger possible transitions
        agent1.set_emotion("anger", min(1.0, agent1.emotion + 0.6))
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.set_emotion("joy", min(1.0, agent2.emotion + 0.4))
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return transcript
