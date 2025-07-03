"""Module that connects agents with specific tasks."""
from __future__ import annotations

from typing import List

from .agent import Agent


class Modul:
    """Represents a logical module containing a task for agents."""

    def __init__(self, ime: str, naloga: str) -> None:
        self.ime = ime
        self.naloga = naloga
        self.agenti: List[Agent] = []

    def dodaj_agenta(self, agent: Agent) -> None:
        """Add an agent to this module."""
        self.agenti.append(agent)
        print(f"Agent {agent.name} je bil dodan v modul {self.ime}.")

    def izvedi_naloge(self) -> None:
        """Execute module task with all agents."""
        for agent in self.agenti:
            print(f"Agent {agent.name} izvaja nalogo {self.naloga}.")
            agent.ontoznano.prehod_v_ontoznano(self.naloga)
