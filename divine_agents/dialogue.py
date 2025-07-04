from typing import List
from .agent import Agent
from .shumnik import (
    Shumnik,
    tension_effect,
    reflection_effect,
    emotional_balance_effect,
)


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial exchange based on current states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Apply shumniki to influence each agent
    shumnik_tension = Shumnik("ŠumT", "Tension phase", tension_effect)
    shumnik_reflection = Shumnik("ŠumR", "Reflection phase", reflection_effect)

    agent1.interact_with_shumnik(shumnik_tension)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.interact_with_shumnik(shumnik_reflection)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final exchange after state changes
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
