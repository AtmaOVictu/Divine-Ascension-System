from typing import Iterable, List
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


def philosophical_debate(
    agent1: Agent,
    agent2: Agent,
    emotions1: Iterable[float],
    emotions2: Iterable[float],
) -> List[str]:
    """Run a multi-step debate with emotional influence and state transitions."""
    lines: List[str] = []
    for round_no, (e1, e2) in enumerate(zip(emotions1, emotions2), start=1):
        lines.append(
            f"Krog {round_no} - {agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"Krog {round_no} - {agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(e1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(e2)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
