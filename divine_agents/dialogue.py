from typing import List
from .agent import Agent
from .command_center import CommandCenter


def philosophical_dialogue(agent1: Agent, agent2: Agent, center: CommandCenter | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    If a ``CommandCenter`` is provided, agents send reports upward and
    receive commands back, demonstrating two-way transfer.
    """
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    if center:
        center.receive_from_agent(agent1, "Potrebujem usmeritev")
        center.send_command(agent1, "excite")
        center.receive_from_agent(agent2, "Zaznavam spremembo")
        center.send_command(agent2, "calm")
        # escalate emotions to trigger transitions
        agent1.update_emotion(0.8)
        agent2.update_emotion(0.6)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
