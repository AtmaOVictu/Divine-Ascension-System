from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, max_rounds: int = 10) -> List[str]:
    """Simulate an interactive philosophical dialogue between two agents."""
    lines: List[str] = []
    rounds = 0

    while rounds < max_rounds and agent1.state != "Enotnost" and agent2.state != "Enotnost":
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # both agents experience a slight emotional shift
        agent1.feel(0.1)
        agent2.feel(0.1)

        # apply tension feedback and check for transitions
        agent1.update_tension()
        agent2.update_tension()

        if agent1.transition() == "Enotnost" or agent2.transition() == "Enotnost":
            break

        rounds += 1

    lines.append(
        "Eden od agentov je dosegel Enotnost." if agent1.state == "Enotnost" or agent2.state == "Enotnost" else "Dialog je končan brez dosega Enotnosti."
    )
    return lines
