import random


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        use_random: bool = False,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = ""
        self.use_random = use_random
        self.history = [state]

    def update_emotion(self, value: float, kind: str = "") -> None:
        """Update emotion intensity, label and adjust tension."""
        self.emotion = value
        self.emotion_type = kind
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotion."""
        base = {
            "Ego": [
                "Resnica je absolutna in neodvisna od drugih.",
                "Resnica je neodvisna od drugih.",
            ],
            "Jaz": [
                "Resnica je relativna, oblikovana z našimi odnosi.",
                "Resnica se spreminja z izkušnjami in odnosi.",
            ],
            "Enotnost": [
                "Vse resnice so eno, medsebojno povezane.",
                "Vse je medsebojno prepleteno v eni resnici.",
            ],
        }

        options = base[self.state]
        text = random.choice(options) if self.use_random else options[0]
        if self.emotion > 0.5 and self.emotion_type:
            text += f" Čutim {self.emotion_type}."
        return text
