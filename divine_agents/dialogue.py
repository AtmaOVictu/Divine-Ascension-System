from typing import List

from .agent import Agent
from .shumnik import Shumnik, tension_effect, reflection_effect


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    sh_tension = Shumnik("ŠumT", "Tension phase", tension_effect)
    sh_reflection = Shumnik("ŠumR", "Reflection phase", reflection_effect)
    agent1.interact_with_shumnik(sh_tension)
    lines.append(f"{agent1.name} uporablja {sh_tension.symbol}")
    agent2.interact_with_shumnik(sh_reflection)
    lines.append(f"{agent2.name} uporablja {sh_reflection.symbol}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
