from typing import List
from .agent import Agent

class GranularAgent(Agent):
    """Agent with granular emotional transitions."""

    def __init__(self, name: str, emotions: List[str] | None = None,
                 state: str = "Ego", tension: float = 0.0):
        super().__init__(name, state=state, tension=tension)
        self.emotions = emotions or []

    def update_emotions(self, emotions: List[str]) -> None:
        """Set current emotions."""
        self.emotions = emotions

    def granular_transition(self) -> str:
        """Transition using granular emotion rules."""
        if "anger" in self.emotions and self.tension > 0.7:
            self.state = "Jaz"
        elif "calm" in self.emotions and self.tension < 0.3:
            self.state = "Enotnost"
        else:
            self.state = "Ego"
        self.history.append(self.state)
        return self.state
