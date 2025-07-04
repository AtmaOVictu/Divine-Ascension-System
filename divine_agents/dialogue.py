from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent 1 reacts emotionally to Agent 2's statement
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")

    # Agent 2 responds and may also transition
    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Conduct a debate where agents discuss truth and may change state."""
    transcript = []
    transcript.extend(philosophical_dialogue(agent1, agent2))

    # Continue debate with increased tension
    agent1.update_tension(0.8)
    transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    transcript.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")

    agent2.update_tension(0.8)
    transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    transcript.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return transcript
