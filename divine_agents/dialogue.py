from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dynamic philosophical dialogue with emotional depth."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally to the conversation
    agent1.update_emotion("anger", 0.3)
    agent2.update_emotion("joy", 0.2)

    lines.append(f"{agent1.name} reacts emotionally and transitions to: {agent1.state}")
    lines.append(f"{agent2.name} reacts emotionally and transitions to: {agent2.state}")

    lines.append(f"{agent1.name} (Post-transition): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} (Post-transition): {agent2.respond('Kaj je resnica?')}")

    return lines
