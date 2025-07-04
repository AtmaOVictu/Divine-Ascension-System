from typing import List
from .agent import Agent
from .simulation import Simulation
from .speculation import SpeculativeAgent


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


def dialogue_with_simulation(
    agent1: Agent,
    agent2: Agent,
    simulation: Simulation,
    speculative_agent: SpeculativeAgent,
) -> List[str]:
    """Extended dialogue that includes simulation and speculation."""
    lines = philosophical_dialogue(agent1, agent2)

    simulated = simulation.simulate_future(lines[-1])
    lines.append(f"Simulacija prihodnosti: {simulated}")

    speculative = speculative_agent.speculate(lines[-1])
    lines.append(f"\u0160pekulacija prihodnosti: {speculative}")

    return lines
