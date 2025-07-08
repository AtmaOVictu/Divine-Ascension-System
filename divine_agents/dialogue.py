from typing import List
from .agent import Agent


def emotional_feedback(agent1: Agent, agent2: Agent) -> None:
    """Adjust emotions based on current states."""
    if agent1.state == "Ego" and agent2.state == "Jaz":
        agent1.update_emotion(0.6)
        agent2.update_emotion(0.4)
    elif agent1.state == "Jaz" and agent2.state == "Enotnost":
        agent1.update_emotion(0.5)
        agent2.update_emotion(0.3)
    else:
        agent1.update_emotion(0.6)
        agent2.update_emotion(0.6)


def decay_agents(agent1: Agent, agent2: Agent) -> None:
    """Apply tension decay based on each agent's current emotion."""
    agent1.decay_tension(agent1.emotion)
    agent2.decay_tension(agent2.emotion)


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
    """Run an automated dialogue with feedback loops and tension decay."""
    lines: List[str] = []
    for _ in range(steps):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        emotional_feedback(agent1, agent2)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
        decay_agents(agent1, agent2)
    return lines
