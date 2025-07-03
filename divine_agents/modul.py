from __future__ import annotations

from typing import List

from .agent import Agent


class Modul:
    """Group of agents executing a common task."""

    def __init__(self, ime: str, naloga: str) -> None:
        self.ime = ime
        self.naloga = naloga
        self.agenti: List[Agent] = []

    def dodaj_agenta(self, agent: Agent) -> None:
        self.agenti.append(agent)

    def izvedi_naloge(self) -> None:
        for agent in self.agenti:
            agent.sprejmi_nalogo(self.naloga)
