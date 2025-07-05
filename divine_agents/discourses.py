from typing import List
from .agent import Agent


def truth_discourse(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate discourse about the nature of truth."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): Resnica je večna in neodvisna od človeške percepcije.")
    agent1.update_emotion(0.2)
    lines.append(f"{agent2.name} ({agent2.state}): Ampak, resnica je subjektivna. To, kar je resnično za enega, ni nujno resnično za drugega.")
    agent2.update_emotion(0.3)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def morality_discourse(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate discourse about morality and ethics."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): Moralnost je absolutna in neodvisna od kulture.")
    agent1.update_emotion(0.5)
    lines.append(f"{agent2.name} ({agent2.state}): Kultura in družbeni kontekst oblikujeta moralo. Kaj je sprejemljivo v eni družbi, morda ni v drugi.")
    agent2.update_emotion(0.4)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je morala?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je morala?')}")
    return lines


def science_discourse(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate discourse about science and research."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): Znanost je iskanje objektivnih resnic v svetu, ki je podvržen natančnemu preučevanju.")
    agent1.update_emotion(0.4)
    lines.append(f"{agent2.name} ({agent2.state}): Ampak znanost se vedno spreminja. To, kar danes velja za resnično, jutri morda ne bo.")
    agent2.update_emotion(0.3)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je znanost?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je znanost?')}")
    return lines


def liberation_discourse(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate discourse about liberation and control."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): Osvoboditev je notranja izkušnja, kjer se posameznik osvobodi omejitev svojega uma.")
    agent1.update_emotion(0.6)
    lines.append(f"{agent2.name} ({agent2.state}): Ampak nadzor je potreben za ohranjanje reda v svetu. Osvoboditev brez discipline vodi v kaos.")
    agent2.update_emotion(0.5)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je osvoboditev?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je osvoboditev?')}")
    return lines
