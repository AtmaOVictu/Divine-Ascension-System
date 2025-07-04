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


def philosophical_debate(agent1: Agent, agent2: Agent, turns: int = 3, delta: float = 0.3) -> List[str]:
    """Run a multi-turn philosophical debate with emotional progression."""
    transcript: List[str] = []
    for _ in range(turns):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.adjust_emotion(delta)
        new_state_1 = agent1.transition()
        transcript.append(f"{agent1.name} prehaja v stanje: {new_state_1}")

        agent2.adjust_emotion(delta)
        new_state_2 = agent2.transition()
        transcript.append(f"{agent2.name} prehaja v stanje: {new_state_2}")

    return transcript
