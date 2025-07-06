from typing import List
from .dynamic_agent import DynamicAgent


def dinamicka_inicializacija(agenti: List[DynamicAgent]) -> List[DynamicAgent]:
    """Connect agents dynamically based on their state."""
    for i in range(len(agenti)):
        for j in range(i + 1, len(agenti)):
            if agenti[i].stanje == "aktiviran" and agenti[j].stanje == "aktiviran":
                agenti[i].komunikacija(agenti[j])
                agenti[i].reorganiziraj(agenti[j])
                agenti[j].reorganiziraj(agenti[i])
    return agenti


def reorganizacija_sistema(agenti: List[DynamicAgent]) -> List[DynamicAgent]:
    """Automatically reorganize agents based on activity."""
    for agent in agenti:
        agent.aktivnosti += 1
        if agent.aktivnosti > 10:
            agent.stanje = "reorganizirano"
    return agenti
