from __future__ import annotations

import random
from typing import Dict

from .agent import Agent


class Codex:
    """Manage agents and their interactions."""

    def __init__(self) -> None:
        self.elements: Dict[str, Agent] = {}

    def add_element(self, element: Agent) -> None:
        """Register a new agent in the system."""
        self.elements[element.name] = element
        element._log(f"Added to Codex with initial state: {element.state}")

    def simulate_interaction(self, element1: Agent, element2: Agent) -> None:
        """Simulate an interaction causing emotional updates and transitions."""
        element1._log(f"Initiating interaction with {element2.name}")
        element2._log(f"Responding to interaction from {element1.name}")

        element1.update_emotion(random.uniform(0.4, 0.9))
        element2.update_emotion(random.uniform(0.4, 0.9))

        element1.transition()
        element2.transition()

        resp1 = element1.respond("Kaj je resnica?")
        resp2 = element2.respond("Kaj je resnica?")

        element1._log(f"Interaction resulted in: {resp1}")
        element2._log(f"Interaction resulted in: {resp2}")

    def save_all_logs(self) -> None:
        for element in self.elements.values():
            element.save_history()
            element._log(f"Log saved with version {element.version}")
