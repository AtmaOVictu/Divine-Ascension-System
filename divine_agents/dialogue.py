from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a minimal philosophical dialogue for backward compatibility."""
    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    ]

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_dialogue(agent1: Agent, agent2: Agent, max_rounds: int = 10) -> List[str]:
    """Run a dialogue until one agent reaches ``Enotnost`` or rounds expire."""
    transcript: List[str] = []
    rounds = 0
    while rounds < max_rounds and 'Enotnost' not in (agent1.state, agent2.state):
        transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.feel(0.1)
        agent2.feel(0.1)
        agent1.transition()
        agent2.transition()

        rounds += 1

    if 'Enotnost' in (agent1.state, agent2.state):
        transcript.append("Eden od agentov je dosegel Enotnost.")
    else:
        transcript.append("Dialog je končan brez dosega Enotnosti.")
    return transcript
