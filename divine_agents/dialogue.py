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


def dynamic_dialogue(agent1: Agent, agent2: Agent, steps: int = 3) -> List[str]:
    """Run a multi-step dialogue where emotions grow and states may change."""
    transcript: List[str] = []
    for step in range(steps):
        transcript.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        transcript.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # increase emotions which raise tension
        agent1.update_emotion(0.2 + 0.2 * step)
        agent2.update_emotion(0.1 + 0.3 * step)

        agent1.logistic_update(step / steps)
        agent2.logistic_update(step / steps)

        agent1.transition()
        agent2.transition()

        transcript.append(f"{agent1.name} se premakne v: {agent1.state}")
        transcript.append(f"{agent2.name} se premakne v: {agent2.state}")

    return transcript
