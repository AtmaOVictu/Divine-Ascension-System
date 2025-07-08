from typing import List
from .agent import Agent
from .utils import parse_philosophical_statement, self_reflection
from .memory import memory


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    line1 = f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    line2 = f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    lines.extend([line1, line2])
    parse_philosophical_statement(line1)
    parse_philosophical_statement(line2)

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    line3 = f"{agent1.name}: {agent1.respond('Kaj je resnica?')}"
    line4 = f"{agent2.name}: {agent2.respond('Kaj je resnica?')}"
    lines.extend([line3, line4])

    memory.store_long_term({"dialogue": lines})
    lines.append(self_reflection())
    return lines
