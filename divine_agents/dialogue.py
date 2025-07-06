from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements reflecting each agent's state
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally to each other's statement
    agent1.set_emotion("jeza", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("presenečenje", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses in their new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj pa zdaj?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj pa zdaj?')}")
    return lines


def emotional_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a longer dialogue demonstrating emotional transitions."""
    conversation = philosophical_dialogue(agent1, agent2)

    # A second round where both agents calm down
    agent1.set_emotion("radost", 0.4)
    agent2.set_emotion("sočutje", 0.4)
    conversation.append(f"{agent1.name} čuti pomiritev: {agent1.respond('Kaj je resnica?')}")
    conversation.append(f"{agent2.name} čuti povezanost: {agent2.respond('Kaj je resnica?')}")
    return conversation
