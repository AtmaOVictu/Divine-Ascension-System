from typing import List
from .agent import Agent, OracleAgent


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


def oracle_dialogue(agent1: Agent, agent2: Agent, oracle: OracleAgent) -> List[str]:
    """Dialogue where an oracle tracks transitions and suggests next steps."""
    lines = []
    lines.extend(philosophical_dialogue(agent1, agent2))
    # Record transitions observed by the oracle
    oracle.update_emotion(0.0)  # ensure tension does not trigger transition
    oracle.transitions.extend(
        [{"from": oracle.state, "to": agent1.state}, {"from": oracle.state, "to": agent2.state}]
    )
    lines.append(f"Oracle predlaga, da naslednje stanje po {agent2.state} je {oracle.predict_future() or agent2.state}")
    return lines
