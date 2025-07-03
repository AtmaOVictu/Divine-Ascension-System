"""High level system orchestrating multiple agents and modules."""
from __future__ import annotations

import random
from typing import Dict, List

from .agent import Agent
from .knowledge_base import KnowledgeBase
from .modul import Modul


class Codex:
    """Main entry point for running agent interactions."""

    def __init__(self, stevilo_agentov: int = 3) -> None:
        self.agenti: List[Agent] = []
        self.moduli: List[Modul] = []
        self.stevilo_agentov = stevilo_agentov
        self.knowledge_base = KnowledgeBase()
        self.inicializiraj_agente()
        self.inicializiraj_module()

    def inicializiraj_agente(self) -> None:
        for i in range(self.stevilo_agentov):
            ime = f"Agent{i+1}"
            self.dodaj_agenta(ime)

    def inicializiraj_module(self) -> None:
        self.moduli.append(Modul("Modul 1", "samospoznanje"))
        self.moduli.append(Modul("Modul 2", "logični prehod"))
        self.moduli.append(Modul("Modul 3", "emotivni prehod"))
        for modul in self.moduli:
            for agent in self.agenti:
                modul.dodaj_agenta(agent)

    def dodaj_agenta(self, ime: str) -> None:
        emocionalno_stanje = random.choice(["nevtralno", "srečno", "žalostno", "jeza"])
        agent = Agent(ime, state="Ego")
        agent.update_emotion(random.random())
        print(f"Agent {ime} je bil ustvarjen z čustvom: {emocionalno_stanje}")
        self.agenti.append(agent)

    def generiraj_vnos(self, vsebina: str) -> str:
        vnos = f"00 11 RESNICAMI: {vsebina}"
        print(f"Vnos: {vnos}")
        return vnos

    def simuliraj_komunikacijo(self) -> None:
        if len(self.agenti) > 1:
            agent1, agent2 = random.sample(self.agenti, 2)
            agent1.interact(agent2)
            agent2.interact(agent1)

    def pridobi_stanje(self) -> Dict[str, str]:
        return {agent.name: agent.state for agent in self.agenti}

    def cycle_once(self) -> Dict[str, str]:
        self.simuliraj_komunikacijo()
        for modul in self.moduli:
            modul.izvedi_naloge()
        return self.pridobi_stanje()
