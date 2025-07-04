from typing import List
from .agent import Agent
from .spiritual_processes import VERA, VOLJA, LJUBEZEN


class VeraVoljaLjubAgent(Agent):
    """Agent incorporating faith, will, and love processes."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.vera = VERA()
        self.volja = VOLJA()
        self.ljubezen = LJUBEZEN()

    def run_process(self) -> List[str]:
        """Run spiritual processes and update state accordingly."""
        logs = []
        logs.append(self.vera.aktivacija())
        logs.append(self.volja.aktivacija())
        logs.append(self.ljubezen.aktivacija())
        self.update_emotion(0.6)
        logs.append(f"{self.name} prehaja v stanje: {self.transition()}")

        logs.append(self.vera.sprememba())
        logs.append(self.volja.sprememba())
        logs.append(self.ljubezen.sprememba())
        self.update_emotion(0.6)
        logs.append(f"{self.name} prehaja v stanje: {self.transition()}")

        logs.append(self.vera.harmonija())
        logs.append(self.volja.harmonija())
        logs.append(self.ljubezen.harmonija())
        self.update_emotion(0.6)
        logs.append(f"{self.name} prehaja v stanje: {self.transition()}")

        return logs
