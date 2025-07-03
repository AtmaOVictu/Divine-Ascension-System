from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dialogue demonstrating state transitions influenced by emotions."""
    lines: List[str] = []

    # Initial stances
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 becomes agitated by Agent2's argument
    agent1.update_emotion("anger", 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 reacts with fear and shifts further
    agent2.update_emotion("fear", 0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of responses after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
