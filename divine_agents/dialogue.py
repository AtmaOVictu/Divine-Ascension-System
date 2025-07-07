from __future__ import annotations

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue updating emotions and states."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}")

    agent1.update_emotion("anger", 0.8)
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('And now?')}")
    lines.append(f"{agent2.name}: {agent2.respond('And now?')}")
    return lines
