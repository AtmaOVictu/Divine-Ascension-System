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


def emotional_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a dialogue where emotions drive transitions."""
    transcript: List[str] = []
    for i in range(rounds):
        transcript.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        transcript.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # Apply emotions that influence tension and potentially trigger transitions
        agent1.apply_emotion("anger" if i == 0 else "joy")
        transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.apply_emotion("fear" if i == 0 else "joy")
        transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements after transitions
    transcript.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    transcript.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return transcript
