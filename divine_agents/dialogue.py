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
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    shumnik_t = Shumnik("ŠumT", "Tension phase", tension_effect)
    agent1.interact_with_shumnik(shumnik_t)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    shumnik_r = Shumnik("ŠumR", "Reflection phase", reflection_effect)
    agent2.interact_with_shumnik(shumnik_r)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
