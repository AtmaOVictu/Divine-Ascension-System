class Agent:
    """Ontological agent capable of transitioning states and adapting attributes."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.norm = ""
        self.shape = ""
        self.moral_value = ""
        self.history = [state]

        self.change_norm()
        self.change_shape()
        self.update_moral_value()

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally its descriptive type."""
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value

    def change_norm(self) -> None:
        """Adjust normative guideline based on current state."""
        if self.state == "Ego":
            self.norm = "Samooskrba"
        elif self.state == "Jaz":
            self.norm = "Sodelovanje"
        else:
            self.norm = "Enotnost"

    def change_shape(self) -> None:
        """Change physical or symbolic shape according to state."""
        if self.state == "Ego":
            self.shape = "kocka"
        elif self.state == "Jaz":
            self.shape = "krogla"
        else:
            self.shape = "sfera"

    def update_moral_value(self) -> None:
        """Update moral value tied to the state."""
        if self.state == "Ego":
            self.moral_value = "Self-preservation"
        elif self.state == "Jaz":
            self.moral_value = "Cooperation"
        else:
            self.moral_value = "Unity"

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
            self.change_norm()
            self.change_shape()
            self.update_moral_value()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Čutim {self.emotion_type}."
        return base
