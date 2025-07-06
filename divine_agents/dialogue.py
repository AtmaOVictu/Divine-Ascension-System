from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a debate where agents update emotion and may change states."""
    transcript = []
    question = "Kaj je resnica?"
    for _ in range(rounds):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        agent1.update_emotion(0.6, "anger")
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.4, "joy")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return transcript
