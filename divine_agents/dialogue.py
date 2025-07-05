from typing import List
from .agent import Agent
from .math_utils import logistic_function, logarithmic_function


def philosophical_dialogue(agent1: Agent, agent2: Agent, time: float = 1.0) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The agents adjust their emotional state using a logistic or logarithmic
    progression, after which potential state transitions occur.
    """
    lines: List[str] = []

    # Initial statements based on current ontological states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions evolve over time and influence tension
    agent1.update_emotion(logistic_function(time))
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(logarithmic_function(time * 2))
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again reflecting possible new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
