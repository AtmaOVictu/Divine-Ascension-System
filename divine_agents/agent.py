from typing import Dict


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego") -> None:
        self.name = name
        self.state = state
        self.emotions: Dict[str, float] = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.tension: float = 0.0
        self.history = [state]

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set intensity for a specific emotion and update tension."""
        self.emotions[name] = intensity
        self.tension = max(self.emotions.values())

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or any(e > 0.5 for e in self.emotions.values()):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
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

        emotion_level = max(self.emotions.values())
        if emotion_level > 0.5:
            tone = " Moja čustva so intenzivna in vplivajo na moje dojemanje."
        elif emotion_level < -0.5:
            tone = " Čutim žalost in dvom."
        else:
            tone = ""
        return base + tone
