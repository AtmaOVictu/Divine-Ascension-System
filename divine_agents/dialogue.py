from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion("fear", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_debate(agent1: Agent, agent2: Agent, turns: int = 2) -> List[str]:
    """Engage two agents in a multi-turn debate."""
    transcript: List[str] = []
    for _ in range(turns):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Evolve emotions and tension as debate progresses
        agent1.update_emotion("anger", agent1.emotion + 0.3)
        agent2.update_emotion("joy", agent2.emotion + 0.2)

        agent1.transition()
        agent2.transition()

        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return transcript
