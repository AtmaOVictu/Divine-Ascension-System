import random
import time
from .agent import Agent


class EternalAgent(Agent):
    """Agent with self-motivation cycles."""

    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(name, **kwargs)
        self.routine = 0
        self.kronika = []

    def event(self, note: str) -> None:
        entry = note.upper()
        self.kronika.append(entry)

    def self_motivation(self, max_iter: int = 7, event_delay: float = 0.0) -> None:
        events = ["objem", "izliv", "pesem", "ekstaza", "smrt"]
        for _ in range(max_iter):
            evt = random.choice(events)
            if self.kronika and self.kronika[-1].startswith(evt.upper()):
                self.routine += 1
            else:
                self.routine = 0

            if self.routine >= 2:
                self.event("pesem")
                self.routine = 0
            else:
                self.event(evt)
            if event_delay:
                time.sleep(event_delay)
