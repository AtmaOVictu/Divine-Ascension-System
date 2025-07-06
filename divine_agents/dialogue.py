from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dynamic philosophical dialogue with emotional depth."""
    lines: List[str] = []

    # Initial exchange based on current states
    lines.append(agent1.respond())
    lines.append(agent2.respond())

    # Emotions influence the next steps in the dialogue
    agent1.update_emotion("anger", 0.8)
    agent2.update_emotion("joy", 0.8)

    lines.append(
        f"{agent1.name} reacts emotionally and transitions to: {agent1.state}"
    )
    lines.append(
        f"{agent2.name} reacts emotionally and transitions to: {agent2.state}"
    )

    # Post-transition responses
    lines.append(f"{agent1.name} (Post-transition): {agent1.respond()}")
    lines.append(f"{agent2.name} (Post-transition): {agent2.respond()}")

    return lines
