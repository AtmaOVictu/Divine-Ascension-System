from typing import List
from .agent import Agent
from .symbolic import Symbol, Expression


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

    # Symbolic exchange using special characters
    var = Symbol('Š')
    expr = Expression(var, Symbol('Č'))
    lines.append(f"{agent1.name} math: {agent1.discuss_expression(expr, var)}")
    lines.append(f"{agent2.name} math: {agent2.discuss_expression(expr, var)}")
    return lines
