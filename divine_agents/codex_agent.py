from typing import List


class CodexAgent:
    """Agent capable of transitioning ontological states based on emotion and tension."""

    STATES = ["Ego", "Jaz", "Enotnost"]

    def __init__(
        self,
        ime: str,
        filozofija: str,
        motivacija: str,
        dimenzija: str = "Ego",
        tension_threshold: float = 0.7,
        emotion_threshold: float = 0.5,
    ) -> None:
        self.ime = ime
        self.filozofija = filozofija
        self.motivacija = motivacija
        self.state = dimenzija
        self.tension_threshold = tension_threshold
        self.emotion_threshold = emotion_threshold
        self.tension: float = 0.0
        self.emotion: float = 0.0
        self.history: List[str] = [self.state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if thresholds are reached."""
        if self.tension >= self.tension_threshold or self.emotion >= self.emotion_threshold:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical response based on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
