from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive transitions."""

    lines: List[str] = []
    for i in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotional intensity over time
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        agent2.update_emotion(min(agent2.emotion + 0.4, 1.0))

        # perform potential state transitions
        agent1.transition()
        agent2.transition()

        lines.append(
            f"-- po rundi {i + 1}: {agent1.name}={agent1.state}, {agent2.name}={agent2.state}"
        )

    # Final reflections with potentially heightened emotions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
