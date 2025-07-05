from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts emotionally to Agent2's argument
    agent1.update_emotion(0.6)
    prev_state = agent1.state
    agent1.transition()
    lines.append(f"{agent1.name} prehaja iz {prev_state} v {agent1.state}.")

    # Agent2 also responds emotionally
    agent2.update_emotion(0.7)
    prev_state = agent2.state
    agent2.transition()
    lines.append(f"{agent2.name} prehaja iz {prev_state} v {agent2.state}.")

    # Final statements reflecting new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
