from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    agent1.update_emotion(0.8)
    prev_state = agent1.state
    agent1.transition()
    if agent1.state != prev_state:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.update_emotion(0.6)
    prev_state = agent2.state
    agent2.transition()
    if agent2.state != prev_state:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Run a debate for a given number of rounds with emotional escalation."""
    transcript = []
    for _ in range(rounds):
        transcript.extend(philosophical_dialogue(agent1, agent2))
    return transcript
