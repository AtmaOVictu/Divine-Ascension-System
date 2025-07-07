from typing import Callable, List
from .agent import Agent, InsertionAgent


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


def dynamic_dialogue(names: List[str]) -> List[str]:
    """Run a dynamic conversation using InsertionAgent instances."""
    a1 = InsertionAgent(names[0], state="Ego")
    a2 = InsertionAgent(names[1], state="Jaz")

    a1.insert_knowledge("Verjamem v absolutne resnice.")
    a2.insert_knowledge("Moja resnica je odvisna od tvojega pogleda.")

    lines = [
        f"{a1.name} ({a1.state}): {a1.respond('Kaj je resnica?')}",
        f"{a2.name} ({a2.state}): {a2.respond('Kaj je resnica?')}",
    ]

    a1.update_emotion(0.6)
    a2.update_emotion(0.8)
    lines.append(f"{a1.name} prehaja v stanje: {a1.transition()}")
    lines.append(f"{a2.name} prehaja v stanje: {a2.transition()}")

    a1.insert_knowledge("Zdaj razumem relativnost.")
    a2.insert_behavior(lambda r: f"{r} #Refleksija")
    a2.insert_state("Enotnost")

    lines.extend([
        f"{a1.name} ({a1.state}): {a1.respond('Kaj je resnica?')}",
        f"{a2.name} ({a2.state}): {a2.respond('Kaj je resnica?')}",
    ])

    return lines
