from typing import List
from .agent import Agent


def simulate_loading_screen(agent_name: str, max_cycles: int = 10) -> List[str]:
    """Simulate a loading screen and return progress messages."""
    progress = []
    for cycle in range(max_cycles):
        progress.append(f"Loading: {cycle + 1}/{max_cycles} - {agent_name}")
    progress.append(f"Loading Screen končan za {agent_name}.")
    return progress


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
