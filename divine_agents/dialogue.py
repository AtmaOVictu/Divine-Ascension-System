from typing import List
from .agent import Agent
from .utils import evaluate_equation


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

    # Demonstrate equation evaluation and ontological scale
    result = evaluate_equation('sin(pi/2)')
    lines.append(f"Matematicni rezultat: {result}")
    scale1 = ','.join(agent1.ontological_scale())
    lines.append(f"{agent1.name} igra lestvico: {scale1}")

    return lines
