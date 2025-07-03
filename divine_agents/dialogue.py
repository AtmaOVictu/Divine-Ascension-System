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


def ontological_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a debate where emotions trigger state transitions."""
    transcript: List[str] = []

    transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.6, name="anger")
    agent1.transition()
    transcript.append(f"{agent1.name} \u010duti {agent1.emotion_name} in je zdaj {agent1.state}.")

    agent2.update_emotion(0.8, name="joy")
    agent2.transition()
    transcript.append(f"{agent2.name} \u010duti {agent2.emotion_name} in je zdaj {agent2.state}.")

    transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return transcript
