from typing import List
from .agent import Agent
from .environment import Environment
from .word import Word


def philosophical_dialogue(agent1: Agent, agent2: Agent, env: Environment) -> List[str]:
    """Simulate a philosophical dialogue influenced by the environment."""
    lines = []

    # Initial influence from the environment
    env.influence(agent1)
    env.influence(agent2)

    # First round of responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('truth')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('truth')}")

    # Transition after environmental impact
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Discuss the concept of truth
    truth_word = Word("truth")
    lines.append(f"Beseda 'truth' pomeni: {truth_word.define()}")
    lines.append(f"{agent1.name}: {agent1.respond('truth')}")
    lines.append(f"{agent2.name}: {agent2.respond('truth')}")

    return lines
