from typing import List

from .agent import Agent
from .insertion import InsertionAgent


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


def dynamic_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a dialogue where insertion agents modify agents dynamically."""
    insert_agent1 = InsertionAgent(agent1)
    insert_agent2 = InsertionAgent(agent2)

    lines: List[str] = []
    lines.append(f"Initial state: {agent1.state}, {agent2.state}")

    insert_agent1.insert_state("Transitional")
    insert_agent2.insert_data({"philosophy": "Existentialism"})
    insert_agent1.modify_behavior("Defensive Argument")

    lines.extend(philosophical_dialogue(agent1, agent2))
    return lines
