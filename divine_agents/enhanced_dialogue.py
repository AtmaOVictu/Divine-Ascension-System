from typing import List
from .optimized_agent import OptimizedAgent


def dynamic_philosophical_dialogue(agent1: OptimizedAgent, agent2: OptimizedAgent) -> List[str]:
    """Simulate a dynamic philosophical dialogue influenced by emotions."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally to each other
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.4)
    lines.append(f"{agent2.name} ostaja v stanju: {agent2.state}")

    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
