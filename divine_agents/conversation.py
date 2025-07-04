"""Dynamic philosophical debate module."""
from typing import List
from .agent import Agent


def interactive_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a debate and evolve agents based on emotion and tension."""
    lines = []
    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally to each other's stance
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} čuti močna čustva. Prehod: {agent1.transition()}")

    agent2.update_emotion(0.4)
    agent2.update_tension(agent2.tension + 0.4)
    lines.append(f"{agent2.name} se odziva. Prehod: {agent2.transition()}")

    # Responses after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
