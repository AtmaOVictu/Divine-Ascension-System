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


def simulate_conversation(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Run a multi-round dialogue updating emotion and tension each time."""
    transcript: List[str] = []
    for i in range(rounds):
        transcript.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        transcript.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # Gradually escalate emotion which also increases tension.
        agent1.update_emotion(0.4 + 0.2 * i)
        new_state1 = agent1.transition()
        transcript.append(f"{agent1.name} prehaja v stanje: {new_state1}")

        agent2.update_emotion(0.5 + 0.1 * i)
        new_state2 = agent2.transition()
        transcript.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    return transcript
