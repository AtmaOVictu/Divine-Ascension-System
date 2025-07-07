"""Core agent models used for philosophical interactions."""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    idself: Dict[str, object] = field(default_factory=lambda: {
        "role": "Philosopher",
        "principles": ["logic", "emotion", "growth"],
    })
    iffself: Dict[str, str] = field(default_factory=dict)
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.evaluate_iffself()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.evaluate_iffself()

    def evaluate_iffself(self) -> None:
        """Determine conditional decision based on current emotion and tension."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.iffself = {"decision": "advance", "target": "Jaz"}
            elif self.state == "Jaz":
                self.iffself = {"decision": "advance", "target": "Enotnost"}
            else:
                self.iffself = {"decision": "remain", "target": self.state}
        else:
            self.iffself = {"decision": "remain", "target": self.state}

    def transition(self) -> str:
        """Perform state transition when :pyattr:`iffself` demands it."""
        self.evaluate_iffself()
        if self.iffself.get("decision") == "advance":
            self.state = self.iffself["target"]
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Čutim močna čustva, kar vpliva na mojo perspektivo."
        return base

    def speak(self, topic: str) -> str:
        """Compose an answer incorporating the provided topic."""
        answer = self.respond(topic)
        return f"{answer}"
