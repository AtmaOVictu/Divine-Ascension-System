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


def dynamic_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a multi-round debate where emotions drive state transitions."""
    transcript: List[str] = []
    for i in range(rounds):
        transcript.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        transcript.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # escalate emotions and thus tension
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))

        prev1, prev2 = agent1.state, agent2.state
        agent1.transition()
        agent2.transition()

        if agent1.state != prev1:
            transcript.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != prev2:
            transcript.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return transcript
