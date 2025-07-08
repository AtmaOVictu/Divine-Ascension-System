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
    """Simulate a dynamic debate where emotions influence state transitions."""
    transcript: List[str] = []
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions based on interaction
        agent1.update_emotion(min(1.0, agent1.emotion + 0.6))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.6))

        # perform transitions if thresholds are met
        agent1.transition()
        agent2.transition()
    transcript.append(f"{agent1.name} končno stanje: {agent1.state}")
    transcript.append(f"{agent2.name} končno stanje: {agent2.state}")
    return transcript
