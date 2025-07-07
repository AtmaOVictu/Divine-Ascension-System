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


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a multi-round debate updating emotions and triggering transitions."""
    debate_lines: List[str] = []
    for _ in range(rounds):
        debate_lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        debate_lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # escalate emotions based on current state
        agent1.update_emotion(agent1.emotion + 0.4,
                              "anger" if agent1.state == "Ego" else agent1.emotion_name)
        prev1 = agent1.state
        agent1.transition()
        if agent1.state != prev1:
            debate_lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        agent2.update_emotion(agent2.emotion + 0.4,
                              "curiosity" if agent2.state == "Jaz" else agent2.emotion_name)
        prev2 = agent2.state
        agent2.transition()
        if agent2.state != prev2:
            debate_lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")
    return debate_lines
