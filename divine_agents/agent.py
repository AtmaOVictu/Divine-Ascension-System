class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name:
        Name of the agent.
    state:
        Current ontological state (Ego, Jaz, Enotnost).
    tension:
        Current tension value that may trigger a transition.
    emotion_value:
        Intensity of the current emotion.
    emotion_type:
        Descriptive label of the emotion (e.g., 'fear', 'joy').
    history:
        List of previously visited states including the initial one.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_value: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_value = emotion_value
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        emotion_type:
            Description of the felt emotion (fear, joy, anger...).
        value:
            Intensity of the emotion which also increases tension.
        """
        self.emotion_type = emotion_type
        self.emotion_value = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_value > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane."
        }[self.state]

        emotion_prefix = {
            "fear": "S strahom verjamem, da",
            "joy": "Z veseljem menim, da",
            "anger": "Z jezo trdim, da",
            "sorrow": "S žalostjo spoznavam, da",
            "neutral": "Verjamem, da"
        }.get(self.emotion_type, "Verjamem, da")

        return f"{emotion_prefix} {base}"
