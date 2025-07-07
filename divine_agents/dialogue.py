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


def dynamic_philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 3) -> List[str]:
    """Run a dialogue where emotions drive state transitions."""
    lines: List[str] = []
    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

        agent1.update_emotion(min(agent1.emotion + 0.6, 1.0), agent1.emotion_type)
        agent2.update_emotion(min(agent2.emotion + 0.6, 1.0), agent2.emotion_type)

        if agent1.transition() != agent1.history[-2]:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        if agent2.transition() != agent2.history[-2]:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
