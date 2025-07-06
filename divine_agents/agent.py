from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of transitioning between states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotional_state: str = "neutral"
    loyalty: float = 0.5
    experiences: List[str] = field(default_factory=list)
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, emotional_state: str, intensity: float) -> None:
        """Set emotional state and adjust tension based on emotion."""
        self.emotional_state = emotional_state
        self.emotion = intensity
        if emotional_state == "angry":
            self.tension += 0.3
        elif emotional_state == "happy":
            self.tension -= 0.2
        else:
            self.tension += 0.1

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds or conditions are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"

        last_exp = self.experiences[-1] if self.experiences else ""
        if self.state == "Jaz" and (self.loyalty > 0.8 or "selfish" in last_exp):
            self.state = "Enotnost"

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

        if self.emotional_state == "angry":
            return base + " Ob tem čutim jezo."
        if self.emotional_state == "happy":
            return base + " To me navdaja z veseljem."
        if self.emotional_state == "fearful":
            return base + " Preveva me strah."
        return base
