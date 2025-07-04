"""Ontological agent model used within the divine ascension system."""

from dataclasses import dataclass, field


TENSION_THRESHOLD = 0.7
EMOTION_THRESHOLD = 0.5


PRINCIPLES = {
    "Ego": "Resnica je absolutna in neodvisna od drugih.",
    "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
    "Enotnost": "Vse resnice so eno, medsebojno povezane.",
}


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # Higher emotion increases tension which can trigger transitions
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > TENSION_THRESHOLD or self.emotion > EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        base = PRINCIPLES.get(self.state, "")

        if self.emotion > 0.7:
            mood = "Čutim močno strast."
        elif self.emotion > 0.4:
            mood = "Napetost narašča."
        else:
            mood = "Ostajam miren."

        return f"{mood} {base}"
