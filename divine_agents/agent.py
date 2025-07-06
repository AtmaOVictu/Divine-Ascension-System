class Agent:
    """Ontological agent capable of state transitions and responses."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    # ------------------------------------------------------------------
    # Updates
    # ------------------------------------------------------------------
    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and optionally its label.

        Parameters
        ----------
        value: float
            Intensity of emotion in [0, 1].
        label: str, optional
            Emotion descriptor (e.g., 'fear', 'joy', 'anger').
        """
        self.emotion = value
        if label:
            self.emotion_label = label

        # Emotion contributes to tension. Fear or anger increase it further.
        self.tension += value
        if self.emotion_label in ("fear", "anger"):
            self.tension += 0.1 * value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # Behaviour
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        prefix_map = {
            "fear": "Z zaskrbljenostjo menim, da ",
            "joy": "Z veseljem verjamem, da ",
            "anger": "Z jezo vztrajam, da ",
        }
        prefix = prefix_map.get(self.emotion_label, "Menim, da ")
        return prefix + base

