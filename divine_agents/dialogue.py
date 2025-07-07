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
    """Run a dynamic debate updating emotion and tension each round."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions as the debate continues
        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.2))

        previous_state1 = agent1.state
        previous_state2 = agent2.state
        agent1.transition()
        agent2.transition()

        if agent1.state != previous_state1:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.state != previous_state2:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
