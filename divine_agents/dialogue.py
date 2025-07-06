from typing import List
from .agent import AgentWithHistory


def philosophical_dialogue(agent1: AgentWithHistory, agent2: AgentWithHistory) -> List[str]:
    """Simulate a philosophical dialogue considering emotional changes."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion("joy", agent1.emotion["joy"] + 0.8)
    agent2.update_emotion("anger", agent2.emotion["anger"] + 0.6)

    agent1.transition()
    agent2.transition()

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")
    return lines
