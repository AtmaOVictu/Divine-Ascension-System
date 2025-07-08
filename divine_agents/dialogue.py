from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each round both agents respond and potentially change state based on
    updated emotion. The emotion value grows slightly each round to mimic
    increasing tension in the debate.
    """

    lines: List[str] = []
    for i in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        agent2.update_emotion(min(1.0, agent2.emotion + 0.3))

        new_state1 = agent1.transition()
        new_state2 = agent2.transition()

        lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # final statements after all transitions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
