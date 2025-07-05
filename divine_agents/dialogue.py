from typing import List
from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate between two agents.

    The debate influences each agent's emotional state and may trigger
    transitions through the ontological phases.
    """

    lines: List[str] = []

    # Initial positions on truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Hearing the other's argument increases emotion and tension
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.7)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses from their new perspectives
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
