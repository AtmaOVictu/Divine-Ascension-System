from typing import List
from .agent import Agent


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
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a debate where emotions influence state transitions."""
    conversation = []
    # initial statements
    conversation.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    conversation.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # influence emotions during debate
    agent1.update_emotion(agent1.emotion + 0.4, "anger")
    agent2.update_emotion(agent2.emotion + 0.4, "joy")

    agent1.transition()
    agent2.transition()

    conversation.append(f"{agent1.name} je zdaj v stanju {agent1.state} z custvom {agent1.emotion_label}.")
    conversation.append(f"{agent2.name} je zdaj v stanju {agent2.state} z custvom {agent2.emotion_label}.")

    conversation.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    conversation.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return conversation
