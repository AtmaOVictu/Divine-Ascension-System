from __future__ import annotations

import random
from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue
from .knowledge_base import KnowledgeBase
from .modul import Modul


class Codex:
    """Main system orchestrating agents and modules."""

    def __init__(self, stevilo_agentov: int = 3) -> None:
        self.knowledge_base = KnowledgeBase()
        self.agenti: List[Agent] = []
        self.moduli: List[Modul] = []
        self._init_agents(stevilo_agentov)
        self._init_moduli()

    def _init_agents(self, stevilo: int) -> None:
        for i in range(stevilo):
            ime = f"Agent{i+1}"
            state = random.choice(["Ego", "Jaz"])
            agent = Agent(ime, state=state)
            self.agenti.append(agent)

    def _init_moduli(self) -> None:
        self.moduli.append(Modul("Modul 1", "samospoznanje"))
        self.moduli.append(Modul("Modul 2", "logični prehod"))
        for modul in self.moduli:
            for agent in self.agenti:
                modul.dodaj_agenta(agent)

    def simulate_dialogue(self) -> List[str]:
        a1, a2 = random.sample(self.agenti, 2)
        return philosophical_dialogue(a1, a2)
