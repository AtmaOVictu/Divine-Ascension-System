from typing import List

from .agent import Agent
from .granular_transitions import GranularniPrehodi
from .nanoaplikacija import Nanoaplikacija
from .interactions import Interakcije


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents interact and influence each other
    interakcija = Interakcije(agent1, agent2)
    agent1.update_emotion(0.8, "anger")
    agent2.update_emotion(0.2, "calm")
    interakcija.medsebojna_interakcija()

    # Optimize parameters
    nano1 = Nanoaplikacija(agent1)
    nano2 = Nanoaplikacija(agent2)
    nano1.optimiziraj_napetost()
    nano2.optimiziraj_napetost()

    # Perform transitions with granular control
    prehodi1 = GranularniPrehodi(agent1)
    prehodi2 = GranularniPrehodi(agent2)
    lines.append(f"{agent1.name} prehaja v stanje: {prehodi1.prehod(agent1.emotion, agent1.tension)}")
    lines.append(f"{agent2.name} prehaja v stanje: {prehodi2.prehod(agent2.emotion, agent2.tension)}")

    # Increase emotion for a further transition
    agent2.update_emotion(0.9, "anger")
    lines.append(f"{agent2.name} prehaja v stanje: {prehodi2.prehod(agent2.emotion, agent2.tension)}")

    # Final statements reflecting new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
