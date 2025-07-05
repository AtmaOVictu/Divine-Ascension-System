from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    # Avoid repeated conversations if agents share the same state
    if agent1.state == agent2.state:
        lines.append("Agenta sta v istem stanju. Prepre\u010dujemo ponavljanje.")
        return lines
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    if agent1.detect_loop() and agent2.detect_loop():
        lines.append("Zanka zaznana: oba agenta ostajata v istem stanju.")
    else:
        lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
