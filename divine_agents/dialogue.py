from typing import List

from .agent import Agent
from .systems import EmotionalTensionDynamics


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.set_emotional_state("angry")
    agent1.update_emotion(0.8)
    EmotionalTensionDynamics(agent1).adjust_tension_based_on_emotions()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotional_state("happy")
    agent2.update_emotion(0.6)
    EmotionalTensionDynamics(agent2).adjust_tension_based_on_emotions()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
