from typing import List
from .agent import Agent
from .interaction import OkenskoSporocilo


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Intensify emotions and transition states
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica sedaj?')}")

    agent2.update_tension(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa sedaj?')}")

    # Optional interactive prompt for demonstration purposes
    window = OkenskoSporocilo("Nadaljujte dialog?", input_func=lambda _: "zaključi")
    user_choice = window.prikazi_okno()
    lines.append(f"Uporabnik je izbral: {user_choice}")

    return lines
