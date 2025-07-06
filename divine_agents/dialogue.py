from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The interaction alters each agent's emotional state and may trigger
    ontological transitions based on the defined thresholds.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent2's argument creates tension in Agent1
    agent1.update_emotion(0.6, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent1's response affects Agent2 who stays calmer but moves slightly
    agent2.update_emotion(0.4, "veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
