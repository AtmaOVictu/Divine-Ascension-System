from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    return dynamic_dialogue(agent1, agent2, rounds=1)


def dynamic_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a multi-round dialogue where emotions drive state transitions."""
    lines: List[str] = []
    question = "Kaj je resnica?"

    for _ in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}, {agent1.emotion_name}): {agent1.respond(question)}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}, {agent2.emotion_name}): {agent2.respond(question)}"
        )

        agent1.update_emotion(agent1.emotion + 0.4)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.4)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
