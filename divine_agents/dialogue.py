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


def dynamic_debate(agent1: Agent, agent2: Agent, steps1: List[tuple], steps2: List[tuple]) -> List[str]:
    """Run a multi-step debate where emotional states drive transitions."""
    transcript: List[str] = []
    steps = min(len(steps1), len(steps2))
    for i in range(steps):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        e1, v1 = steps1[i]
        agent1.feel(e1, v1)
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        e2, v2 = steps2[i]
        agent2.feel(e2, v2)
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return transcript
